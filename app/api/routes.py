from app.api import api_bp
from app import api
from flask_restx import Resource
from app.api.dao import EventDao
from app.api.marshal_models import time_line_model

import datetime

e1 = EventDao(date=str(datetime.date(2000, 11, 11)), value=10)
e2 = EventDao(date=str(datetime.date(2010, 10, 2)), value=8)


@api_bp.route('/timeline')
class Todo(Resource):
    @api.marshal_with(time_line_model)
    def get(self, **kwargs):
        return {'timeline': [e1, e2]}
