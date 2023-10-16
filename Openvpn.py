import os
from time import sleep
import random
import subprocess


def change_vpn():

    print("disconnecting")
    subprocess.run("C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe --command disconnect_all")
    sleep(10)
    configs =["vpnbook-de20-tcp80.ovpn","vpnbook-fr1-tcp80.ovpn","vpnbook-fr8-udp25000.ovpn"]
    config =random.choice(configs)
    print("connecting")
    subprocess.run("C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe --connect %s" %config)
    print("connecting to %s"%config)
    sleep(30)
    print("done")
    return

def close_vpn():
    subprocess.run("C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe --command disconnect_all")
    sleep(10)
    return