from app import api
from flask_restx import fields

event_model = api.model('PointModel', {
    'date': fields.String,
    'value': fields.String,
})

time_line_model = api.model('TimeLineModel', {
    'timeline': fields.List(fields.Nested(event_model)),
})
