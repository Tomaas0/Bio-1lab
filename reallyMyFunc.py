from Bio import SeqIO

def myFunc(file):

    bpLen = 100

    startCodon = "ATG"
    stopCodons = ["TAG", "TAA", "TGA"]

    orfs = []

    for sequence in SeqIO.parse(file, "fasta"):
        frame = sequence.seq
        inside = False
        orf = ""
        for i in range(round(len(frame) / 3)):
            triplet = frame[i * 3:(i * 3) + 3]
            if inside == True and triplet not in stopCodons:
                orf += triplet
            elif inside == True and triplet in stopCodons:
                orf += triplet
                if len(orf) > bpLen:
                    orfs.append(orf)
                orf = ""
                inside = False
            elif inside == False and triplet == startCodon:
                inside = True
                orf += triplet
    return orfs