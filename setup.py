#!/usr/bin/env python

from setuptools import setup

setup(
    name='pygments-apiblueprint',
    version='0.1.0',
    description='An API Blueprint Lexer for Pygments.',
    url='https://github.com/kylef/pygments-apiblueprint',
    packages=['pygments_apiblueprint'],
    install_requires=['pygments-markdown-lexer'],
    entry_points = {
        'pygments.lexers': ['apiblueprint = pygments_apiblueprint.lexer:APIBlueprintLexer'],
    },
    author='Kyle Fuller',
    author_email='kyle@fuller.li',
    license='BSD',
    classifiers=(
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'License :: OSI Approved :: BSD License',
    )
)
