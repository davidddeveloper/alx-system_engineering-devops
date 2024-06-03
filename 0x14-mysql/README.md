# MySQL MASTER-SLAVE REPLICATION

Replication definition
replication means have multiple copies of your databases, such that if one fails the other will act as a failover. The master-slave replaction works like this; we are going to have a primary db server that we are going to do every event that involves writing (INSERTING, DELETING and UPDATING), next we are going to have a replica/slave which is going to be an exact copy of master on a different server, the slave will handle all read operation.

As we can see from the explanation above, master-slave replication have two benefits
  - (redundancy) - we have a fallback incase something goes wrong. This ensures data availability at all time.
  - (High availabilty) - since load are shared between master and slave, it ensures speed.

You might be interested in how mysql implements master-slave replaction. This is how it does it underhood after you've setup correctly.

mysql keeps record of all the operation done in the master mysql server in a file called mysql-bin.log.
the slave mysql server will read from this file everytime there is a change and copies everything to a file in the server where the mysql slave server resides called mysql-relay.log
the slave will start executing everythin in the relay log on the mysql server. This thus ensure the master and slave are in sync.

Now lemme get you through quickly how to setup the mysql master-slave replication.

## STEP 1: Install MYSQL57
  execute ![1-install_mysql57](https://github.com/davidddeveloper/alx-system_engineering-devops/blob/master/0x14-mysql/1-install_mysql57) to install mysql

## STEP 2: CREATE DATABASE and TABLE in both servers
Inorder to setup mysql master-slave replication you did to have a database and at least one record
  execute the fabric script ![create_db_and_table.py](https://github.com/davidddeveloper/alx-system_engineering-devops/blob/master/0x14-mysql/create_db_and_table.py)
  
    example: fab -i /vagrant/key -f create_db_and_table.py create

  ## STEP 3: CREATE A slave replica_user
  You did to create a replica user and grant it the SLAVE privileges, like so
  GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

  I have already did it for you in this fabric script: ![create_replica_user.py](https://github.com/davidddeveloper/alx-system_engineering-devops/blob/master/0x14-mysql/create_replica_user.py)

    example: fab -i /vagrant/key -f create_replica_user.py create_replica_user

Next we need to setup master and slave. I've written the following bash script to assist you: ![setup_master](https://github.com/davidddeveloper/alx-system_engineering-devops/blob/master/0x14-mysql/setup_master) and ![setup_slave](https://github.com/davidddeveloper/alx-system_engineering-devops/blob/master/0x14-mysql/setup_slave)

But this part is crucial, so I'm going to show you here

## STEP 4: SETUP MASTER
  ### step 1
    open this file: sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
  ### step 2: add the following
    add the following
    server-id        = 1
    log_bin          = /var/log/mysql/mysql-bin.log # binary log - record changes made to the db in binary formart
    binlog_do_db     = tyrell_corp

  note: remember to comment this line if you see it
      bind-address 127.0.0.1

  ### step 3: find coordinates of master
  the slave is going to need two coordinates
  the binary-log file and the position to read from
  here's how to find those information
  
    FLUSH TABLES WITH READ LOCK;
    SHOW MASTER STATUS;

  status should look like this
  
    mysql-bin.000002        154     tyrell_corp,tyrell_corp

  ### step 4: create a dump utility
  a dump is a backup of your database, the slave is going to need it so let's create it

    example: sudo mysqldump tyrell_corp > tyrell_corp.sql

  At this point you should now know the following information
    - binary log file
    - position to read from
    - sql backup

  note: make sure to transfer your sql backup to the server where mysql slave resides
  
      example: scp -i /vagrant/key backup.sql ubuntu@ip:/tmp/

STEP 5: setup slave
again i've written a script, but i'm going to show you here how to do it.
  step 1: 
  
    open this file: sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf

  step 2: add the following
  
    server-id               = 2
    log_bin                 = /var/log/mysql/mysql-bin.log
    binlog_do_db            = tyrell_corp
    relay-log               = /var/log/mysql/mysql-relay-bin.log 
    # Contain everything read from master bin log
    # Store events that need to be applied to slave db locally
    # Events are read from relay log and applied to slave

  step 3: configure the replication by running the following in mysql server
  
    configure replication by running
    CHANGE MASTER TO
    MASTER_HOST='master_ip',
    MASTER_USER='replica_user',
    MASTER_PASSWORD='password#70',
    MASTER_LOG_FILE='mysql-bin.000001',
    MASTER_LOG_POS=154;

  this is just an example, remember to replace
  MASTER_LOG_POS, MASTER_LOG_FILE, MASTER_PASSWORD (the password you set for replica_user)
  with you own from above, where you setup master

  ### step 4: start slave
    START SLAVE;
    SHOW SLAVE STATUS\G;

## Step 6: confirm replication
if you have no errors up to this point it means replication should now wrok, but to confirm try doing some operation in master

    example:
      USE tyrell_corp;
      INSERT INTO nexus6 (name) VALUES ('David'), ('Ben');
      SELECT * FROM nexus6;
        id  | name
        1   | David
        2   | Ben

Now go to you replica/slave server and select

    SELECT * FROM nexus6;
        id  | name
        1   | David
        2   | Ben

If you see the same output it means replica is setup correctily.











