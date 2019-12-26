#Author: David Geller
#Student ID: 214404255
#course: EECS 4482

import scapy
from scapy.all import * 

print("Enter IP address of sender: ")
x = input()

print("IP address is of sender is " + x)
print("Program will sniff for 15 seconds. After that program will exit.")
print("Packet sniffing...")

#Sniffs for 15 seconds until printing out msg and exiting
p = sniff(timeout=15, filter= "ip and icmp and host " + x)
p.show()

#Empty msg string
msg = ""

#Converts each number from ID field into character and then adds it to msg string
for y in range(len(p)):
    msg = msg + chr(p[y].id)

#Prints msg
print(msg)
