with open("inputFile.txt",'r') as file:
    lines = file.readlines()

Batch = 3
end = 0
for i in range(1,Batch + 1):
    if i == 1:
        start = 0
    increase = int(len(lines)/Batch)
    end = end + increase
    with open("splitText_" + str(i) + ".txt",'w') as file:
        for line in lines[start:end]:
            file.write(line)
    
    start = end