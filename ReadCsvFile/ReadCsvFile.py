import csv

file_name = 'ReadCsvFile/sample-synthetic-healthcare.csv'
health_dic = []
def csv_reader():
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for row in reader:
           health_dic.append(row)
        return health_dic