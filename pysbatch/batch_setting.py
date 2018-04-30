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
                                        mem="8", time='1-0', log='', empty_set=False):
        if empty_set:
            return
        else:
            self.ntasks=str(ntasks)
            self.cpus_per_task=str(cpus_per_task)
            self.N=str(N)
            self.job_name=str(job_name)
            self.mem=str(mem)
            self.time=str(time)
            self.log=str(log)

    def __str__(self):
...         return self.ntasks, self.cpus_per_task, self.N, self.job_name, \
            self.mem, self.time, self.log

    def edit_default(self, edit):
        try:
            for x in edit.split(" "):
                var, value = x.split("=")
                var = '_'.join(filter(None, var.split("-")))
                _='value'
                exec("self.{} = {}".format(var, _))
        except:
             sys.exit("Edit string is in wrong format/include options other than default")

    def edit_ntasks(self, edit):
        try:
            edit=int(edit)
        except ValueError:
            print("dependency input should be integer")
            return
        self.ntasks=str(edit)

    def edit_cpus_per_task(self, edit):
        try:
            edit=int(edit)
        except ValueError:
            print("dependency input should be integer")
            return
        self.cpus_per_task=str(edit)

    def edit_N(self, edit):
        try:
            edit=int(edit)
        except ValueError:
            print("dependency input should be integer")
            return
        self.N=str(edit)

    def edit_job_name(self, edit):
        try:
            edit=str(edit)
        except ValueError:
            print("dependency input should be string")
            return
        self.job_name=str(edit)

    def edit_mem(self, edit):
        try:
            edit=int(edit)
        except ValueError:
            print("dependency input should be integer")
            return
        self.mem=str(edit)

    def edit_time(self, edit):
        try:
            edit=str(edit)
        except ValueError:
            print("dependency input should be slurm time format in string")
            return
        self.time=str(edit)

    def edit_log(self, edit):
        try:
            edit=str(edit)
        except ValueError:
            print("dependency input should be path to outfile in string")
            return
        self.log=str(edit)

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
