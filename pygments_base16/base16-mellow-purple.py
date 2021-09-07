from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, String, Text
)


class BaseSixteenStyle(Style):
    base00 = '#1e0528'
    base01 = '#1A092D'
    base02 = '#331354'
    base03 = '#320f55'
    base04 = '#873582'
    base05 = '#ffeeff'
    base06 = '#ffeeff'
    base07 = '#f8c0ff'
    base08 = '#00d9e9'
    base09 = '#aa00a3'
    base0a = '#955ae7'
    base0b = '#05cb0d'
    base0c = '#b900b1'
    base0d = '#550068'
    base0e = '#8991bb'
    base0f = '#4d6fff'

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
    capwords('mellow-purple', '-').replace('-', '')
)
globals()[BaseSixteenStyle.__name__] = globals()['BaseSixteenStyle']
del globals()['BaseSixteenStyle']
del capwords
