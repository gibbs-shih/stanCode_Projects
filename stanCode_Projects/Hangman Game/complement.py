"""
Name:　Gibbs
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This function will find the complement strand of a DNA sequence input by user.
    """
    dna = input("Please give me a DNA strand and I'll find the complement: ")
    dna = dna.upper()
    new_dna = build_complement(dna)
    print('The complement of '+str(dna)+' is '+str(new_dna)+'.')


def build_complement(dna):
    """
    :param dna: The original DNA strand input by user.
    :return: The complement strand of the original DNA.
    """
    new_dna = ''
    for nucleotide in dna:
        if nucleotide == "A":
            new_dna = new_dna + "T"
        elif nucleotide == "T":
            new_dna = new_dna + "A"
        elif nucleotide == "C":
            new_dna = new_dna + "G"
        elif nucleotide == "G":
            new_dna = new_dna + "C"
    return new_dna


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
