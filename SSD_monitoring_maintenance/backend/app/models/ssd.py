from app import db

class SSD(db.Model):
    __tablename__ = 'ssds'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80), unique=True, nullable=False)
    health_status = db.Column(db.String(120), nullable=False)
    read_cycles = db.Column(db.Integer, nullable=False, default=0)
    write_cycles = db.Column(db.Integer, nullable=False, default=0)
    used_space = db.Column(db.Float, nullable=False, default=0.0)  # In GB
    total_space = db.Column(db.Float, nullable=False, default=0.0)  # In GB
