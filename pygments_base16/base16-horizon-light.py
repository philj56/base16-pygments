from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, String, Text
)


class BaseSixteenStyle(Style):
    base00 = '#FDF0ED'
    base01 = '#FADAD1'
    base02 = '#F9CBBE'
    base03 = '#BDB3B1'
    base04 = '#948C8A'
    base05 = '#403C3D'
    base06 = '#302C2D'
    base07 = '#201C1D'
    base08 = '#F7939B'
    base09 = '#F6661E'
    base0a = '#FBE0D9'
    base0b = '#94E1B0'
    base0c = '#DC3318'
    base0d = '#DA103F'
    base0e = '#1D8991'
    base0f = '#E58C92'

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
    capwords('horizon-light', '-').replace('-', '')
)
globals()[BaseSixteenStyle.__name__] = globals()['BaseSixteenStyle']
del globals()['BaseSixteenStyle']
del capwords
