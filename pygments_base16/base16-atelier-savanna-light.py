from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, String, Text
)


class BaseSixteenStyle(Style):
    base00 = '#ecf4ee'
    base01 = '#dfe7e2'
    base02 = '#87928a'
    base03 = '#78877d'
    base04 = '#5f6d64'
    base05 = '#526057'
    base06 = '#232a25'
    base07 = '#171c19'
    base08 = '#b16139'
    base09 = '#9f713c'
    base0a = '#a07e3b'
    base0b = '#489963'
    base0c = '#1c9aa0'
    base0d = '#478c90'
    base0e = '#55859b'
    base0f = '#867469'

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
    capwords('atelier-savanna-light', '-').replace('-', '')
)
globals()[BaseSixteenStyle.__name__] = globals()['BaseSixteenStyle']
del globals()['BaseSixteenStyle']
del capwords
