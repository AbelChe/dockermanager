#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author: AbelChe
# E-mail: C305790018@163.com
# Blog: https://www.abelche.com
# FileName: manage
# Date: 2020-2-20-0020

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import *
from app import creat_app

app = creat_app()
manager = Manager(app)
migrate = Migrate(app, db)
db.init_app(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
