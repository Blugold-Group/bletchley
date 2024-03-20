"""
Provides functions to perform frequency analysis on a given text

Can return the analysis programatically or in graphical charts

"""

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
        return foundCharacters, counts
    elif mode=="p":
        textlength=len(text)
        length=len(counts)
        i=0

        while i<length:
            counts[i]=counts[i]/textlength
            i+=1
        
        return foundCharacters, counts



