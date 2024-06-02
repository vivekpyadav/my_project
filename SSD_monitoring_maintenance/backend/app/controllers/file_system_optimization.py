from flask import Blueprint, jsonify
from app.models.optimization import FileSystemOptimizationSettings
from app import db

file_system_optimization_blueprint = Blueprint('file_system_optimization', __name__)

@file_system_optimization_blueprint.route('/file-system-optimization', methods=['GET'])
def get_file_system_optimization_settings():
    optimization_settings = FileSystemOptimizationSettings.query.first()
    return jsonify({'enabled': optimization_settings.enabled})
