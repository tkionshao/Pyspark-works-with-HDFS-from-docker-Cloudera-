docker run --hostname=quickstart.cloudera --name docker_cloudera --privileged=true -it -v /home/cyh/MEGA/MEGAsync/docker/cloudera/data:/data -p 50070:50070 -p 9000:9000 -p 8020:8020 -p 8888:8888 newcloudera /usr/bin/docker-quickstart

