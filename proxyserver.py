import requests
from requests.sessions import HTTPAdapter


def server0_list():
    list = str(requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt").content).split("\\n")
    list.pop(0)
    list.pop(1)
    return list
def server1_list():
    list = str(requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt").content).split("\\n")
    return list
def server2_list():
    list = str(requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt").content).split("\\n")
    return list
def server3_list():
    list = str(requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt").content).split("\\n")
    return list
def server4_list():
    list = str(requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt").content).split("\\n")
    return list
def server5_list():
    list = str(requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").content).split("\\n")
    return list
def server6_list():
    list = str(requests.get("https://raw.githubusercontent.com/almroot/proxylist/master/list.txt").content).split("\\n")
    return list
def server7_list():
    list = str(requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/proxies-socks5.txt").content).split("\\n")
    return list
def server8_list():
    list = str(requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/proxies-http.txt").content).split("\\n")
    return list
def server9_list():
    list = str(requests.get("https://raw.githubusercontent.com/almroot/proxylist/master/list.txt").content).split("\\n")
    return list
def server10_list():
    list = str(requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/proxies-socks4.txt").content).split("\\n")
    return list

def server11_list():
    list = str(requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").content).split("\\n")
    return list
def server12_list():
    list = str(requests.get("https://raw.githubusercontent.com/r3xzt/proxy-list/main/all.txt").content).split("\\n")
    return list
def server13_list():
    list = str(requests.get("https://raw.githubusercontent.com/Volodichev/proxy-list/main/http.txt").content).split("\\n")
    return list
def server14_list():
    list = str(requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt").content).split("\\n")
    return list
def server15_list():
    list = str(requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt").content).split("\\n")
    return list
def server16_list():
    list = str(requests.get("https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt").content).split("\\n")
    return list
def server17_list():
    list = str(requests.get("https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-socks5.txt").content).split("\\n")
    return list
def server18_list():
    list = str(requests.get("https://raw.githubusercontent.com/roma8ok/proxy-list/main/proxy-list-http.txt").content).split("\\n")
    return list
def server19_list():
    list = str(requests.get("").content).split("\\n")
    return list
def server20_list():
    list = str(requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt").content).split("\\n")
    return list

def build(server):
    if server == 0:
        return server0_list()
    if server == 1:
        return server1_list()
    if server == 2:
        return server2_list()
    if server == 3:
        return server3_list()
    if server == 4:
        return server4_list()
    if server == 5:
        return server5_list()
    if server == 6:
        return server6_list()
    if server == 7:
        return server7_list()
    if server == 8:
        return server8_list()
    if server == 9:
        return server9_list()
    if server == 10:
        return server10_list()
    if server == 11:
        return server11_list()
    if server == 12:
        return server12_list()
    if server == 13:
        return server13_list()
    if server == 14:
        return server14_list()
    if server == 15:
        return server15_list()
    if server == 16:
        return server16_list()
    if server == 17:
        return server17_list()
    if server == 18:
        return server18_list()
    if server == 19:
        return server19_list()
    if server == 20:
        return server20_list()
        