# markdown-backup-images
Script to download images from a markdown file and replace URL to point at backup location.

Comes in handy if you:
* don't want to rely on internet connection
* don't trust hackmd to keep your files forever
* just experienced imgur purging your most important screenshots (or favourite memes) from their servers

## Usage:
```
usage: python3 markdown-backup-images.py [-h] inputfile outputfile path

positional arguments:
  inputfile   markdown file which images should be backed up
  outputfile  filename of new file with replaced image paths
  path        location of images backup (by default current directory)

optional arguments:
  -h, --help  show this help message and exit
```

###### If you use Joplin you might want to configure how the path is changed in the new .md file, because it has problems with relative path (and extensions)
