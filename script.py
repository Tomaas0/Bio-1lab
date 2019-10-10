from reallyMyFunc import myFunc
from myfunc import make_protein_record

orfs = []
proteins = []

for file in ["plazmide.fasta", "ls_orchid.fasta"]:
    fileOrfs = myFunc(file)
    for orf in fileOrfs:
        orfs.append(orf)
        proteins.append(make_protein_record(orf))

file = open("res.txt", "w")
for orf in orfs:
    file.write(str(orf))
    file.write("\n")

file.write("\n")
    
for protein in proteins:
    file.write(str(protein.seq))
    file.write("\n")