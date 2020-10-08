# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 15:41:07 2017

@author: devin
"""

import socket
import sys
from datetime import datetime
from time import sleep
import time
import enum

version = sys.version_info[0]

class socket_control:
    def __init__(self, iAddr, iPort = 5025):
        self.ip_addr = iAddr
        self.port = iPort
        self.status = connection_status.idle
        
    def __del__(self):
        self.close()

    @property
    def is_connected(self):
        return self.status == connection_status.connected

    def connect(self, Mode = 'TCP'):
        if Mode == 'TCP' :
            print('IP = {} and port = {}'.format(self.ip_addr, self.port))
            self._socket = socket.create_connection([self.ip_addr, self.port], timeout = 3)
            self.status = connection_status.connected
        else:
            self._socket = socket(socket.AF_INET, socket.SOCK_DGRAM)
            self._socket.settimeout(3)
        
    def close(self):
        try:
            self._socket.close()
        except AttributeError:
            pass
        finally:
            self.status = connection_status.closed
        
        
    def send(self, String, toLog = False, delay = 0):
        ByteString = bytes(String, encoding = 'utf-8')

        if self.is_connected :
            if version == 3 :
            
                try:
                    self._socket.send(ByteString)
                except socket.timeout as stex:
                    self.status = connection_status.timeout
                    return stex.strerror
                sleep(delay)
                return self.receive()
            else:
                try:
                    self._socket.send(String)
                except socket.timeout as stex:
                    self.close()
                    return stex.strerror
                sleep(delay)
                return self.receive()
        return 'Not Connected'

    def receive(self, MaxBytes=2048):
        if self.is_connected:
            if version == 3:
                try:
                    ByteString = self._socket.recv(MaxBytes)
                except socket.timeout as stex:
                    ByteString = b'-1'
                except ConnectionResetError:
                    self.close()
                    ByteString = b'-1'
                String = str(ByteString, encoding='utf-8')
                String = String.replace('\r','').replace('\n', '')
                return String
            else:
                try:
                    ByteString = self._socket.recv(MaxBytes)
                except socket.timeout as stex:
                    ByteString = b'-1'
                except ConnectionResetError:
                    self.close()
                    ByteString = b'-1'
                String = str(ByteString, encoding='utf-8')
                String = String.replace('\r','').replace('\n', '')
                return String
        return 'Not Connected'

    def print_hex(self, string):
        tempString = ":".join('{:02x}'.format(ord(c)) for c in string)
        print(tempString)


class connection_status(enum.Enum):
    idle = 1
    connecting = 2
    connected = 3
    canceled = 4
    closed = 5
    timeout = 6
    socket_error = 7
    bad_port = 8



if __name__ == "__main__":
    test = socket_control('169.254.208.100', 5025)
    print(test.is_connected)

    try:
        test.connect()
        sleep(0.5)
        print(test.is_connected)
        sleep(1)

    finally:
        test.close()
        print(test.is_connected)






    
        
        
        
        

