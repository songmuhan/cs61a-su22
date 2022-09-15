test = {
  'name': 'Question 7',
  'points': 2,
  'suites': [
    {
      'cases': [
        {
          'answer': 'A player and a message (in that order).',
          'choices': [
            'A message.',
            'A player.',
            'A message and a player (in that order).',
            'A player and a message (in that order).'
          ],
          'hidden': False,
          'locked': False,
          'multiline': False,
          'question': 'What does a commentary function return?'
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(4, 6, 4), goal=10, say=announce_lead_changes)
          Player 0 takes the lead by 4
          Player 1 takes the lead by 2
          Player 0 takes the lead by 2
          Player 1 takes the lead by 2
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(1), always_roll(2), dice=make_test_dice(1, 3, 3), goal=10, say=announce_lead_changes)
          Player 0 takes the lead by 2
          Player 1 takes the lead by 4
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1, player=None):
          ...     return player, f"{s0} {s1}" # message of the form: "s0 s1"
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(3), goal=6, say=echo) # Remember pigs on prime!
          5 0
          5 5
          8 5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> def count(n):
          ...     def say(s0, s1, curr_count=None):
          ...         if curr_count is None:
          ...           curr_count = n
          ...         return curr_count + 1, str(curr_count) + " " + str(s0)
          ...     return say
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(5), goal=15, say=count(1))
          1 7
          2 7
          3 12
          4 12
          5 19
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, announce_lead_changes
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> #
          >>> def echo(s0, s1, player=None):
          ...     return player, str(s0) + " " + str(s1)
          >>> strat0 = lambda score, opponent: 1 - opponent // 10
          >>> strat1 = always_roll(3)
          >>> s0, s1 = play(strat0, strat1, dice=make_test_dice(4, 2, 6), goal=15, say=echo)
          4 0
          4 12
          7 12
          7 24
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def total(s0, s1, player=None):
          ...     return player, str(s0 + s1)
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2, 5), goal=10, say=total)
          3
          10
          14
          19
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> def echo_0(s0, s1, player=None):
          ...     return player, f"* {s0}" # message of the form: "* s0"
          >>> def echo_1(s0, s1, player=None):
          ...     return player, f"** {s1}" # message of the form: "** s1"
          >>> s0, s1 = play(always_roll(1), always_roll(1), dice=make_test_dice(2), goal=5, say=both(echo_0, echo_1))
          * 3
          ** 0
          * 3
          ** 3
          * 7
          ** 3
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> #
          >>> s0, s1 = play(always_roll(3), always_roll(3), dice=make_test_dice(1, 2, 3, 3), goal=8, say=both(say_scores, announce_lead_changes))
          Player 0 now has 2 and now Player 1 has 0
          Player 0 takes the lead by 2
          Player 0 now has 2 and now Player 1 has 2
          Player 0 now has 5 and now Player 1 has 2
          Player 0 takes the lead by 3
          Player 0 now has 5 and now Player 1 has 10
          Player 1 takes the lead by 5
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from hog import play, always_roll, both, announce_lead_changes, say_scores
      >>> from dice import make_test_dice
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
