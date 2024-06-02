from app.models.ssd import SSD
from app import db

def get_smart_data(ssd_id):
    """
    Retrieve SMART data for a specific SSD.
    Args:
        ssd_id (int): The ID of the SSD.
    Returns:
        dict: SMART data for the SSD.
    """
    ssd = SSD.query.get(ssd_id)
    if ssd:
        smart_data = {
            'temperature': ssd.temperature,
            'power_on_hours': ssd.power_on_hours,
            'remaining_lifetime': ssd.remaining_lifetime
        }
        return smart_data
    else:
        return None
