import time
import yaml
from prometheus_client import start_http_server, Gauge

PORT = 8000
POLL_INTERVAL = 15

LABELS = ["device", "device_id", "workspace"]

roomos_device_online = Gauge("roomos_device_online", "1=online, 0=offline", LABELS)
roomos_health_score = Gauge("roomos_health_score", "Calculated health score", LABELS)
roomos_people_count = Gauge("roomos_people_count", "Current people count", LABELS)
roomos_call_connected = Gauge("roomos_call_connected", "1=in call, 0=not in call", LABELS)
roomos_microphones_muted = Gauge("roomos_microphones_muted", "1=muted, 0=unmuted", LABELS)
roomos_standby_state = Gauge("roomos_standby_state", "1=standby/halfwake, 0=active", LABELS)
roomos_temperature_alarm = Gauge("roomos_temperature_alarm", "1=alarm, 0=normal", LABELS)
roomos_packet_loss = Gauge("roomos_packet_loss", "Packet loss in percent", LABELS + ["direction", "media"])
roomos_jitter_ms = Gauge("roomos_jitter_ms", "Jitter in ms", LABELS + ["direction", "media"])


def load_devices(path="devices.yml"):
    with open(path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    return data.get("devices", [])


def bool_to_int(value):
    return 1 if value else 0


def collect_device_metrics(device):
    labels = {
        "device": device["device"],
        "device_id": device["device_id"],
        "workspace": device.get("workspace", "")
    }

    # Werte direkt aus Datei lesen
    online = device.get("online", 1)
    people_count = device.get("people_count", 0)
    muted = device.get("microphone_muted", 0)
    in_call = device.get("call_connected", 0)
    standby = device.get("standby_state", 0)
    temperature_alarm = device.get("temperature_alarm", 0)
    packet_loss = device.get("packet_loss", 0)
    jitter_ms = device.get("jitter_ms", 0)

    health = device.get("health_score")
    if health is None:
        health = 100
        if not online:
            health -= 60
        if muted:
            health -= 5
        if packet_loss > 2:
            health -= 15
        if jitter_ms > 30:
            health -= 10
        if temperature_alarm:
            health -= 30
        health = max(0, health)

    roomos_device_online.labels(**labels).set(online)
    roomos_health_score.labels(**labels).set(health)
    roomos_people_count.labels(**labels).set(people_count)
    roomos_call_connected.labels(**labels).set(in_call)
    roomos_microphones_muted.labels(**labels).set(muted)
    roomos_standby_state.labels(**labels).set(standby)
    roomos_temperature_alarm.labels(**labels).set(temperature_alarm)

    roomos_packet_loss.labels(
        **labels,
        direction="incoming",
        media="audio"
    ).set(packet_loss)

    roomos_jitter_ms.labels(
        **labels,
        direction="incoming",
        media="audio"
    ).set(jitter_ms)


def main():
    print(f"Exporter läuft auf http://0.0.0.0:{PORT}/metrics")
    start_http_server(PORT, addr="0.0.0.0")

    while True:
        devices = load_devices()

        for device in devices:
            collect_device_metrics(device)

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
