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
    execute https://github.com/davidddeveloper/alx-system_engineering-devops/blob/master/0x14-mysql/1-install_mysql57 to install mysql














