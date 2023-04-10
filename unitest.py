#!/usr/bin/env python3

import unittest
from netmiko import ConnectHandler

def fetchip(org_IP):
    R3 = {"device_type" : 'cisco_ios','ip' : '198.51.100.13','username' : 'netman','password' : 'netman','secret' : 'netman', }
    net_connect = ConnectHandler(**R3)
    net_connect.enable()
    output = net_connect.send_command('sh ip int loop99')
#    print(output)
    for line in output.split("\n"):
        if "Internet address" in line:
            ip = line.split()[-1]
#            print(ip)
            break
    if org_IP == ip:
        return True
    else:
        return False

def fetcharea():
    R1 = {"device_type" : 'cisco_ios','ip' : '198.51.100.11','username' : 'netman','password' : 'netman','secret' : 'netman', }
    net_connect = ConnectHandler(**R1)
    net_connect.enable()
    output = net_connect.send_command('sh ip ospf | in area')
#    print(output)
    for line in output.split("\n"):
        if "Number of areas in this router" in line:
            area = line.split()[-7]
            print("Total number of areas: "+area)
            break
    if area == "1.":
        return True
    else:
        return False
            

def pingR2R5():
    R2 = {"device_type" : 'cisco_ios','ip' : '198.51.100.12','username' : 'netman','password' : 'netman','secret' : 'netman', }
    net_connect = ConnectHandler(**R2)
    net_connect.enable()
    output = net_connect.send_command('ping 10.1.5.1 source 10.1.2.1')
    print(output)
    for line in output.split("\n"):
        if "!!!!!" in line:
            result = line
            break
    if result == "!!!!!":
        return True
    else:
        return False

class TestConfiguration(unittest.TestCase):
    def testR3loop99ip(self):
        print("\nTesting IP address of Loopback99 interface on R3 to 10.1.3.1/24....")
        self.assertTrue(fetchip("10.1.3.1/24"))

    def testR1area(self):
        print("\nTesting number of areas on R1....")
        self.assertTrue(fetcharea())


    def testR2pingR5(self):
        print("\nTesting reachability from R2 loopback to R5 loopback....")
        self.assertTrue(pingR2R5())

if __name__ == '__main__':
	unittest.main()
