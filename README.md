# Installation

## Preparation

- cmake v3.1 or higher

  `sudo apt-get install cmake`

- g++ v4.8.4

  `sudo apt-get install g++`

- Redis v3.2.8 or higher

  Download and install **redis-3.2.8.tar.gz**.

  `tar -zxvf redis-3.2.8.tar.gz`

  `cd redis-3.2.8.tar.gz`

  `make`

  `sudo make install`

  Install redis as a background daemon. You can just use the default settings.

  `cd utils`

  `sudo ./install_server.sh`

  Configure redis to be remotely  accessible.

  `sudo service redis_6379 stop`

  Edit */etc/redis/6379.conf*. Find the line with <u>bind 127.0.0.0</u> and modify it with <u>bind 0.0.0.0</u>

  sudo service redis_6379 start

- hiredis

  `Download and install hiredis`

  `tar -zxvf hiredis.tar.gz`

  `cd hiredis`
  `make` 

  `sudo make install`

- gf-complete v1.03

  `tar -zxvf gf-complete.tar.z`

  `cd gf-complete`

  `./autogen.sh`

  `./configure`

  `make`

  `sudo make install`

- ISA-L v2.14.0 or higher

  Download and install isa-2.14.0.tar.gz.

  `tar -zxvf isa-l-2.14.0.tar.gz`

  `./autogen.sh`

  `./configure`

  `make`

  `sudo make install` 

- maven v3.5.0 or higher 

  `tar -zxvf apache-maven-3.5.0-bin.tar.gz`

  Set the environment variables.

  `export M2_HOME=/home/openec/apache-maven-3.5.0`

  `export PATH=$PATH:$M2_HOME/bin`

- java8

- HDFS-3

  Download and install HDFS3

  `tar -zxvf hadoop-3.0.0-src.tar.gz`

  Set the environment variables.

  `export HADOOP SRC DIR=/home/openec/hadoop-3.0.0-src`

  `export HADOOP HOME=$HADOOP SRC DIR/hadoop-dist/target/hadoop-3.0.0`

  `export PATH=$HADOOP HOME/bin:$HADOOP HOME/sbin:$PATH`

  `export HADOOP CLASSPATH=$JAVA HOME/lib/tools.jar:$HADOOP CLASSPATH`

  `export CLASSPATH=hadoop classpath -globa`

  `export LD LIBRARY PATH=$HADOOP HOME/lib/native:$JAVA HOME/jre/lib/`

  `amd64/server/:/usr/local/lib:$LD LIBRARY PATH`

- Hybridlazy

  Download hybridlazy and extract the code to /home/openec/. We can install HybridLazy into HDFS-3 by simply run the script *install.sh*. 

​		`tar -zxvf hybridlazy.tar.gz`

​		`cd hybridlazy/hdfs3-integration`

​		`./install.sh`

​		Run the following commands to compile HybridLazy for HDFS-3.

​		`cd HybridLazy`

​		`cmake . -DFS_TYPE:STRING=HDFS3`

​		`make`

## HDFS-3 Configuration



## Run

Please make sure that you have configured HDFS-3 successfully and correctly.

Then you can run coordinator by the script *start_coor.sh*.

`cd hdbridlazy`

`./start_coor.sh`

Then you can run all agents by the script start_all_ag.py.

`./start_all_ag.py`

## Write

Before you start writing blocks into bybridlazy, you should start the encoding daemon of OpenEC by the follwing command.Please make sure that this command is excuted in the agent's node. 

`./OECClient startEncode`

You can write blocks into hybridlazy by the script *encode.sh*. Please make sure that encode.sh is excuted in the agent's node. 

`./encode.sh stripe_num k block_path saveas ec_pool_id ec_policy block_size`

After finishing the encoding, you can stop the encoding daemon by the following command. Please make sure that this command is excuted in the agent's node.

`./OECClient stopEncode`

## Read

You can read file by the following command. Please make sure that this command is excuted in the agent's node.

`./OECClient read inputfilename saves`

## Repair

You can repair the failed blocks by the following command. Please make sure that this command is excuted in the agent's node.

`./OECClient startRepair`

After finishing the repair, you can stop repair by the following command. Please make sure that this command is excuted in the agent's node.

`./OECClient stopRepair`

## Stop

You can stop the coordinator and all agents by the script *stop.sh*. 

`./stop.sh`
