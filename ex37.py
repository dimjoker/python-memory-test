# -*- coding: utf-8 -*-
def start():
    print "Which test do you want to run?"
    print "Keywords, Data Types, String Escape Sequences, String Formats or Operators"
    program = raw_input("> ")
    exercise(program)
    
def exercise(program):
    filename_exercise = program + "_exercise.txt"
    filename_answer = program + "_answer.txt"
    exercise_in_file = open(filename_exercise)
    answer_in_file = open(filename_answer)
    questions = exercise_in_file.read().splitlines()
    answers = answer_in_file.read().splitlines()
    right = 0
    wrong = 0
    i = 0
    incorrect = []
    incorrect_result = []
    for question in questions:
        print question
        answer_input = raw_input("> ")
        print answers[i]
        if answer_input == answers[i]:
            print "right"
            right += 1
        else:
            print "wrong"
            wrong += 1
            incorrect.append(question)
            incorrect_result.append(answers[i])
        i += 1
    print "right = %d, wrong = %d" % (right, wrong)
    for w in range(0, i - right):
        print incorrect_result[w], incorrect[w]
        w += 1
    
start()