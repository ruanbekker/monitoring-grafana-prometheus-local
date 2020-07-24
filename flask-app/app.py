# https://github.com/rycus86/prometheus_flask_exporter/blob/master/README.md
# https://blog.viktoradam.net/2020/05/11/prometheus-flask-exporter/
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics
from time import sleep as delay

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'foobar', version='1.0.3', service_name='flask-app')

@app.route('/')
def main():
    return '<html><p><a href="/wait/4">/wait/4</a><p><a href="/status/500">/status/500</a></html></html>'

@app.route('/wait/<int:seconds>')
def delayme(seconds):
    delay(seconds)
    return 'hello'

@app.route('/skip')
@metrics.do_not_track()
def skip():
    return 'metric not collected'

@app.route('/status/<int:status>')
@metrics.do_not_track()
@metrics.summary('requests_by_status', 'Request latencies by status', labels={'status': lambda r: r.status_code})
@metrics.histogram('requests_by_status_and_path', 'Request latencies by status and path', labels={'status': lambda r: r.status_code, 'path': lambda: request.path})
def echo_status(status):
    return 'Status: %s' % status, status

if __name__ == '__main__':
    app.run(host='0.0.0.0')
