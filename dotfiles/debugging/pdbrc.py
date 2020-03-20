#!python

# Should go at  ~/.pdbrc.py 
# From https://github.com/pdbpp/pdbpp/issues/36

import pdb
from pygments.formatters import Terminal256Formatter
from pygments.lexers import PythonLexer
from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, Text, Number, Operator, Generic, Whitespace, Punctuation, Other, Literal

# Colors are taken from https://chriskempson.github.io/base16/
RED = "#cc6666"
ORANGE = "#de935f"
YELLOW = "#f0c674"
GREEN = "#b5bd68"
CYAN = "#8abeb7"
BLUE = "bold #81a2be"  # See http://pygments.org/docs/styles/#style-rules
MAGENTA = "#b294bb"
BROWN = "#a3685a"

WHITE = "#ffff"
BLACK = "#1d1f21"
GRAY = "#969896"
LIGHTGRAY = "#e0e0e0"

FOREGROUND = LIGHTGRAY
COMMENT = GRAY


class base16_tomorrow_dark(Style):
    # Class structure taken from https://bitbucket.org/birkenfeld/pygments-main/src/7941677dc77d4f2bf0bbd6140ade85a9454b8b80/pygments/styles/?at=default
    # token names can be taken from http://pygments.org/docs/tokens/
    styles = {Text: FOREGROUND,
        Error: RED,
        Comment: COMMENT,
        Keyword: MAGENTA,
        Keyword.Namespace: MAGENTA,
        Keyword.Type: YELLOW,
        Operator: FOREGROUND,
        Punctuation: FOREGROUND,
        Name: FOREGROUND,
        Name.Attribute: BLUE,
        Name.Class: YELLOW,
        Name.Constant: ORANGE,
        Name.Decorator: BLUE,
        Name.Exception: RED,
        Name.Function: BLUE,
        Name.Namespace: FOREGROUND,
        Name.Other: BLUE,
        Name.Tag: BLUE,
        Name.Variable: ORANGE,
        Number: ORANGE,
        Literal: ORANGE,
        String: GREEN,
        String.Doc: COMMENT,
        String.Escape: ORANGE,
        String.Interpol: ORANGE}


class Config(pdb.DefaultConfig):
    editor = "vi"
    stdin_paste = "epaste"
    prompt = "(pdb) \033[?25h"  # Workaround for missing block cursor
    sticky_by_default = True

    use_pygments = True
    use_terminal256formatter = True
    highlight = True
    filename_color = pdb.Color.darkgray
    line_number_color = pdb.Color.darkgray
    #exec_if_unfocused = "play ~/sounds/dialtone.wav 2> /dev/null &"

    def setup(self, pdb):
        pdb_class = pdb.__class__
        pdb_class.do_l = pdb_class.do_longlist  # alias l
        pdb_class.do_st = pdb_class.do_sticky  # alias st

        # Workaround for https://bitbucket.org/antocuni/pdb/src/cf937bbd910a8f7fe2b84af7cf5ee9dc96c2fe25/pdb.py?at=default#pdb.py-352
        pdb_class._lexer = PythonLexer()
        pdb_class._fmt = Terminal256Formatter(style=base16_tomorrow_dark)  # Force 256 terminal even if TERM="xterm" and not "color256"

