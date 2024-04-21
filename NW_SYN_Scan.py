from  scapy.all  import  IP,sr,TCP 
import scapy.all as scapy

port =[22,21,53,443,80,3389]

host ="8.8.8.8"

def SynScan(host):

 ans,uns=sr(IP(dst=host)/TCP(dport=port,flags="S"),timeout=2,verbose=0)

 if ans:
    for(s,r) in ans:
        if s[TCP].dport==r[TCP].sport:
         #print(s[TCP].dport)
         print(s[TCP].dport)

        else:
           print("No Open Ports") 

SynScan(host)







