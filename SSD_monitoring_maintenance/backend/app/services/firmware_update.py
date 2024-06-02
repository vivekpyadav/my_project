from app.models.ssd import SSD
from app import db

def update_firmware(ssd_id, new_firmware_version):
    """
    Update the firmware version of an SSD.
    Args:
        ssd_id (int): The ID of the SSD.
        new_firmware_version (str): The new firmware version.
    Returns:
        bool: True if the firmware update was successful, False otherwise.
    """
    ssd = SSD.query.get(ssd_id)
    if ssd:
        ssd.firmware_version = new_firmware_version
        db.session.commit()
        return True
    else:
        return False
