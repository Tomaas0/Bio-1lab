from Bio import SeqIO

def myFunc(file):

    startCodon = "ATG"
    stopCodons = ["TAG", "TAA", "TGA"]

    orfs = []

    for sequence in SeqIO.parse(file, "fasta"):
        frame = sequence.seq
        inside = False
        orf = ""
        #Einame per pirmus tris frame
        for j in range(3):
            for i in range(round(len(frame) / 3)):
                triplet = frame[(i * 3) + j:(i * 3) + 3 + j]
                if inside == True and triplet not in stopCodons:
                    orf += triplet
                elif inside == True and triplet in stopCodons:
                    orf += triplet
                    orfs.append(orf)
                    orf = ""
                    inside = False
                elif inside == False and triplet == startCodon:
                    inside = True
                    orf += triplet
        frame = sequence.seq.reverse_complement()
        inside = False
        orf = ""
        #Einame per kitus tris frame
        for j in range(3):
            for i in range(round(len(frame) / 3)):
                triplet = frame[(i * 3) + j:(i * 3) + 3 + j]
                if inside == True and triplet not in stopCodons:
                    orf += triplet
                elif inside == True and triplet in stopCodons:
                    orf += triplet
                    orfs.append(orf)
                    orf = ""
                    inside = False
                elif inside == False and triplet == startCodon:
                    inside = True
                    orf += triplet
    return orfs