"""
Provides functions to perform frequency analysis on a given text

Can return the analysis programatically or in graphical charts

"""

import plotext as plt

def frequencyAnalysis(text, mode="c"):
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



frequencyAnalysis("jkwbefjwbefjwetrytuyiuoplkamhbgcfyxtuvwbkxuiywqtrcfhvjuy546756uyfvtyrew243546okulwef", "vsbcar")