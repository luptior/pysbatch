# pysbatch

Submit(sbatch) slurm cluster job inside python and avoid shell script for complicated pipeline jobs. For sbatch options, now only supports job name, memory size(in GBs), time limit(in days), dependency and ouput file. But you can use add_option parameter to add more.

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

jobid=sbatch(wrap="python hello.py").split(" ")[-1] # dependency example
sbatch(job_name="py_job", mem=16, dep="--dependency:afterok:{}".format(jobid), days=3, log="submit.out", wrap="python hello.py") # more options

sbatch(job_name="py_job", add_option="--cpus-per-task=1 --nodes=1", wrap="python hello.py") # add more options

```
