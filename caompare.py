path1 = 'chefserver_cookbook_old.txt'
path2 = 'bitbucket_cookbook_new.txt'
import csv

fileAddr = []
fileAddr.append(path1)
fileAddr.append(path2)


def readFile(filePath):
    # Open the file with read only permit
    f = open(filePath, "r")
    # use readlines to read all lines in the file
    # The variable "lines" is a list containing all lines in the file
    lines = f.readlines()
    # close the file after reading the lines.
    f.close()
    return lines


def main():
    list_of_file_old = readFile(fileAddr[0])
    list_of_file_new = readFile(fileAddr[1])
    # print (list_of_file_old)
    # print (list_of_file_new)

    max_length = len(list_of_file_new)

    not_found = []
    with open('persons.csv', 'w') as csvfile:
        #fieldnames = ['header', 'missing_in_old_file', 'extra_in_old_file']
        filewriter = csv.writer(csvfile, delimiter = ';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Filename','missing_in_old_file','extra_in_old_file'])
        for i in range(0, max_length, 1):
            try:
                #file_old_txt_lines = list_of_file_old[i].split()
                file_new = list_of_file_new[i].split()
                search = file_new[0]

                #Logic for taking the matching line
                found = False
                for j in range(0, len(list_of_file_old), 1):
                    if search == list_of_file_old[j].split()[0]:
                        file_old = list_of_file_old[j].split()
                        found = True

                if not found:
                    not_found.append(search)
                else:
                    i = len(file_new)
                    count = {}

                    count['matching'] = ''
                    count['missing_in_old_file'] = ''
                    count['extra_in_old_file'] = []
                    extra = []

                    for j in range(1, i, 1):
                        try:
                            if file_new[j] in file_old:
                                count['matching'] = file_new[j] + " ," + count['matching']
                                extra.append(file_new[j])
                            else:
                                count['missing_in_old_file'] = file_new[j] + " ," + count['missing_in_old_file']
                                extra.append(file_new[j])
                        except IndexError:
                            pass

                    header = file_new.pop(0)
                    old_variable = file_old
                    old_variable.pop(0)
                    extra = list(set(old_variable) - set(extra))
                    count['extra_in_old_file'] = extra
                    print(header + ": " + str(count))
                    filewriter.writerow([header, count['missing_in_old_file'], count['extra_in_old_file']]);

            except IndexError:
                pass
        print("Not found in old file : "+str(not_found))


if __name__ == '__main__':
    main()
