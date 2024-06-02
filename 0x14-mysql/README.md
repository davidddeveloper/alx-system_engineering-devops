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
    open this file: vi /etc/mysql/mysql.conf.d/mysqld.cnf
  ### step 2: add the following
    add the following
    server-id        = 1
    log_bin          = /var/log/mysql/mysql-bin.log # binary log - record changes made to the db in binary formart
    binlog_do_db     = tyrell_corp

  note: remember to comment this line if you see it
      bind-address 127.0.0.1

  ### step 3: 












