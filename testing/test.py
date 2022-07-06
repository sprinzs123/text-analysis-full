import json

from debate.news.make_data.person_class import PersonSentiment
from debate.news.make_data.make_words import WordType
from debate.news.make_data.make_sentences import SentencesSentiment
from debate.news.make_data.make_graph import SentimentGraph
from debate.news.make_data.main_sentiment import SentimentSpeech

# create dummy objects that going to have all full object
# pass the correct data into object to be compared to
# paste text from multiple scores here and then compare result to that is meant to be correct answers
class MultipleTester:
    def __init__(self, text, ignore_people, limit, correct_text, people_in_text):
        self.full_object = SentimentSpeech(text, ignore_people, limit)
        self.correct_text = correct_text
        self.people_in_text = people_in_text

    # compare strings if they are matching from full text analyze
    def check_full(self):
        test_results = self.full_object.get_all_people_objects()
        return test_results == self.correct_text

    # check if over plot was made if more than two people
    # check if overall plot wasn't made when there is only one person
    def check_overall(self):
        people_found = len(self.full_object.get_all_people_objects())
        if people_found == 1 and self.people_in_text == 1:
            return True
        # checking if overall line was created bc overall line is going to have one more Person object
        elif people_found > 1 and (people_found == (self.people_in_text-1)):
            return True
        return False

    def get_full_text(self):
        return self.full_object

    # test ignoring people limit
    def check_correct_count(self):
        people_count = len(self.full_object.get_all_people_objects())
        print(self.full_object.get_people_names())
        return people_count <= self.full_object.get_limit()




    # create string so that can compare
    def to_string(self):
        for person in self.full_object.get_all_people_objects():
            name = person.get_name()
            # record all things that got from sentiment object
            person_sentiment = person.get_person_sentiment()
            avg_polarity = person_sentiment.get_person_polarity()
            avg_objectivity = person_sentiment.get_person_subjectivity()
            positive_sentences = json.dumps(person_sentiment.get_most_positives())
            negative_sentences = json.dumps(person_sentiment.get_most_negatives())
            objective_sentences = json.dumps(person_sentiment.get_most_objective())
            subjective_sentences = json.dumps(person_sentiment.get_most_subjective())

            # record all thing related to person words objects
            person_words = person.get_person_words()
            all_adjectives = json.dumps(person_words.get_adjectives())
            all_adverbs = json.dumps(person_words.get_adverbs())
            all_nouns = json.dumps(person_words.get_nouns())
            all_verbs = json.dumps(person_words.get_verbs())





