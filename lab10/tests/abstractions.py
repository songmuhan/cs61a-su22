test = {
  'name': 'What Would Scheme Display?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define x (rational 2 5))
          adfa7f54c8ad7613f4804096e85be4da
          # locked
          scm> (numer x)
          8f01429f05539100445ff1214be81240
          # locked
          scm> (denom x)
          fc2b3643bc0ad882bd631ec7e0059563
          # locked
          scm> (define y (rational 1 4))
          612417f3d036b486fb3efc75ae7d405e
          # locked
          scm> (define z1 (add-rational x y))
          274d3e28850a058b5ae7f1ca8bf21015
          # locked
          scm> (numer z1)
          fcb47d3be02a041669f09feae9b3221b
          # locked
          scm> (denom z1)
          6551524ccbb73a0b37abe37be7e51ac9
          # locked
          scm> (define z2 (mul-rational x y))
          683b24063935b4b9d6f175f8c8f69198
          # locked
          scm> (numer z2)
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          scm> (denom z2)
          e22bdbd25c9aca39ec85b51ce5397f2c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define t (tree 1 (list (tree 2 nil))))
          e5df112e96ca0ed3ddf1a8fbf736ff6e
          # locked
          scm> (label t)
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          scm> (length (branches t))
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          scm> (define child (car (branches t)))
          d6f2118d71ff2b7c36eda17afffcdd74
          # locked
          scm> (label child)
          8f01429f05539100445ff1214be81240
          # locked
          scm> (is-leaf child)
          77a392e3d9610adc8d0a003c4882ee01
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          scm> (define b1 (tree 5 (list (tree 6 nil) (tree 7 nil)) )) 
          a705337a27c3bd333ed5a85047c51718
          # locked
          scm> (map is-leaf (branches b1))  ; draw the tree if you get stuck!
          b6bcbe60f92a6fa69b24ebe1b51d37a6
          # locked
          scm> (define b2 (tree 8 (list (tree 9 (list (tree 10 nil)) )) )) 
          1097480fe81d68228e29b960c30f5f37
          # locked
          scm> (map is-leaf (branches b2))  ; draw the tree if you get stuck!
          446d85e85160b384cbe7209917d5bea3
          # locked
          scm> (define t (tree 11 (list b1 b2)))
          e5df112e96ca0ed3ddf1a8fbf736ff6e
          # locked
          scm> (label t)
          2e82c04b3502c98add74b4a4ed6a3950
          # locked
          scm> (map (lambda (b) (label b)) (branches t))
          d923e19c51d23bab15b99cb707567811
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./lab10.scm")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
