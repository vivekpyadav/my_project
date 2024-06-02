# Import necessary libraries
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for our models
Base = declarative_base()

# Define the SSD model class
class SSD(Base):
    # Table name
    __tablename__ = 'ssds'

    # Table columns
    id = Column(Integer, primary_key=True)
    model = Column(String(100))
    capacity_gb = Column(Integer)
    health_status = Column(String(50))

    # Constructor method
    def __init__(self, model, capacity_gb, health_status):
        self.model = model
        self.capacity_gb = capacity_gb
        self.health_status = health_status
