import csv

out = []
with open("Appearances-Grid view.csv", "r") as f:
    data = csv.reader(f)
    next(data)
    for row in data:
        pref = [row[5],row[7],row[6]]
        cands = row[11].split(",")
        partys = row[14].split(",")

        for i, v in enumerate(cands):
                tmprow = []
                tmprow.extend(pref)
                tmprow.append(v)
                tmprow.append(partys[i])
                tmprow.append(row[3])

                out.append(tmprow)

with open('tv_cands.csv', mode='w') as out_file:
    w = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    w.writerow(["Дата", "Телевизия","Предаване", "Кандидат", "Партия", "Линк"])
    for row in out:
        w.writerow(row)