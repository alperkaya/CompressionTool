#!/usr/bin/env python

import heapq
import json
from huffman_tree import HuffmanTree

def print_freq_table(char_freq):
    for ch in char_freq:
        print(f"{ch} : {char_freq[ch]}")

def calculate_char_frequencies(content):
    char_frequencies = {}

    for ch in content:
        char_frequencies[ch] = char_frequencies.get(ch, 0) + 1
    
    return char_frequencies

def create_priority_queue(char_frequencies):
    queue_list = []

    for char, freq in char_frequencies.items():
        node = HuffmanTree(int(freq), char)
        queue_list.append(node)
    
    heapq.heapify(queue_list)

    return queue_list

def build_huffman_tree(priority_queue):
    while len(priority_queue) > 1:
        node1 = heapq.heappop(priority_queue)
        node2 = heapq.heappop(priority_queue)

        internal_node = HuffmanTree(node1.weight() + node2.weight(), None, node1, node2)
        heapq.heappush(priority_queue, internal_node)

    return priority_queue[0]

def generate_huffman_code(node, current_node="", code_map=None):
    if code_map is None:
        code_map = {}

    if node.is_leaf():
        code_map[node.symbol()] = current_node
    else:
        generate_huffman_code(node.left, current_node+"0", code_map)
        generate_huffman_code(node.right, current_node+"1", code_map)

    return code_map

def huffman_encode(filename, codes):
    encoded_data = "".join(codes[ch] for line in filename for ch in line)
    return encoded_data

def get_enclosed_json(json_content):
    json_end = json_content.find('}')

    while json_end != -1 and (json_end + 1 < len(json_content)) and (json_content[json_end+1] not in {"0", '1'}):
        json_end = json_content.find('}', json_end+1)
    
    if json_end == -1:
        raise TypeError("Header does not end with correct encoder format")
    
    return json_end

def decode_header(output):
    with open(output, 'r') as out_file:
        json_content = out_file.read()
        json_start = json_content.find('{')
        if json_start == -1:
            raise TypeError("Header does not start with correct encoder format")
        
        json_end = get_enclosed_json(json_content)
        
        json_parsed = json_content[json_start:json_end+1]

        try:
            json_data = json.loads(json_parsed)
            return json_data
        except json.JSONDecodeError:
            return None
        
def decode_text_from_huffman_code(tree, binary_content):
    if binary_content == "" or tree == None:
        return ""
    
    result = ""
    current_node = tree
    for bit in binary_content: 

        if current_node.is_leaf():
            result += current_node.symbol()
            current_node = tree
        
        if bit == '1':
            current_node = current_node.right
        elif bit == '0':
            current_node = current_node.left
        else:
            raise Exception("File contains non binary content")
        
    if current_node.is_leaf():
        result += current_node.symbol()
        current_node = tree

    return result  

def fetch_binary_content(output_file):
    with open(output_file, 'r') as out_file:
        binary_content = out_file.read()
        content_start_idx = get_enclosed_json(binary_content) + 1
        binary_content = binary_content[content_start_idx:]
    
    return binary_content

def decode_text_from_huffman_code(tree, binary_content):
    if binary_content == "" or tree == None:
        return ""
    
    result = ""
    current_node = tree
    for bit in binary_content: 

        if current_node.is_leaf():
            result += current_node.symbol()
            current_node = tree
        
        if bit == '1':
            current_node = current_node.right
        elif bit == '0':
            current_node = current_node.left
        else:
            raise Exception("File contains non binary content")
    
    if current_node.is_leaf():
        result += current_node.symbol()
        current_node = tree

    return result 
