class Sequence(object):
    def __init__(self, string: str):
        self.string = string

    def transcribe(self) -> None:
        raise NameError
    
    def hamming_distance(self, string2: str) -> int:
        if len(self.string) != len(string2):
            raise ValueError('line lengths are different')
        else:
            c = 0
            for i in range(0, len(self.string)):
                if self.string[i] != string2[i]:
                    c += 1
            self.h_d = c
        return self.h_d

class DNA(Sequence):
    def count_nucleotides_DNA(self) -> dict:
        c_a = self.string.count('A')
        c_t = self.string.count('T')
        c_g = self.string.count('G')
        c_c = self.string.count('C')
        self.count_DNA = {'A': c_a, 'T': c_t, 'G': c_g, 'C': c_c}
        return self.count_DNA
    
    def transcribe(self) -> str:
        self.string_tr_DNA = self.string.replace('T', 'U')
        return self.string_tr_DNA
    
    def complement_dna(self) -> str:
        self.string_cm = self.string
        self.string_cm = self.string_cm.replace('A', '1')
        self.string_cm = self.string_cm.replace('T', 'A')
        self.string_cm = self.string_cm.replace('1', 'T')
        self.string_cm = self.string_cm.replace('G', '2')
        self.string_cm = self.string_cm.replace('C', 'G')
        self.string_cm = self.string_cm.replace('2', 'C')
        return self.string_cm

class RNA(Sequence):
    def transcribe(self) -> str:
        self.string_tr_RNA = self.string.replace('U', 'T')
        return self.string_tr_RNA
    
    def count_nucleotides_RNA(self) -> dict:
        c_a = self.string.count('A')
        c_u = self.string.count('U')
        c_g = self.string.count('G')
        c_c = self.string.count('C')
        self.count_RNA = {'A': c_a, 'U': c_u, 'G': c_g, 'C': c_c}
        return self.count_RNA

