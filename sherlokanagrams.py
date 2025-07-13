from collections import defaultdict

def sherlockAndAnagrams(s):
    """
    Find the number of unordered anagrammatic pairs of substrings.
    Two strings are anagrams if they contain the same characters with the same frequency.
    """
    def get_signature(substring):
        # Create a signature for the substring by sorting its characters
        return ''.join(sorted(substring))
    
    # Dictionary to store frequency of each signature
    signature_count = defaultdict(int)
    
    # Generate all possible substrings and their signatures
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            signature = get_signature(substring)
            signature_count[signature] += 1
    
    # Count anagrammatic pairs
    pairs = 0
    for count in signature_count.values():
        # For n substrings with same signature, number of pairs = n*(n-1)/2
        if count > 1:
            pairs += count * (count - 1) // 2
    
    return pairs

# Test the function
if __name__ == "__main__":
    # Test cases
    test_strings = ["abba", "abcd", "ifailuhkqq", "kkkk"]
    
    for test in test_strings:
        result = sherlockAndAnagrams(test)
        print(f"String: '{test}' -> Anagrammatic pairs: {result}")
    
    # Interactive test
    print("\nEnter a string to test:")
    user_input = input().strip()
    if user_input:
        result = sherlockAndAnagrams(user_input)
        print(f"Number of anagrammatic pairs: {result}")

# from primePy import primes
# n = int(input("Enter n: "))
# print(primes.upto(n))  # List of all primes up to n


