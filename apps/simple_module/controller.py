from flask import Blueprint, request, jsonify,current_app
from apps.factory import executor
#from run import mqtt_client

import os



# setting up blueprint
simple_blueprint= Blueprint('simple_module',__name__,url_prefix='/simple_module')



def long_task(test_param):
    # Magic to send an email

    import time

    # printing the start time
    print("The time of code execution begin is : ", time.ctime())

    # using sleep() to hault the code execution
    time.sleep(15)

    # printing the end time
    print("The time of code execution end is : ", time.ctime())


    return True


@simple_blueprint.route('/long_task_endpoint')
def long_task_api():
    # Do signup form
    current_app.logger.info("TTttttttTTTTTTTTTTTTTT")
    print(executor)
    executor.submit(long_task," test")
    return jsonify({})