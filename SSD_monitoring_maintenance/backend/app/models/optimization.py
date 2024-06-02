# backend/app/models/optimization.py

from .. import db  # Correcting the import statement

class FileSystemOptimizationSettings(db.Model):
    """Model for File System Optimization Settings."""
    id = db.Column(db.Integer, primary_key=True)
    # Define your file system optimization settings columns here
    # For example:
    # optimization_enabled = db.Column(db.Boolean, default=False)
    # optimization_schedule = db.Column(db.String(50), default='weekly')

    def __repr__(self):
        return '<FileSystemOptimizationSettings {}>'.format(self.id)
