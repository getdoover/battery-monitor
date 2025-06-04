from pydoover import ui

from .app_config import SystemVoltage

LOW_MAP = {
    SystemVoltage.V12: (0, 12),
    SystemVoltage.V24: (0, 24),
    SystemVoltage.V48: (0, 48),
}

OK_MAP = {
    SystemVoltage.V12: (12, 13),
    SystemVoltage.V24: (24, 26),
    SystemVoltage.V48: (48, 52),
}

CHARGING_MAP = {
    SystemVoltage.V12: (13, 14.2),
    SystemVoltage.V24: (26, 29),
    SystemVoltage.V48: (52, 58),
}

HIGH_MAP = {
    SystemVoltage.V12: (14.2, 14.6),
    SystemVoltage.V24: (29, 32),
    SystemVoltage.V48: (58, 61),
}

LOW_ALERT_MAP = {
    SystemVoltage.V12: (6, 11),
    SystemVoltage.V24: (12, 23),
    SystemVoltage.V48: (24, 47),
}


class BatteryMonitorUI:
    def __init__(self, system_voltage: SystemVoltage):
        self.battery_voltage = ui.NumericVariable(
            "voltage",
            "Battery Voltage",
            precision=2,
            ranges=[
                ui.Range("Low", *LOW_MAP[system_voltage], ui.Colour.yellow),
                ui.Range("OK", *OK_MAP[system_voltage], ui.Colour.blue),
                ui.Range("Charging", *CHARGING_MAP[system_voltage], ui.Colour.green),
                ui.Range("High", *HIGH_MAP[system_voltage], ui.Colour.red),
            ],
        )

        self.battery_low_voltage_alert = ui.Slider(
            "low_voltage_alert",
            "Low Voltage Alert",
            *LOW_ALERT_MAP[system_voltage],
            dual_slider=False,
            inverted=False,
            step=0.25,
            default=10.5,
        )

    def fetch(self):
        return self.battery_voltage, self.battery_low_voltage_alert

    def update(self, voltage: float):
        self.battery_voltage.update(voltage)
