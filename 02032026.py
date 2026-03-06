# import matplotlib.pyplot as plt
# genes = ["GeneA", "GeneB", "GeneC"]
# control = [5, 3, 8]
# treatment = [7, 4, 9]

# fig, ax = plt.subplots(1, 2)

# ax[0].bar(genes, control)
# ax[0].set_title("Control")

# ax[1].bar(genes, treatment)
# ax[1].set_title("Treatment")

# plt.tight_layout()
# plt.show()

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(3, 2)
# ax[0,0].set_title("Plot 1")
# ax[0,1].set_title("Plot 2")
# ax[1,0].set_title("Plot 3")
# ax[1,1].set_title("Plot 4")
# ax[2,0].set_title("Plot 5")
# ax[2,1].set_title("Plot 6")
# plt.tight_layout()
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
genes = ["GeneA", "GeneB", "GeneC"]
control = [5, 3, 8]
treatment = [7, 4, 9]
x = np.arange(len(genes))
width = 0.35
fig, ax = plt.subplots(3, 2, figsize=(10, 12))
# -------- Row 1 --------
ax[0,0].bar(x - width/2, control, width, label="Control")
ax[0,0].bar(x + width/2, treatment, width, label="Treatment")
ax[0,0].set_xticks(x)
ax[0,0].set_xticklabels(genes)
ax[0,0].set_title("Plot 1")
ax[0,1].bar(x - width/2, control, width)
ax[0,1].bar(x + width/2, treatment, width)
ax[0,1].set_xticks(x)
ax[0,1].set_xticklabels(genes)
ax[0,1].set_title("Plot 2")
# -------- Row 2 --------
ax[1,0].bar(x - width/2, control, width)
ax[1,0].bar(x + width/2, treatment, width)
ax[1,0].set_xticks(x)
ax[1,0].set_xticklabels(genes)
ax[1,0].set_title("Plot 3")
ax[1,1].bar(x - width/2, control, width)
ax[1,1].bar(x + width/2, treatment, width)
ax[1,1].set_xticks(x)
ax[1,1].set_xticklabels(genes)
ax[1,1].set_title("Plot 4")

# -------- Row 3 --------
ax[2,0].bar(x - width/2, control, width)
ax[2,0].bar(x + width/2, treatment, width)
ax[2,0].set_xticks(x)
ax[2,0].set_xticklabels(genes)
ax[2,0].set_title("Plot 5")
ax[2,1].bar(x - width/2, control, width)
ax[2,1].bar(x + width/2, treatment, width)
ax[2,1].set_xticks(x)
ax[2,1].set_xticklabels(genes)
ax[2,1].set_title("Plot 6")
# Common legend
fig.legend(["Control", "Treatment"], loc="upper right")
plt.tight_layout()
plt.show()