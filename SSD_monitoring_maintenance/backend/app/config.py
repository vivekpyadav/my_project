# Import necessary libraries
import os

# Define the base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

# Define the database URL based on the chosen database system
# For SQLite (local file-based database)
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data', 'ssd_data.db')

# For PostgreSQL (replace 'username', 'password', 'host', 'port', 'database_name' with you>
# SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@host:port/database_name'

# Additional configurations (optional)
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking to improve performance

# Define the AppConfig class for additional application configurations
#class AppConfig:
 #   DEBUG = True  # Set to False in production
  #  SECRET_KEY = 'mivivim'
    # Add more application configurations as needed
