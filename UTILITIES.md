* csplit - split a file into sections determined by context lines

* nl - number lines of files

* tac - concatenate and print files in reverse

* head - output the first part of files (tail - opposite)

* sort - sort lines of text files

* uniq - report or omit repeated lines

* seq - print a sequence of numbers

* strace - trace system calls and signals

## File format converter

* pandoc
    * [MD to] PDF conversion dependencies:
        * texlive-latex-base -> pdflatex
        * lmodern -> To avoid "LaTeX Error: File `lmodern.sty' not found." error
        * texlive-fonts-recommended -> to avoid "Font T1/cmr/m/n/10=ecrm1000 at 10.0pt not loadable: Metric (TFM) file not found." error
        * texlive-latex-recommended texlive-pictures texlive-latex-extra -> recommended for more styles also avoids "LaTeX Error: File `booktabs.sty' not found." error

* convert - convert between image formats as well as resize an image, blur, crop, despeckle, dither, draw on, flip, join, re-sample, and much more
  - can be used to lower quality of images in PDF

    e.g., `convert -density 50x50 -quality 65 -compress jpeg input.pdf output.pdf`

    Ref: https://askubuntu.com/q/113544

  - can convert images to PDF

    e.g., `convert $IMAGE $FILE.pdf`

    Ref: https://askubuntu.com/a/246653/732512

* gs - Ghostscript (PostScript and PDF language interpreter and previewer)

  - can be used to downsize a PDF

    e.g., `gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/screen -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf input.pdf`

    Ref: https://askubuntu.com/q/113544

* ps2pdf - Convert PostScript to PDF using ghostscript

## Audio & Video

* ffmpeg - can be used to convert between different formats

  e.g. To convert `*.wma`files  to `*.mp3`,

  ```
    for file in *.wma
    do
      ffmpeg -i "${file}"  -acodec libmp3lame -ab 192k "${file/.wma/.mp3}"
    done
   ```

  e.g. To crop an audio file (without any transcoding),

  ```
   ffmpeg -ss ${start_time} -t ${time_duration_from_start} -i ${input_file} -acodec copy ${output_file}
  ```

## Device related

* lsblk - list block devices

* lsusb - list USB devices

* lspci - list all PCI devices

#### Disk related

* df - report filesystem disk space usage

* du - estimate file space usage

    Typical usage: du -hs path/to/directory

* fdisk - manipulate disk partition table

* hdparm - get/set SATA/IDE device parameters

* fsck - clean and repair a linux filesystem
