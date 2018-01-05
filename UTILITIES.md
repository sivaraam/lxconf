* csplit - split a file into sections determined by context lines

* nl - number lines of files

* tac - concatenate and print files in reverse

* head - output the first part of files (tail - opposite)

* sort - sort lines of text files

* uniq - report or omit repeated lines

* seq - print a sequence of numbers


Audio & Video
===
* ffmpeg - can be used to convert between different formats

  e.g., convert `*.wma` to `*.mp3`

```
    for file in *.wma
    do
      ffmpeg -i "${file}"  -acodec libmp3lame -ab 192k "${file/.wma/.mp3}"
    done
```


Device related
===
* fdisk - manipulate disk partition table

* hdparm - get/set SATA/IDE device parameters

* lsblk - list block devices

* lsusb - list USB devices

* lspci - list all PCI devices

* df - report filesystem disk space usage

* fsck - clean and repair a linux filesystem