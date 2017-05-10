# -*- encoding:utf-8 -*-
from eve.auth import BasicAuth
from werkzeug.security import check_password_hash
from flask import current_app as app
import genToken


class PassAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        '''
        通过用户名密码对用户进行认证，认证成功之后更新数据库中的Token
        :param username:用户名
        :param password:用户密码
        :param allowed_roles:允许的角色
        :param resource:资源，url节点
        :param method:请求方法
        :return:
        '''
        # use Eve's own db driver; no additional connections/resources are used
        accounts = app.data.driver.db['accounts']
        account = accounts.find_one({'username': username})
        if account and check_password_hash(account['password'], password):
            accounts.update(
                {'username': username},
                # {'token': account['token']},
                # 保证用户只能改变自己的Token，上面一句是原有记录，下面一句是设定数据内容
                {"$set": {"token": genToken.gen_token(username)}}
            )
        return account and \
            check_password_hash(account['password'], password)
