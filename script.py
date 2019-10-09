from Bio import SeqIO
from myfunc import make_protein_record
from reallyMyFunc import myfunc
proteins = (make_protein_record(seq_record) for seq_record in \
SeqIO.parse("C:\\Users\\tukrinas\\Documents\\ManoProjektai\\BioInformatika\\1 lab\\ls_orchid.fasta", "fasta"))
SeqIO.write(proteins, "translations.fasta", "fasta")
myFunc("BMW", "res.txt")
