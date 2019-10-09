from Bio.SeqRecord import SeqRecord
def make_protein_record(nuc_record):
    print (nuc_record)
    """Returns a new SeqRecord with the translated sequence (default table)."""
    return SeqRecord(seq = nuc_record.seq.translate(cds=True), \
                     id = "trans_" + nuc_record.id, \
                     description = "translation of CDS, using default table")