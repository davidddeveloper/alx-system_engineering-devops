#!/usr/bin/env python3
"""
this fabric script creates a database with at least one table and one row 
in (web-01) MYSQL Server to replicate from.
"""
from fabric.api import run, env


env.user = "ubuntu"
env.hosts = ["35.153.17.38", "54.90.53.190"]

def create_db():
    """
        creates database
    """

    sql_command = "CREATE DATABASE IF NOT EXISTS tyrell_corp;"
    run(f'echo "{sql_command}" | sudo mysql -u root')

def create_table():
    """
        creates table
    """
    sql_command = "\
    USE tyrell_corp;\
    CREATE TABLE IF NOT EXISTS nexus6(\
        id INT AUTO_INCREMENT PRIMARY KEY,\
        name VARCHAR(256));\
    INSERT INTO nexus6 (name) VALUES ('David'), ('Ben');\
    "
    #sql_command = f"{sql_command} CREATE TABLE IF NOT EXISTS nexus6("
    #sql_command = f"{sql_command}id INT AUTO_INCREMENT PRIMARY KEY,"
    #sql_command = f"{sql_command} name VARCHAR(256));"
    #sql_command = f"{sql_command} INSERT INTO nexus6 (name) VALUES ('David'), ('Ben');"

    run(f'echo "{sql_command}" | sudo mysql -u root')

def create():
    """
        creates database and table
    """
    create_db()
    create_table()
