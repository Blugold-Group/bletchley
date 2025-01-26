"""
Functions to measure statistics on a text

A lot of ideas are outlined in the readme for lightbulb
"""

import math
from collections import Counter
from itertools import islice

# Helper functions
def frequency_analysis(text):
    """Compute the frequency of each character in the text."""
    return Counter(text)

def ngrams(text, n):
    """Generate n-grams from the text."""
    return [text[i:i + n] for i in range(len(text) - n + 1)]

def normalize_frequencies(freqs, length):
    """Normalize frequencies to proportions."""
    return {char: count / length for char, count in freqs.items()}

# 1. Average Single Letter - Digraph Discrepancy Score (SDD)
def average_sdd(text):
    freqs = normalize_frequencies(frequency_analysis(text), len(text))
    digraphs = normalize_frequencies(Counter(ngrams(text, 2)), len(text) - 1)
    avg_freq = sum(freqs.values()) / len(freqs)
    avg_digraph = sum(digraphs.values()) / len(digraphs)
    return abs(avg_freq - avg_digraph)

# 2. Chi-Square (CHI2)
def chi_square(text):
    freqs = frequency_analysis(text)
    expected = len(text) / len(freqs)
    return sum(((count - expected) ** 2) / expected for count in freqs.values())

# 3. Digraphic Index of Coincidence (DIC)
def digraphic_ic(text):
    bigrams = ngrams(text, 2)
    freqs = frequency_analysis(bigrams)
    total = sum(freqs.values())
    return sum(count * (count - 1) for count in freqs.values()) / (total * (total - 1))

# 4. Double Letter (DBL)
def double_letter(text):
    doubles = [text[i] for i in range(len(text) - 1) if text[i] == text[i + 1]]
    return len(doubles) / len(text)

# 5. Estimated Auto Correlation (AUTO)
def auto_correlation(text, shift=1):
    return sum(1 for i in range(len(text) - shift) if text[i] == text[i + shift]) / len(text)

# 6. Frequencies (FRQ)
def frequencies(text):
    return normalize_frequencies(frequency_analysis(text), len(text))

# 7. Has Space (HAS_SP)
def has_space(text):
    return ' ' in text

# 8. Index of Coincidence (IoC)
def index_of_coincidence(text):
    freqs = frequency_analysis(text)
    total = sum(freqs.values())
    return sum(count * (count - 1) for count in freqs.values()) / (total * (total - 1))

# 9. Log Digraph Score (LDI)
def log_digraph_score(text):
    bigrams = ngrams(text, 2)
    freqs = frequency_analysis(bigrams)
    total = sum(freqs.values())
    return sum(math.log2(count / total) for count in freqs.values() if count > 0)

# 10. Log Digraph Score Variants (A_LDI, B_LDI, etc.)
def log_digraph_score_variant(text, key_variant):
    # Adjust scoring based on specific cipher variants
    return log_digraph_score(text)  # Placeholder

# 11. Long Repeat (LR)
def long_repeat(text):
    max_len = 0
    for length in range(1, len(text) // 2):
        repeats = set(ngrams(text, length))
        max_len = max(max_len, max((len(rep) for rep in repeats if text.count(rep) > 1), default=0))
    return max_len

# 12. Max Bifid DIC (BDI)
def max_bifid_dic(text):
    return max(digraphic_ic(text[i::period]) for period in range(3, 16))

# 13. Max Columnar SDD Score (CDD)
def max_columnar_sdd(text):
    return max(average_sdd(text[i::period]) for period in range(4, 16))

# 14. Max Kappa (MKA)
def max_kappa(text):
    return max(auto_correlation(text, shift) for shift in range(1, len(text) // 2))

# 15. Max Nicodemus IC (NIC)
def max_nicodemus_ic(text):
    return max(index_of_coincidence(text[i::period]) for period in range(1, len(text) // 2))

# 16. Max STD Score (SSTD)
def max_std_score(text):
    return max(auto_correlation(text, shift) for shift in range(4, 9))

# 17. Maximum Index of Coincidence (MIC)
def max_ic(text):
    return max(index_of_coincidence(text[i::period]) for period in range(1, len(text) // 2))

# 18. Normal Order (NOMOR)
def normal_order(text):
    return ''.join(sorted(text))

# 19. Phillips IC (PHIC)
def phillips_ic(text):
    return index_of_coincidence(text) * len(text)

# 20. Repetition Feature (REP)
def repetition_feature(text):
    return sum(1 for i in range(len(text) - 1) if text[i] == text[i + 1]) / len(text)

# 21. Repetition Odd (ROD)
def repetition_odd(text):
    return sum(1 for i in range(len(text) - 2) if text[i] == text[i + 2]) / len(text)

# 22. Reverse Log Digraph (RDI)
def reverse_log_digraph(text):
    reversed_text = text[::-1]
    return log_digraph_score(reversed_text)

# 23. Shannon’s Entropy Equation (SHAN)
def shannon_entropy(text):
    freqs = normalize_frequencies(frequency_analysis(text), len(text))
    return -sum(p * math.log2(p) for p in freqs.values() if p > 0)
