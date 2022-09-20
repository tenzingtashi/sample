iimport os
import sys
from collections import OrderedDict
from PyPDF2 import PdfFileReader

from termcolor import colored

url = “http://192.168.1.106/webapps/sqli/sqli.php?id=INJECT_HERE”

def detect(url):

    f = open(“fuzzing.txt”, “r”)

    payloads = f.read().splitlines()

    for item in payloads:

        #print (item)

        url_mod = url.replace(“INJECT_HERE”,item)

        #print (url_mod)

        http_request = requests.get(url_mod)

        #print (http_request.content)

        if http_request.content.find(b’MySQL’) != -1:

            print (url_mod + colored(” – potential error based SQLi detected”, ‘red’))

        else:

            print(url_mod + colored(” – no injection found”,’green’))

if __name__ == “__main__”:

    detect(url)