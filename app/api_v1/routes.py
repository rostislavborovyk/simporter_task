import datetime

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
