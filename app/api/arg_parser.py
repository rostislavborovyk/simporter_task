from flask_restx import reqparse

arg_parser = reqparse.RequestParser(bundle_errors=True)

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

arg_parser.add_argument(
    "asin",
    type=str
)

arg_parser.add_argument(
    "brand",
    type=str
)

arg_parser.add_argument(
    "stars",
    type=str,
    choices=("1", "2", "3", "4", "5"),
    help="Invalid choice:"
)
