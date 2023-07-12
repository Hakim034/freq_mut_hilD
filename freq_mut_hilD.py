from collections import defaultdict

file_path = "C:/Users/Hakim/Downloads/seqdump(1).txt"

# read seq from file
with open(file_path, "r") as file:
    lines = file.readlines()

alignment = []
sequence = ""
for line in lines:
    if line.startswith(">"):
        if sequence:
            alignment.append(sequence)
            sequence = ""
    else:
        sequence += line.strip()

if sequence:
    alignment.append(sequence)
    
# Dictionary to store mut frequencies
mutation_counts = defaultdict(int)  

# Iterate
for i in range(len(alignment[0])):
    reference_aa = alignment[0][i]  

    # Iterate through each seq and compare nucleotides
    for sequence in alignment[1:]:
        # Check if the seq is long enough
        if i < len(sequence) and sequence[i] != reference_aa:
            mutation = f"{reference_aa}{i+1}{sequence[i]}"  
            mutation_counts[mutation] += 1  

# sort the mut frequencies
sorted_mutations = sorted(mutation_counts.items(), key=lambda x: x[1], reverse=True)

output_file_path = "C:/Users/Hakim/Downloads/output_frequency_11.csv"

# output file format
with open(output_file_path, "w") as output_file:
    for mutation, count in sorted_mutations:
        output_file.write(f"{mutation}: {count}\n")

print("exported")