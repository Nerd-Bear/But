import json
import time

from flask import Response
from flask_restful import Resource
from werkzeug.exceptions import HTTPException


class BaseResource(Resource):
    def __init__(self):
        self.now = time.strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def unicode_safe_json_dumps(cls, data, status_code=200, **kwargs) -> Response:
        return Response(
            json.dumps(data, ensure_ascii=False),
            status_code,
            content_type='application/json; charset=utf8',
            **kwargs
        )

    class ValidationError(Exception):
        def __init__(self, description='', *args):
            self.description = description

            super(BaseResource.ValidationError, self).__init__(*args)


def load_api():
    from app.views import sample


def route(app):
    from app import api_v1_blueprint

    load_api()

    app.register_blueprint(api_v1_blueprint)
