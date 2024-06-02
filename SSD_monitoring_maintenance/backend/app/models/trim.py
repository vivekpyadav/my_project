# backend/app/models/trim.py

from .. import db  # Correcting the import statement

class TrimSettings(db.Model):
    """Model for Trim Settings."""
    id = db.Column(db.Integer, primary_key=True)
    # Define your trim settings columns here
    # For example:
    # trim_enabled = db.Column(db.Boolean, default=False)
    # trim_schedule = db.Column(db.String(50), default='daily')

    def __repr__(self):
        return '<TrimSettings {}>'.format(self.id)
