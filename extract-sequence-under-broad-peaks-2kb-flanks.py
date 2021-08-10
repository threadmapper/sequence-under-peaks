"""

Writing the fasta file with +/-2Kb flanking sequence from a bed formatted peak file

"""

import jitu

tube, seqD = jitu.getTubeD('magna_mg8.fa')

# change here for a different flank
flank = 2000

with open('rep1_diff_fdr10perc_peaks.broadPeak') as inp, open('rep1-broad-peak-genomic-seqs-hox7-2kb.fa','w') as outf:

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
        
        L = len(seqD[d['chrom']]) 

        # check bounds and adjust 
        beg_2k =  max(0, d['start'] - flank)
        end_2k =  min(d['end']   + flank, L)

        seqa = seqD[d['chrom']][beg_2k : end_2k]

        assert len(seqa)  <= L 

        header = d['gene']
        outf.write('>' + header + '\n')
        outf.write(seqa+ '\n')

print ('DONE')

                   
         

   
