from locust import HttpUser, task

class Info(HttpUser):
    @task
    def info(self):
        self.client.get("/")
        self.client.get("/other")
        self.client.get("/exp")