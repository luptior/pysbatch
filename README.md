# pysbatch

Submit(sbatch) slurm cluster job inside python and avoid shell script for complicated pipeline jobs. For sbatch options, now only supports job name, memory size(in GBs), time limit(in days), dependency and ouput file. But you can use add_option parameter to add more.

## install in linux/unix
```
git clone https://github.com/luptior/pysbatch.git
cd pysbatch
pip install .
```

pysbatch contains only 2 functions sbatch() and run_cmd()

## running in python
```
from pysbatch import *
sbatch(wrap="python hello.py") # simplest

jobid=sbatch(wrap="python hello.py").split(" ")[-1] # dependency example
sbatch(job_name="py_job", mem=16, dep="--dependency:afterok:{}".format(jobid), days=3, log="submit.out", wrap="python hello.py") # more options

sbatch(job_name="py_job", add_option="--cpus-per-task=1 --nodes=3", wrap="python hello.py") # add more options

```

## running with custormized setting
```
x = batch_setting()
x.edit_default("--cpus-per-task=2 --job-name=lalaland")
x.add_options("--ccc hwlo")
x.sbatch("python hello.py")

```


## run_cmd()
```
#simplified subprocess.run() of running linux command in python
>>>print(run_cmd(['ls', '..']))
unrar
var
zlib-1.2.11
```
