def frequency_table(text, k):
    freq_map = {}
    n = len(text)

    for i in range(n - k):
        pattern = text[i:i + k]
        if not pattern in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] = freq_map[pattern] + 1

    return freq_map

def max_map(freq_map):
    values = freq_map.values()
    return max(values)

def better_frequent_words(text, k):
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    max = max_map(freq_map)
    for pattern in freq_map.keys():
        if freq_map[pattern] == max:
            frequent_patterns.append(pattern)
    
    return frequent_patterns