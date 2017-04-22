#!/usr/bin/env python
# coding: utf-8


#from requests import get


def xpl(site, tipo):
    """Uma simples docstring"""
    with open("vullns/"+tipo+".txt", "r") as vull:
        for vulls in vull.readlines():
            print(vulls)

