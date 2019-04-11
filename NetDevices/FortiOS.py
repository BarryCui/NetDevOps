#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#This module is not completed yet
#not usable
from NetDevices.Device import Device
import paramiko

class FortiOS(Device):

    def __init__(self, device):
        super().__init__(device)

    async def login(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        await ssh.connect(self.mgt_ip, self.port, self.username, self.password)
        return ssh

    async def get_config(self):
        ssh = await login()
        stdin, stdout, stderr = await ssh.exec_command("show")
