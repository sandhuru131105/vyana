import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from vyana.demo import ABOUT, HELP, MAX_INPUT, main, reply
class CliTests(unittest.TestCase):
    def test_about(self): self.assertEqual(reply('/about'), ABOUT)
    def test_help(self): self.assertEqual(reply('/help'), HELP)
    def test_empty(self): self.assertIn('Type a message', reply('  '))
    def test_demo(self): self.assertIn('Real AI integration is not built', reply('வணக்கம்'))
    def test_no_echo(self): self.assertNotIn('private input', reply('private input'))
    def test_unknown(self): self.assertIn('Unknown', reply('/exec'))
    def test_length(self): self.assertIn('too long', reply('a'*(MAX_INPUT+1)))
    def test_quit(self): self.assertEqual(reply(' /quit '), 'Bye.')
    def test_main_about(self):
        with patch('sys.argv',['vyana','--about']), redirect_stdout(io.StringIO()) as out: main()
        self.assertEqual(out.getvalue().strip(),ABOUT)
    def test_eof(self):
        with patch('sys.argv',['vyana']), patch('builtins.input',side_effect=EOFError), redirect_stdout(io.StringIO()) as out: main()
        self.assertIn('Bye.',out.getvalue())
    def test_main_quit(self):
        with patch('sys.argv',['vyana']), patch('builtins.input',return_value='/quit'), redirect_stdout(io.StringIO()) as out: main()
        self.assertIn('Vyana> Bye.',out.getvalue())
