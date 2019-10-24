from Bio import SeqIO

def getOrfsFromFrame(frame):

    startCodon = "ATG"
    stopCodons = ["TAG", "TAA", "TGA"]

    orfs = []
    inside = False
    orf = ""
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


def myFuncThatGetsOrfsFromFile(file):

    orfs = []

    for sequence in SeqIO.parse(file, "fasta"):
        #Einame per pirmus tris frame
        frame = sequence.seq
        orfs += getOrfsFromFrame(frame)
        #Einame per kitus tris frame
        frame = sequence.seq.reverse_complement()
        orfs += getOrfsFromFrame(frame)
    return orfs