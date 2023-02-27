import random
import requests
from apps.factory import celery
from flask import current_app
from apps.factory import device_id




@celery.task(name="worker_name",bind=True,queue="test_que")
def task(self,**kwargs):

    request_params = kwargs.get('test')

    #setting up logs
    current_app.logger.info("Task Received and executed")
    current_app.logger.info(request_params)



@celery.task(queue="test_que")
def periodic_task():
    print('Hi! from periodic_task',flush=True)
    list1 = ['1', '2', '3', '4', '5','6']
    device_name = device_id
    #publish_result = mqtt_client.publish('server', 'SENSOR DATA '+ device_name)
    data_to_send = {
                        "topic":"server",
                        "msg": "SENSOR "+device_name + ' VALUE - '+random.choice(list1)
                    }
    #res = requests.post('http://192.168.1.6:80/dummy_module/publish', json=data_to_send)
    res = requests.post('http://0.0.0.0:9001/dummy_module/publish', json=data_to_send)
    #print ('response from server:',res.text)

    current_app.logger.info("Data pushed to server")
    current_app.logger.info(data_to_send.get('msg'))
    current_app.logger.info('---------------------------------')