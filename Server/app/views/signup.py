from flasgger import swag_from
from flask import request
from flask_restful import Api

from uuid import uuid4

from app import signup_blueprint
from app.docs.signup import *
from app.models.user import UserModel
from app.models.friend import FriendModel
from app.views import BaseResource

api = Api(signup_blueprint)
api.prefix = '/signup'


@api.resource('/')
class Signup(BaseResource):
    @swag_from(SIGNUP_POST)
    def post(self):
        """
        정보 등록
        """
        payload = request.json
        uuid = str(uuid4())

        user = UserModel(uuid=uuid, **payload).save()
        FriendModel(
            user=user
        ).save()
        return self.unicode_safe_json_dumps({'user_id': uuid}, 201)
