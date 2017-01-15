# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import sys
import os
sys.path.append(os.path.abspath(os.path.join(sys.path[len(sys.path)-1], 'octoprint_helloworld', 'raspi')))
import onewire

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin,octoprint.plugin.SettingsPlugin,octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("octotemp-raspi plugin loaded")
    def get_settings_defaults(self):
        probes = onewire.getDeviceList()
        pd = {}
        i = 0
        for probe in probes:
            if "_bus_" in probe:
                probes.remove(probe)
            else:
                pname = "probe-" + str(i)
                d = {pname : probe}
                pd.update(d)
            i = i+1
        self._logger.info(str(pd))
        return pd
    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]
    def get_assets(self):
        return dict(
            js=["js/helloworld.js"],
            css=["css/helloworld.css"],
            less=["less/helloworld.less"]
        )
__plugin_name__ = "Hello World"
__plugin_implementation__ = HelloWorldPlugin()