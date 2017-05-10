from datetime import datetime, timedelta
import base64
import json

JWT_EXP_DELTA_SECONDS = 864000


def gen_token(username):
    payload = {
        'username': username,
        'exp': (datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)).strftime("%Y-%m-%d %H:%M:%S"),
    }
    token = base64.urlsafe_b64encode(json.dumps(payload).encode("utf-8"))
    return token
