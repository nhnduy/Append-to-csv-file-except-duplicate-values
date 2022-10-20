import csv
with open("file2.csv", "r") as file2:
    file2_reader = csv.reader(file2)
    #Append all value in this file to a list.
    list2 = []
    for line in file2_reader:
        list2.append(line)
        
    with open("file1.csv", "r") as ledger_file:
        ledger_file_reader = csv.reader(ledger_file)
        #Open the ledger file to see if value is in the list, if yes, then remove from the list.
        for line in ledger_file_reader:
            if line in list2:
                print("Data ID", line[0], "is already loaded")
                list2.remove(line)

    with open("file1.csv", "a") as ledger_file:
        ledger_file_writer = csv.writer(ledger_file, lineterminator = "\n")
        for i in range(0, len(list2)):
            ledger_file_writer.writerow(list2[i])