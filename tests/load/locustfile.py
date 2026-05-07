from locust import HttpUser, task, between


class GiteaUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def homepage(self):
        self.client.get("/")

    @task(1)
    def explore_repos(self):
        self.client.get("/explore/repos")
