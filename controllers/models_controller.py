from flask import Blueprint, request
from services import models_service
import logging 

api = Blueprint(
    name="models_controller",
    import_name="models_controller",
    url_prefix="/emp/api/v1/models"
)

# main end point thats gets data from the form
@api.route("/", methods=['POST', 'GET']) 
def model_response():
    data = request.json
    return (models_service.test_function_with_data(data)), 200


