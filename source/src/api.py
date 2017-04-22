#!/usr/bin/env python
# coding: utf-8


from requests import post
from json import loads
from urllib.parse import urlencode
from urllib.request import Request, urlopen


def ApiSearch(alvo):
    user = "Mozilla/5.0 (X11; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0 Iceweasel/22.0"
    url = "http://domains.yougetsignal.com/domains.php"
    contenttype = "application/x-www-form-urlencoded; charset=UTF-8"
    post = [('remoteAddress', alvo)]
    post = urlencode(post).encode('utf-8')
    req = Request(url, post)
    req.add_header("Content-Type", contenttype)
    req.add_header("User-Agent", user)
    result = urlopen(req).read()
    result = loads(result.decode('utf-8'))
    return result

