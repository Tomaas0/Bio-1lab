from reallyMyFunc import myFunc

orfs = []

for file in ["plazmide.fasta", "ls_orchid.fasta"]:
    fileOrfs = myFunc(file)
    for orf in fileOrfs:
        orfs.append(orf)

file = open("res.txt", "w")
for orf in orfs:
    file.write(str(orf))
    file.write("\n")