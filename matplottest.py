import numpy as np
import matplotlib.pyplot as plt
dna="ATCTGATATC"
dna_array=np.array(list(dna))
counts={"A":np.sum(dna_array=="A"),"T":np.sum(dna_array=="T"),"G":np.sum(dna_array=="G"),"C":np.sum(dna_array=="C")}
#plot results
plt.bar(counts.keys(),counts.values(),color=["red","blue","orange","black"])
plt.xlabel("Nucleotide")
plt.ylabel('Count')
plt.title("Nucleotide Composition in DNA sequence")
plt.show()
plt.savefig("dna_composition_plot.png", dpi=300)