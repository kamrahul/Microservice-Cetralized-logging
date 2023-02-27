import logging
import os
import sys

#from celery import Celery
from flask import Flask
from flask_executor import Executor

executor = Executor()

#initializing celery
# celery = Celery(__name__, include=["apps.mqtt_module.task"])

def create_app(config_type=None):
    
    # Create flask app object
    app = Flask(__name__)

    executor.init_app(app)

    # Setting configuration for the project 
    app.config.from_object(config_type)

    # Adding log level
    app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
    app.logger.setLevel(logging.DEBUG)

    #Register blueprint
    from apps.simple_module.controller import simple_blueprint
    app.register_blueprint(simple_blueprint)

    return app

