import csv
file=open("data.csv")
csv_reader=csv.reader(file)
data_list=list(csv_reader)
def find_most_run_scorer(data:list):
    most_runs=0
    scorer=[]
    for row in data:
        if int(row [4])>most_runs:
            scorer=row
            most_runs=int(row[4])
    print(scorer)
    return
find_most_run_scorer(data_list[1:])
