from reallyMyFunc import myFuncThatGetsOrfsFromFile
from Bio.SeqUtils import GC
from myfunc import make_protein_record

orfs = []
proteins = []

for file in ["plazmide.fasta", "ls_orchid.fasta"]:
    fileOrfs = myFuncThatGetsOrfsFromFile(file)
    for orf in fileOrfs:
        orfs.append(orf)
        protein = make_protein_record(orf)
        if len(str(protein.seq)) > 100:
            proteins.append(protein)

file = open("res.txt", "w")
for orf in orfs:
    file.write(str(orf))
    file.write("\n")
    file.write(str(GC(orf))) #4
    file.write("\n\n")

file.write("\n")
    
for protein in proteins:
    file.write(str(protein.seq))
    file.write("\n")
