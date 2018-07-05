# Pyspark works with HDFS from docker Cloudera 

## Preparation
Install --> Scala,
,JAVA
,Spark
,python3(Including ipython3)

> vim ~/.bashrc<br>

>export JAVA_HOME=/home/cloudera/jdk1.8.0_171
export PATH=$JAVA_HOME/bin:$PATH
>export SCALA_HOME=/home/cloudera/scala-2.11.12
export PATH=$SCALA_HOME/bin:$PATH
>export SPARK_HOME=/home/cloudera/spark-2.2.1-bin-hadoop2.6
export PATH=$SPARK_HOME/bin:$PATH
export PYSPARK_PYTHON=python3
export PYSPARK_DRIVER_PYTHON=ipython3



# Docker and HDFS
>docker pull quickstar/cloudera<br>

>docker run --hostname=quickstart.cloudera --name [give.name]] --privileged=true -it -v /home/cyh/MEGA/MEGAsync/docker/cloudera/data:/data -p 50070:50070 -p 9000:9000 -p 8020:8020 -p 8888:8888 quick/cloudera /usr/bin/docker-quickstart<br>

###
> docker exec -it [container.id] /bin/bash<br>

# Setting Authority
>sudo chmod 777 -R /tmp/hive<br>
>sudo su - hdfs
hadoop fs -chmod -R 777 /tmp/hive
exit<br>
> hadoop fs -mkdir /user/[user.name]/foods/input<br>
> hadoop fs -put ./data/[file] /user/[user.name]/foods/input<br>




# Port
8088 -> spark_status
7077 -> spark_cluster -> sc
50070 -> hadoop_status

# Start to use
>docker start 9b5b<br>
>docker exec -itd 9b5b /bin/bash<br>
>docker exec -it 9b5b /bin/bash<br>

### Please wait hdfs initial then do below commands

>cd ~/spark-2.2.1-bin-hadoop2.6/sbin<br>
>./start-all.sh<br>
>spark-submit --master spark://[user.name]:7077 foods_test.py

# Others

## Pyspark
>pyspark --master spark://[user.name]:7077<br>

## Docker 
>docker start [Container ID]<br>
>docker exec -itd [Container ID] /bin/bash<br>