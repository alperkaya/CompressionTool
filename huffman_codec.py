#!/usr/bin/env python

from huffman_module_helpers import *

class HuffmanCodec:

    def __init__(self):
        self.char_freq = []
        self.huffman_tree = []

    def encode(self, content, output_file=None):
        if content is not "":
            self.char_freq    = calculate_char_frequencies(content)
            pr_queue          = create_priority_queue(self.char_freq)
            self.huffman_tree = build_huffman_tree(pr_queue)
            codes             = generate_huffman_code(self.huffman_tree, '')
            encoded_content   = huffman_encode(content, codes)
            write(self.char_freq, encoded_content, output_file, header_include=True)
        else:
            write(self.char_freq, "", output_file)

    def decode(self, file_to_read, output_file=None):
        self.char_freq    = decode_header(file_to_read)
        binary_content    = fetch_binary_content(file_to_read)
        pr_queue          = create_priority_queue(self.char_freq)
        self.huffman_tree = build_huffman_tree(pr_queue)
        decoded_text      = decode_text_from_huffman_code(self.huffman_tree, binary_content)

        write(self.char_freq, decoded_text, output_file)
        
        