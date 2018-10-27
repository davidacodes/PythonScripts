#! python 3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado':
            'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida':
            'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho':
            'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa':
            'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana':
            'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts':
            'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi':
            'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska':
            'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey':
            'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina':
            'Raleigh', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island':
            'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre',
            'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming':
            'Cheyenne'}

#Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:')

    # TODO: Shiffle the order of the states.

    # TODO: Loop through all 50 states, making a question for each.
