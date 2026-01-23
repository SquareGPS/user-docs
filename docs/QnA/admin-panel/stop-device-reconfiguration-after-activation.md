# Stop device reconfiguration after activation

### Question

I configured my device before connecting it. After activation, settings changed. How do I stop this?

### Answer

By default, the platform can send activation and default configuration commands.

Disable it in Admin Panel:

Account Management → Service Preferences → Device Activation → **Do not send default settings**

This prevents the platform from sending default settings after activation.

It can also prevent SMS activation commands (if used).

### Links

* [Service preferences](https://docs.navixy.com/admin-panel/service-preferences)
