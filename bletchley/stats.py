"""
Provides statistical analysis functions for text.

This module includes various statistical metrics that can be used for:
    - Cryptanalysis (e.g. ciphertext pattern analysis)
    - Text characterization (entropy, index of coincidence)
    - Detecting structural patterns in text

Many of these measures help identify cryptographic properties,
such as whether a text follows a specific frequency distribution
or contains structured repetitions.

A lot of ideas are outlined in the readme for lightbulb
"""

import math
from collections import Counter
from itertools import islice

# Helper functions
def frequency_analysis(text):
    """
    Computes the frequency of each character in the given text.

    Args:
        text (str): The input text.

    Returns:
        Counter: A dictionary-like object mapping characters to their frequency count.
    """
    return Counter(text)

def ngrams(text, n):
    """
    Generates n-grams from the given text.

    Args:
        text (str): The input text.
        n (int): The length of each n-gram.

    Returns:
        list: A list of n-grams (substrings of length n).
    """
    return [text[i:i + n] for i in range(len(text) - n + 1)]

def normalize_frequencies(freqs, length):
    """
    Normalizes charcter frequencies to proportions.

    Args:
        freqs (dict): Dictionary of character frequencies.
        length (int): Total length of the text.

    Returns:
        dict: A dictionary mapping chracters to their frequency as a proportion of total length.
    """
    return {char: count / length for char, count in freqs.items()}

# 1. Average Single Letter - Digraph Discrepancy Score (SDD)
def average_sdd(text):
    """
    Computes the average single-letter to digraph discrepancy score (SDD).

    This metric measures the difference between single-character and bigram frequencies.

    Args:
        text (str): The input text.

    Returns:
        float: The computed SDD score.
    """
    freqs = normalize_frequencies(frequency_analysis(text), len(text))
    digraphs = normalize_frequencies(Counter(ngrams(text, 2)), len(text) - 1)
    avg_freq = sum(freqs.values()) / len(freqs)
    avg_digraph = sum(digraphs.values()) / len(digraphs)
    return abs(avg_freq - avg_digraph)

# 2. Chi-Square (CHI2)
def chi_square(text):
    """\
    Computes the chi-square statistic for letter frequency distribution.

    Args:
        text (str): The input text.

    Returns:
        float; The computed chi-square statistic.
    """
    freqs = frequency_analysis(text)
    expected = len(text) / len(freqs)
    return sum(((count - expected) ** 2) / expected for count in freqs.values())

# 3. Digraphic Index of Coincidence (DIC)
def digraphic_ic(text):
    """
    Computes the digraphic index of coincidence (DIC).

    Args:
        text (str): The input text.

    Returns:
        float: The computed digraphic IC.
    """
    bigrams = ngrams(text, 2)
    freqs = frequency_analysis(bigrams)
    total = sum(freqs.values())
    return sum(count * (count - 1) for count in freqs.values()) / (total * (total - 1))

# 4. Double Letter (DBL)
def double_letter(text):
    """
    Computes the ratio of consecutive identical letters in the text.

    Args:
        text (str): The input text.

    Returns:
        float: The proportion of double letters in the text.
    """
    doubles = [text[i] for i in range(len(text) - 1) if text[i] == text[i + 1]]
    return len(doubles) / len(text)

# 5. Estimated Auto Correlation (AUTO)
def auto_correlation(text, shift=1):
    """
    Computes the auto-correlation of the text.

    Args:
        text (str): The input text.
        shift (int): The shift distance.

    Returns:
        float: The auto-correlation ratio.
    """
    return sum(1 for i in range(len(text) - shift) if text[i] == text[i + shift]) / len(text)

# 6. Frequencies (FRQ)
def frequencies(text):
    """
    Computes the normalized frequency of each character in the text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary of character frequencies.
    """
    return normalize_frequencies(frequency_analysis(text), len(text))

# 7. Has Space (HAS_SP)
def has_space(text):
    """
    Checks if the given text contains spaces.

    Args:
        text (str): The input text.

    Returns:
        bool: True if the text contains spaces, False otherwise.
    """
    return ' ' in text

# 8. Index of Coincidence (IoC)
def index_of_coincidence(text):
    """
    Computes the index of coincidence (IoC).

    Args:
        text (str): The input text.

    Returns:
        float: The computed IoC.
    """
    freqs = frequency_analysis(text)
    total = sum(freqs.values())
    return sum(count * (count - 1) for count in freqs.values()) / (total * (total - 1))

# 9. Log Digraph Score (LDI)
def log_digraph_score(text):
    """
    Computes the log digraph score.

    Args:
        text (str): The input text.

    Returns:
        float: The computed log digraph score.
    """
    bigrams = ngrams(text, 2)
    freqs = frequency_analysis(bigrams)
    total = sum(freqs.values())
    return sum(math.log2(count / total) for count in freqs.values() if count > 0)

# 10. Log Digraph Score Variants (A_LDI, B_LDI, etc.)
def log_digraph_score_variant(text, key_variant):
    """
    Computes the log digraph score.

    Args:
        text (str): The input text.
        key_variant (str): The variant of log digraph score something something
        probably something else here
    
    Returns:
        probalby reutnrs something interesting
    """
    # Adjust scoring based on specific cipher variants
    return log_digraph_score(text)  # Placeholder

# 11. Long Repeat (LR)
def long_repeat(text):
    """
    Finds the longest repeated substring in the text.

    Args:
        text (str): The input text.

    Returns:
        int: The length of the longest repeated substring.
    """
    max_len = 0
    for length in range(1, len(text) // 2):
        repeats = set(ngrams(text, length))
        max_len = max(max_len, max((len(rep) for rep in repeats if text.count(rep) > 1), default=0))
    return max_len

# 12. Max Bifid DIC (BDI)
def max_bifid_dic(text):
    """
    Computes the maximum bifid digraphic index of coincidence (BDI).

    This function calculates the BDI over different periods and returns the highest value.

    Args:
        text (str): The input text.

    Returns:
        float: The maximum bifid DIC score.
    """
    return max(digraphic_ic(text[i::period]) for period in range(3, 16))

# 13. Max Columnar SDD Score (CDD)
def max_columnar_sdd(text):
    """
    Computes the maximum columnar single-letter to digraph discrepancy score (CDD).

    This function calculates the average SDD score over different periods
    and returns the highest value.

    Args:
        text (str): The input text.

    Returns:
        float: THe maximum columnar SDD score.
    """
    return max(average_sdd(text[i::period]) for period in range(4, 16))

# 14. Max Kappa (MKA)
def max_kappa(text):
    """
    Computes the maxiumum kappa test score.

    This function calculates auto-correlation at different shift values
    and returns the maximum result.

    Args:
        text (str): The input text.j

    Returns:
        float: The highest kappa test score.
    """
    return max(auto_correlation(text, shift) for shift in range(1, len(text) // 2))

# 15. Max Nicodemus IC (NIC)
def max_nicodemus_ic(text):
    """
    Computes the maximum Nicodemus index of coincidence (NIC).

    This function calculates the index of coincidence over different periods
    and returns the highest value.

    Args:
        text (str): The input text.

    Returns:
        float: The highest Nicodemus IC score.
    """
    return max(index_of_coincidence(text[i::period]) for period in range(1, len(text) // 2))

# 16. Max STD Score (SSTD)
def max_std_score(text):
    """
    Computes the maximum standard deviation score (SSTD).

    This function calculates auto-correlation at specific shift values
    and returns the highest value.

    Args:
        text (str): The input text.

    Returns:
        float: The highest standard deviation score.
    """
    return max(auto_correlation(text, shift) for shift in range(4, 9))

# 17. Maximum Index of Coincidence (MIC)
def max_ic(text):
    """
    Computes the maximum index of coincidence (MIC).

    This function calculates the index of coincidence over different periods
    and returns the highest value.

    Args:
        text (str): The input text.

    Returns:
        float: The highest index of coincidence score.
    """
    return max(index_of_coincidence(text[i::period]) for period in range(1, len(text) // 2))

# 18. Normal Order (NOMOR)
def normal_order(text):
    """
    Returns the characters of the text sorted in normal order.

    Args:
        text (str): The input text.

    Returns:
        str: The sorted version of the input text.
    """
    return ''.join(sorted(text))

# 19. Phillips IC (PHIC)
def phillips_ic(text):
    """
    Computes the Phillips index of coincidence (PHIC).

    This function multiplies the standard index of coincidence by the text length.

    Args:
        text (str): The input text.

    Returns:
        float: The computed Phillips IC score.
    """
    return index_of_coincidence(text) * len(text)

# 20. Repetition Feature (REP)
def repetition_feature(text):
    """
    Measures how often characters are repeated in the text.

    Args:
        text (str): The input text.

    Returns:
        float: The repetition ratio.
    """
    return sum(1 for i in range(len(text) - 1) if text[i] == text[i + 1]) / len(text)

# 21. Repetition Odd (ROD)
def repetition_odd(text):
    """
    Measures how often characters repeat with a one-character gap.

    Args:
        text (str): The input text.

    Returns:
        float: The ratio of odd-positioned repeated characters.
    """
    return sum(1 for i in range(len(text) - 2) if text[i] == text[i + 2]) / len(text)

# 22. Reverse Log Digraph (RDI)
def reverse_log_digraph(text):
    """
    Computes the log digraph score for the reversed text.

    Args:
        text (str): The input text.

    Returns:
        float: The log digraph score for the reversed text.
    """
    reversed_text = text[::-1]
    return log_digraph_score(reversed_text)

# 23. Shannon’s Entropy Equation (SHAN)
def shannon_entropy(text):
    """
    Computes entropy, a measure of randomness, using Shannon's Entropy Equation.

    Args:
        text (str): The input text.

    Returns:
        float: The Shannon entropy of the text.
    """
    freqs = normalize_frequencies(frequency_analysis(text), len(text))
    return -sum(p * math.log2(p) for p in freqs.values() if p > 0)
