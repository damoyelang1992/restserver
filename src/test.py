# -*- encoding:utf-8 -*-
from eve import Eve
from werkzeug.security import generate_password_hash
from eve.auth import TokenAuth
import genToken
from datetime import datetime
import base64
import json
from flask import abort, Response


class TokAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
            accounts = app.data.driver.db['accounts']
            lookup = {'token': token}
            account = accounts.find_one(lookup)
            # 查找账户,验证Token有效期
            try:
                tokenstr = base64.urlsafe_b64decode(account['token'].encode("utf-8"))
            except TypeError:
                resp = Response(None, 401, {'WWW-Authenticate': 'Basic realm="%s"' %
                                                                __package__})
                abort(401, description='The Token is invalid!',
                      response=resp)
            jsontoken = json.loads(tokenstr)
            time = datetime.strptime(jsontoken['exp'], "%Y-%m-%d %H:%M:%S")
            if datetime.utcnow() > time:
                resp = Response(None, 401, {'WWW-Authenticate': 'Basic realm="%s"' %
                                                                __package__})
                abort(401, description='Token timeout, Please visit /v1/gettoken to get a new token!',
                      response=resp)
            else:
                return account


# Hooks
# def pre_get_callback(resource, request, lookup):
#     lookup["username"] = {'$exists': True}
#     print("Hello")
#     print("A Get request on the %s endpoint has just been received!" % resource)
#
# #
# def pre_contacts_get_callback(request, lookup):
#     print 'A GET request on the contacts endpoint has just been received!'


# def pre_post_callback(request, lookup):
#     print(request)


def add_token(documents):
    for document in documents:
        document["password"] = generate_password_hash(document["password"])
        # salt = (''.join(random.choice(string.ascii_uppercase) for x in range(10)))
        document["token"] = genToken.gen_token(document["username"])
        # print(document["username"])


app = Eve(auth=TokAuth)
# app = Eve(auth=PassAuth)
# app = Eve()
app.on_insert_accounts += add_token
# app.on_pre_POST += pre_post_callback
# app.on_pre_GET += pre_get_callback
# app.on_pre_GET_contacts += pre_contacts_get_callback
# app.run(host='0.0.0.0', port=5000)
