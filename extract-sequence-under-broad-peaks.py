"""

Writing the fasta file from a bed formatted peak file given the input genome fasta

input: magna_mg8.fa and macs peak bed file 
"""

import jitu

tube, seqD = jitu.getTubeD('magna_mg8.fa') 

with open('rep1_diff_fdr10perc_peaks.broadPeak') as inp, open('rep1-broad-peak-genomic-seqs-hox7.fa','w') as outf:
 for line in inp:
  if '#' not in line:
     A = line.strip().split()
     
     if len(A) > 3:
        d={}
        d['gene']= A[3]
        d['chrom']= A[0]
        d['start']= int(A[1])
        d['end']= int(A[2])
        d['strand']= '.'
        seqa = seqD[d['chrom']][d['start']:d['end']]
        head = d['gene']
        outf.write('>' + head + '\n')
        outf.write(seqa+ '\n')

print('DONE')           
         

   
