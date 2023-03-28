class Job:
    def __init__(self, jobName, freq):
        self.jobName = jobName
        self.freq = freq
    def myJob(self):

        print(f"The job name is {self.jobName} and schedule is {self.freq}")



EOD = Job("EOD", "Daily")

EOD.myJob()







