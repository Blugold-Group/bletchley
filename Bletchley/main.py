# The interface for using the methods in this directory

import ciphers
import plotext as plt
import bruteforce

text="nifon aicum niswt luvet vxshk nissx wsstb husle chsnv ytsro cdsoy nisgx lnona chvch gnonw yndlh sfrnh npblr yowgf unoca cossu ouoll iuvef issoe xgosa cpbew uormh lftaf cmwak bbbdv cqvek muvil qbgnh ntiri ljgig atwnv yuvev iorim cpbsb hxviv buvet vxshk uorim mjbdb pjrut fbueg ntgof yuwmx miodm ipdek uuswx lfjek sewfy yssnm zscmm bpgeb huvez ysaag usaew mffvb wfgim qpilw bbjeu yfbef vbfrt mtwnz uorig wpbvx hjsnm zpfag uhsnm npglb jbqrh mttrh huwek mpfak ljjen hbbnh ooqew vzdak udvum yucbx yoquf vffew vzonx hjumt lfgef vmwnz uxsiz bumag xbbtb kvotx xumpx qswtx l"

#plt.bar(ciphers.frequencyAnalysis(text))
#plt.title("Frequency Analysis")
#plt.show()

print(ciphers.frequencyAnalysis(text))

#for i in range(15):


testlist=list(text[::6])
print(testlist)
print(ciphers.frequencyAnalysis(testlist))

