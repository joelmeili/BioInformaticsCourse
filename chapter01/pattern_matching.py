pattern = "CTTGATCAT"
with open("Vibrio_cholerae.txt", "r") as file:
    genome = file.read()

def match_pattern(pattern, genome):
    found_indices = []
    for i in range(len(genome) - len(pattern)):
        if pattern == genome[i:i + len(pattern)]:
            found_indices.append(i)

    found_indices = [str(value) for value in found_indices]

    return " ".join(found_indices)

print(match_pattern(pattern, genome))