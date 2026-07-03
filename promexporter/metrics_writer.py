import yaml
from pathlib import Path


class MetricsWriter:
    def __init__(self, filename="devices.yml"):
        self.filename = Path(filename)

        if not self.filename.exists():
            self._write({"devices": []})

    def _read(self):
        with self.filename.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file) or {}

        if "devices" not in data:
            data["devices"] = []

        return data

    def _write(self, data):
        tmp_file = self.filename.with_suffix(".tmp")

        with tmp_file.open("w", encoding="utf-8") as file:
            yaml.safe_dump(
                data,
                file,
                sort_keys=False,
                allow_unicode=True
            )

        tmp_file.replace(self.filename)

    def calculate_health(self, metrics):
        health = 100

        if not metrics.get("online", 0):
            health -= 60

        if metrics.get("microphone_muted", 0):
            health -= 5

        if metrics.get("packet_loss", 0) > 2:
            health -= 15

        if metrics.get("jitter_ms", 0) > 30:
            health -= 10

        if metrics.get("temperature_alarm", 0):
            health -= 30

        return max(0, health)

    def update(self, metrics):
        required = ["device_id", "device", "workspace"]

        for key in required:
            if key not in metrics:
                raise ValueError(f"Pflichtfeld fehlt: {key}")

        metrics["health_score"] = self.calculate_health(metrics)

        data = self._read()
        devices = data["devices"]

        for index, device in enumerate(devices):
            if device.get("device_id") == metrics["device_id"]:
                devices[index] = metrics
                break
        else:
            devices.append(metrics)

        self._write(data)
