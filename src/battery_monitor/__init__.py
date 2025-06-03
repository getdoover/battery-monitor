from pydoover.docker import run_app

from .application import BatteryMonitorApplication
from .app_config import BatteryMonitorConfig


def main():
    """
    Run the application.
    """
    run_app(BatteryMonitorApplication(config=BatteryMonitorConfig()))
