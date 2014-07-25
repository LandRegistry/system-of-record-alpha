from healthcheck import HealthCheck
from systemofrecord import app

class Health(object):

    def __init__(self, app, endpoint='/health', checks=None):
        self.health = HealthCheck(app, endpoint)

        # extra health checks
        [self.health.add_check(check) for check in checks if callable(check)]
