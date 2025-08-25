from pathlib import Path

from pydoover import config


class SystemVoltage:
    V12 = "12V"
    V24 = "24V"
    V48 = "48V"


class BatteryMonitorConfig(config.Schema):
    def __init__(self):
        self.system_voltage = config.Enum(
            "System Voltage",
            choices=[SystemVoltage.V12, SystemVoltage.V24, SystemVoltage.V48],
            default=SystemVoltage.V12,
        )

        self.position = config.Integer("UI Position", default=100)

def export():
    BatteryMonitorConfig().export(
        Path(__file__).parents[2] / "doover_config.json", "battery_monitor"
    )
