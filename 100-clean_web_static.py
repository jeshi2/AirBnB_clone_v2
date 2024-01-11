#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
""'
from fabric.api import env, run, local, lcd
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<your_username>'
env.key_filename = '<path_to_your_ssh_keys>'
def do_clean(number=0):
"""
Deletes out_of_date archives
"""
