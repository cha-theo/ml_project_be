from flask import Blueprint, request
from services import models_service
import logging 

api = Blueprint(
    name="models_controller",
    import_name="models_controller",
    url_prefix="/bnb/api/v1/models"
)

# main end point thats gets data from the form to calculate price from our model
@api.route("/", methods=['POST']) 
def model_response():
    data = request.json
    return (models_service.calculate_price(data)), 200


