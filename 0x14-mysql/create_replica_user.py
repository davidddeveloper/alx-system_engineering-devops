#!/usr/bin/env python3
"""
    this script creates a replica user for the primary MYSQL SERVER in web-01
"""

from fabric.api import run, env

env.user = "ubuntu"
env.hosts = ["35.153.17.38"]

def create_replica_user(pwd):
    """
        creates a replica user for MYSQL SERVER in web-01
    """
    sql_command = f'CREATE USER IF NOT EXISTS "replica_user"@"%" IDENTIFIED BY "{pwd}";'

    run(f"echo '{sql_command}' | sudo mysql -u root")

    sql_command = 'GRANT REPLICATION SLAVE ON *.* TO "replica_user"@"%";'

    run(f"echo '{sql_command}' | sudo mysql -u root")
