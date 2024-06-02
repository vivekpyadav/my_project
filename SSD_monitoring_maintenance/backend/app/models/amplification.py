# backend/app/models/amplification.py

from .. import db  # Correcting the import statement

class WriteAmplificationSettings(db.Model):
    """Model for Write Amplification Settings."""
    id = db.Column(db.Integer, primary_key=True)
    # Define your write amplification settings columns here

    def __repr__(self):
        return '<WriteAmplificationSettings {}>'.format(self.id)
