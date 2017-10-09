# coding=utf-8

DB_config = {
    # 'db_type': 'mongodb',
    'db_type': 'mysql',

    'mysql': {
        'host': '192.168.103.237',
        'port': 3306,
        'user': 'cnki',
        'password': 'cnki',
        'charset': 'utf8',
    },
    # 'redis': {
    #     'host': 'localhost',
    #     'port': 6379,
    #     'password': '123456',
    #     'db': 1,
    # },
    # 'mongodb':{
    #     'host': 'localhost',
    #     'port': 27017,
    #     'username': '',
    #     'password': '',
    # }
}

database = 'spiders'
free_ipproxy_table = 'free_ipproxy'
httpbin_table = 'httpbin'

data_port = 8000
