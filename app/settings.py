#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: settings
# Date: 2020-2-20-0020

import os

# 基础路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# templates路径
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')

# static路径
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')

# media路径
# MEDIA_FOLDER = os.path.join(FOLDER, 'media')

# 保存图片的路径
# UPLOAD_FOLDER = os.path.join(FOLDER, 'upload')

# MySQL 配置
DB_DIALECT = 'mysql'
DB_DRIVER = 'pymysql'
DB_USERNAME = '*****'
DB_PASSWORD = '***********'
DB_HOST = '********'
DB_PORT = '3306'
DB_DATABASE = 'dockermanager'

# 参数设置
CONFIG = {
    'DEBUG': True,
    'STATIC_FOLDER': STATIC_FOLDER,
    'TEMPLATE_FOLDER': TEMPLATE_FOLDER,
    'SQLALCHEMY_DATABASE_URI': '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(
        DB_DIALECT, DB_DRIVER, DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT, DB_DATABASE
    ),
    'SQLALCHEMY_COMMIT_ON_TEARDOWN': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    'SQLALCHEMY_POOL_SIZE': 10,
    'SQLALCHEMY_MAX_OVERFLOW': 5,
}
