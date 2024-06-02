from flask import Flask
from .controllers.health_monitoring import health_monitoring_blueprint
from .controllers.trim_management import trim_management_blueprint
from .controllers.file_system_optimization import file_system_optimization_blueprint
from .controllers.write_amplification import write_amplification_blueprint
from .controllers.over_provisioning import over_provisioning_blueprint
from .controllers.swap_optimization import swap_optimization_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(health_monitoring_blueprint)
    app.register_blueprint(trim_management_blueprint)
    app.register_blueprint(file_system_optimization_blueprint)
    app.register_blueprint(write_amplification_blueprint)
    app.register_blueprint(over_provisioning_blueprint)
    app.register_blueprint(swap_optimization_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
