from flask_restx import reqparse

arg_parser = reqparse.RequestParser()

# todo change to type date
arg_parser.add_argument("startDate", type=str, help="Date should be in format yyyy-mm-dd")
arg_parser.add_argument("endDate", type=str, help="Date should be in format yyyy-mm-dd")

arg_parser.add_argument(
    "Type",
    type=str,
    choices=("cumulative", "usual"),
    help="Invalid choice:")

arg_parser.add_argument(
    "Grouping",
    type=str,
    choices=("weekly", "bi-weekly", "monthly"),
    help="Invalid choice:"
)

# args = parser.parse_args()

# todo add filtering by attributes
