import scapy
from scapy.all import *
import time

resp = []
for t in range(1,25):
    ip = IP(dst='8.8.8.8', ttl=t, id=RandShort())
    ts = time.time()
    r = sr1(ip/ICMP(), retry=1, timeout=3)
    te = time.time()
    resp.append((t,r, (te-ts)*1000))
    print( t)
    if r and r.src == '8.8.8.8':
        break

print( len(resp), 'responses' )

for l in resp:
    print( '{:2} {:8.3f} ms    '.format(l[0], l[2]), end= '')
    if l[1]:
           print( l[1].src)
    else:
           print( '*' )
           
