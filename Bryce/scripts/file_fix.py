import json

marked_rows = []

def row_fix(row):
    open_brac = row.find("{")
    close_brac = row.find("}")
    if (open_brac != -1 and close_brac != -1):
        object_string = row[open_brac:close_brac + 1]
        object_string = object_string.replace("'", '"')
        print(object_string)
        try:
            object = json.loads(object_string)
            translated = object["translatedText"]
            
            output = row[0: open_brac] + translated + row[close_brac + 1:]
        except:
            output = row
            marked_rows.append(output)
    else:
        output = row
    return output


input_path = '/Users/navba/Downloads/ADevenirProjects/Organizations/DTML.PerformancePrediction/Bryce/NewData/translated_data.csv'
output_path = '/Users/navba/Downloads/ADevenirProjects/Organizations/DTML.PerformancePrediction/Bryce/NewData/translated_data_fix.csv'

with open(input_path, "r", encoding="utf-8") as input:
    with open(output_path, 'w', encoding="utf-8") as output:
        for line in input:
            output.write(row_fix(line))
print(marked_rows)


