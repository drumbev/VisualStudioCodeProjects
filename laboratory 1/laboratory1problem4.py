print("LALL")
with open('sequence.txt') as fh:
    paper = []
    for chislo in fh:
        if chislo!=0:
            paper.append(float(chislo))
            print (paper)
print ('Количество чисел меньше и больше 0:', len(paper))