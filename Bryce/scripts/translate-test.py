import csv
import pandas
from google.cloud import translate

translate_dictionary = {}
translate_client = translate.Client()

def translate_row(row):
    starting = row['word']
    if starting not in translate_dictionary:
        try:
            translate_dictionary[starting] = translate_client.translate(
            starting,
            target_language='es')['translatedText']
        except:
            translate_dictionary[starting] = 'Could not translate'
    output = translate_dictionary[starting]
    print(output)
    return output

file_path = '/Users/navba/Downloads/ADevenirProjects/Organizations/DTML.PerformancePrediction/Bryce/NewData/merged_mutated_data_0.csv'
df = pandas.read_csv(file_path, low_memory=False)
df['correct_word'] = df.apply (lambda row: translate_row(row), axis=1)
output_path = '/Users/navba/Downloads/ADevenirProjects/Organizations/DTML.PerformancePrediction/Bryce/NewData/translated_data.csv'
df.to_csv(path_or_buf=output_path, index=False)