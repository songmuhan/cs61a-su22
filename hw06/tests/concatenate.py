test = {
  'name': 'concatenate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (concatenate (list (list 1 2) (list 5 1)))
          (1 2 5 1)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (concatenate (list (list 1 2) (list)))
          (1 2)
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (tail-list n so-far)
          ....   (if (= n 0)
          ....       so-far
          ....       (tail-list (- n 1) (cons 1 so-far)))) ; What does scheme return after a `define` statement?
          tail-list
          scm> (define big-list (tail-list 500 '()))
          big-list
          scm> (define result (concatenate (list big-list (list 1 2 3 4)))) ; Test for tail recursion
          result
          """,
          'hidden': False,
          'locked': False,
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
