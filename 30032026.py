from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
print(my_seq)

complement = my_seq.complement()
print(complement)

reverse_complement = my_seq.reverse_complement()
print(reverse_complement)