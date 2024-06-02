# backend/app/models/provisioning.py

from .. import db  # Correcting the import statement

class OverProvisioningSettings(db.Model):
    """Model for Over-Provisioning Settings."""
    id = db.Column(db.Integer, primary_key=True)
    # Define your over-provisioning settings columns here

    def __repr__(self):
        return '<OverProvisioningSettings {}>'.format(self.id)
