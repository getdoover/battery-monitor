"""
Basic tests for an application.

This ensures all modules are importable and that the config is valid.
"""

def test_import_app():
    from battery_monitor.application import BatteryMonitorApplication
    assert BatteryMonitorApplication

def test_config():
    from battery_monitor.app_config import BatteryMonitorConfig

    config = BatteryMonitorConfig()
    assert isinstance(config.to_dict(), dict)

def test_ui():
    from battery_monitor.app_ui import BatteryMonitorUI
    assert BatteryMonitorUI

def test_state():
    from battery_monitor.app_state import BatteryMonitorState
    assert BatteryMonitorState