from datetime import datetime
from werkzeug.exceptions import BadRequest
from flask_restx import Resource

from app.api_v1.arg_parser import arg_parser
from app.api_v1.dao import EventDao
from app.api_v1.marshal_models import events_model
from app.api_v1.data_processor import dp
from app.api_v1 import ns


@ns.route('/timeline')
class Timeline(Resource):

    @ns.doc("List of events")
    @ns.marshal_with(events_model)
    @ns.expect(arg_parser)
    def get(self, **kwargs):
        args = arg_parser.parse_args()

        raw_start_date = args.get("startDate", None)
        raw_end_date = args.get("endDate", None)

        if raw_start_date is not None:
            start_date = int(datetime.fromisoformat(raw_start_date).timestamp())
        else:
            start_date = None

        if raw_start_date is not None:
            end_date = int(datetime.fromisoformat(raw_end_date).timestamp())
        else:
            end_date = None

        if start_date is not None and end_date is not None and start_date > end_date:
            raise BadRequest("startDate should be less then endDate")

        data = dp.get_data(
            start_date=start_date,
            end_date=end_date,
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
