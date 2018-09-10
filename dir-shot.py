import sys
version=sys.version[0:3]
if version == '2.7' :
    pass
elif version == '3.7':
    print ("You Must Use Python 2.x")
    exit()
else:
    exit()
import banner
import argparse
import os
import platform
import requests
name=platform.system()
if name == "Windows":
    os.system("cls")
elif name == "Linux":
    os.system("clear")
else:
    pass
print (banner.x+"\n")
#take args from user
parser = argparse.ArgumentParser()
parser.add_argument("-u","--url", help="The Domain or Url")
parser.add_argument("-f","--file", help="The Wordlist directory")
args = parser.parse_args()
link=args.url
list=args.file
#you can replace
#url=raw_input("Enter The Url Like[ http://test.com/ ] : ")
try:
    f=open(list,'r')
    words=f.read()
    out=words.split('\n')
    print ("-"*90)
    for i in out:
        url=link+i
        r=requests.get(url)
        if r.status_code == 200 :
            print ("[+] Found "+url)
        else:
            pass
except KeyboardInterrupt:
        print("=_= "*40)
        print ("\n[!] Exit")
except TypeError:
        print ("""
            optional arguments:
              -h, --help  Show this help message and exit
              -u  The Domain or Url
              -f  The Wordlist Path
              Example : dir-shot.py -u https://google.com -f /Wordlist/dirlist.txt
              """)
except IOError:
    print ("[-] There Is No File Found There : '{0}'\n[-] OR The Link Is Wrong : '{1}''").format(list,link)



    ###words=doc.read()
    ###out=words.split('\n')
    #url=raw_input("Enter The Url Like[ http://test.com/ ] : ")
"""try:

        for i in out:
            url=link+i
            r=requests.get(url)
            if r.status_code == 200:
                print "[+] Found "+url
            else:
                pass
    except KeyboardInterrupt:
        print"=_= "*40
        print "\n[!] Exit"
    except TypeError:
    """
