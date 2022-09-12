test = {
  'name': 'teacher_student_selectors',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (define student-rachel (student-create 'rachel '(astronomy))) ; a student named rachel who has attended astronomy once
          student-rachel
          scm> (student-get-name student-rachel)
          rachel
          scm> (student-get-classes student-rachel)
          (astronomy)
          scm> (define student-lucy (student-create 'lucy '(astronomy astronomy))) ; a student named lucy who has attended astronomy twice
          student-lucy
          scm> (student-get-name student-lucy)
          lucy
          scm> (student-get-classes student-lucy)
          (astronomy astronomy)
          scm> (define students (cons student-rachel (cons student-lucy nil)))
          students
          scm> (define teacher-pamela (teacher-create 'pamela 'cs61a students)) ; they are pamela's students!
          teacher-pamela
          scm> (teacher-get-name teacher-pamela)
          pamela
          scm> (teacher-get-class teacher-pamela)
          cs61a
          scm> (map student-get-name (teacher-get-students teacher-pamela))
          (rachel lucy)
          scm> (map student-get-classes (teacher-get-students teacher-pamela))
          ((astronomy) (astronomy astronomy))
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
