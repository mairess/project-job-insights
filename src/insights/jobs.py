from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as job_file:
            content = csv.DictReader(job_file, delimiter=",", quotechar='"')
            self.jobs_list = [row for row in content]

    def get_unique_job_types(self) -> List[str]:
        unique_job = set()
        for row in self.jobs_list:
            job_type = row["job_type"]
            if job_type and job_type not in unique_job:
                unique_job.add(job_type)
        return list(unique_job)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
