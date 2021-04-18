* `csplit` - split a file into sections determined by context lines

* `nl` - number lines of files

* `tac` - concatenate and print files in reverse

* `head` - output the first part of files (tail - opposite)

* `sort` - sort lines of text files

* `uniq` - report or omit repeated lines

* `seq` - print a sequence of numbers

* `strace` - trace system calls and signals

## File format converter

* `pandoc`
    * [MD to] PDF conversion dependencies:
        * texlive-latex-base -> pdflatex
        * lmodern -> To avoid "LaTeX Error: File `lmodern.sty' not found." error
        * texlive-fonts-recommended -> to avoid "Font T1/cmr/m/n/10=ecrm1000 at 10.0pt not loadable: Metric (TFM) file not found." error
        * texlive-latex-recommended texlive-pictures texlive-latex-extra -> recommended for more styles also avoids "LaTeX Error: File `booktabs.sty' not found." error

* `convert` - convert between image formats as well as resize an image, blur, crop, de-speckle, dither, draw on, flip, join, re-sample, and much more
  - can be used to lower quality of images in PDF

    e.g., `convert -density 50x50 -quality 65 -compress jpeg input.pdf output.pdf`

    Ref: https://askubuntu.com/q/113544

  - can convert images to PDF

    e.g., `convert $IMAGE $FILE.pdf`

    Ref: https://askubuntu.com/a/246653/732512

  - can convert PDF file with images to TIFF format

    e.g., `convert source.pdf dest.tiff`

    Ref: https://stackoverflow.com/a/75567/5614968

* `gs` - Ghostscript (PostScript and PDF language interpreter and previewer)

  - can be used to downsize a PDF

    e.g., `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`

    Ref: https://askubuntu.com/q/113544

  - can be used to convert colour images in a PDF to black and white (b/w). The following script could be used for that:

      ```shell
	#!/bin/bash

	gs \
	 -sOutputFile=output.pdf \
	 -sDEVICE=pdfwrite \
	 -sColorConversionStrategy=Gray \
	 -dProcessColorModel=/DeviceGray \
	 -dCompatibilityLevel=1.4 \
	 -dNOPAUSE \
	 -dBATCH \
	 $1
      ```

      Ref: https://unix.stackexchange.com/a/93971

* `ps2pdf` - Convert PostScript to PDF using `ghostscript`

* `qpdf` - PDF transformation software

  - Removing password protection from a PDF file

    e.g., `qpdf --password="$PASS" --decrypt restricted-input.pdf unrestricted-output.pdf`

  Ref: https://superuser.com/a/850972/563569

## Audio & Video

* `ffmpeg` - can be used for a lot of things

  * To convert `*.wma`files  to `*.mp3`,

    ```
    for file in *.wma
    do
      ffmpeg -i "${file}"  -acodec libmp3lame -ab 192k "${file/.wma/.mp3}"
    done
    ```

  * To crop an audio file (without any transcoding),

    ```
    ffmpeg -ss ${start_time} -t ${time_duration_from_start} -i ${input_file} -acodec copy ${output_file}
    ```

    Examples:
    1. To remove the first 5 seconds from an audio file:
       ```
       ffmpeg -ss 0:05 -i ${input_file} -acodec copy ${output_file}
       ```

    2. To remove the last five seconds from an audio file (5:23 seconds)
       ```
       ffmpeg -t 5:18 -i ${input_file} -acodec copy ${output_file}
       ```
  * To remove audio from video file. Ref: https://superuser.com/a/268986/563569

    ```
    ffmpeg -i ${input_file} -c copy -an ${output_file}
    ```

  * To merge a set of `.ts` files. Ref: https://superuser.com/a/693009/563569

    ```
    cat audio_1.ts audio_2.ts audio_3.ts >all.ts
    ffmpeg -i all.ts -bsf:a aac_adtstoasc -acodec copy output.mp4
    ```

  * To extract `.mp3` audio from `.mp4`. Ref: https://stackoverflow.com/a/36324719/5614968

    ```
    ffmpeg -i input.mp4 -vn -q:a 0 -map a output.mp3
    ```

  * To reduce the size of a `.mp4` file without compromising quality. Ref: https://unix.stackexchange.com/a/38380/182996

    ```
    ffmpeg -i input.mp4 -vcodec libx264 -crf 20 output.mp4
    ```

  * To merge multiple `.mp4` files. Ref: https://stackoverflow.com/a/17487021/5614968

    ```
    # Create a text file (inputs.txt) with input file names. Each line
    # having the following format:
    #
    #    file <mp4_file_name>
    #
    # Eg.
    #
    #    file input_1.mp4
    #    file input_2.mp4
    #    file input_3.mp4
    #

    # Then execute the following command
    ffmpeg -f concat -i inputs.txt -vcodec copy -acodec copy concat_output.mp4
    ```

## Device related

* `lsblk` - list block devices

* `lsusb` - list USB devices

* `lspci` - list all PCI devices

#### Disk related

* `df` - report file-system disk space usage

* `du` - estimate file space usage

    Typical usage: du -hs path/to/directory

* `fdisk` - manipulate disk partition table

* `hdparm` - get/set SATA/IDE device parameters

* `fsck` - clean and repair a linux file-system

## Display

* `xrandr` - primitive command line interface to RandR extension

  It could be used to connect and configure a HDMI projector

  Possible example: `xrandr --output HDMI-0 --mode 1280x720 --right-of DVI-0`

## General Notes

* `grep` turns off colouring when piping, if it detects the
  destination is not a tty. To over come this use `--color=always`.
  Defining an alias for this as `alias cgrep=grep --color=always`
  would help.

  Ref: https://superuser.com/a/36045/563569

* Sometimes `less` might not recognize the special ASCII control
  characters that were piped to it. This could be overcome by
  passing the `-R` option.

  Ref: https://superuser.com/a/117842/563569

* Typically, if you want to page the coloured output of `grep` to
  `less`. You would have to do `grep --color=always ... | less -R`.

* The GNOME display manager (GDM3) might not work correctly after
  upgrading to debian testing from debian current stable. In that case,
  the following should be done to restore Gnome:

  ```
  apt --reinstall install gdm3
  apt --reinstall install gnome
  apt --reinstall install gnome-shell
  dpkg-reconfigure gdm3
  ```

  Ref: https://wiki.debian.org/DebianTesting
