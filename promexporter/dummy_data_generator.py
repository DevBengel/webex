import random
import time
import yaml
from pathlib import Path

DEVICES_FILE = Path("devices.yml")
INTERVAL_SECONDS = 5

DEVICES = [
    {
        "device_id": "Y2lzY29-001",
        "device": "RoomKit Mini Schulung 1",
        "workspace": "Raum 1",
    },
    {
        "device_id": "Y2lzY29-002",
        "device": "RoomKit Mini Schulung 2",
        "workspace": "Raum 2",
    },
    {
        "device_id": "Y2lzY29-003",
        "device": "Boardroom",
        "workspace": "Konferenzraum",
    },
]


def calculate_health(device):
    health = 100

    if not device["online"]:
        health -= 60
    if device["microphone_muted"]:
        health -= 5
    if device["packet_loss"] > 2:
        health -= 15
    if device["jitter_ms"] > 30:
        health -= 10
    if device["temperature_alarm"]:
        health -= 30

    return max(0, health)


def generate_metrics(device):
    online = random.choice([1, 1, 1, 1, 0])
    in_call = random.choice([0, 0, 1]) if online else 0

    generated = {
        **device,
        "online": online,
        "people_count": random.randint(0, 8) if online else 0,
        "microphone_muted": random.choice([0, 0, 0, 1]) if online else 0,
        "call_connected": in_call,
        "standby_state": random.choice([0, 0, 1]) if online else 1,
        "temperature_alarm": random.choice([0, 0, 0, 0, 1]) if online else 0,
        "packet_loss": round(random.uniform(0, 3), 2) if in_call else 0,
        "jitter_ms": round(random.uniform(2, 40), 1) if in_call else 0,
    }

    generated["health_score"] = calculate_health(generated)
    return generated


def write_devices_file(devices):
    tmp_file = DEVICES_FILE.with_suffix(".tmp")

    with tmp_file.open("w", encoding="utf-8") as file:
        yaml.safe_dump(
            {"devices": devices},
            file,
            sort_keys=False,
            allow_unicode=True,
        )

    tmp_file.replace(DEVICES_FILE)


def main():
    print(f"Demo-Generator schreibt alle {INTERVAL_SECONDS}s nach {DEVICES_FILE}")

    while True:
        generated_devices = [generate_metrics(device) for device in DEVICES]
        write_devices_file(generated_devices)

        print("devices.yml aktualisiert")
        time.sleep(INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
