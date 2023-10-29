import json


with open('rna_codon_table.json') as f:
    #######################################################################
    # TODO:                                                               #
    # Use json.load function to load contents of json file to a dict      #
    #######################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    r_c_t = json.load(f)
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


# Вспомогательный класс для вызова SequenceError
# raise SequenceError('Error text')
class SequenceError(Exception):
    def __init__(self, message: str) -> None:
        self.message = message
    
    def __str__(self) -> str:
        return f'{self.message}'

class Sequence(object):
    seq_type = None
    types = set(['DNA', 'RNA', 'Protein']) # all possible sequence types

    #######################################################################
    # TODO:                                                               #
    # Create sets: _prot_acids (a set of all amino acids using            #  
    # json codon_table), _dna_nucls (a set of all nucleotides in a DNA),  #
    # _rna_nucls (a set of all nucleotides in a RNA)                      #
    #######################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    _prot_acids = set(r_c_t.values())
    _dna_nucls = set(['A', 'T', 'G', 'C'])
    _rna_nucls = set(['A', 'U', 'G', 'C'])
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    def __init__(self, file_name: str) -> None:
        """
        Input:
        - file_name : FASTA file with sequence_name, sequence_type and 
        the sequence itself

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Using _parse and _check methods check that input sequence is        #
        # correct. Add an extra check that resulting sequence type corresponds#
        # to the given sequence_type. if everything is fine then create       #
        # sequence_attribute to store given sequence and change self.seq_type # 
        # to sequence_type, else raise Error                                  #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.file_name = file_name
        self.seq_type, self.seq = self._parse(file_name)
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        
    def _parse(self, file_name: str) -> tuple[str, str]:
        """
        Input:
        - file_name : FASTA file with sequence_name, sequence_type and 
        the sequence itself

        Output: A tuple with (sequence, sequence_type)
        """
        #######################################################################
        # TODO:                                                               #
        # Open file_name and read its contents.                               #
        # Input file format:                                                  #
        # >sequence_name sequence_type                                        #
        # sequence                                                            #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        with open(self.file_name, 'r') as fl:
            lns = fl.readlines()
            seq = ''
            seq_type = ''
            for i, ln in enumerate(lns):
                ln = ln.strip()
                if '>' in ln:
                    seq_type = ln.split()[1]
                    seq = lns[i+1].strip()
                    break
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def _check(self, string: str) -> bool:
        """
        Input:
        - string : sequence from FASTA file

        Output: A boolean value (True or False)
        """
        #######################################################################
        # TODO:                                                               #
        # Check that given type is in self.types                              #
        # Check that every element of given string is either in               #
        # self._prot_acids/self._dna_nucls/self._rna_nucls. If its true,      #
        # return True, else return False                                      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        if self.seq_type not in self.types:
            return False
        if self.seq_type == 'Protein':
            for i in self.seq:
                if i not in self._prot_acids:
                    return False
        if self.seq_type == 'DNA':
            for i in self.seq:
                if i not in self._dna_nucls:
                    return False
        if self.seq_type == 'RNA':
            for i in self.seq:
                if i not in self._rna_nucls:
                    return False
        else:
            return True
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def hamming_distance(self, seq, str2: str) -> int:
        """
        Input:
        - sequence : another sequence of nucleotides

        Output: number of different letters 
        between sequence_attribute and given string sequence
        """
        #######################################################################
        # TODO:                                                               #
        # First, check that sequence_attribute and given string have the same #
        # length, if not raise Error.                                         #
        # If the length of strings is the same, loop over one of the strings  #
        # and count different letters.                                        #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        c = 0
        if len(self.seq) != len(str2):
            raise ValueError('string lengths are not the same')
        else:
            for i in range(min(len(self.seq), len(str2))):
                if self.seq[i] != str2[i]:
                    c += 1
        self.h_d = c
        return self.h_d
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def count_nucleotides(self) -> None:
        """
        Input: None

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Raise an error, since transrcibe method can work only with elements #
        # of DNA, RNA or Protein classes                                      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        raise NameError
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> None:
        """
        Input: None

        Output: Non
        """
        #######################################################################
        # TODO:                                                               #
        # Raise an error, since transrcibe method can work only with elements #
        # of DNA, RNA or Protein classes                                      #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        raise NameError
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> None:
        """
        Input: None

        Output: None
        """
        #######################################################################
        # TODO:                                                               #
        # Raise an error, since transrcibe method can work only with elements #
        # of DNA or RNA classes                                               #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        raise NameError
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class DNA(Sequence):
    _type = 'DNA'
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'T', 'G', 'C' and their 
        corresponding amounts in sequence_attribute. 
        {'A': count_A, 'T': count_T, 'G': count_G, 'C': count_C}
        """
        #######################################################################
        # TODO:                                                               #
        # Counting 'A's, 'T's, 'G's, 'C's either by                           #
        # looping over sequence_attribute or using a standard string method.  #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        c_a = self.seq.count('A')
        c_t = self.seq.count('T')
        c_g = self.seq.count('G')
        c_c = self.seq.count('C')
        self.count_DNA = {'A': c_a, 'T': c_t, 'G': c_g, 'C': c_c}
        return self.count_DNA
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def complement_dna(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'A's were changed to 'T's
        and vice versa, all 'C's changed to 'G's and vice versa
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over sequence_attribute with        #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.seq_cm = self.seq
        self.seq_cm = self.seq_cm.replace('A', '1')
        self.seq_cm = self.seq_cm.replace('T', 'A')
        self.seq_cm = self.seq_cm.replace('1', 'T')
        self.seq_cm = self.seq_cm.replace('G', '2')
        self.seq_cm = self.seq_cm.replace('C', 'G')
        self.seq_cm = self.seq_cm.replace('2', 'C')
        return self.seq_cm
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'T's were changed to 'U's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over sequence_attribute with        #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.seq_tr = self.seq.replace('T', 'U')
        return self.seq_tr
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output: a NEW string, where all nucleotides are replaced with codons
        """
        #######################################################################
        # TODO:                                                               #
        # First transcribe DNA sequence to RNA using transcribe() method.     #
        # Second find 'AUG' - start codon. If it is found use json codon table#
        # to transcribe every 3 nucleotides of sequence_attribute to a codon, #
        # if a stop-codon is met then stop the transcription, else transcribe #
        # untill the end of the sequence.                                     #
        # If start codon was not found - raise Error                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.seq_tr = self.seq.replace('T', 'U')
        if 'AUG' not in self.seq_tr:
            raise ValueError('Start codon is not defind')
        codons = []
        k = self.seq_tr.index('AUG')
        for i in range(k+3, len(self.seq_tr), 3):
            codon = self.seq_tr[i:i+3]
            codons.append(r_c_t[codon])
            if codon in ['UAA', 'UAG', 'UGA']:
                break
        if 'Stop' in codons:
            codons.remove('Stop')
        self.codons = codons
        return self.codons
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def restriction_slices(self) -> int:
        """
        Input: None

        Output: number of slices by EcoRI restrictase
        """
        #######################################################################
        # TODO:                                                               #
        # EcoRI restrictase slices 'GAATTC'/'CTTAAG' sequences, return        #
        # resulting number of slices                                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        c = 0
        for i in range(0, (len(self.seq - 5))):
            if self.seq[i:i+6] == 'GAATTC' or self.seq[i:i+6] == 'CTTAAG':
                c += 1
        self.r_s = c
        return self.r_s
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class RNA(Sequence):
    _type = 'RNA'
    def count_nucleotides(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with keys 'A', 'U', 'G', 'C' and their 
        corresponding amounts in sequence_attribute. 
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C}
        """
        #######################################################################
        # TODO:                                                               #
        # Counting 'A's, 'U's, 'G's, 'C's either by                           #
        # looping over sequence_attribute or using a standard string method.  #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        c_a = self.seq.count('A')
        c_u = self.seq.count('U')
        c_g = self.seq.count('G')
        c_c = self.seq.count('C')
        self.count = {'A': c_a, 'U': c_u, 'G': c_g, 'C': c_c}
        return self.count
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def transcribe(self) -> str:
        """
        Input: None

        Output: a NEW string, where all 'U's were changed to 'T's
        """
        #######################################################################
        # TODO:                                                               #
        # Create a new empty string. Loop over sequence_attribute with        #
        # if-statements, while adding corresponding letters                   #
        # to the empty string.                                                #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        self.seq_tr = self.seq.replace('U', 'T')
        return self.seq_tr
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output: a NEW string, where all nucleotides are replaced with codons
        """
        #######################################################################
        # TODO:                                                               #
        # First find 'AUG' - start codon. If it is found use json codon table #
        # to transcribe every 3 nucleotides of sequence_attribute to a codon, #
        # if a stop-codon is met then stop the transcription, else transcribe #
        # untill the end of the sequence.                                     #
        # If start codon was not found - raise Error                          #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        if 'AUG' not in self.seq_tr:
            raise ValueError('Start codon is not defind')
        codons = []
        k = self.seq_tr.index('AUG')
        for i in range(k+3, len(self.seq_tr), 3):
            codon = self.seq_tr[i:i+3]
            codons.append(r_c_t[codon])
            if codon in ['UAA', 'UAG', 'UGA']:
                break
        if 'Stop' in codons:
            codons.remove('Stop')
        self.codons = codons
        return self.codons
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

class Protein(Sequence):
    _type = 'Protein'
    #######################################################################
    # TODO:                                                               #
    # Create two sets of positive charge amino acids and negative charge  #
    # amino acids: _pos_acids and _neg_acids                              #
    #######################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    _pos_acids = set(['K', 'R', 'H'])
    _neg_acids = set(['D', 'E'])
    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    def count_amino_acids(self) -> dict:
        """
        Input: None

        Output:
        - a dictionary with amino acids as keys and their corresponding
        amounts in sequence_attribute
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C ...}
        """
        #######################################################################
        # TODO:                                                               #
        # Using dictionary with codons as values, create a new dictionary     #
        # with amino acids and count them in sequence_attribute by            #
        # looping over sequenceattribute or using a standard string method.   #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        c_A=self.seq.count('A')
        c_R=self.seq.count('R')
        c_N=self.seq.count('N')
        c_D=self.seq.count('D')
        c_C=self.seq.count('C')
        c_Q=self.seq.count('Q')
        c_E=self.seq.count('E')
        c_G=self.seq.count('G')
        c_H=self.seq.count('H')
        c_I=self.seq.count('I')
        c_L=self.seq.count('L')
        c_K=self.seq.count('K')
        c_M=self.seq.count('M')
        c_F=self.seq.count('F')
        c_P=self.seq.count('P')
        c_S=self.seq.count('S')
        c_T=self.seq.count('T')
        c_W=self.seq.count('W')
        c_Y=self.seq.count('Y')
        c_V=self.seq.count('V')
        self.count = {'A': c_A, 'R': c_R, 'N': c_N, 'D': c_D, 'C': c_C, 'Q': c_Q, 'E': c_E, 'G': c_G, 'H': c_H, 'I': c_I,
                      'L': c_L, 'K': c_K, 'M': c_M, 'F': c_F, 'P': c_P, 'S': c_S, 'T': c_T, 'W': c_W, 'Y': c_Y, 'V': c_V}
        return self.count
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def to_protein(self) -> str:
        """
        Input: None

        Output:
        - sequence of amino acids
        {'A': count_A, 'U': count_U, 'G': count_G, 'C': count_C ...}
        """
        #######################################################################
        # TODO:                                                               #
        # Returning sequence_attribute is enough                              #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        return self.seq
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    
    def charge(self) -> int:
        """
        Input: None

        Output:
        - resulting charge of sequence
        """
        #######################################################################
        # TODO:                                                               #
        # Loop over the amino acids and check if they are in _pos_acids or    #
        # _neg_acids. If in _pos_acids then charge increases by 1, if in      #
        # _neg_acids decreases by 1, else does not changes                    #
        #######################################################################
        # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        crg = 0
        for i in self.seq:
            if i in self._pos_acids:
                crg += 1
            if i in self._neg_acids:
                crg+= 1
        self.chrg = crg
        return self.chrg
        # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
        # _neg_acids. If in _pos_acids then charge increases by 1, if in      #
print(f)