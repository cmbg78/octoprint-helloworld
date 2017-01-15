# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import sys
import os
sys.path.append(os.path.abspath(os.path.join(sys.path[len(sys.path)-1], 'octoprint_octotemp', 'raspi')))
import onewire

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin,octoprint.plugin.SettingsPlugin,octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("octotemp-raspi plugin loaded")
        self._logger.info(self._settings.get(["probe-0"]))
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
            #js=["js/octotemp.js"],
            css=["css/octotemp.css"],
            less=["less/octotemp.less"]
        )
    #def get_template_vars(self):
        #tvars = dict(probe-0=self._settings.get(["probe-0"]), probe-1=self._settings.get(["probe-1"]))
        #self._logger.info(str(tvars))
        #return tvars
__plugin_name__ = "OctoTemp"
__plugin_implementation__ = HelloWorldPlugin()