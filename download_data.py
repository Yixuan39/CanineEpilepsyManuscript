import subprocess
import os

os.makedirs('Epilepsy_data/sra', exist_ok=True)
subprocess.call('prefetch -O Epilepsy_data/sra PRJNA612483', shell=True)
sra_numbers = os.listdir('Epilepsy_data/sra')


# this will extract the .sra files from above into a folder named 'fastq'
for sra_id in sra_numbers:
    print('Downloading ' + sra_id)
    fastq_dump = "fasterq-dump Epilepsy_data/sra/" + sra_id + " -O Epilepsy_data/fastq"
    subprocess.call(fastq_dump, shell=True)
