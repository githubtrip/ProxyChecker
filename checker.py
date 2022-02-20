import requests
import proxyserver
from threading import Thread
import datetime
from termcolor import colored
import time
import os
import sys

checked = 0
good = 0
bad = 0
running = True

def check(proxy, url):
    try:
        r = requests.get(url, proxies={'http' : 'http://'+proxy, 'https' : 'http://'+proxy}, timeout=3)
    except:
        return False
    if r.status_code == 200:
        return True


def print_status():
    while running:
        print(f"Checked: {checked} | Good: {good} | Bad: {bad}")
        time.sleep(0.3)
        os.system("cls")

def check_proxy_list(proxies, url, path):
    global checked
    global good
    global bad
    for proxy in proxies:
        res = check(proxy, url)
        checked+=1
        if res:
            stat = colored(f"Good Proxy: {proxy} | Type: null", "green")
            #print(stat)
            f = open(path, "a+")
            f.write(proxy + "\n")
            f.close()
            
            good+=1
        else:
            stat = colored(f"Bad Proxy: {proxy} | Type: null", "red")
            #print(stat)
            bad+=1



if __name__ == "__main__":
    proxies = []
    proxies = proxyserver.server0_list()
    proxies = proxies + proxyserver.server1_list()
    proxies = proxies + proxyserver.server2_list()
    proxies = proxies + proxyserver.server3_list()
    proxies = proxies + proxyserver.server4_list()
    proxies = proxies + proxyserver.server5_list()
    proxies = proxies + proxyserver.server6_list()
    proxies = proxies + proxyserver.server7_list()
    proxies = proxies + proxyserver.server8_list()
    proxies = proxies + proxyserver.server9_list()
    proxies = proxies + proxyserver.server10_list()
    proxies = proxies + proxyserver.server11_list()
    proxies = proxies + proxyserver.server12_list()
    proxies = proxies + proxyserver.server13_list()
    proxies = proxies + proxyserver.server14_list()
    proxies = proxies + proxyserver.server15_list()
    proxies = proxies + proxyserver.server16_list()
    proxies = proxies + proxyserver.server17_list()
    proxies = proxies + proxyserver.server18_list()
    #proxies = proxies + proxyserver.server19_list()
    proxies = proxies + proxyserver.server20_list()

    #proxies = open('HTTP-proxies.txt', 'r').read().splitlines()
    #proxies = proxies + open('SOCKS4-proxies.txt', 'r').read().splitlines()
    #proxies = proxies + open('SOCKS5-proxies.txt', 'r').read().splitlines()
    
    threads = 1000

    print(f"total proxies: {len(proxies)} | threads: {threads}")
    time.sleep(2)

    url = sys.argv[1]
    path = sys.argv[2]
    a = int(len(proxies)/threads)
    c = 0
    m = []
    for i in range(0, threads):
        cur_list = []
        for x in range(c, c+a):
            cur_list.append(proxies[x])
        m.append(cur_list)
        c+=a
    for l in m:
        thread = Thread(target=check_proxy_list, args=(l, url, path))
        thread.start()
        
    thread = Thread(target=print_status)
    thread.start()
    
