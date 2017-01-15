# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import sys
import os
#sys.path.append(os.path.abspath(os.path.join(sys.path[len(sys.path)-1], 'octoprint_helloworld', 'raspi')))
import onewire

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.TemplatePlugin,octoprint.plugin.SettingsPlugin,octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info(sys.path[len(sys.path)-1])
        #self._logger.info(onewire.testPrint())
        #for i in sys.path:
        #    self._logger.info(i)
    def get_settings_defaults(self):
        return dict(url="https://en.wikipedia.org/wiki/Hello_world")
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