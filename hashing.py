import csv
import hashlib

#Input and Hashing
h = hashlib.new('sha256')
output = [["Hash-Wert", "Studiengang"]]
line = []

with open ('Testdatensatz.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            h.update(bytes(row[0] + row[1] + row[2] + row[3], "utf8"))
            hashvalue = h.hexdigest()
            line = []
            line.append(hashvalue)
            line.append(row[4])
            output.insert(line_count, line)
            line_count += 1
    print(output)


#Output
with open('Ausgabe.txt', mode='w', newline='') as outputFile:
    output_writer = csv.writer(outputFile, delimiter=';')
    output_writer.writerows(output)
