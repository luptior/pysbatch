import subprocess as sps
import sys, os
sys.path.append(os.getcwd())

def shell_ver(job_name="py_job", mem=8, dep="", days=3, log="submit.out",wrap="python hello.py"):
    # store cmd as .sh file then run shell file.
    sub=['sbatch',
         '--ntasks=1',
         '--cpus-per-task=1', '-N', '1',
         '--job-name={}'.format(job_name),
         '--mem={}000'.format(mem),
         dep,
         '--time={}-0'.format(days),
         '--out={}'.format(log)]
    sub.append('--wrap="{}"'.format(wrap.strip()))

    script="submit.sh"
    with open(script, "w") as myfile:
        myfile.write(" ".join(sub))

    # sps.run(['sh', script])


def sps_ver(job_name="py_job", mem=8, dep="", days=3, log="submit.out",wrap="python hello.py"):
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
    sps_ver(wrap="python hello.py")
