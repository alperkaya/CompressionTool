#!/usr/bin/env python

import sys
import heapq
import click
import json

from huffman_tree import HuffmanTree
from huffman_codec import HuffmanCodec

def read_file(filename):
    content = []
    for line in filename:
        content.extend(line)
    return content


@click.command()
@click.option('--output', prompt='The output filename')
@click.argument('filename', type=click.File('r'), default=sys.stdin)
def main(output, filename):

    content = read_file(filename)
    hf_r = HuffmanCodec()
    #hf_r.encode(content, output)

    hf_w = HuffmanCodec()
    hf_w.decode(output)    


if __name__ == "__main__":
    main()