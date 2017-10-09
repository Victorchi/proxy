# -*- coding: utf-8 -*-
# auhtor by:Victor chi

import requests
import pymysql
import config
from proxy import Proxy
from sql.sql_base import SqlBase
from sql.sql_manager import SqlManager
from sql.mysql import MySql
import logging
import time


if __name__ == '__main__':

    while True:
        test = SqlManager()
        a=test.vaildator_ip(config.free_ipproxy_table)
        time.sleep(4000)