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

We are using loki to ship logs from our containers, so we need to install the loki docker driver:

```
$ docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions
```

To boot your stack in localhost mode (ie. traefik.localdns.xyz -> 127.0.0.1):

```
$ docker-compose up --build -d
```

To boot your stack in ip mode (ie. traefik.10.2.3.4.nip.io -> 10.2.3.4):

```
$ IP=$(curl -s -4 ifconfig.co)
$ export DOMAIN=${IP}.nip.io
$ docker-compose up --build -d
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

For more detailed alerting have a look at my [prometheus-alerting-alertmanager](https://github.com/ruanbekker/prometheus-alerting-alertmanager) repo:
- [alertmanager.yml](https://github.com/ruanbekker/prometheus-alerting-alertmanager/blob/main/alertmanager/alertmanager.yml)
- [host_alerts.rules](https://github.com/ruanbekker/prometheus-alerting-alertmanager/blob/main/prometheus-a/rules/host_alert.rules)

