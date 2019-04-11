#!/home/py3/bin/python
# -*- coding: utf-8 -*-
#Import modules
import paramiko
import time
import yaml
import sys
import time
import os

class Device():
    '''
    Read from a yaml file.
    Take a dictionary as input.
    The keys of the dictionary are:
        hostname(hostname of the device)
        mgt_ip(ip address of the device)
        username(login username)
        password(login password)
        port(port, default 22)
    '''
    def __init__(self, device):
        self.hostname = device.get("hostname")
        self.mgt_ip = device.get("mgt_ip")
        self.username = device.get("username")
        self.password = device.get("password")
        self.port = device.get("port", 22)
    #login method
    def login(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.mgt_ip, self.port, self.username, self.password)
        return ssh

#Method of getting configs
def get_config(device):
    fw = Device(device)
    ssh = fw.login()
    stdin, stdout, stderr = ssh.exec_command("show")
    filename = FILEPATH + r"/" + fw.hostname
    with open(filename, 'w') as file_object:
        for i in stdout.readlines():
            file_object.write(i)
        print("%s is saved" % filename)

#Path to be saved
FILEPATH = "/home/NetBackup/firewalls_cfg/" + str(time.strftime("%Y-%m-%d", time.localtime()))
deviceinfos = {}

#Create path if not exist
if not os.path.exists(FILEPATH):
    os.makedirs(FILEPATH)

#Print error information if no yaml config file given
try:
    yaml_cfg = sys.argv[1]
except IndexError:
   print("please give yaml configure file")
   sys.exit(1)

#Read a yaml file
f =  open(yaml_cfg)
deviceinfos = yaml.load(f.read())

#For each device in the yaml file, get config and save to file
for i in deviceinfos.get("devices"):
    get_config(i)
