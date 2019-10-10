from Bio.SeqRecord import SeqRecord
def make_protein_record(nuc_record):
    """Returns a new SeqRecord with the translated sequence (default table)."""
    return SeqRecord(seq = nuc_record.translate(cds=True), \
                     id = "translation", \
                     description = "translation of CDS, using default table")