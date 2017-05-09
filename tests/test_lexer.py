import unittest
from pygments_apiblueprint import APIBlueprintLexer


class APIBlueprintLexerTests(unittest.TestCase):
    def setUp(self):
        self.lexer = APIBlueprintLexer

    def test_name(self):
        self.assertEqual(self.lexer.name, 'API Blueprint')

    def test_aliases(self):
        self.assertEqual(self.lexer.aliases, ['apiblueprint', 'apib'])

    def test_filenames(self):
        self.assertEqual(self.lexer.filenames, ['*.apib'])

    def test_mimetypes(self):
        self.assertEqual(self.lexer.mimetypes, ['text/vnd.apiblueprint'])

    def test_analyse_unrealted_text(self):
        self.assertEqual(self.lexer.analyse_text('Hello'), 0.0)

    def test_analyse_format_text(self):
        self.assertEqual(self.lexer.analyse_text('FORMAT: 1A\n\n# API'), 1.0)

    def test_analyse_response_text(self):
        self.assertEqual(self.lexer.analyse_text('+ Response 200 (application/json)'), 0.9)
