#!/usr/bin/env python3
# home route page
from flask import Blueprint, Flask, render_template, request, redirect, url_for, flash

about_bp= Blueprint('about', __name__)


@about_bp.route('/about', methods=['GET', 'POST'])
def about():
    """
        home route handler
    """
    return render_template('about.html')
