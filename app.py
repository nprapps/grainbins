#!/usr/bin/env python

import json
from mimetypes import guess_type
from models import Incident
import urllib

import envoy
from flask import Flask, Markup, abort, render_template

import app_config
from render_utils import flatten_app_config, make_context
app = Flask(app_config.PROJECT_NAME)

# Example application views
@app.route('/')
def index():
    """
    Example view demonstrating rendering a simple HTML page.
    """
    incidents_with_age = Incident.select().where(Incident.age > 0).order_by(Incident.age.asc())
    incidents_without_age = Incident.select().where(Incident.age >> None).order_by(Incident.age.asc())
    incidents = list(incidents_with_age) + list(incidents_without_age)
    states = [i.state for i in Incident.select(Incident.state).distinct().order_by(Incident.state)]

    def slug(incident):
        uniq = incident.name or 'unknown'

        if (incident.postofficename):
            uniq += '-' + incident.postofficename

        uniq += '-' +  incident.state

        return uniq.lower().replace(' ', '-').replace('.', '').replace('--', '-')

    return render_template('index.html', incidents=incidents, states=states, slug=slug, **make_context())

@app.route('/doc-grainbins.html')
def doc_grainbins():
    """
    Document Cloud page
    """
    return render_template('doc-grainbins.html', **make_context())

@app.route('/widget.html')
def widget():
    """
    Embeddable widget example page.
    """
    return render_template('widget.html', **make_context())

@app.route('/test_widget.html')
def test_widget():
    """
    Example page displaying widget at different embed sizes.
    """
    return render_template('test_widget.html', **make_context())

# Render LESS files on-demand
@app.route('/less/<string:filename>')
def _less(filename):
    try:
        with open('less/%s' % filename) as f:
            less = f.read()
    except IOError:
        abort(404)

    r = envoy.run('node_modules/.bin/lessc -', data=less)

    return r.std_out, 200, { 'Content-Type': 'text/css' }

# Render JST templates on-demand
@app.route('/js/templates.js')
def _templates_js():
    r = envoy.run('node_modules/.bin/jst --template underscore jst')

    return r.std_out, 200, { 'Content-Type': 'application/javascript' }

# Render application configuration
@app.route('/js/app_config.js')
def _app_config_js():
    config = flatten_app_config()
    js = 'window.APP_CONFIG = ' + json.dumps(config)

    return js, 200, { 'Content-Type': 'application/javascript' }

# Server arbitrary static files on-demand
@app.route('/<path:path>')
def _static(path):
    try:
        with open('www/%s' % path) as f:
            return f.read(), 200, { 'Content-Type': guess_type(path)[0] }
    except IOError:
        abort(404)

@app.template_filter('urlencode')
def urlencode_filter(s):
    """
    Filter to urlencode strings.
    """
    if type(s) == 'Markup':
        s = s.unescape()

    s = s.encode('utf8')
    s = urllib.quote_plus(s)

    return Markup(s)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=app_config.DEBUG)
