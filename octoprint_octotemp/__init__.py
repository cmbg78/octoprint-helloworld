# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import sys
import os
sys.path.append(os.path.abspath(os.path.join(sys.path[len(sys.path)-1], 'octoprint_octotemp', 'raspi')))
import onewire

class OctotempPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin,octoprint.plugin.SettingsPlugin,octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("octotemp-raspi plugin loaded")
        self._logger.info(self._settings.get(["probe_0"]))

    def get_settings_defaults(self):
        probes = onewire.getDeviceList()
        if len(probes) > 10:
            self._logger.warn("The Octotemp plugin only supports up to 10 OneWire probes. Only the first 10 probes enumerated will be avaialble for use.")
        pd = {}
        i = 0
        for probe in probes:
            if "_bus_" in probe:
                probes.remove(probe)
            else:
                pname = "probe_" + str(i)
                pdata = [probe, '']
                d = {pname : pdata}
                pd.update(d)
                #f = {probe.replace("-", "_") : ""}
                #pd.update(f)
            i = i+1
        self._logger.info(str(pd))
        return pd
    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    def get_assets(self):
        return dict(
            #js=["js/octotemp.js"],
            css=["css/octotemp.css"],
            less=["less/octotemp.less"]
        )

__plugin_name__ = "OctoTemp"
__plugin_implementation__ = OctotempPlugin()