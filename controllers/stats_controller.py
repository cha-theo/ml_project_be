from flask import Flask, Blueprint, jsonify, request
from services import stats_service
import logging 

api = Blueprint(
    name="stats_controller",
    import_name="stats_controller",
    url_prefix="/bnb/api/v1/stats",
)


@api.route("/")
def stats():
    return (stats_service.stat_for_charts()), 200



@api.route("/raw_data")
def get_raw_data():
    return (stats_service.get_all_data()), 200


