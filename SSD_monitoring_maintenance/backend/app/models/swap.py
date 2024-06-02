# backend/app/models/swap.py

from .. import db  # Correcting the import statement

class SwapOptimizationSettings(db.Model):
    """Model for Swap Optimization Settings."""
    id = db.Column(db.Integer, primary_key=True)
    # Define your swap optimization settings columns here

    def __repr__(self):
        return '<SwapOptimizationSettings {}>'.format(self.id)
