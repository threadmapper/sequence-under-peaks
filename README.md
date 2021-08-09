# Scripts to find the sequences under ChIP-seq peaks

- This repository contain the scripts to find the sequences under peaks for MST12/HOX genes.
- Please find more detail in the manuscript, Oses-Ruiz et al (2021).
- In case you would like to you this scripts for your analysis please modify the input  file names accordingly.

```python
input files: genome.fasta and peak file(bed formatted)

python extract-sequence-under-broad-peaks.py  

output file: sequence fasta file

# For a desired flank change line number 12 accordingly, below is for a 2kb flank 

flank = 2000

# After changing the input and output file name run the following

python extract-sequence-under-broad-peaks-2kb-flanks.py



```

- Please note we have tested this on Python 2.7 and Python 3.8 on linux and windows environment.


