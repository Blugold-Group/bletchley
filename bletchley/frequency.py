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
        #count
        return foundCharacters, counts
    elif mode=="p":
        #percentage
        textlength=len(text)
        length=len(counts)
        i=0

        while i<length:
            counts[i]=counts[i]/textlength
            i+=1
        
        return foundCharacters, counts
    
    elif mode=="vsbc":
        #verbose simple bar - cout
        plt.simple_bar(foundCharacters, counts)
        plt.title("Frequency Analysis")
        plt.ticks_color('red')
        plt.ticks_style('bold')

        return(plt.show())

    elif mode=="vbc":
        #verbose bar - cout
        plt.bar(foundCharacters, counts)
        plt.title("Frequency Analysis")
        plt.ticks_color('red')
        plt.ticks_style('bold')
        #plt.yticks(list(range(1,max(counts))))

        #plt.show()
        return(plt.show())
    
    raise ValueError("No recognized mode given")


        



