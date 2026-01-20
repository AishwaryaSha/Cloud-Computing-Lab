from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def view_events(self):
        self.client.get(
            "/events",
            params={"user": "locust_user"},
            name="/events"
        )
