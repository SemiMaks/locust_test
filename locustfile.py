from locust import HttpUser, task, between


class WebsiteTestuser(HttpUser):
    wait_time = between(0, 0)

    def on_start(self):
        """on_start"""
        pass

    def on_stop(self):
        """on+stop"""
        pass

    @task(1)
    def run_test(self):
        self.client.get("http://12.0.0.1:5000")

    @task(2)
    def run_test(self):
        self.client.get("http://12.0.0.1:5000/index")
