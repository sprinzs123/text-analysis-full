import json

from debate.news.make_data.person_class import PersonSentiment
from debate.news.make_data.make_words import WordType
from debate.news.make_data.make_sentences import SentencesSentiment
from debate.news.make_data.make_graph import SentimentGraph
from debate.news.make_data.main_sentiment import SentimentSpeech

# create dummy objects that going to have all full object
# pass the correct data into object to be compared to
# paste text from multiple scores here and then compare result to that is meant to be correct answers
# true if test pass, false if test fails
class MultipleTester:
    def __init__(self, text, ignore_people, limit, people_in_text):
        self.full_object = SentimentSpeech(text, ignore_people, limit)
        self.people_in_text = people_in_text
        self.limit = limit

    def get_full_text(self):
        return self.full_object

    # test that provided number of people matches found number of people
    def check_coded_count(self):
        return len(self.full_object.get_all_people_objects()) == self.people_in_text

    # test word correct word count
    # how many words were created so can compare to the limit
    # can be used for multiple and single people text
    def check_word_count(self):
        word_count = 0
        for person in self.full_object.get_all_people_objects():
            words_dic = person.get_person_words().get_all_words()
            word_count += len(words_dic.get('nouns'))
            word_count += len(words_dic.get('verbs'))
            word_count += len(words_dic.get('adverb'))
            word_count += len(words_dic.get('adjective'))
        # get count all words and compare to correct word count
        return word_count == len(self.full_object.get_people_names()) * 4 * self.limit

    # check if sentences were created correctly
    def check_sentence_count(self):
        sentence_count = 0
        for person in self.full_object.get_all_people_objects():
            sentence_dic = person.get_person_sentiment().get_all_sentences()
            sentence_count += len(sentence_dic.get('subjective'))
            sentence_count += len(sentence_dic.get('objective'))
            sentence_count += len(sentence_dic.get('positive'))
            sentence_count += len(sentence_dic.get('negative'))
        return sentence_count == len(self.full_object.get_people_names()) * 4 * self.limit

    # check if overall line was created for graphs
    def check_overall(self):
        print(self.full_object.get_polarity_graph())

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





