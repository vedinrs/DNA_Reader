dna_to_amino = {
    "TTT": "F", "TTC": "F",
    "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y",
    "TAA": "X", "TAG": "X",
    "TGT": "C", "TGC": "C",
    "TGA": "STOP",
    "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I",
    "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N",
    "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S",
    "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}


class NoAAEntryException(Exception):
    def __init__(self):
        super(NoAAEntryException, self)


# Takes DNA input and searches for amino acid contained within
def dna_to_aa_reader(text_file, aa_to_find):
    with open(text_file, "r") as f:
        string = f.read()
    string_size = len(string)

    # Return for empty cases
    if aa_to_find == "":
        raise NoAAEntryException
    if string == "":
        return []

    # Set up first amino acid, size of amino acid chain in DNA length, and empty locations list
    aa_first = aa_to_find[0]
    aa_size = len(aa_to_find) * 3
    locations = []

    # Search DNA sequence until there is no possible space for the amino acid chain to fit
    for position in range(0, string_size - aa_size + 1):
        # Calculate the first amino acid by converting 3 DNA letters
        dna_first = string[position] + string[position + 1] + string[position + 2]
        if dna_to_amino[dna_first] == aa_first:
            # Search section of DNA sequence for only the size of the amino acid chains
            for i in range(0, aa_size, 3):
                # Convert DNA a codon at a time (3 letters)
                codon = string[position + i] + string[position + i + 1] + string[position + i + 2]
                # If any DNA codons don't match an amino acid, break from matching
                if dna_to_amino[codon] != aa_to_find[int(i/3)]:
                    break
                # If DNA codons match the whole way through, add the starting location to locations
                elif i + 3 == aa_size:
                    locations.append(position + 1)
    return locations


def dna_reader(text_file, dna_to_find):

    # get text file as string
    with open(text_file, "r") as f:
        string = f.read()
    string_size = len(string)

    # get sequence to find first cha and sequence_size
    if dna_to_find == "" or string == "":
        return []
    first = dna_to_find[0]
    sequence_size = len(dna_to_find)

    # init locations, position, and character in text file
    locations = []
    position = 0

    for c in string:
        if c == first and string_size >= sequence_size + position:
            if dna_to_find == string[position:position + sequence_size]:
                locations.append(position+1)
        position += 1

    return locations
