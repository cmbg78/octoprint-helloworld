# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import sys
import os
import imp

# import included onewire-raspi module
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), 'octoprint_octotemp', 'raspiutils')))
import onewire

# random debug imports
import inspect

class OctotempPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin,octoprint.plugin.SettingsPlugin,octoprint.plugin.AssetPlugin):

    def __init__(self):
        self.probeData = {}

    def on_after_startup(self):
        self._logger.info("octotemp-raspi plugin loaded")
        #self._logger.info(sys.path)
        
    def get_settings_defaults(self):
        probes = onewire.getDeviceList()
        i = 0

        for probe in probes:
            if "_bus_" in probe:
                probes.remove(probe)
            else:
                pname = "probe_" + str(i)
                pdata = [probe, '']
                d = {pname : pdata}
                self.probeData.update(d)
            i = i + 1
        
        # debug
        self._logger.info("****BEGIN DEBUG INFO****")
        aProbe = self.probeData[self.probeData.iterkeys().next()][0]
        self._logger.info(aProbe + " temp = " + str(onewire.readTempF(aProbe)))

        return self.probeData
        
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