#!/usr/bin/env python3
# home route page
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash

contact_bp= Blueprint('contact', __name__)


@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    """
        services route handler
    """
    return render_template('contact.html')
