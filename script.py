from reallyMyFunc import myFuncThatGetsOrfsFromFile
from Bio.SeqUtils import GC
from myfunc import make_protein_record
from matrix import getDistanceMatrix

orfs = []
proteins = []

for file in ["plazmide.fasta", "ls_orchid.fasta"]:
    fileOrfs = myFuncThatGetsOrfsFromFile(file)
    for orf in fileOrfs:
        protein = make_protein_record(orf)
        if len(str(protein.seq)) > 100:
            orfs.append(orf)
            proteins.append(protein)

file = open("res.txt", "w")
file.write("------Found orfs:\n")
for orf in orfs:
    file.write(str(orf))
    file.write("\n")
    file.write("GC: " + str(GC(orf))) #4
    file.write("\n\n")

file.write("\n")
    
file.write("------Proteins translated from orfs:\n")
for protein in proteins:
    file.write(str(protein.seq))
    file.write("\n")

#Kodonų matrica
matrix_file = open("codon_distance_matrix.txt", "w")
matrix = getDistanceMatrix(proteins)
matrix_file.write(str(len(matrix)) + "\n")
for row in matrix:
    for cell in row:
        matrix_file.write(str(cell))
        matrix_file.write(" ")
    matrix_file.write("\n")
