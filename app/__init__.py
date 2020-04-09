#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: __init__
# Date: 2020-2-20-0020
import os

from flask import Flask
from app.views import bpviews
from app.settings import CONFIG


def creat_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_mapping(CONFIG)
    app.register_blueprint(blueprint=bpviews, url_prefix='/')
    return app
