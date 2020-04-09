import re

from pygments.lexer import inherit, bygroups
from pygments.lexers.markup import MarkdownLexer
from pygments.token import *


class APIBlueprintLexer(MarkdownLexer):
    name = 'API Blueprint'
    aliases = ['apiblueprint', 'apib']
    filenames = ['*.apib']
    mimetypes = ['text/vnd.apiblueprint']

    tokens = {
        'root': [
            # Metadata
            (r'^(\S+)(:\s*)(.*)$',
                bygroups(Name.Variable.Global, Operator, Literal)),

            # Resource Group
            (r'^(#+)(\s*Group\s+)(.*)$',
                bygroups(Keyword, Keyword, Generic.Heading)),

            # Resource \ Action
            (r'^(#+)(.+)(\[)(.+)(\])$',
                bygroups(Keyword, Generic.Heading, Keyword, Name.Variable, Keyword)),

            # Parameters / Attributes
            (r'^(\s*[\+\-\*]\s*)([Aa]ttributes|[Pp]arameters)(.*)$',
                bygroups(Keyword, Keyword, Literal)),
            (r'^(\s*[\+\-\*]\s*)([`\w]+)(:\s*)(.*)$',
                bygroups(Keyword, Name.Variable, Operator, Literal)),

            # Request
            (r'^(\s*[\+\-\*]\s*)(Request)(?:(\s*\()(.*)(\)))?$',
                bygroups(Keyword, Keyword, Keyword, Name.Variable, Keyword)),

            (r'^(\s*[\+\-\*]\s*)(Body|Headers)$',
                bygroups(Keyword, Keyword)),

            # Response
            (r'^(\s*[\+\-\*]\s*)(Response)(\s+)(\d\d\d)(?:(\s*\()(.*)(\)))?$',
                bygroups(Keyword, Keyword, Number, Literal, Keyword, Name.Variable, Keyword)),

            inherit
        ]
    }

    def analyse_text(text):
        if text.startswith('FORMAT: 1A\n'):
            return 1.0

        if re.search(r'^[-*+]\s+Response\s+\d\d\d', text):
            return 0.9

        return 0.0
