def reverse_complement(input):
    output = [0] * len(input)
    
    for i in range(len(input)):
        if input[i] == "A":
            output[i] = "T"
        elif input[i] == "T":
            output[i] = "A"
        elif input[i] == "G":
            output[i] = "C"
        elif input[i] == "C":
            output[i] = "G"

    output = output[::-1]
    return "".join(output)