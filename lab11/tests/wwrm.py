test = {
  'name': 'wwrm',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'answer': 'f59bf86c61665238acb6dc96c16fe4c1',
          'choices': [
            'Any 6-digit hexadecimal color code, like #fdb515',
            'A hexadecimal color code that starts with letters and ends with numbers, like #gg1234',
            'Any hexadecimal color code with 0-6 digits',
            'A hexadecimal color code with 3 letters and 3 numbers'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '#[a-f0-9]{6}'
        },
        {
          'answer': '37b878beb08822b3099080ababc220e1',
          'choices': [
            'Only fizzbuzz',
            'Only fizz',
            'Only fizzbuzz, fizz, and buzz',
            'Only fizzbuzzbuzz',
            'Only fizzbuzz or buzz'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '(fizz(buzz|)|buzz)'
        },
        {
          'answer': '369730cd8c646cf676a78d3f345b9ffb',
          'choices': [
            'Signed or unsigned numbers like +1000, -1.5, .051',
            'Only unsigned numbers like 0.051',
            'Only signed numbers like +1000, -1.5',
            'Only signed or unsigned integers like +1000, -33'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '[-+]?\\d*\\.?\\d+'
        },
        {
          'answer': '9e6a5047e6ce550cd40a61f6f8d46913',
          'choices': [
            'Numbers that are both greater than 5 and divisible by 5 like 10, 25, 800',
            'Numbers that are divisible by 5 like 5, 20, 6325',
            'Any positive number',
            'Numbers that are divisible by 5 but do not have the digits 0 and 5 adjacent to each other as the last 2 digits'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': '[1-9]+[05]+'
        }
      ],
      'scored': False,
      'type': 'concept'
    }
  ]
}
