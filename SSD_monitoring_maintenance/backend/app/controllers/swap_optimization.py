from flask import Blueprint, jsonify
from app.models.swap import SwapOptimizationSettings
from app import db

swap_optimization_blueprint = Blueprint('swap_optimization', __name__)

@swap_optimization_blueprint.route('/swap-optimization', methods=['GET'])
def get_swap_optimization_settings():
    swap_optimization_settings = SwapOptimizationSettings.query.first()
    return jsonify({'enabled': swap_optimization_settings.enabled})

