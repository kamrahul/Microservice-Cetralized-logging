# Flask-background worker
 
##  use correct version of Python when creating VENV
python3 -m venv venv

##  activate on Unix or MacOS
source venv/bin/activate

##  activate on Windows (cmd.exe)
venv\Scripts\activate.bat

##  activate on Windows (PowerShell)
venv\Scripts\Activate.ps1

##  Activated environment will appear
(venv) D:\Flask-Simple-app>

# Send request below which will execute a long running tasks but the api will give quick response.
<pre>

curl --location --request GET 'http://127.0.0.1:9001/simple_module/long_task_endpoint'
</pre>

# Setting up requirements

## requirement.txt
### -  Create requirements.txt file
### - Add flask as primary requirement
### - celery==5.2.7 , redis

##  install the modules in your requirements.txt file

### pip install -r requirements.txt

# Run the application 
## Run docker compose file up command
<pre>
docker compose -f "docker-compose.yml" up -d --build 
</pre>



# Overall Fluent Bit implementation 
## Docker compose will up 3 containers 
-  flask service which prints stdout statements
-  fluent bit container 
-  Elastic search 


# Send request below which will execute a task with a print statement provided
<pre>

curl --location --request GET 'http://127.0.0.1:9001/simple_module/long_task_endpoint'
</pre>

### This reqeuest will be logged to stdout and will be read by fluent bit input plugin and send the data to elastic cloud using output plugin

#### The fluent bit configruation can be found on fluent-bit/fluent-bit.conf
<pre>
[SERVICE]
    log_level debug

[INPUT]
    Name forward
    Listen 0.0.0.0
    port 24224

[OUTPUT]

    Name es   // this tells that the output would be sent to elastic search
    Match **
    Host elasticsearch  // Name of the docker name
    Port 9200 // port which es runs
    # When Logstash_Format is enabled, the Index name is composed using a prefix and the date
    Logstash_Format True

</pre>

## Check if data is getting saved in elastic
- Go to elastic search server
- curl localhost:9200/_cat/indices
- This will show all the indexes
- curl localhost:9200/logstash-2023.02.27/_search?pretty=true&q={'matchAll':{''}}

# References
### https://docs.fluentd.org/v/0.12/container-deployment/docker-compose
### https://kevcodez.de/posts/2019-08-10-fluent-bit-docker-logging-driver-elasticsearch/

### https://www.velebit.ai/blog/tech-blog-connecting-elasticsearch-logs-to-grafana-and-kibana/