from local_align import localAlign as LA

""" 
Test File for local_align.py
""" 


""" 
TEST 1
Perfect matches
"""
# seq1 = "AAAARRRRNNNNNDDDDDD"
# seq2 = "AAAARRRRNNNNNDDDDDD"

# align = LA(seq1, seq2)
# align.kOptimalAlignments(1)
# align.printAlignment()


""" 
Test
"""

seq1 = "AAAA"
seq2 = "AAAAA"
align = LA(seq1, seq2)
align.kOptimalAlignments(2)
align.printAlignment()


"""
TEST 2
Matches with gaps
"""
seq1 = "AAAADDDDDDRRRRDDDDDNNNNNFFFFFFDDDDDD"
seq2 = "AAAAFFFFFFRRRRFFFFFNNNNNDDDDDDDDDDDD"
align = LA(seq1, seq2)
align.kOptimalAlignments(4)
align.printAlignment()



"""
TEST 3
Tests provided with assignment 2 
(Uses Protein sequences)
"""

# # OSXR1_HUMAN in uniprot data
seq1 = ("MSEDSSALPWSINRDDYELQEVIGSGATAVVQAAYCAPKKEKVAIKRINLEKCQTSMDEL"
	"LKEIQAMSQCHHPNIVSYYTSFVVKDELWLVMKLLSGGSVLDIIKHIVAKGEHKSGVLDE"
	"STIATILREVLEGLEYLHKNGQIHRDVKAGNILLGEDGSVQIADFGVSAFLATGGDITRN"
	"KVRKTFVGTPCWMAPEVMEQVRGYDFKADIWSFGITAIELATGAAPYHKYPPMKVLMLTL"
	"QNDPPSLETGVQDKEMLKKYGKSFRKMISLCLQKDPEKRPTAAELLRHKFFQKAKNKEFL"
	"QEKTLQRAPTISERAKKVRRVPGSSGRLHKTEDGGWEWSDDEFDEESEEGKAAISQLRSP"
	"RVKESISNSELFPTTDPVGTLLQVPEQISAHLPQPAGQIATQPTQVSLPPTAEPAKTAQA"
	"LSSGSGSQETKIPISLVLRLRNSKKELNDIRFEFTPGRDTAEGVSQELISAGLVDGRDLV"
	"IVAANLQKIVEEPQSNRSVTFKLASGVEGSDIPDDGKLIGFAQLSIS")

# NEK3_HUMAN
seq2 = ("MDDYMVLRMIGEGSFGRALLVQHESSNQMFAMKEIRLPKSFSNTQNSRKEAVLLAKMKHP"
	"NIVAFKESFEAEGHLYIVMEYCDGGDLMQKIKQQKGKLFPEDMILNWFTQMCLGVNHIHK"
	"KRVLHRDIKSKNIFLTQNGKVKLGDFGSARLLSNPMAFACTYVGTPYYVPPEIWENLPYN"
	"NKSDIWSLGCILYELCTLKHPFQANSWKNLILKVCQGCISPLPSHYSYELQFLVKQMFKR"
	"NPSHRPSATTLLSRGIVARLVQKCLPPEIIMEYGEEVLEEIKNSKHNTPRKKTNPSRIRI"
	"ALGNEASTVQEEEQDRKGSHTDLESINENLVESALRRVNREEKGNKSVHLRKASSPNLHR"
	"RQWEKNVPNTALTALENASILTSSLTAEDDRGGSVIKYSKNTTRKQWLKETPDTLLNILK"
	"NADLSLAFQTYTIYRPGSEGFLKGPLSEETEASDSVDGGHDSVILDPERLEPGLDEEDTD"
	"FEEEDDNPDWVSELKKRAGWQGLCDR")

align = LA(seq1, seq2)
align.kOptimalAlignments(1)
align.printAlignment()

seq2 = ("MSLCGARANAKMMAAYNGGTSAAAAGHHHHHHHHLPHLPPPHLHHHHHPQHHLHPGSAAA"
	"VHPVQQHTSSAAAAAAAAAAAAAMLNPGQQQPYFPSPAPGQAPGPAAAAPAQVQAAAAAT"
	"VKAHHHQHSHHPQQQLDIEPDRPIGYGAFGVVWSVTDPRDGKRVALKKMPNVFQNLVSCK"
	"RVFRELKMLCFFKHDNVLSALDILQPPHIDYFEEIYVVTELMQSDLHKIIVSPQPLSSDH"
	"VKVFLYQILRGLKYLHSAGILHRDIKPGNLLVNSNCVLKICDFGLARVEELDESRHMTQE"
	"VVTQYYRAPEILMGSRHYSNAIDIWSVGCIFAELLGRRILFQAQSPIQQLDLITDLLGTP"
	"SLEAMRTACEGAKAHILRGPHKQPSLPVLYTLSSQATHEAVHLLCRMLVFDPSKRISAKD"
	"ALAHPYLDEGRLRYHTCMCKCCFSTSTGRVYTSDFEPVTNPKFDDTFEKNLSSVRQVKEI"
	"IHQFILEQQKGNRVPLCINPQSAAFKSFISSTVAQPSEMPPSPLVWE")

align = LA(seq1, seq2)
align.kOptimalAlignments(1)
align.printAlignment()


