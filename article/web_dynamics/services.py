#!/usr/bin/env python3
# home route page
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash

services_bp= Blueprint('services', __name__)


@services_bp.route('/services', methods=['GET', 'POST'])
def services():
    """
        services route handler
    """
    return render_template('services.html')
