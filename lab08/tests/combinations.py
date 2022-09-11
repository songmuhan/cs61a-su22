test = {
  'name': 'What Would Scheme Display?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (- 10 4)
          de2a3ba9669b4d14ff0cc8972c673db4
          # locked
          scm> (* 7 6)
          d55067d1ee8473920d3d5fa44df70822
          # locked
          scm> (+ 1 2 3 4)
          8be8039fce6ea3657f1a0a9143efa89d
          # locked
          scm> (/ 8 2 2)
          9338923f09aac77121029c604f7ce4f3
          # locked
          scm> (quotient 29 5)
          3595d1fdbdda5f2ecaa323401627e273
          # locked
          scm> (modulo 29 5)
          612ff2a71cad53bc4c7f85fac678a06d
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (= 1 3)                    ; Scheme uses '=' instead of '==' for comparison
          819754a8855b4dc4ac5aaafaca9d759f
          # locked
          scm> (< 1 3)
          61e66592bf67fa9271ff8949e03b640a
          # locked
          scm> (or 1 #t)                  ; or special form short circuits
          802285b020b27240a3824a7e42f8cc8c
          # locked
          scm> (and #t #f (/ 1 0))
          819754a8855b4dc4ac5aaafaca9d759f
          # locked
          scm> (not #t)
          819754a8855b4dc4ac5aaafaca9d759f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define x 3)
          351b65f35ffafa60c1ba486a65d13075
          # locked
          scm> x
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          scm> (define y (+ x 4))
          d5584e1ba2324d1d0e65eb4a3b51c792
          # locked
          scm> y
          c998dea41dacea22138dcbd029eda02f
          # locked
          scm> (define x (lambda (y) (* y 2)))
          351b65f35ffafa60c1ba486a65d13075
          # locked
          scm> (x y)
          2e474b516ec5dd08108727ad9182a2cd
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (if (not (print 1)) (print 2) (print 3))
          802285b020b27240a3824a7e42f8cc8c
          a6a221ff20ce085ab4bedaca5044f971
          # locked
          scm> (* (if (> 3 2) 1 2) (+ 4 5))
          7227ddd8995f4e683b97d1c6795c7513
          # locked
          scm> (define foo (lambda (x y z) (if x y z)))
          7074a0568ca671bc694d2144b0fc8cd6
          # locked
          scm> (foo 1 2 (print 'hi))
          094f9aef0e1f015dcb4f9085c4e23b99
          9338923f09aac77121029c604f7ce4f3
          # locked
          scm> ((lambda (a) (print 'a)) 100)
          1ecad7fe5d364cc03d7cbb65478e1c8a
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
