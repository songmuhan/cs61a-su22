test = {
  'name': 'vehicles_selectors',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define owner-laryn (make-owner 'laryn 18)) ; a owner 
          owner-laryn
          scm> (get-name owner-laryn)
          laryn
          scm> (get-age owner-laryn)
          18
          scm> (define owner-richard (make-owner 'richard 17)) ; a owner
          owner-richard
          scm> (get-name owner-richard)
          richard
          scm> (get-age owner-richard)
          17
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
          scm> (get-model car-prius)
          prius
          scm> (get-year car-prius)
          2010
          scm> (get-owners car-prius)
          ((cooper 16) (jordan 16))
          scm> (define ford-owners (cons owner-richard nil))
          ford-owners
          scm> (define car-ford (make-vehicle 'ford 2020 ford-owners))
          car-ford
          scm> (get-model car-ford)
          ford
          scm> (get-year car-ford)
          2020
          scm> (get-owners car-ford)
          ((richard 17))
          scm> (define bmw-owners (cons owner-laryn (cons owner-angel nil)))
          bmw-owners
          scm> (define car-bmw (make-vehicle 'bmw 2023 bmw-owners))
          car-bmw
          scm> (get-model car-bmw)
          bmw
          scm> (get-year car-bmw)
          2023
          scm> (get-owners car-bmw)
          ((laryn 18) (angel 20))
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
