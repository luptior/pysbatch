import subprocess as sps
import sys, os, time


def sbatch(job_name="py_job", mem='8', dep="", time='3-0', log="submit.out",wrap="python hello.py", add_option=""):
    sub=['sbatch',
         '--ntasks=1',
         '--cpus-per-task=1', '-N', '1',
         '--job-name={}'.format(job_name),
         '--mem={}'.format(mem+"000"),
         '--time={}'.format(time),
         dep, add_option,
         '--out={}'.format(log)]
    sub.append('--wrap="{}"'.format(wrap.strip()))
    # print(" ".join(sub))
    process = sps.Popen(" ".join(sub), shell=True, stdout=sps.PIPE)
    stdout = process.communicate()[0].decode("utf-8")
    return(stdout)


def run_cmd(cmd):
    # simplified subprocess.run() of running linux command in python
    # cmd pass in as a list of strings, i.e. cd .. should be ['cd', '..']
    # return screen print as a string
    process=sps.run(cmd, stdout=sps.PIPE)
    return process.stdout.decode("utf-8")


def limit_jobs(limit=20000):
    l_jobs=run_cmd(['squeue', '-u', '$USER']).split("\n")
    # limit the total number of jobs in slurm job queue
    while int(l_jobs) >= 20000:
        time.sleep(300)


if __name__ == '__main__':
    sbatch(wrap="python hello.py")
