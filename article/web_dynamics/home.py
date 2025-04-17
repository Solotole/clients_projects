#!/usr/bin/env python3
# home route page
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash
from web_dynamics.about import about_bp
from web_dynamics.services import services_bp
from web_dynamics.contact import contact_bp

app = Flask(__name__)
app.register_blueprint(about_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(services_bp)


@app.route('/home', methods=['GET', 'POST'])
def home():
    """
        home route handler
    """
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)