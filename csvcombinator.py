import csv
import sys
import os


def csv_combiner(filenames):
    with open('combined.csv', 'w', newline='', buffering=1024*1024) as f:
        writer = csv.writer(f)
        col_names = []
        for filename in filenames:
            with open(filename, 'r', buffering=1024*1024) as file:
                reader = csv.reader(file)
                header = next(reader)
                for col in header:
                    if col not in col_names:
                        col_names.append(col)
        col_names.append("file name")
        writer.writerow(col_names)

        for filename in filenames:
            with open(filename, 'r', buffering=1024*1024) as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    while len(row) < len(col_names)-1:
                        row.append("Null")
                    row.append(os.path.basename(filename))
                    writer.writerow(row)


if __name__ == '__main__':
    csv_combiner(sys.argv[1:])
