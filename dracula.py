book= open("dracula.txt","r")
count = 0
for line in book:
    if "vampire" in line.lower():
        count+=1
        print(line)
        print(count)
book.close()

