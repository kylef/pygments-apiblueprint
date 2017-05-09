from pygments_apiblueprint.lexer import APIBlueprintLexer


def setup(app):
    """
    Initializer for Sphinx extension API
    http://www.sphinx-doc.org/en/stable/extdev/index.html#dev-extensions
    """

    lexer = APIBlueprintLexer()

    add.add_lexer('apiblueprint', lexer)
    add.add_lexer('apib', lexer)

    return dict(version='0.1.0')
