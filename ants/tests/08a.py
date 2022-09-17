test = {
  'name': 'Problem 8a',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': "In the ContainerAnt's ant_contained instance attribute",
          'choices': [
            "In the ContainerAnt's ant_contained instance attribute",
            "In the ContainerAnt's ant_contained class attribute",
            "In its place's ant instance attribute",
            "Nowhere, a ContainerAnt has no knowledge of the ant that it's protecting"
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'Where is the ant contained by a ContainerAnt stored?'
        },
        {
          'answer': 'By protecting the ant from Bees and allowing it to perform its original action',
          'choices': [
            'By protecting the ant from Bees and allowing it to perform its original action',
            'By attacking Bees that try to attack it',
            "By increasing the ant's health",
            'By allowing Bees to pass without attacking'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'How does a ContainerAnt guard its ant?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> container = ContainerAnt(1)
          >>> container2 = ContainerAnt(2)
          >>> container3 = ContainerAnt(3)
          >>> throw_long = LongThrower(1)
          >>> container.can_contain(container2)
          False
          >>> container3.can_contain(throw_long)
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(2)
          >>> friend = HungryAnt()
          >>> container.ant_contained is None
          True
          >>> container.store_ant(friend)
          >>> container.ant_contained is friend
          True
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': False,
      'setup': r"""
      >>> from ants import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
