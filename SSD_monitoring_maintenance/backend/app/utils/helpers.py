def calculate_remaining_lifetime(health_status):
    """
    Calculate the remaining lifetime of an SSD based on its health status.
    Args:
        health_status (int): The health status of the SSD (e.g., percentage).
    Returns:
        float: The remaining lifetime of the SSD (in years).
    """
    # Example logic to calculate remaining lifetime based on health status
    remaining_lifetime = (100 - health_status) / 100 * 5  # Assuming 5 years lifespan
    return remaining_lifetime
