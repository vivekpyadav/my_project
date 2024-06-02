from flask import Blueprint, jsonify
from app.models.ssd import SSD
from app import db

health_monitoring_blueprint = Blueprint('health_monitoring', __name__)

@health_monitoring_blueprint.route('/ssds', methods=['GET'])
def get_ssd_health():
    ssds = SSD.query.all()
    ssd_data = [{'model': ssd.model, 'health_status': ssd.health_status} for ssd in ssds]
    return jsonify(ssd_data)

@health_monitoring_blueprint.route('/ssds/usage', methods=['GET'])
def get_ssd_usage():
    ssds = SSD.query.all()
    usage_data = [{'model': ssd.model, 'read_cycles': ssd.read_cycles, 'write_cycles': ssd.write_cycles, 'used_space': ssd.used_space, 'total_space': ssd.total_space} for ssd in ssds]
    return jsonify(usage_data)

@health_monitoring_blueprint.route('/ssds/lifespan', methods=['GET'])
def get_ssd_lifespan():
    ssds = SSD.query.all()
    lifespan_data = []

    for ssd in ssds:
        # Simple estimation logic (for illustration purposes)
        estimated_lifespan = (ssd.total_space / (ssd.read_cycles + ssd.write_cycles + 1)) * 100  # Simplified formula
        lifespan_data.append({
            'model': ssd.model,
            'estimated_lifespan': estimated_lifespan,
            'used_space': ssd.used_space,
            'total_space': ssd.total_space
        })

    return jsonify(lifespan_data)
