#!/usr/local/bin/python
import wget
import re

def download_image(url, output_directory):
    filename = wget.download(url, output_directory)
    # uncomment the line below if you want to strip extension
    #filename = re.sub(r"\.[A-Za-z0-9]+", "", filename)
    return filename
    
def replace_paths(match, output_directory):
    if match.group(1) is not None and match.group(1) is not None:
        return (match.group(1)+"("+download_image(match.group(2), output_directory)+")")

def main(args):
    input_file = open(args.inputfile, "r")
    output_file = open(args.outputfile, "w")

    for line in input_file:
        output_file.write(
            re.sub(
                r"(\!\[.*\])\((http(s)?\:\/\/.+)\)",
                lambda match: replace_paths(match, args.path),
                line
            )
        )

    input_file.close()
    output_file.close()
    

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('inputfile', type=str,
                        help='markdown file which images should be backed up')
    parser.add_argument('outputfile', type=str,
                        help='filename of new file with replaced image paths')
    parser.add_argument('--path', type=str,
                        help='location of images backup')
    args = parser.parse_args()
    main(args)