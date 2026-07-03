# Webex RoomOS Monitoring – File Based Metrics Pipeline

Dieses Projekt demonstriert eine einfache und modulare Monitoring-Architektur für Cisco Webex RoomOS-Geräte.

Die Komponenten sind bewusst voneinander getrennt, damit sie unabhängig entwickelt und getestet werden können.

```
                Webex API
                     │
                     ▼
           get_room_metrics()
                     │
                     ▼
              MetricsWriter
                     │
                     ▼
               devices.yml
                     │
                     ▼
          Prometheus Exporter
                     │
                     ▼
               Prometheus
                     │
                     ▼
                 Grafana
```

---

# Projektstruktur

```
roomkit-monitor/
│
├── metrics_writer.py
├── exporter.py
├── demo_generator.py
├── devices.yml
├── requirements.txt
└── README.md
```

---

# Komponenten

## metrics_writer.py

Der Writer ist die einzige Komponente, die Schreibzugriff auf `devices.yml` besitzt.

Aufgabe:

* neue Geräte anlegen
* bestehende Geräte aktualisieren
* Health Score berechnen
* YAML-Datei schreiben

Der Aufrufer kennt weder YAML noch den Dateiaufbau.

Beispiel:

```python
from metrics_writer import MetricsWriter

writer = MetricsWriter()

writer.update(metrics)
```

---

## exporter.py

Der Exporter besitzt keinerlei Webex-Kenntnisse.

Er

* liest regelmäßig `devices.yml`
* exportiert alle Werte als Prometheus-Metriken
* stellt `/metrics` bereit

Prometheus liest anschließend diese Daten ein.

---

## demo_generator.py

Der Demo-Generator simuliert RoomOS-Geräte.

Er erzeugt regelmäßig neue Messwerte und schreibt diese über den `MetricsWriter` in die Datei.

Später wird der Demo-Generator durch echte Webex-Abfragen ersetzt.

---

# Datenformat

Alle Daten werden als Python-Dictionary an den Writer übergeben.

Beispiel:

```python
metrics = {

    "device_id": "Y2lzY29zcGFyazovL3VzL0RFVklDRS8xMjM=",
    "device": "Room Kit Mini Schulung",
    "workspace": "Trainingsraum",

    "online": 1,
    "people_count": 4,

    "microphone_muted": 0,
    "call_connected": 1,
    "standby_state": 0,

    "temperature_alarm": 0,

    "packet_loss": 0.2,
    "jitter_ms": 8.5
}
```

Der Writer berechnet daraus automatisch den `health_score`.

---

# Beispiel

```python
from metrics_writer import MetricsWriter

writer = MetricsWriter()

writer.update({

    "device_id": "device-001",
    "device": "Room Kit Mini",
    "workspace": "Raum 1",

    "online": 1,
    "people_count": 3,

    "microphone_muted": 0,
    "call_connected": 1,
    "standby_state": 0,

    "temperature_alarm": 0,

    "packet_loss": 0.3,
    "jitter_ms": 12.5
})
```

Es sind keine Dateizugriffe erforderlich.

---

# devices.yml

Nach dem ersten Aufruf erzeugt der Writer automatisch:

```yaml
devices:

  - device_id: device-001
    device: Room Kit Mini
    workspace: Raum 1

    online: 1
    people_count: 3

    microphone_muted: 0
    call_connected: 1
    standby_state: 0

    temperature_alarm: 0

    packet_loss: 0.3
    jitter_ms: 12.5

    health_score: 100
```

Beim nächsten Aufruf mit derselben `device_id` wird dieser Eintrag aktualisiert.

Neue Geräte werden automatisch ergänzt.

---

# Ablauf

## 1. Demo

```
demo_generator.py
        │
        ▼
MetricsWriter
        │
        ▼
devices.yml
        │
        ▼
exporter.py
        │
        ▼
Prometheus
        │
        ▼
Grafana
```

---

## 2. Produktion

```
Webex Devices API
        │
        ▼
get_room_metrics()
        │
        ▼
MetricsWriter
        │
        ▼
devices.yml
        │
        ▼
Prometheus Exporter
        │
        ▼
Grafana
```

---

# Vorteile

* Klare Trennung zwischen Datenerfassung und Monitoring
* Kein Prometheus-Code im Webex-Modul
* Kein Webex-Code im Exporter
* Geräte können dynamisch hinzugefügt werden
* Sehr einfach testbar
* Austauschbare Komponenten

---

# Erweiterungsmöglichkeiten

Neue Metriken können jederzeit ergänzt werden.

Beispielsweise:

```python
metrics["ambient_noise"] = 42
metrics["air_quality"] = 98
metrics["speaker_track"] = 1
metrics["presentation_active"] = 0
metrics["cpu_temperature"] = 53.7
```

Der `MetricsWriter` speichert zusätzliche Felder automatisch.

Der Exporter muss anschließend lediglich erweitert werden, um diese neuen Werte als Prometheus-Metriken bereitzustellen.

---

# Nächster Entwicklungsschritt

Im nächsten Modul wird `demo_generator.py` durch einen echten RoomOS-Collector ersetzt.

Dieser

* liest die Geräte über die Webex Devices API,
* fragt die gewünschten xAPI-Statuswerte ab,
* erstellt das Metrics-Dictionary und
* übergibt es unverändert an den `MetricsWriter`.
