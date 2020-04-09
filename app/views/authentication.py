#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: authentication
# Date: 2020-2-20-0020

from flask import request, render_template, jsonify, session, redirect
from app.views import bpviews as bp
from models import *


@bp.before_request
def check_ticket():
    if request.remote_addr == '39.155.107.222':
        session['username'] = 'abelche'
        pass
    else:
        white_list = [
            '/login',
            '/login/authentication',
        ]
        if request.path in white_list:
            return None
        username = session.get('username')
        if username:
            return None
        return redirect("/login")


@bp.route('/login')
def login():
    return render_template('login.html')


@bp.route('/login/authentication', methods=['POST'])
def authentication():
    sql = Users.query.filter(Users.name == request.form.get('username'),
                             Users.password == request.form.get('password')).first()
    if sql:
        session['username'] = sql.name
        return jsonify({'code': 0})
    return jsonify({'code': 1})


@bp.route('/logout')
def logout():
    pass
