test = {
  'name': 'What Would Scheme Print?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cons 1 (cons 2 nil))
          953ec0ef55a30b96faf05f65484ecf36
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (car (cons 1 (cons 2 nil)))
          802285b020b27240a3824a7e42f8cc8c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (cdr (cons 1 (cons 2 nil)))
          5d2599c86459134fdf14f34d84aaee6c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (list 1 2 3)
          d700f681c276ab11887fdae2968b7d51
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> '(1 2 3)
          d700f681c276ab11887fdae2968b7d51
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (cons 1 '(list 2 3))  ; Recall quoting
          92f7d479489db57c65770fe45f112d5b
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> '(cons 4 (cons (cons 6 8) ()))
          664bde2b2222f616d2c0eb939c6c246a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (cons 1 (list (cons 3 nil) 4 5))
          1c679094912cc7efb2e08bd0af96762d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
