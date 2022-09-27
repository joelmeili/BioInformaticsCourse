def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text)):
        if text[i:i + len(pattern)] == pattern:
            count += 1

    return count