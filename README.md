# pysbatch 0.1.4 
![PyPI - Python Version](https://img.shields.io/badge/python-≥3.5-blue.svg)
![PyPI - Slurm Version](https://img.shields.io/badge/slurm-≥18-green.svg)


Submit(sbatch) slurm cluster job inside python and avoid shell script for complicated pipeline jobs. For sbatch options, now only supports job name, memory size(in GBs), time limit(in days), dependency and ouput file. But you can use add_option parameter to add more.

## install in linux/unix
```bash
# now published to PyPI, only support python version >= 3.5
pip install pysbatch

# now also availale with conda
conda install -c luptior pysbatch

# newer version is not published on PyPI
git clone https://github.com/luptior/pysbatch.git
cd pysbatch
pip install .
```

## customized settings
Recommended way to use the pysbatch, batch_setting object can be resued and avoid trouble
```python
from pysbatch import *
x = batch_setting_new() # with default settings
x2 = batch_setting_new("--cpus-per-task=2 --job-name=lalaland") # with customized settings
x.edit_default("--cpus-per-task=2 --job-name=lalaland") # now replace the default instead of "edit"
x.add_options("--begin=16:00")

# dependency works in the same way
# edit dependency, de
x.add_dep(27561)
x.add_dep(27562)
x.reset_dep()

# the settings object can be reused
x.sbatch("python hello.py")

```


## running sbatch() function in python
```python
from pysbatch import *
sbatch(wrap="python hello.py") # simplest

jobid=sbatch(wrap="python hello.py").strip("\n").split(" ")[-1] # dependency example
sbatch(job_name="py_job", mem=16, dep="--dependency:afterok:{}".format(jobid), time=3-0, log="submit.out", wrap="python hello.py") # more options

sbatch(job_name="py_job", add_option="--cpus-per-task=1 --nodes=3", wrap="python hello.py") # add more options

```


## limit total numbers in running/queued
useful if your slurm has a queue quota set and you need to submit a large batch of jobs
```python
# example
for job in job_batch:
  sbatch(job)
  limit_jobs(limit=10000) # default is 200000
```


## run_cmd()
```sh
# simplified subprocess.run() of running linux command in python

# in linux
$ ls ..
unrar
var
zlib-1.2.11
```

```python
# in python
>>>print(run_cmd(['ls', '..']))
unrar
var
zlib-1.2.11
```

## customized settings(in 0.1.2, still works)
(a little bit messy, implemented it a better way)
```python
from pysbatch import *

# initialize and edit batch_setting object
x = batch_setting() # start with default settings
x2 = batch_setting(mem="16") # change settings when initialize

# edit default options contain in this pakcage:
# --ntasks, --cpus-per-task, -N, --job-name, --mem, --time, --out
x.edit_cpus_per_task(8)
x.edit_mem("16") # one at a time
x.edit_default("--cpus-per-task=2 --job-name=lalaland") # all together

# edit dependency, de
x.add_dep(27561)
x.add_dep(27562)
x.reset_dep()

# add aditional
x.add_options("--begin=16:00")

x = batch_setting(empty_set=True)
x.add_options("--cpus-per-task=2 --job-name=lalaland ")

# the settings object can be reused
x.sbatch("python hello.py")

```


## Authors

* **Gan Xu**  - [Ganxu.science](https://ganxu.science)


## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/luptior/pysbatch/blob/master/LICENSE) file for details
