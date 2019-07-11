import os

class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    GITHUB_TOKEN=os.environ['GITHUB_TOKEN']
    SENDGRID_API_KEY=os.environ['SENDGRID_API_KEY']
    TWILIO_ACCOUNT_SID=os.environ['TWILIO_ACCOUNT_SID']
    TWILIO_AUTH_TOKEN=os.environ['TWILIO_AUTH_TOKEN']

