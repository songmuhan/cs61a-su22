test = {
  'name': 'Problem 8a',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'cf13df85d8ffea8b7928c6f0f860c5e1',
          'choices': [
            "In the ContainerAnt's ant_contained instance attribute",
            "In the ContainerAnt's ant_contained class attribute",
            "In its place's ant instance attribute",
            "Nowhere, a ContainerAnt has no knowledge of the ant that it's protecting"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'Where is the ant contained by a ContainerAnt stored?'
        },
        {
          'answer': '22a2c7eb1d7adee7ea4eb970d3cc09e9',
          'choices': [
            'By protecting the ant from Bees and allowing it to perform its original action',
            'By attacking Bees that try to attack it',
            "By increasing the ant's health",
            'By allowing Bees to pass without attacking'
          ],
          'hidden': False,
          'locked': True,
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
          03456a09f22295a39ca84d133a26f63d
          # locked
          >>> container3.can_contain(throw_long)
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> container = ContainerAnt(2)
          >>> friend = HungryAnt()
          >>> container.ant_contained is None
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          >>> container.store_ant(friend)
          >>> container.ant_contained is friend
          c7a88a0ffd3aef026b98eef6e7557da3
          # locked
          """,
          'hidden': False,
          'locked': True,
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
