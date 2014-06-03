# -*- coding: utf-8 -*-

from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('first_view.html')

@app.route('/two')
def two():
	return render_template('two.html')


@app.route('/three')
def three():
	return render_template('three.html')


