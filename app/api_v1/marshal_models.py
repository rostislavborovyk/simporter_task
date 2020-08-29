from flask_restx import fields

from app import api

event_model = api.model('Timeline', {
    'date': fields.String,
    'value': fields.String,
})

events_model = api.model('Timeline', {
    'timeline': fields.List(fields.Nested(event_model)),
})
