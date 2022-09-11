test = {
  'name': 'ascending?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (ascending? '(1 2 3 4 5))  ; #t or #f
          61e66592bf67fa9271ff8949e03b640a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 5 2 4 3))  ; #t or #f
          819754a8855b4dc4ac5aaafaca9d759f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(2 2))  ; #t or #f
          61e66592bf67fa9271ff8949e03b640a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (ascending? '(1 2 2 4 3))  ; #t or #f
          819754a8855b4dc4ac5aaafaca9d759f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load-all ".")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
