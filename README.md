# pysbatch

Submit slurm cluster job inside python and avoid shell script. Submission commands can be customized but only supports job name, memory size(in GBs), time limit(in days), dependency and ouput file. But you can edit pysbatch.py to add more.

## install in linux/unix
```
git clone https://github.com/luptior/pysbatch.git
cd pysbatch
pip install .
```

pysbatch contains only 1 function sbatch()

## running in python
```
from pysbatch import *
sbatch(wrap="python hello.py") # simplest

jobid=sbatch(wrap="python hello.py").split(" ")[-1] # more options
sbatch(job_name="py_job", mem=16, dep="--dependency:afterok{}".format(jobid), days=3, log="submit.out",wrap="python hello.py")

```
