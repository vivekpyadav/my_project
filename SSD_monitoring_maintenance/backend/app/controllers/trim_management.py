# Import necessary libraries
from flask import Blueprint, jsonify
from app.models.trim import TrimSettings
from app import db

# Create a Blueprint for the trim management controller
trim_management_blueprint = Blueprint('trim_management', __name__)

# Define a route to retrieve trim settings
@trim_management_blueprint.route('/trim', methods=['GET'])
def get_trim_settings():
    trim_settings = TrimSettings.query.first()
    return jsonify({'trim_enabled': trim_settings.enabled})
