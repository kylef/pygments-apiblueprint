from pygments.lexer import inherit, bygroups
from pygments.token import *
from pygments_markdown_lexer.lexer import MarkdownLexer, Markdown


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
                bygroups(Markdown.Markup, Keyword, Generic.Heading)),

            # Resource \ Action
            (r'^(#+)(.+)(\[)(.+)(\])$',
                bygroups(Markdown.Markup, Markdown.Heading, Markdown.Markup, Name.Variable, Markdown.Markup)),

            # Parameters / Attributes
            (r'^(\s*[\+\-\*]\s*)([Aa]ttributes|[Pp]arameters)(.*)$',
                bygroups(Markdown.Markup, Keyword, Literal)),
            (r'^(\s*[\+\-\*]\s*)([`\w]+)(:\s*)(.*)$',
                bygroups(Markdown.Markup, Name.Variable, Operator, Literal)),

            # Request
            (r'^(\s*[\+\-\*]\s*)(Request)(?:(\s*\()(.*)(\)))?$',
                bygroups(Markdown.Markup, Keyword, Markdown.Markup, Name.Variable, Markdown.Markup)),

            (r'^(\s*[\+\-\*]\s*)(Body|Headers)$',
                bygroups(Markdown.Markup, Keyword)),

            # Response
            (r'^(\s*[\+\-\*]\s*)(Response)(\s+)(\d\d\d)(?:(\s*\()(.*)(\)))?$',
                bygroups(Markdown.Markup, Keyword, Number, Literal, Markdown.Markup, Name.Variable, Markdown.Markup)),

            inherit
        ]
    }
