# Pygments API Blueprint

## Installation

```shell
$ pip install pygments-apiblueprint
```

## Usage

Once installed, the Pygments API Blueprint lexer is instantly available to
Pygments.

```python
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments_apiblueprint import APIBlueprintLexer

source = '''
# GET /

+ Response 200 (application/json)
    + Attributes
        + name: `pygments-apiblueprint`
'''

lexer = APIBlueprintLexer()
formatter = HtmlFormatter(linenos='table', cssclass='highlight')
result = highlight(source, lexer, formatter)

print(result)
```
