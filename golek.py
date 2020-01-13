#!/usr/bin/python3
# Author : Mr.Zck18

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time
import os
m = '\033[91m' #merah
g = '\033[92m' #green
k = '\033[93m' #kuning
b = '\033[94m' #biru
u = '\033[95m' #ungu
c = '\033[96m' #cyen
p = '\033[97m' #putih

global starttime

class ZeroScann():

    def __init__(self):
        self.scan()
        
    def scan(self):
        # argument parser taiik
        parser = argparse.ArgumentParser(prog="PosiX.py", description="Simple Find Shell in Website")
        parser.add_argument("-u", dest="domain", help="your url")
        parser.add_argument("-w", dest="wordlist", help="your wordlsit")
        args = parser.parse_args()
        if not args.domain:
            sys.exit("\033[32mCara : golek.py -u xnxx.com -w list.txt")
        if not args.wordlist:
            sys.exit("\033[36musage: golek.py -u example.com -w list.txt")
            
        #Untuk url cuk
        site = args.domain
        print("\033[96m[?] \033[0mMemulai Program...")
        print("\033[96m[!] \033[0mTunggu Sebentar !")
        print("\033[96m[Mr.Zck18] \033[0mBismillahirrohmanirrohim","\n")
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # baca wordlist
        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print("\033[91mUpss, Wordlist tidak ditemukan !!!\033[0m")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print("\033[91mWordlist Can\'t Close!\033[0m")
        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        #Ngentod lah kau
        found = []
        # respon code
        resp_codes = {403 : "403 forbidden", 401 : "401 unauthorized"}
        # loop untuk mencoba password
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[92mfound:","\033[0m/"+psx)
                    found.append(url)
                    
                except HTTPError as e:
                    if e.code == 404:
                        print("\033[95m[\033[96m{0}\033[95m]".format(time.strftime("%H:%M:%S")),"\033[91mMencoba:","\033[0m/"+psx)
                    else:
                        print("\033[95m[\033[96m{0}\033[95m]".format(time.strftime("%H:%M:%S")),"\033[92minfo :","\033[33m/"+psx,"\033[92mstatus:\033[33m",resp_codes[e.code])
                        
                except URLError as e:
                    sys.exit("\033[31m[!] Ups ! Tidak ada koneksi internet :v ")
                except Exception as er:
                    print("\n\033[93m[?] \033[0mYour Connection Is Bad")
                    print("\033[93m[!] \033[0mKeluar Program")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print("\n\033[96m[?] \033[0mCTRL+C Terdeteksi")
                print("\033[96m[!] \033[0mKeluar Program")
                time.sleep(2)
                exit()
        
        if found:
            print("\n\033[96m[+] \033[0mResult Found\033[92m")
            print("\n".join(found))
            print("\033[96m[?] \033[0mTime Elasped: \033[35m%.2f\033[0m Seconds" % float(time.time()-starttime))
        else:
            print("\n\033[96m[!] \033[0mCould Not Find Any Shell Backdoor")
            print("\033[96m[?] \033[0mTime Elasped: \033[33m%.2f\033[0m Seconds" % float(time.time()-starttime))
                
    os.system('clear')
    def banner():
        # Biarkan Kami Berkarya,Orang noob mah Bebas Awokawok
        print (m+"             ,        , ")
        print (k+"            /(        )` ")
        print (c+"            \ \___   / | ") 
        print (m+"            /- _  `-/  ' ")
        print (k+"           (/\/ \ \   /\ ")
        print (c+"           / /   | `    \ ")
        print (m+"           O O   ) /    | ")
        print (k+"           `-^--'`<     ' ")
        print (c+"          (_.)  _  )   / ")
        print (m+"           `.___/`    / ")
        print (k+"             `-----' / ")
        print (c+" <----.     __ / __   \ ")
        print (m+" <----|====O)))==) \) /==== ")
        print (k+" <----'    `--' `.__,' \ ")
        print (c+"             |         | ")
        print (m+"              \       / ")
        print (k+"        ______( (_  / \______ ")
        print (c+"      ,'  ,-----'   |        \ ")
        print ("\033[97m""+=====\033[96m`--{__________)\033[97m========\033[96m\/\033[97m===============+") 
        print ("+ Author  :  \033[95mMr.Zck18\033[97m                         +")
        print ("+=============================================+")
        print ("+ Member  :  \033[91mindonesia er\033[97mror system           +")
        print ("+==============================================")
        print ("+ Github  :  \033[94mgithub.com/Mr-Zck18\033[97m              +")
        print ("+=============================================+")
        print ("")

    print(banner())
                
if __name__ == '__main__':
    ZeroScann()
