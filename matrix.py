
from pyjarowinkler import distance

def getDistanceMatrix(proteins):
    matrix = []
    i = 1

    for protein in proteins:
        name = "protein-" + str(i)
        distances = [name]
        i += 1

        for protein_to_compare in proteins:
            distances.append(distance.get_jaro_distance(str(protein), str(protein_to_compare)))
        
        matrix.append(distances)
    
    return matrix