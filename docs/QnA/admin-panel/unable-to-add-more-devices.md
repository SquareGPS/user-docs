# Unable to add more devices

### Question

Why am I unable to add a device when the user is paid up?

### Answer

If you’re unable to add devices to a user, it may be related to your device plan limit.

The platform uses the least-rights approach: if there is a conflict between two plans under a user, it applies the most restrictive values.

Example:

* Plan A: limit 100
* Plan B: limit 50

Result: effective limit is 50.

Fix: update the lowest plan limit to match the higher one.

![](<../.gitbook/assets/Unknown image (136)>)

It’s usually best to keep this limit field maxed out to avoid hitting this issue.
