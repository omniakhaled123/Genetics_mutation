codon = {
   'UUU': 'Phe',
   'UUC': 'Phe',
   'uua': 'Leu',
   'UUG': 'Leu',
   'CUU': 'Leu',
   'CUC': 'Leu',
   'CUA': 'Leu',
   'CUG': 'Leu',
   'AUU': 'Ile',
   'AUC': 'Ile',
   'AUA': 'Ile',
   'AUG': 'Met',
   'GUU': 'Val',
   'GUC': 'Val',
   'GUA': 'Val',
   'GUG': 'Val',
   'UCU': 'Ser',
   'UCC': 'Ser',
   'UCA': 'Ser',
   'UCG': 'Ser',
   'CCU': 'Pro',
   'CCC': 'Pro',
   'CCA': 'Pro',
   'CCG': 'Pro',
   'ACU': 'Thr',
   'ACC': 'Thr',
   'ACA': 'Thr',
   'ACG': 'Thr',
   'GCU': 'Ala',
   'GCC': 'Ala',
   'GCA': 'Ala',
   'GCG': 'Ala',
   'UAU': 'Tyr',
   'UAC': 'Tyr',
   'UAA': 'STOP',
   'UAG': 'STOP',
   'CAU': 'His',
   'CAC': 'His',
   'CAA': 'Gln',
   'CAG': 'Gln',
   'AAU': 'Asn',
   'AAC': 'Asn',
   'AAA': 'Lys',
   'AAG': 'Lys',
   'GAU': 'Asp',
   'GAC': 'Asp',
   'GAA': 'Glu',
   'GAG': 'Glu',
   'UGU': 'Cys',
   'UGC': 'Cys',
   'UGA': 'STOP',
   'UGG': 'Trp',
   'CGU': 'Arg',
   'CGC': 'Arg',
   'CGA': 'Arg',
   'CGG': 'Arg',
   'AGU': 'Ser',
   'AGC': 'Ser',
   'AGA': 'Arg',
   'AGG': 'Arg',
   'GGU': 'Gly',
   'GGC': 'Gly',
   'GGA': 'Gly',
   'GGG': 'Gly',
    'UUA':'STOP',
   'UAG' :'STOP',
}
#=================================================
list = ['C', 'T', 'G', 'A']
file = open(r'D:\Genatics\P53_seq.txt', 'r')
seq=file.read()
file.close()
seq=seq.replace('\n',"")
#==================================================
def dna_compliment (seq):
   seq2=""
   for i in seq:
      if i=='C':
         seq2+='G'
      if i=='A':
         seq2+='T'
      if i=='T':
         seq2+='A'
      if i=='G':
         seq2+='C'

   return seq2



# =========================================================

seqrna = dna_compliment(seq).replace('T', 'U')

print(seqrna)


# ========================================================

def listing_rna (seqrna):
     triple=[]
     for i in range(0,len(seqrna),3):
        x=""
        x=seqrna[i:i+3]
        if x=='UGA'or x=='UAG'or x=='UAA':
           break
        triple.append(x)
     return triple
#==========================================================
triple1 =listing_rna(seqrna)
#==========================================================
def getamino (triple1):
   listamino=[]
   for i in triple1:
      listamino .append([i])
   return listamino
getamino (triple1)
#==========================================================
def check_mutation(str1,str2):
   if str1==str2:
      print("identical")
   else :
      list1=listing_rna(str1)
      list2=listing_rna(str2)
      for i in range(0,len(list1)):
          if list1[i]!=list2[i]:
             print ("diff codon ")
             print (i+1)
             print("Normal " )
             print (list1[i])
             print (codon[list1[i]])
             print ("abNormal" )
             print ( list2[i] )
             print (codon[list2[i]])
#============================================================











str1="ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACT"
str2="ATGGTGCACCTGACTCCTGTGGAGAAGTCTGCCGTTACT"
str1=str1.replace('T','U')
str2=str2.replace('T','U')
check_mutation(str1,str2)
seq2=dna_compliment(seq)
#print(seq2)



#validation(seq)






