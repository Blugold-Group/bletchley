"""
Provides functions to perform frequency analysis on a given text

This module can return frequency analysis results programmatically or display them as charts.

Modes:
    - "c" (counts): Returns a list of unique characters and their respective counts.
    - "p" (percentages): Returns a list of unique characters and their relative frequency (percentage).
    - "vsbc" (verbose simple bar - count): Displays a simple bar chart of character counts.
    - "vbc" (verbose bar - count): Displays a detailed bar chart of character counts.
    - "vsbca" (verbose simple bar - count, alphabetized): Displays a simple bar chart with characters sorted alphabetically.
    - "vbca" (verbose bar - count, alphabetized): Displays a detailed bar chart with characters sorted alphabetically.
    - "vsbcar" (verbose simple bar - count, alphabetized reverse): Displays a simple bar chart with characters sorted in reverse alphabetical order.
    - "vbcar" (verbose bar - count, alphabetized reverse): Displays a detailed bar chart with characters sorted in reverse alphabetical order.
    - "vsbcos" (verbose simple bar - count ordered smallest to largest): Displays a simple bar chart with counts sorted from smallest to largest.
    - "vbcos" (verbose bar - count ordered smallest to largest): Displays a detailed bar chart with counts sorted from smallest to largest.
    - "vsbcol" (verbose simple bar - count ordered largest to smallest): Displays a simple bar chart with counts sorted from largest to smallest.
    - "vbcol" (verbose bar - count 

TODO:
    - Add an option to ignore special characters (specifically spaces)
    - Add an option to ignore capitalization
    - Add options to get bar charts of percentages

"""

import plotext as plt

def frequencyAnalysis(text, mode="c"):
    """
    Performs frequency analysis on the given text.

    Args:
        text (str): The input text to analyze.
        mode (str, optional): The mode specifying the output format. Defaults to "c".
        
            - "c": Returns a list of unique characters and their counts.
            - "p": Returns a list of unique characters and their relative frequencies (percentages).
            - "vsbc": Displays a simple bar chart of character counts.
            - "vbc": Displays a detailed bar chart of character counts.
            - "vsbca": Displays a simple bar chart with characters sorted alphabetically.
            - "vbca": Displays a detailed bar chart with characters sorted alphabetically.
            - "vsbcar": Displays a simple bar chart with characters sorted in reverse alphabetical order.
            - "vbcar": Displays a detailed bar chart with characters sorted in reverse alphabetical order.
            - "vsbcos": Displays a simple bar chart with counts sorted from smallest to largest.
            - "vbcos": Displays a detailed bar chart with counts sorted from smallest to largest.
            - "vsbcol": Displays a simple bar chart with counts sorted from largest to smallest.
            - "vbcol": Displays a detailed bar chart with counts sorted from largest to smallest.

    Returns:
        tuple: A tuple containing:
            - List of unique characters in the text.
            - List of corresponding counts or percentages, depending on mode.
        
        OR:
        Displays a graphical representation if a verbose mode is selected.

    Raises:
        ValueError: If an unrecognized mode is provided.
    """
    # Performs frequency analysis on a text and displays it in graphs

    foundCharacters=[]
    counts=[]

    for i in text:
        if i not in foundCharacters:
            foundCharacters.append(i)
            counts.append(1)
        else:
            counts[foundCharacters.index(i)]+=1

    if mode=="c":
        # List of counts
        return foundCharacters, counts
    elif mode=="p":
        # List of percentages
        textlength=len(text)
        length=len(counts)
        i=0

        while i<length:
            counts[i]=counts[i]/textlength
            i+=1
        
        return foundCharacters, counts
    
    elif mode=="vsbc":
        # Verbose simple bar - count
        plt.simple_bar(foundCharacters, counts)
        plt.title("Frequency Analysis")
        plt.ticks_color('red')
        plt.ticks_style('bold')

        plt.show()
        return

    elif mode=="vbc":
        # Verbose bar - count
        plt.bar(foundCharacters, counts, marker="fhd")

        plt.yticks(range(min(counts), max(counts) + 1, 1))  # Make Y axis increment by 1
        plt.title("Frequency Analysis")
        plt.theme("pro")

        plt.show()
        return

    elif mode=="vsbca":
        # Verbose simple bar - count, alphabetized

        # Alphabetize the lists
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[0])
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)

        plt.simple_bar(foundCharacters, counts)
        plt.title("Frequency Analysis")
        plt.ticks_color('red')
        plt.ticks_style('bold')

        plt.show()
        return

    elif mode=="vbca":
        # Verbose bar - count, alphabetized

        # Alphabetize the lists
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[0])
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)

        plt.bar(foundCharacters, counts, marker="fhd")

        plt.yticks(range(min(counts), max(counts) + 1, 1))  # Make Y axis increment by 1
        plt.title("Frequency Analysis")
        plt.theme("pro")

        plt.show()
        return

    elif mode=="vsbcar":
        # Verbose simple bar - count, alphabetized reverse

        # Alphabetize the lists
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)

        plt.simple_bar(foundCharacters, counts)
        plt.title("Frequency Analysis")
        plt.ticks_color('red')
        plt.ticks_style('bold')

        plt.show()
        return

    elif mode=="vbcar":
        # Verbose bar - count, alphabetized reverse

        # Alphabetize the lists
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)

        plt.bar(foundCharacters, counts, marker="fhd")

        plt.yticks(range(min(counts), max(counts) + 1, 1))  # Make Y axis increment by 1
        plt.title("Frequency Analysis")
        plt.theme("pro")

        plt.show()
        return


    elif mode=="vsbcos":
        # Verbose simple bar - count ordered smallest (to largest)

        # Order the lists largest to smallest
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[1])
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)


        plt.simple_bar(foundCharacters, counts)
        plt.title("Frequency Analysis")
        plt.ticks_color('red')
        plt.ticks_style('bold')

        plt.show()
        return

    elif mode=="vbcos":
        # Verbose bar - count ordered smallest (to largest)

        # Order the lists largest to smallest
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[1])
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)

        plt.bar(foundCharacters, counts, marker="fhd")

        plt.yticks(range(min(counts), max(counts) + 1, 1))  # Make Y axis increment by 1
        plt.title("Frequency Analysis")
        plt.theme("pro")

        plt.show()
        return
    
    elif mode=="vsbcol":
        # Verbose simple bar - count ordered largest (to smallest)

        # Order the lists largest to smallest
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)

        plt.simple_bar(foundCharacters, counts)
        plt.title("Frequency Analysis")
        plt.ticks_color('red')
        plt.ticks_style('bold')

        plt.show()
        return

    elif mode=="vbcol":
        # Verbose bar - count ordered largest (to smallest)

        # Order the lists largest to smallest
        combined = list(zip(foundCharacters, counts))
        sorted_combined = sorted(combined, key=lambda x: x[1], reverse=True)
        sorted_foundCharacters, sorted_counts = zip(*sorted_combined)
        foundCharacters = list(sorted_foundCharacters)
        counts = list(sorted_counts)

        plt.bar(foundCharacters, counts, marker="fhd")

        plt.yticks(range(min(counts), max(counts) + 1, 1))  # Make Y axis increment by 1
        plt.title("Frequency Analysis")
        plt.theme("pro")

        plt.show()
        return
    raise ValueError("No recognized mode given")
