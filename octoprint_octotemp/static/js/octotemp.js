$(function() {
    function OctotempViewModel(parameters) {
        var self = this;

        self.settings = parameters[0];

        // this will hold the probe settings dictionary as a key/value object
        self.devices = ko.observablearray();
        //self.test = ko.observable();
        
        // This will get called before the OctotempModel gets bound to the DOM, but after its
        // dependencies have already been initialized. It is especially guaranteed that this method
        // gets called _after_ the settings have been retrieved from the OctoPrint backend and thus
        // the SettingsViewModel been properly populated.
        self.onBeforeBinding = function() {
            self.devices(mapDictionaryToArray(self.settings.settings.plugins.octotemp()));
            //self.test("testing");
        }
    }

    function mapDictionaryToArray(dictionary) {
        var result = [];
        for (var key in dictionary) {
            if (dictionary.hasOwnProperty(key)) {
                result.push({ key: key, value: dictionary[key] }); 
            }  
        }
        return result;
    }

    // This is how our plugin registers itself with the application, by adding some configuration
    // information to the global variable OCTOPRINT_VIEWMODELS
    OCTOPRINT_VIEWMODELS.push([
        // This is the constructor to call for instantiating the plugin
        OctotempViewModel,

        // This is a list of dependencies to inject into the plugin, the order which you request
        // here is the order in which the dependencies will be injected into your view model upon
        // instantiation via the parameters argument
        ["settingsViewModel"],

        // Finally, this is the list of selectors for all elements we want this view model to be bound to.
        ["#settings_plugin_octotemp"]
    ]);
});