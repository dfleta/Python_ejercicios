#Dictionaries of Dictionaries (of Dictionaries)

#The next several questions concern the data structure below for keeping 
#track of Udacity's courses (where all of the values are strings):
  
#    { <hexamester>, { <class>: { <property>: <value>, ... },
#                                     ... },
#      ... }

#For example,

courses = {
    'feb2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'apr2012': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'jan2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


#For the following questions, you will find the
#        for <key> in <dictionary>:
#                   <block>
#construct useful.  This loops through the key values in the Dictionary.  For
#example, this procedure returns a list of all the courses offered in the given
#hexamester:

def courses_offered(courses, hexamester):
    res = []
    for c in courses[hexamester]:
        res.append(c)
    return res



def cursoPorSemestre(courses, semestre):

  try:
    return list(courses[semestre])
  except KeyError:
    return False

print cursoPorSemestre(courses, 'feb2012')
# ['cs101', 'cs373']
print cursoPorSemestre(courses, 'may2012')
# False


def cursoPorSemestre_iterando(courses, semestre):

  try:
    diccionarioCursos = courses[semestre]
    
    listaCursos = []
    for curso in diccionarioCursos:
      listaCursos.append(curso)
    return listaCursos

  except KeyError:
    return False

print cursoPorSemestre(courses, 'feb2012')
# ['cs101', 'cs373']
print cursoPorSemestre(courses, 'may2012')
# False


#Define a procedure, is_offered(courses, course, hexamester), that returns True
#if the input course is offered in the input hexamester, and returns False
#otherwise.  For example,

#print is_offered(courses, 'cs101', 'apr2012') => True
#print is_offered(courses, 'cs003', 'apr2012') => False

#(Note: it is okay if your procedure produces an error if the input hexamester is not included in courses.  
#For example, is_offered(courses, 'cs101', 'dec2011') can produce an error.)

def is_offered(courses, course, hexamester):

  try:
    return course in courses[hexamester]
  except KeyError:
    return False



print is_offered(courses, 'cs101', 'apr2012')
# True
print is_offered(courses, 'cs003', 'apr2012')
# False
print is_offered(courses, 'cs101', 'may2012')
# KeyError => False