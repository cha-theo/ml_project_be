from flask import Blueprint
from bnb_base_logger import logger

api = Blueprint(
    name="ping_controller",
    import_name="ping_controller",
    url_prefix="/bnb/api/v1/ping"
)


@api.route("/")
def ping():
    return "Pong",200


