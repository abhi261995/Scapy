from  scapy.all  import  IP,sr,TCP 
import scapy.all as scapy


request =scapy.ARP()            #ARP packet  
request.pdst='192.168.100.1/24' #NW range
ethernet=scapy.Ether()          #Ethernet packet     
ethernet.dst='ff:ff:ff:ff:ff:ff'
request_broadcast=ethernet/request
clients=scapy.srp(request_broadcast,timeout=1)[0]

for r in clients:
    print(r[1].psrc+" "+r[1].hwsrc)
