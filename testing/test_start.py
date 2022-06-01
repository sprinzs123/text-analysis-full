import test
import json




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

# files to compare to that have correct result
with open('correct_one.json', encoding="utf8") as correct_one:
    correct_one = correct_one.read()
correct_one = correct_one




single_test = test.MultipleTester(one_person, "", 5, "", 1)
first_person = single_test.get_full_text().get_all_people_objects()[0]

# print(json.dumps(first_person.get_all_data()))
# print("/n")
# print(json.loads(correct_one))

first_person_str = str(first_person.get_all_data())
correct_one_person_len = len(first_person_str)

# test to see if entire object was created correctly
if correct_one_person_len == 3383:
    print("PASS one person results")
else:
    print("FAIL one person results")
