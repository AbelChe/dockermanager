#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: dashboard
# Date: 2020-2-23-0023

from flask import render_template, jsonify, session
from app.views import bpviews as bp
from app.views import api
import psutil


@bp.route('/')
def dashboard():
    return render_template('dashboard.html', username=session.get('username'))
