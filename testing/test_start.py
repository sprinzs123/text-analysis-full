import test
import json

# global variables to keep error count
single_person_error = 0
multiple_person_error = 0

# global variable to see if all the testes passed or not
test_fail = False

# files with input text
with open('one_person_data.txt', encoding="utf8") as debate:
    fullText = debate.read()
one_person = fullText


with open('three_people_data.txt', encoding="utf8") as multiple:
    multiple = multiple.read()
multiple_people = multiple


with open('three_people_mixed.txt', encoding="utf8") as multiple_mixed:
    multiple_mixed = multiple_mixed.read()
debate_three_people = multiple_mixed


# global variable for error checking
error_found = False

#inputs for creating test objects ###
# text, ignore_people, limit, correct_text, people_in_text
ignore_people = ''
limit = 5
people_in_text = 1
single_test = test.MultipleTester(one_person, ignore_people, limit,  people_in_text)

# multiple people checks start here
ignore_people = ''
limit = 5
people_in_text = 1
three_test = test.MultipleTester(one_person, ignore_people, limit,  people_in_text)

##### test for single and multiple people #########
# check both single and multiple people objects for correct number of words
def word_check(people_object):
    if people_object.check_word_count():
        print("PASS........number of words")
    else:
        print("FAIL........number of words")
        error_found = True


def sentence_check(people_object):
    if people_object.check_sentence_count():
        print("PASS........number of sentences")
    else:
        print("FAIL........number of sentences")
        error_found = True


def count_check(people_object):
    if people_object.check_coded_count():
        print("PASS........number of sentences")
    else:
        print("FAIL........number of sentences")
        error_found = True


# main functions that going to be called to check things
def single_checker():
    print('Start single person test')
    word_check(single_test)
    sentence_check(single_test)
    count_check(single_test)


def multiple_checker():
    print('\n')
    print('Start multiple person test')
    word_check(three_test)
    sentence_check(three_test)
    count_check(three_test)


# calling functions that call tests for person objects
# as well returning boolean to re
def get_error_status():
    single_checker()
    multiple_checker()
    return error_found

get_error_status()
