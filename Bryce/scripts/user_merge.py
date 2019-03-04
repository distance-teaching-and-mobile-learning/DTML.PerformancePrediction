import pandas
import numpy
users = pandas.read_csv("./WordsResearch/RegisteredUsers.csv")
flights = pandas.read_csv("./NewData/merged_mutated_data_0.csv")

merge_result = flights.merge(users, on="userid")
merge_result.to_csv(index=False, path_or_buf="./NewData/user_mutated_merge.csv")