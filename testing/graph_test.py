from debate.news.make_data.make_graph import SentimentGraph
import json

# opening sample data
# return list of object that need to convert
with open('graph_data.json', encoding="utf8") as graph_data:
    graph_data = json.load(graph_data).get("graph_data")

# covert list of objects to dictionary that have all objects
# graph data is in this format
dictionary_data = {}
for item in graph_data:
    dictionary_data.update(item)

# starting testing our graph maker class
new_graph = SentimentGraph(dictionary_data, -1, 1)
new_graph.saved_sorted_graph("tile", "x axis title", "axis label")