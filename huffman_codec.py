#!/usr/bin/env python

import sys
from huffman_module_helpers import *

class HuffmanCodec:

    def __init__(self):
        self.char_freq = []
        self.huffman_tree = []

    def _write(self, encoded_content, output_file):
        header = json.dumps(self.char_freq)

        if output_file:
            with open(output_file, 'w') as f_out:
                f_out.write(header)
                f_out.write(encoded_content)
        else:
            sys.stdout.write(encoded_content)

    def encode(self, content, output_file=None):
        self.char_freq    = calculate_char_frequencies(content)
        pr_queue          = create_priority_queue(self.char_freq)
        self.huffman_tree = build_huffman_tree(pr_queue)
        codes             = generate_huffman_code(self.huffman_tree, '')
        encoded_content   = huffman_encode(content, codes)

        self._write(encoded_content, output_file)

    def decode(self, output_file):
        self.char_freq    = decode_header(output_file)
        binary_content    = fetch_binary_content(output_file)
        pr_queue          = create_priority_queue(self.char_freq)
        self.huffman_tree = build_huffman_tree(pr_queue)
        decoded_text      = decode_text_from_huffman_code(self.huffman_tree, binary_content)

        self._write(decoded_text, output_file)
        
        