import csv


def writer(filename, ls):

    with open(
        filename,
        'w',
        newline='',
        encoding='utf-8'
    ) as file:

        writing = csv.writer(file)

        for item in ls:
            writing.writerow([item])


def listadd(filename, ls):

    ls.clear()

    with open(
        filename,
        'r',
        encoding='utf-8'
    ) as file:

        reading = csv.reader(file)

        for row in reading:

            if row:
                ls.append(row[0])