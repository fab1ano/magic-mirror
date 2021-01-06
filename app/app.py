#!/usr/bin/env python
"""Flask app providing a magic mirror dashboard."""
import sys

from flask import Flask, render_template
from waitress import serve

import greeting
import weather

app = Flask(__name__)


@app.route('/')
def render_static():
    """Gathers data and returns rendered html file."""
    greet = greeting.get_greeting()
    weather_data = []

    for i, content in enumerate(weather.get_data()):
        weather_data.append({
            'id': weather.get_ids()[i],
            'pre': weather.get_pre()[i],
            'post': weather.get_post()[i],
            'content': map(str, content),
        })

    return render_template('index.html', **locals())


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'production':
        serve(app, host='127.0.0.1', port=8080)
    else:
        app.run(debug=True)
