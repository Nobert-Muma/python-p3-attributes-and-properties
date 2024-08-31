#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        self.name=name
        self.job=job
    def get_name(self):
        print("Retrieving the name of the person.")
        return self._name
    def set_name(self, name):
        if name is None:
            self._name=None
        elif (type(name)==str) and 1 <= len(name) <=25:
            print(f"Setting name to {name}")
            self._name=name.title()
        else:
            print("Name must be string between 1 and 25 characters.")
    def get_job(self):
        print("Retrieving the name of the job.")
        return self._job
    def set_job(self, job):
        if job is None:
            self._job=None
        elif job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job=job
    name=property(get_name, set_name)
    job=property(get_job, set_job)
