#Author: David Geller
#Student ID: 214404255
#course: EECS 4482

import scapy
from scapy.all import *

print("Enter IP address of receiver: ")
x = input()

print("IP address is of receiver is " + x)

print("Enter secret message: ")
msg = input()
print("Secret message is " + msg)

#Converts string msg into chracter array
L = list(msg)

#Places each character in array into packet
for y in range(len(L)):
    #Packet id field is the character converted into ascii int value
    p = IP(dst=x,id=ord(L[y]))/ICMP()/"testing"
    send(p)
    print(ord(L[y])) #For testing of id
