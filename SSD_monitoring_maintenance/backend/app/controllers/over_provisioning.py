from flask import Blueprint, jsonify
from app.models.provisioning import OverProvisioningSettings
from app import db

over_provisioning_blueprint = Blueprint('over_provisioning', __name__)

@over_provisioning_blueprint.route('/over-provisioning', methods=['GET'])
def get_over_provisioning_settings():
    over_provisioning_settings = OverProvisioningSettings.query.first()
    return jsonify({'size_gb': over_provisioning_settings.size_gb})
