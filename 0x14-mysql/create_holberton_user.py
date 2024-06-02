#!/usr/bin/env python3
"""
a fabric script to create a  MySQL user named holberton_user on both web-01 and web-02
"""

from fabric.api import env, run
env.user="ubuntu"
env.hosts=["35.153.17.38", "54.90.53.190"]

def create_user(pwd):
	sql_command = f"CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY \"{pwd}\";"
	sql_command = f"{sql_command} GRANT ALL ON *.* TO holberton_user@localhost"
	run(f"echo '{sql_command}' | sudo mysql -u root")

