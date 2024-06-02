# Import necessary libraries
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for our models
Base = declarative_base()

# Define the User model class
class User(Base):
    # Table name
    __tablename__ = 'user'

    # Table columns
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))

    # Constructor method
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
