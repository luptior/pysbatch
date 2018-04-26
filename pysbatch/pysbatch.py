import subprocess as sps
import sys, os


sys.path.append(os.getcwd())


class batch_setting:
    ntasks=''
    cpus_per_task=''
    N=''
    job_name=''
    dep=''
    mem=''
    days=''
    log=''
    options=''

    def __init__(self):
        self.ntasks='1'
        self.cpus_per_task='1'
        self.N='1'
        self.job_name="py_job"
        self.dep=""
        self.mem="8"
        self.days='3'
        self.log="submit.out"
        self.options=""

    def edit_default(self, edit):
        try:
            for x in edit.split(" "):
                var, value = x.split("=")
                var = '_'.join(filter(None, var.split("-")))
                print(var)
                _='value'
                exec("self.{} = {}".format(var, _))
        except:
             sys.exit("Edit string is in wrong format/include options other than default")


    def add_options(self, edit):
        self.options=edit


    def sbatch(self, wrap):
        sub=['sbatch',
             '--ntasks={}'.format(self.ntasks),
             '--cpus-per-task={}'.format(self.cpus_per_task), '-N', self.N,
             '--job-name={}'.format(self.job_name),
             '--mem={}'.format(self.mem+"000"),
             '--time={}'.format(self.days+"-0"),
             self.dep, self.options,
             '--out={}'.format(self.log),
             '--wrap="{}"'.format(wrap.strip())]
        # print(" ".join(sub))
        process = sps.Popen(" ".join(sub), shell=True, stdout=sps.PIPE)
        stdout = process.communicate()[0].decode("utf-8")
        return(stdout)


def sbatch(job_name="py_job", mem='8', dep="", days='3', log="submit.out",wrap="python hello.py", add_option=""):
    sub=['sbatch',
         '--ntasks=1',
         '--cpus-per-task=1', '-N', '1',
         '--job-name={}'.format(job_name),
         '--mem={}'.format(mem+"000"),
         '--time={}'.format(days+"-0"),
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


if __name__ == '__main__':
    sbatch(wrap="python hello.py")
