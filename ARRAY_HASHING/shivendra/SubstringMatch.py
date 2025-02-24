def find_needle(haystack, needle):
    # Edge case: if needle is longer than haystack, return -1
    if len(needle) > len(haystack):
        return -1

    # Loop through haystack to find needle
    for i in range(len(haystack) - len(needle) + 1):  # Ensure we don't go out of bounds
        if haystack[i:i+len(needle)] == needle:  # Check substring match
            return i  # Return the starting index of the first occurrence
    
    return -1  # If not found, return -1
