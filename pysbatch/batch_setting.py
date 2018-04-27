import subprocess as sps
import sys, os


class batch_setting:
    ntasks=''
    cpus_per_task=''
    N=''
    job_name=''
    dep=''
    mem=''
    time=''
    log=''
    options=''

    def __init__(self, ntasks='1', cpus_per_task='1', N='1', job_name="py_job",
                                        mem="8", time='3-0', log="submit.out"):
        self.ntasks=str(ntasks)
        self.cpus_per_task=str(cpus_per_task)
        self.N=str(N)
        self.job_name=str(job_name)
        self.mem=str(mem)
        self.time=str(time)
        self.log=str(log)

    def edit_default(self, edit):
        try:
            for x in edit.split(" "):
                var, value = x.split("=")
                var = '_'.join(filter(None, var.split("-")))
                _='value'
                exec("self.{} = {}".format(var, _))
        except:
             sys.exit("Edit string is in wrong format/include options other than default")

    def reset_dep(self):
        # if not dep is needed
        self.dep = ''

    def add_dep(self, edit):
        # if need to add dep
        try:
            edit=int(edit)
        except ValueError:
            print("dependency input should be numerical jobid")
            return

        if not self.dep:
            self.dep = "--dependency=afterok:{}".format(str(edit))
        else:
            self.dep += ":{}".format(str(edit))

    def add_options(self, edit):
        self.options=edit


    def sbatch(self, wrap):
        sub=['sbatch',
             '--ntasks={}'.format(self.ntasks),
             '--cpus-per-task={}'.format(self.cpus_per_task), '-N', self.N,
             '--job-name={}'.format(self.job_name),
             '--mem={}'.format(self.mem+"000"),
             '--time={}'.format(self.time),
             self.dep, self.options,
             '--out={}'.format(self.log),
             '--wrap="{}"'.format(wrap.strip())]
        # print(" ".join(sub))
        process = sps.Popen(" ".join(sub), shell=True, stdout=sps.PIPE)
        stdout = process.communicate()[0].decode("utf-8")
        return(stdout)
