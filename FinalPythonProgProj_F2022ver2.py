#FINAL PROJECT

##SPECIAL NOTES: DO NOT INCLUDE ANY FUNCTION CALLS IN YOUR FINAL CODE
## ALSO, USE THE FUNCTION NAMES EXACTLY AS I HAVE WRITTEN THEM
##  AND DO NOT CHANGE THE NUMBER OR TYPES OF PARAMETERS

# NOTE: Function 1 and 3 do not return values. Instead, they write files.
#       For Function 1 and 3 you can return 1 if you like but not necessary.
#       
#       Function 2 DOES return a value though (see below).

#Global Variables used in functions 1 and 2 below:
standard_code = {
     "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "UCU": "S",
     "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y", "UAC": "Y",
     "UAA": "*", "UAG": "*", "UGA": "*", "UGU": "C", "UGC": "C",
     "UGG": "W", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
     "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "CAU": "H",
     "CAC": "H", "CAA": "Q", "CAG": "Q", "CGU": "R", "CGC": "R",
     "CGA": "R", "CGG": "R", "AUU": "I", "AUC": "I", "AUA": "I",
     "AUG": "M", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
     "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "AGU": "S",
     "AGC": "S", "AGA": "R", "AGG": "R", "GUU": "V", "GUC": "V",
     "GUA": "V", "GUG": "V", "GCU": "A", "GCC": "A", "GCA": "A",
     "GCG": "A", "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
     "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

#Function 1: Reads in a DNA sequence fasta file,
#            and outputs a Fasta file of protein translations.
#            This function uses the global variable standard_code above.
#            The output fasta will have the same titles as the input file.

def dna_2_prot(f1, f2="translated_fasta.txt"):
    """f1=input file name, f2=output file name"""
    return

#Example function call:

#dna_2_prot("testDNA.txt")

#Function 2: One hot encoding function. This function turns a DNA sequence in to
#            0s and 1s for computer analysis. This is useful for machine learning.
#            The function takes a DNA sequence as a parameter and returns a 2D list
#            (a list within a list) of the DNA in bits.

#For example if seq1 is:
seq1="AGCT"
#The one hot encoding of seq1 will be:
one_hot_for_seq1=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
#Each element of the list is a list of one_hot_encoding for each base of the sequence
# The order within each of the lists is A,G,T,C
#if the base is an A, the list will be [1,0,0,0]
#if the base is a G, the list will be  [0,1,0,0]..etc.
#Here another example:
seq2="AATTT"
one_hot_for_seq2=[[1,0,0,0],[1,0,0,0],[0,0,0,1],[0,0,0,1],[0,0,0,1]]


def hot_code_DNA(seq):
    """Input is a DNA sequence of any length"""
    return

#Test function call:
output=hot_code_DNA(seq1)
print(output)
##Sould print: [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


#Function 3: Reads in a fasta file and searches for a given motif. Outputs a
#    file of the number of times that the motif was found in each sequence. The
#    output file will be tab-delimited.

#Here is a little code snippet that might be useful. 

"""
import re
Seq1="MNGMNNMNRVFRLVQRM"
y=re.findall("V[A-Z]R[ML]",Seq1)
print(y)
['VFRL', 'VQRM']
"""
#And the output should look like this
"""
SeqName     Motif       Hits            
Seq1        MN[A-Z]        2
Seq2        MN[A-Z]        0
Seq3        MN[A-Z]        1
""" 

def motif_finder(f1, motif, f2="motifs.txt"):
    """f1=input file name, motif=the motif pattern, f2=output file name"""
    return

#Example function call:

#motif_finder("testProtein.txt","MN[A-Z]")

