test = {
  'name': 'concatenate',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (concatenate (list (list 1 2) (list 5 1)))
          3d4c7ecb4acfaf693aa03b7427dad047
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (concatenate (list (list 1 2) (list)))
          c96202ad0aa1f77601870e46735eabbd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define (tail-list n so-far)
          ....   (if (= n 0)
          ....       so-far
          ....       (tail-list (- n 1) (cons 1 so-far)))) ; What does scheme return after a `define` statement?
          f78cf18d5af5423c2aee0ccd66948c3d
          # locked
          scm> (define big-list (tail-list 500 '()))
          075a5fc57934b88f3466d0a1ac677996
          # locked
          scm> (define result (concatenate (list big-list (list 1 2 3 4)))) ; Test for tail recursion
          5f671986309a3dd5da78c746300e0efa
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
