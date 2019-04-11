#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import getpass
import paramiko
import time

def login(hostname, username, password, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    return ssh


if __name__ == '__main__':
    hostname = '10.3.0.253'
    username = 'icicle'
    password = 
    ssh = login(hostname, username, password)
    stdin, stdout, stderr = ssh.exec_command("dis cu")
    filename = "/root/device_cfg/" + hostname + str(time.strftime("%Y-%m-%d", time.localtime()))
    with open(filename, 'w') as file_object:
        for i in stdout.readlines():
            file_object.write(i)
