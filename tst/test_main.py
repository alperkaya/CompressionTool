import unittest

from main import print_freq_table
from click.testing import CliRunner

class TestMain(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_print_freq_table(self):
        result = self.runner.invoke(print_freq_table, ["data/test.txt"])
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output, '119\n')


if __name__ == '__main__':
    unittest.main()