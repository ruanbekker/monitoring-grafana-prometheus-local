# monitoring-grafana-prometheus-local

This is a local stack that you can boot with docker-compose which will give you: Traefik, Grafana, Prometheus, cAdvisor, Node-Exporter, AlertManager, Python App instrumented with Prometheus

## Contents

Stack will give you:

- Traefik: Reverse Proxy and domain configured is `*.localdns.xyz` which all resolves to 127.0.0.1
- Grafana: Dashboarding `grafana.localdns.xyz`
- Prometheus: Time Series DB `prometheus.localdns.xyz`
- Node-Exporter: Node Level Metrics
- cAdvisor: Container Level Metrics
- Alertmanager: Creates Alerts from Prometheus Metrics `alertmanager.localdns.xyz`
- Python Flask App: Instrumented with Prometheus `flask-app.localdns.xyz`

## Usage

To boot your stack:

```
$ docker-compose build
$ docker-compose up -d
```

Access [http://traefik.localdns.xyz](http://traefik.localdns.xyz) for viewing the Traefik Dashboard, or [grafana.localdns.xyz](http://grafana.localdns.xyz) to access Grafana and 2 pre-made dashboards will be visible to view node and container level metrics.

The default user/pass is admin/admin

Access [prometheus.localdns.xyz](http://prometheus.localdns.xyz) to access Prometheus UI

For the web application you can access it on [flask-app.localdns.xyz](http://flask-app.localdns.xyz), and has the following endpoints:

- `/`
- `/wait/{int}` - how long the request should take in seconds
- `/status/{int}` - the status code that should be captured
- `/skip` - does not collect metrics
- `/metrics` view the metrics that is exporter for prometheus to scrape


