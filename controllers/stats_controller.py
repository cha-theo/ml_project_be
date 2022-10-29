from flask import Blueprint, jsonify, request
from services import stats_service
import logging 

api = Blueprint(
    name="stats_controller",
    import_name="stats_controller",
    url_prefix="/emp/api/v1/stats",
)


@api.route("/")
def stats():
    return "Hello", 200



@api.route("/raw_data")
def get_raw_data():
    return (stats_service.get_all_data()), 200


@api.route("/max_id")
def get_max_host_id():
    return (stats_service.max_host_id()), 200

