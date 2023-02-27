import os
from datetime import timedelta

class Config(object):
    DEBUG = True
     # MQTT Brocker Configuration 
    MQTT_BROKER_URL = 'broker.emqx.io'
    MQTT_BROKER_PORT=1883
    MQTT_USERNAME=""
    MQTT_PASSWORD=""
    MQTT_KEEPALIVE=5
    MQTT_TLS_ENABLED=False

    # Celery Configuration 
    BROKER_URL ="redis://redis:6379/0"
    CELERY_RESULT_BACKEND ="redis://redis:6379/0"
    CELERY_DEFAULT_QUEUE ="test_queue"

    # # Celery Beat 
    # CELERYBEAT_SCHEDULE = {
    # 'periodic_task': {
    #     'task': 'apps.mqtt_module.task.periodic_task',
    #     # Every minute
    #     'schedule': crontab(minute="*"),
    #     }
    # }



class TestingConfig(Config):
    TESTING = True
    MY_DB ="db.your.configuration.url"
    WTF_CSRF_ENABLED = False
