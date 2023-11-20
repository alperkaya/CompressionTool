import unittest
from io import StringIO
import sys
import string
import random


from huffman_codec import HuffmanCodec 

class TestHuffmanCodec(unittest.TestCase):
    def setUp(self) -> None:
        self.hf = HuffmanCodec()
        self.temp_out_file = 'data/output.txt'
        
        # Capture the stdout content
        self.captured_output = StringIO()
        sys.stdout = self.captured_output

    def tearDown(self) -> None:
        # Reset sys.stdout to its original value
        sys.stdout = sys.__stdout__

    def test_encode_single_char(self):
        self.hf.encode("a")

        # Get the captured content
        actual_output = self.captured_output.getvalue().strip()

        self.assertEqual(actual_output, '0')

    def test_encode_empty_string(self):
        self.hf.encode("")

        # Get the captured content
        actual_output = self.captured_output.getvalue().strip()

        self.assertEqual(actual_output, '')
    
    def test_codec_with_multiple_inputs(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        random_text = ''.join(random.choices(characters, k=5000))

        test_list = ["aaaAbBBBB", "@#$%^&*()", " ", random_text]
        for test_case in test_list:
            self.hf.encode(test_case, self.temp_out_file)
            self.hf.decode(self.temp_out_file, 'data/test_decode.txt')

            with open('data/test_decode.txt', 'r') as f_out:
                actual_output = f_out.read()

            self.assertEqual(actual_output, test_case)

    def test_codec_large_input(self):
        with open('data/test.txt','r') as f_out:
            test_case = f_out.read()    
        self.hf.encode(test_case, self.temp_out_file)
        self.hf.decode(self.temp_out_file, 'data/test_decode.txt')

        with open('data/test_decode.txt', 'r') as f_out:
                actual_output = f_out.read()
                
        self.assertEqual(actual_output, test_case)



if __name__ == '__main__':
    unittest.main()