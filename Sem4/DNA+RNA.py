class DNA(object):
    def __init__(self, string: str) -> None:
        self.string = string

    def count_nucleotides(self) -> dict:
        c_a = self.string.count('A')
        c_t = self.string.count('T')
        c_g = self.string.count('G')
        c_c = self.string.count('C')
        self.count = {'A': c_a, 'T': c_t, 'G': c_g, 'C': c_c}
        return self.count
    
    def transcribe(self) -> str:
        self.string_tr = self.string.replace('T', 'U')
        return self.string_tr
    
    def complement_dna(self) -> str:
        self.string_cm = self.string
        self.string_cm = self.string_cm.replace('A', '1')
        self.string_cm = self.string_cm.replace('T', 'A')
        self.string_cm = self.string_cm.replace('1', 'T')
        self.string_cm = self.string_cm.replace('G', '2')
        self.string_cm = self.string_cm.replace('C', 'G')
        self.string_cm = self.string_cm.replace('2', 'C')
        return self.string_cm

    def hamming_distance(self, string2 : str) -> int:
        if len(self.string) != len(string2):
            self.h_d = 'Error'
        else:
            c = 0
            for i in range(0, len(self.string)):
                if self.string[i] != string2[i]:
                    c += 1
            self.h_d = c
        return self.h_d


class RNA(object):
    def __init__(self, string : str) -> None:
        self.string = string
    
    def transcribe(self) -> str:
        self.string_tr = self.string.replace('U', 'T')
        return self.string_tr
    
s = DNA('ATGCATGCATGC')
s.count_nucleotides()
s.transcribe()
s.complement_dna()
s.hamming_distance('AGGTGTCCTCAC')
print(s.count, s.string_tr, s.string_cm, s.h_d)

r = RNA('AUGCAUGCAUGC')
r.transcribe()
print(r.string_tr)