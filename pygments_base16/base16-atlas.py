from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, String, Text
)


class BaseSixteenStyle(Style):
    base00 = '#002635'
    base01 = '#00384d'
    base02 = '#517F8D'
    base03 = '#6C8B91'
    base04 = '#869696'
    base05 = '#a1a19a'
    base06 = '#e6e6dc'
    base07 = '#fafaf8'
    base08 = '#ff5a67'
    base09 = '#f08e48'
    base0a = '#ffcc1b'
    base0b = '#7fc06e'
    base0c = '#14747e'
    base0d = '#5dd7b9'
    base0e = '#9a70a4'
    base0f = '#c43060'

    default_style = ''

    background_color = base00
    highlight_color = base02

    styles = {
        Text: base05,
        Error: base08,  # .err

        Comment: f'italic {base03}',  # .c
        Comment.Preproc: base0f,  # .cp
        Comment.PreprocFile: base0b,  # .cpf

        Keyword: base0e,  # .k
        Keyword.Type: base08,  # .kt

        Name.Attribute: base0d,  # .na
        Name.Builtin: base0d,  # .nb
        Name.Builtin.Pseudo: base08,  # .bp
        Name.Class: base0d,  # .nc
        Name.Constant: base09,  # .no
        Name.Decorator: base09,  # .nd
        Name.Function: base0d,  # .nf
        Name.Namespace: base0d,  # .nn
        Name.Tag: base0e,  # .nt
        Name.Variable: base0d,  # .nv
        Name.Variable.Instance: base08,  # .vi

        Number: base09,  # .m

        Operator: base0c,  # .o
        Operator.Word: base0e,  # .ow

        Literal: base0b,  # .l

        String: base0b,  # .s
        String.Interpol: base0f,  # .si
        String.Regex: base0c,  # .sr
        String.Symbol: base09,  # .ss
    }


from string import capwords  # noqa: E402
BaseSixteenStyle.__name__ = 'BaseSixteen{}Style'.format(
    capwords('atlas', '-').replace('-', '')
)
globals()[BaseSixteenStyle.__name__] = globals()['BaseSixteenStyle']
del globals()['BaseSixteenStyle']
del capwords
