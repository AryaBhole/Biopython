# import pandas as pd
# data = {"Gene": ["BRCA1", "TP53", "EGFR"],
# "Expression": [12.5, 8.3, 15.2],
# "Activity": [23,34,56]}
# s=pd.Series(data)
# df=pd.DataFrame(data)
# print("\n\n")
# print(s)
# print("\n\n")
# print(df)


# import pandas as pd
# # Create gene expression dataset
# data = {
# "Gene": ["GeneA", "GeneB", "GeneC", "GeneD"],
# "Control": [5.2, 3.1, 7.8, 2.4],
# "Treatment1": [6.5, 4.0, 8.9, 3.2],
# "Treatment2": [7.1, 4.5, 9.3, 3.8]
# }
# df = pd.DataFrame(data)
# print(df)
# print(df.head()) # First 5 rows if more data is there
# print(df.tail()) # last 5 rows
# print(df.columns) # Column names
# print(df.shape) # Rows and columns
# print(df.describe()) # Statistical summary


# import pandas as pd
# data = {
# "Department": ["IT", "HR", "IT", "HR", "Sales"],
# "Salary": [50000, 40000, 60000, 45000, 70000]
# }
# df = pd.DataFrame(data)
# print(df)
# df.groupby("Department")["Salary"].mean()

import pandas as pd
import matplotlib.pyplot as plt
data = {
"Gene": ["BRCA1", "TP53", "EGFR", "MYC"],
"Control": [10.2, 8.5, 12.3, 7.8],
"Treatment": [15.4, 9.1, 18.2, 11.3]
}
df = pd.DataFrame(data)
print(df)
df.set_index("Gene")[["Control", "Treatment"]].plot(kind="bar")
plt.title("Gene Expression Comparison")
plt.ylabel("Expression Level")
plt.xlabel("Genes")
plt.show()