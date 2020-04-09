#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: models
# Date: 2020-2-21-0021

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Container(db.Model):
    __tablename__ = 'container'

    container_id = db.Column(db.String(255), primary_key=True)
    image = db.Column(db.String(255))
    command = db.Column(db.String(255))
    name = db.Column(db.String(255))
    port = db.Column(db.String(255))
    state = db.Column(db.String(255))
    created_date = db.Column(db.DateTime)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
