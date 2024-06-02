""" 
this script give access alx access to my servers
"""


from fabric.api import env, run
env.user="ubuntu"
env.hosts=['ubuntu@54.90.53.190']

def access(key):
    file_name="~/.ssh/authorized_keys"
    run(f"sudo echo '{key}' >> {file_name}")
