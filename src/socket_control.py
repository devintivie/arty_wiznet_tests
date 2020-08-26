# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:41:07 2017

@author: devin
"""

import socket
from datetime import datetime
from time import sleep
import time

class socket_control:
    def __init__(self, iAddr, iPort = 5025):
        self.ip_addr = iAddr
        self.port = iPort
        
    def __del__(self):
        self.close()

    def connect(self, Mode = 'TCP'):
        if Mode == 'TCP' :
            print('IP = {} and port = {}'.format(self.ip_addr, self.port))
            self.Socket = socket.create_connection([self.ip_addr, self.port], timeout = 3)
        else:
            self._udp = socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._udp.settimeout(3)
        
    def close(self):
        self.Socket.close()
        
    def send(self, String):
        ByteString = bytes(String, encoding = 'utf-8')
        self.Socket.send(ByteString)
        return self.receive()
        
    def receive(self, MaxBytes=2048):
        ByteString = self.Socket.recv(MaxBytes)
        String = str(ByteString, encoding = 'utf-8')
        if String.endswith('\n'):
            String = String.rstrip('\n')
        return String
        
    
        
        
        
        