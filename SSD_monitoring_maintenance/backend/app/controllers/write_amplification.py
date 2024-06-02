from flask import Blueprint, jsonify
from app.models.amplification import WriteAmplificationSettings
from app import db

write_amplification_blueprint = Blueprint('write_amplification', __name__)

@write_amplification_blueprint.route('/write-amplification', methods=['GET'])
def get_write_amplification_settings():
    write_amplification_settings = WriteAmplificationSettings.query.first()
    return jsonify({'level': write_amplification_settings.level})
