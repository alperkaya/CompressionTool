#!/usr/bin/env python

import sys
import json

def print_freq_table(char_freq):
    for ch in char_freq:
        print(f"{ch} : {char_freq[ch]}")

def calculate_char_frequencies(content):
    char_frequencies = {}

    for ch in content:
        char_frequencies[ch] = char_frequencies.get(ch, 0) + 1
    
    return char_frequencies

def write(char_freq, encoded_content, output_file, header_include=False):
    if output_file:
        if header_include: 
            header = json.dumps(char_freq)
            encoded_content = header + encoded_content

        with open(output_file, 'w') as f_out:
            f_out.write(encoded_content)
    else:
        sys.stdout.write(encoded_content)

def get_enclosed_json(json_content):
    json_end = json_content.find('}')

    while json_end != -1 and (json_end + 1 < len(json_content)) and (json_content[json_end+1] not in {"0", '1'}):
        json_end = json_content.find('}', json_end+1)
    
    if json_end == -1:
        raise TypeError("Header does not end with correct encoder format")
    
    return json_end


def fetch_binary_content(output_file):
    with open(output_file, 'r') as out_file:
        binary_content = out_file.read()
        content_start_idx = get_enclosed_json(binary_content) + 1
        binary_content = binary_content[content_start_idx:]
    
    return binary_content