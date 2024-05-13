import matplotlib.pyplot as plt
import pandas as pd

data = dict()
fasta_file = "NC_045512.fasta"
with open(fasta_file) as handle:
    for line in handle:
        if line.startswith(">"):
            continue

        for base in line.strip():
            if base not in data:
                data[base] = 0

            data[base] += 1

df_data = {"base": data.keys(), "base_count": data.values()}
print(df_data)

df = pd.DataFrame(df_data)
df.plot(
    kind="bar",
    x="base",
    y="base_count",
    title="Base count",
    xlabel="Base",
    ylabel="Count",
)

plt.savefig("NC_045512.png")
