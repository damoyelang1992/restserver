# -*- encoding:utf-8 -*-
import os
from passwdAuth import PassAuth

SECRET_KEY = os.environ["SECRET_KEY"]
MONGO_HOST = os.environ["MONGO_HOST"]
MONGO_PORT = os.environ["MONGO_PORT"]
MONGO_USERNAME = os.environ["MONGO_USERNAME"]
MONGO_PASSWORD = os.environ["MONGO_PASSWORD"]
MONGO_DBNAME = os.environ["MONGO_DBNAME"]

API_VERSION = 'v1'

RESOURCE_METHODS = ['GET', 'PATCH', 'POST']

ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

accounts = {
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
        'required': True,
        'unique': True,
    },
    'password': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 20,
        'required': True,
    },
    'roles': {
        'type': 'list',
        'allowed': ['user', 'superuser', 'admin'],
        'required': True,
    },
    'token': {
        'type': 'string',
        'required': True,
    },
}

accounts = {
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>'.
    'additional_lookup': {
        'url': 'regex("[\w\S]+")',
        # 匹配非空字符，不允许用户查询所有用户信息
        'field': 'username',
    },
    # We also disable endpoint caching as we don't want client apps to
    # cache account data.
    'cache_control': '',
    'cache_expires': 0,

    'resource_methods': ['GET', 'POST'],
    'item_methods': ['PATCH'],
    # 允许更新资源断点，不允许删除用户信息
    # Only allow superusers and admins.
    'allowed_roles': ['superuser', 'admin'],
    # 上面一行并没有起作用
    # Allow 'token' to be returned with POST responses
    'extra_response_fields': ['token'],
    # 不返回用户密码
    'datasource': {
        'source': 'accounts',
        'projection': {
            'password': 0,
        },
    },
    # Finally, let's add the schema definition for this endpoint.
    'schema': accounts,
    'public_methods': ['POST'],
    # 可公用方法，允许任何人POST（ADD）数据，即为注册
}

gettoken = {
    'item_lookup_field': 'username',
    'item_url': 'regex("[\w\S]+")',
    # upon this will cause source can not look up by id, and will
    # influences accounts what to do?
    # 'additional_lookup': {
    #     'url': 'regex("[\w\S]+")',
    #     'field': 'username',
    # },
    # upon this report Key Error 'username'
    'cache_control': '',
    'cache_expires': 0,
    'resource_methods': ['GET'],
    'datasource': {
            'source': 'accounts',
            'projection': {
                'password': 0,
            },
        },
    # 'resource_methods': ['GET', 'POST'],
    'authentication': PassAuth,
}

devices = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'username': {
        'type': 'string',
        'minlength': 5,
        'maxlength': 20,
        'required': True,
        # 'unique': True,
    },
    'nickname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 20,
    },
    'description': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 50,
    },
    'deviceid': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 128,
        'required': True,
        'unique': True,
    },
    'topic': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 128,
        'required': True,
        # talk about hard constraints! For the purpose of the demo
        # 'lastname' is an API entry-point, so we need it to be unique.
        'unique': True,
    },
    'temperature': {
        'type': 'integer',
        'min': 0,
        'max': 100,
        # 'required': True,
    },
    'humidity': {
        'type': 'integer',
        'min': 0,
        'max': 1024,
        # 'required': True,
    },
    'nutrition': {
        'type': 'float',
        'min': 0,
        'max': 10.0,
        # 'required': True,
    },
    'ph': {
        'type': 'float',
        'min': 0.0,
        'max': 14.0,
        # 'required': True,
    },
    'light': {
        'type': 'integer',
        'min': 0,
        'max': 1024,
        # 'required': True,
    },
}

devices = {
    # the standard account entry point is defined as
    # '/accounts/<ObjectId>'. We define  an additional read-only entry
    # point accessible at '/accounts/<username>'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        # 用户名下设备允许批量查询
        'field': 'username',
    },

    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    'resource_methods': ['GET', 'POST'],

    # Finally, let's add the schema definition for this endpoint.
    'schema': devices,
}

DOMAIN = {
    'accounts': accounts,
    'devices': devices,
    'gettoken': gettoken,
}
