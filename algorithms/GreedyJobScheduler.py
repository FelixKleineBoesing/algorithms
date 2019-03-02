import copy

def load_file(file: str):
    '''
    load file for counting
    :param file: path to file
    :return: list with integers
    '''
    data = []
    with open(file) as f:
        lines = f.readlines()
    sum_jobs = int(lines.pop(0))
    for row in lines:
        val = row.split()
        data += [{"weight": int(val[0]), "length": int(val[1])}]
    return data, sum_jobs


class GreedyJobScheduler:

    def __init__(self, jobs: [dict], number_jobs: int, mode: str = "diff"):
        '''
        schedules jobs based on weight and length
        :param jobs: list of jobs (weight, length)
        :param number_jobs: number of jobs
        :param mode: must be "diff" or "ratio". If diff jobs will be scheduled by weight minus length.
        If ratio it will be weight / length
        '''
        assert type(jobs) == list
        assert type(number_jobs) == int
        assert jobs.__len__() == sum_jobs
        assert type(mode) == str
        assert mode in ["diff", "ratio"]

        self.jobs = jobs
        self.number_jobs = number_jobs
        self.mode = mode

    def run_scheduling(self):
        '''
        run scheduling for given jobs
        :return: nothing
        '''
        if self.mode=="diff":
            self.jobs.sort(key=lambda job: (job["weight"] - job["length"], job["weight"]), reverse=True)
        else:
            self.jobs.sort(key=lambda job: (job["weight"] / job["length"], job["weight"]), reverse=True)

    def get_running_time(self):
        '''
        returns the sum of running time
        :return:
        '''
        elapsed_time = 0
        sum = 0
        for job in self.jobs:
            elapsed_time += job["length"]
            sum += job["weight"] * elapsed_time
        return sum

if __name__ == "__main__":
    data, sum_jobs = load_file("../data/jobs.txt")
    diff_job_scheduler = GreedyJobScheduler(copy.deepcopy(data), sum_jobs, "diff")
    diff_job_scheduler.run_scheduling()

    ratio_job_scheduler = GreedyJobScheduler(copy.deepcopy(data), sum_jobs, "ratio")
    ratio_job_scheduler.run_scheduling()

    print(diff_job_scheduler.get_running_time())
    print(ratio_job_scheduler.get_running_time())