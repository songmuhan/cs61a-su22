test = {
  'name': 'vehicles_older',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define owner-laryn (make-owner 'laryn 18)) ; a owner 
          owner-laryn
          scm> (define owner-richard (make-owner 'richard 17)) ; a owner
          owner-richard
          scm> (define owner-cooper (make-owner 'cooper 16))
          owner-cooper
          scm> (define owner-jordan (make-owner 'jordan 16))
          owner-jordan
          scm> (define owner-angel (make-owner 'angel 20))
          owner-angel
          scm> (define owner-gabe (make-owner 'gabe 17))
          owner-gabe
          scm> (define prius-owners (cons owner-cooper (cons owner-jordan nil)))
          prius-owners
          scm> (define car-prius (make-vehicle 'prius 2010 prius-owners))
          car-prius
          scm> (define ford-owners (cons owner-richard nil))
          ford-owners
          scm> (define car-ford (make-vehicle 'ford 2020 ford-owners))
          car-ford
          scm> (define bmw-owners (cons owner-laryn (cons owner-angel nil)))
          bmw-owners
          scm> (define car-bmw (make-vehicle 'bmw 2023 bmw-owners))
          car-bmw
          scm> (older-vehicle car-bmw car-ford)
          ford
          scm> (older-vehicle car-bmw car-prius)
          prius
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      scm> (load "./lab12.scm")
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
