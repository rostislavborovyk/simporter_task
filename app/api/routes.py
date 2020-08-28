from app.api import api_bp
from app import api
from flask_restx import Resource

from app.api.arg_parser import arg_parser
from app.api.dao import EventDao
from app.api.marshal_models import time_line_model
from app.api.data_processor import dp

import datetime


@api_bp.route('/timeline')
class Todo(Resource):
    @api.marshal_with(time_line_model)
    def get(self, **kwargs):
        args = arg_parser.parse_args()

        data = dp.get_data(
            start_date=int(datetime.datetime.fromisoformat(args.get("startDate", None)).timestamp()),
            end_date=int(datetime.datetime.fromisoformat(args.get("endDate", None)).timestamp()),
            grouping=args.get("Grouping", None),
            data_type=args.get("Type", None),
            asin=args.get("asin", None),
            brand=args.get("brand", None),
            stars=args.get("stars", None),
        )

        response_data = [
            EventDao(date=obj_date.strftime("%y-%m-%d"), value=obj_values["id"])
            for obj_date, obj_values in data.iterrows()
        ]

        return {'timeline': response_data}

# todo add info method
