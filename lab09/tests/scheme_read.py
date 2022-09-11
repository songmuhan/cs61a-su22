test = {
  'name': 'scheme_read',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['nil'])))
          nil
          >>> scheme_read(Buffer(tokenize_lines(['1'])))
          1
          >>> scheme_read(Buffer(tokenize_lines(['true'])))
          True
          >>> read_tail(Buffer(tokenize_lines(['2)'])))
          Pair(2, nil)
          >>> read_tail(Buffer(tokenize_lines(['(2)'])))
          SyntaxError
          >>> read_line('3')
          3
          >>> read_line('-123')
          -123
          >>> read_line('1.25')
          1.25
          >>> read_line('true')
          True
          >>> read_line('(a)')
          Pair('a', nil)
          >>> read_line(')')
          SyntaxError
          >>> read_line('(a))')
          SyntaxError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
          >>> src = Buffer(tokens)
          >>> src.current()
          a89feb44db49f242b94c0375cbb166f2
          # locked
          >>> src.pop_first()
          a89feb44db49f242b94c0375cbb166f2
          # locked
          >>> src.current()
          211dd910bb61b89e684d311ef1cf3173
          # locked
          >>> src.pop_first()
          211dd910bb61b89e684d311ef1cf3173
          # locked
          >>> src.pop_first()
          d912fc844d1dbaeea8a84b3ec8b315bc
          # locked
          >>> scheme_read(src)  # Removes the next complete expression in src and returns it as a Pair
          6181c49f3c95db91af2c7bb01c26ec14
          # locked
          >>> src.current()
          8a5196e53f2e4ca720d1250e2af404e9
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['(18 6)']))) # Type SyntaxError if you think this errors
          5e22332a66344f519c4db1218285b4d5
          # locked
          >>> read_line('(18 6)')  # Shorter version of above!
          5e22332a66344f519c4db1218285b4d5
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines([')'])))
          5d6a7a152299c7febf53176041fe4065
          # locked
          >>> read_tail(Buffer(tokenize_lines(['1 2 3)'])))
          68f50087dd1d3cb41ad3c0f83f2c5751
          # locked
          >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
          c646d063a62455fb2f784bfbc722a97d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines(['(1 2 3)']))) # Type SyntaxError if you think this errors
          c5bf24718fd9f83b31ef401e5c177d96
          # locked
          >>> read_line('((1 2 3)') # Type SyntaxError if you think this errors
          c5bf24718fd9f83b31ef401e5c177d96
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 2)"]))
          >>> scheme_read(src)
          Pair('+', Pair(1, Pair(2, nil)))
          >>> src.current() # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_line("(+ (- 2 3) 1)")
          a03b3e1c2fdcea669103e9841e8066bb
          # locked
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, Pair(1, nil)))))
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil))
          # choice: Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_line("()")
          nil
          >>> read_line("((a))")
          Pair(Pair('a', nil), nil)
          >>> read_line("(+ 1 (- 2 3) 8)")
          Pair('+', Pair(1, Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, 3), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair(Pair('-', Pair(2, 3)), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, Pair(3, nil)), Pair(8, nil))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
