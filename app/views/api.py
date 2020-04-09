#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: api
# Date: 2020-2-23-0023

from flask import jsonify, request
from app.views import bpviews as bp
import psutil
import docker
import subprocess
import json
import time
import base64


@bp.route('/api/equipment-status')
def getEquipmentStatus():
    data = dict()
    data['cpu_count_logical'] = psutil.cpu_count(logical=True)
    data['cpu_count_physical'] = psutil.cpu_count(logical=False)
    data['cpu_percent'] = psutil.cpu_percent(interval=1, percpu=False)
    v = psutil.virtual_memory()
    data['ram_total'] = v.total
    data['ram_available'] = v.available
    data['ram_percent'] = v.percent
    data['ram_used'] = v.used
    data['ram_free'] = v.free
    data['disk'] = []
    for i in psutil.disk_partitions():
        device = i.device
        mountpoint = i.mountpoint
        fstype = i.fstype
        volume, used, free, percent = psutil.disk_usage(mountpoint)
        data['disk'].append(
            {
                'device': device,
                'mountpoint': mountpoint,
                'fstype': fstype,
                'volume': volume,
                'used': used,
                'free': free,
                'percent': percent,
            }
        )
    return jsonify(data)


@bp.route('/api/docker-status')
def getDockerStatus():
    data = dict()
    C = docker.from_env()
    data['images'], data['containers'] = list(), list()
    for i in C.containers.list(all):
        d = {
            'id': i.id,
            'short_id': i.short_id,
            'name': i.name,
            'status': i.status,
            'from': {
                'image_tags': i.image.tags,
                'image_id': i.image.id,
            },
            'port': i.ports,
            'command': i.attrs.get('Path'),
        }
        data.get('containers').append(d)
    for i in C.images.list():
        d = {
            'id': i.id,
            'short_id': i.short_id,
            'tags': i.tags,
            'labels': i.labels,
            'container_id': i.attrs.get('container'),
        }
        data.get('images').append(d)

    return jsonify(data)


@bp.route('/api/container')
def getContainerStatus():
    if request.args.get('id'):
        try:
            if docker.from_env().containers.get(request.args.get('id')):
                r = subprocess.run(['docker', 'stats', '--no-stream', request.args.get('id'), '--format',
                                    '{"ram_percent": "{{ .MemPerc }}","cpu_percent": "{{ .CPUPerc }}","ram_usage":"{{ .MemUsage }}"}'],
                                   capture_output=True, text=True).stdout.replace('\n', '')
            else:
                return '', 404
        except:
            return '', 404
        else:
            return jsonify(json.loads(r))
    else:
        return '', 404


@bp.route('/api/container/shell', methods=['POST'])
def containerExec():
    if request.args.get('id'):
        id = request.args.get('id')
        if request.form.get('command'):
            cmd = request.form.get('command')
            try:
                d = docker.from_env()
                if id in [i.id for i in d.containers.list()]:
                    c = d.containers.get(id)
                    r = c.exec_run(cmd)
                    if not r.exit_code:
                        data = r.output.decode('utf8')
                    else:
                        return '', 500
                else:
                    return '', 404
            except:
                return '', 500
            else:
                return jsonify({'output': data})
        else:
            return '', 500
    else:
        return '', 404


@bp.route('/api/container/pause')
def containerPause():
    if request.args.get('id'):
        id = request.args.get('id')
        try:
            d = docker.from_env()
            if id in [i.id for i in d.containers.list()]:
                d.containers.get(id).pause()
            else:
                return '', 404
        except:
            return '', 500
        else:
            return jsonify({'msg': 'success'})
    else:
        return '', 404


@bp.route('/api/container/unpause')
def containerUnpause():
    if request.args.get('id'):
        id = request.args.get('id')
        try:
            d = docker.from_env()
            if id in [i.id for i in d.containers.list()]:
                d.containers.get(id).unpause()
            else:
                return '', 404
        except:
            return '', 500
        else:
            return jsonify({'msg': 'success'})
    else:
        return '', 404


@bp.route('/api/container/restart')
def containerRestart():
    if request.args.get('id'):
        id = request.args.get('id')
        try:
            d = docker.from_env()
            if id in [i.id for i in d.containers.list()]:
                d.containers.get(id).restart()
            else:
                return '', 404
        except:
            return '', 500
        else:
            return jsonify({'msg': 'success'})
    else:
        return '', 404


@bp.route('/api/container/start')
def containerStart():
    if request.args.get('id'):
        id = request.args.get('id')
        try:
            d = docker.from_env()
            if id in [i.id for i in d.containers.list()]:
                return jsonify({'msg': 'container is running...'})
            else:
                d.containers.get(id).start()
        except:
            return '', 500
        else:
            return jsonify({'msg': 'success'})
    else:
        return '', 404


@bp.route('/api/container/stop')
def containerStop():
    if request.args.get('id'):
        id = request.args.get('id')
        try:
            d = docker.from_env()
            if id in [i.id for i in d.containers.list()]:
                d.containers.get(id).stop()
            else:
                return '', 404
        except:
            return '', 500
        else:
            return jsonify({'msg': 'success'})
    else:
        return '', 404


# @bp.route('/api/container/destroy')
# def containerDestroy():
#     if request.args.get('id'):
#         id = request.args.get('id')
#         try:
#             d = docker.from_env()
#             if id in [i.id for i in d.containers.list()]:
#                 d.containers.get(id).stop()
#             else:
#                 return '', 404
#         except:
#             return '', 500
#         else:
#             return jsonify({'msg': 'success'})
#     else:
#         return '', 404
