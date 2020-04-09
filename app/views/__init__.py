#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: __init__.py
# Date: 2020-2-20-0020

from flask import Blueprint

bpviews = Blueprint('dockerManager', __name__)

from app.views import authentication
from app.views import dockermanager
from app.views import welcome
from app.views import api