# writeup5

``` mount --mkdir -o loop <iso> ./boot2root ```

``` cp ./boot2root/casper/filesystem.squashfs /tmp/ ```

``` cd /tmp ```

``` unsquashfs /tmp/filesystem.squashfs ```

``` cd squashfs_root/root ```

``` grep -A1 "adduser" .bash_history ```
