#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: dockerManager
# Date: 2020-2-21-0021

from flask import request, render_template, jsonify, session, redirect
from app.views import bpviews as bp
from models import *
import docker
import time


@bp.route('/dmr')
def dmr():
    return render_template('dockermanager.html', username=session.get('username'))


@bp.route('/dmr/container')
def dmr_container():
    if request.args.get('id'):
        id = request.args.get('id')
        try:
            d = docker.from_env()
            if id in [i.id[0:12] for i in d.containers.list(all)]:
                c = d.containers.get(id)
                dk = {}
                dk['name'] = c.name
                dk['id'] = c.id
                dk['status'] = c.status
                dk['createdat'] = c.attrs.get('Created').split('.')[0].replace('T', ' ')
                dk['startedat'] = c.attrs.get('State').get('StartedAt').split('.')[0].replace('T', ' ')
                dk['finishedat'] = c.attrs.get('State').get('FinishedAt').split('.')[0].replace('T', ' ')
                dk['pid'] = c.attrs.get('State').get('Pid')
                dk['command_path'] = c.attrs.get('Path')
                dk['command_args'] = ''.join([str(i) for i in c.attrs.get('Args')])
                dk['platform'] = c.attrs.get('Platform')
                dk['from_image_name'] = ','.join(c.image.tags)
                dk['from_image_id'] = c.image.id
                port = []
                ports = c.ports
                for k in ports.keys():
                    port.append(k + '->(' + ','.join([':'.join(a.values()) for a in ports[k]]) + ')')
                dk['port'] = ','.join(port)
                return render_template('manage_container.html', username=session.get('username'), dk=dk)
            else:
                return '', 404
        except:
            return '', 500
    else:
        return '', 404


@bp.route('/dmr/container/console_viewer')
def dmr_container_console_viewer():
    if request.args.get('id'):
        id = request.args.get('id')
        try:
            d = docker.from_env()
            if id in [i.id for i in d.containers.list()]:
                c = d.containers.get(id)
                data = {
                    'id': id,
                    'name': c.name,
                    'from_image_name': ','.join(c.image.tags),
                }
                return render_template('terminal.html', data=data)
            else:
                return '', 404
        except:
            return '', 500
    else:
        return '', 404
