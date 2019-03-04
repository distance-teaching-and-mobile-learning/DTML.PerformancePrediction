import pandas
import numpy
words = pandas.read_csv("./WordsResearch/words.csv")
flights = pandas.read_csv("./WordsResearch/flightdata.csv")

merge_result = flights.merge(words, on="word")
merge_result.to_csv(index=False, path_or_buf="./WordsResearch/merge_result.csv")