import logging
import time

from pydoover.docker import Application
from pydoover.utils import apply_async_kalman_filter

from .app_config import BatteryMonitorConfig
from .app_ui import BatteryMonitorUI

log = logging.getLogger()


class BatteryMonitorApplication(Application):
    config: (
        BatteryMonitorConfig  # not necessary, but helps your IDE provide autocomplete!
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.loop_target_period = 2

        self.started = time.time()
        self.has_sent_alert = False

    async def setup(self):
        self.ui = BatteryMonitorUI(self.config.system_voltage.value)
        self.ui_manager.add_children(*self.ui.fetch())
        self.ui_manager.set_display_name("Battery")

    async def main_loop(self):
        voltage = await self.get_system_voltage()
        log.info("Running loop with voltage: %sV", voltage)

        low_alert = self.ui.battery_low_voltage_alert.current_value
        if low_alert is not None and voltage is not None and low_alert < voltage:
            if not self.has_sent_alert:
                log.warning(f"Battery voltage is low: {voltage}V. Sending alert")
                await self.publish_to_channel(
                    "notifications", f"Battery voltage is low: {voltage}V"
                )
                self.has_sent_alert = True
            else:
                log.debug(f"Battery voltage is still low: {voltage}V")

        self.ui.update(voltage)

        ## Update tags
        # self.set_tag("system_voltage", voltage)

    @apply_async_kalman_filter(
        process_variance=0.05,
        outlier_threshold=0.5,
    )
    async def get_system_voltage(self) -> float:
        # Get the current system voltage
        return await self.platform_iface.get_system_voltage_async()
    
    async def get_system_temperature(self) -> float:
        # Get the current system temperature
        return await self.platform_iface.get_system_temperature_async()
