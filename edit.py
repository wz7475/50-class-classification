# read csv with space and write csv with comma
import csv

path = "Filipecki_Zarzecki.csv"
path_spaces = "Filipecki_Zarzecki.csv"
with open(path_spaces, 'r') as f:
    reader = csv.reader(f, delimiter=' ')
    lines = list(reader)
with open(path, 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(lines)

