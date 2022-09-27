from frequent_words_problem import frequency_table

def find_clumps(text, k, L, t):
    patterns = []
    n = len(text)

    for i in range(n - L):
        window = text[i:i + L]
        freq_map = frequency_table(window, k)

        for key in freq_map.keys():
            if freq_map[key] >= t:
                patterns.append(key)

    patterns = list(set(patterns))
    patterns.sort()
    
    return patterns