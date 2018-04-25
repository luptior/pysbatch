import subprocess as sps
import sys, os
sys.path.append(os.getcwd())

def sbatch(job_name="py_job", mem=8, dep="", days=3, log="submit.out",wrap="python hello.py"):
    sub=['sbatch',
         '--ntasks=1',
         '--cpus-per-task=1', '-N', '1',
         '--job-name={}'.format(job_name),
         '--mem={}000'.format(mem),
         '--time={}-0'.format(days),
         dep,
         '--out={}'.format(log)]
    sub.append('--wrap="{}"'.format(wrap.strip()))
    # print(" ".join(sub))
    process = sps.Popen(" ".join(sub), shell=True, stdout=sps.PIPE)
    stdout = process.communicate()[0].decode("utf-8")
    return(stdout)


if __name__ == '__main__':
    sbatch(wrap="python hello.py")
