from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        salaries = [
            int(row["max_salary"])
            for row in self.jobs_list
            if row["max_salary"] and row["max_salary"].isdigit()
        ]
        return max(salaries)

    def get_min_salary(self) -> int:
        salaries = [
            int(row["min_salary"])
            for row in self.jobs_list
            if row["min_salary"] and row["min_salary"].isdigit()
        ]
        return min(salaries)

    def verify_value(self, value: int | float | str) -> float:
        if value is None or not isinstance(value, (int, float, str)):
            raise ValueError
        return float(value)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError

        min_salary = self.verify_value(job["min_salary"])
        max_salary = self.verify_value(job["max_salary"])

        if min_salary > max_salary:
            raise ValueError

        salary = self.verify_value(salary)

        return min_salary <= salary <= max_salary

    def filter_jobs(self, jobs: List[dict], salary: str | int) -> list:
        filtered_jobs = []

        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filtered_jobs.append(job)
            except ValueError:
                continue

        return filtered_jobs

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        if (
            salary is None
            or not isinstance(salary, (int, float, str))
            or salary == ""
        ):
            return []

        salary = float(salary)

        return self.filter_jobs(jobs, salary)
