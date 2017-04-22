#!/urs/bin/env python
# coding: utf-8


from requests import get
from BeatiufulSoup import *


def dork(parm):
    req = get(parm).text
