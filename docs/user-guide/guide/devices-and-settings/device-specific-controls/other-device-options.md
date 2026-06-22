---
description: Configure per-model device switches such as OBD data acquisition, device-side fuel computation, and the status LED. Options depend on the device.
---

# Other device options

## Purpose

Some device models expose **small, model-specific switches** that don't fit the other categories. They configure the device's own behavior and appear only where the hardware supports them.

<!-- SCREENSHOT: example of a small device-specific option block (e.g. OBD data acquisition or LED display). Annotate: the main toggle and any interval/threshold field. -->

## Settings

The options you may see, depending on the device:

* **OBD data acquisition** — for OBD dongles: enable PID reports and set the data-collection interval and how many records to upload per batch.
* **Device-side fuel configuration** — the device's own fuel computation: fuel type, engine volume, and a multiplier. This is **distinct from** platform-side [fuel sensors and calibration](../vehicle-sensors/measurement-sensors/).
* **LED indicator** — choose whether the device's status LED stays always on or switches off after a timeout.
* **Time shift / device time zone** — the device's time-zone offset. See the dedicated [Device timezone block](../object-management/device-timezone-block.md).

{% hint style="info" %}
Exact controls depend on your device. A given model shows only the options its firmware supports, with vendor-specific labels.
{% endhint %}

{% hint style="warning" %}
**Pending product review:** some device models expose additional security/signature options that are not yet documented here. If you see a control not described on these pages, contact support before changing it.
{% endhint %}

## Appears when

Appears only on device models whose firmware exposes the corresponding option.

## See also

* [Device timezone block](../object-management/device-timezone-block.md) — set the device's time-zone offset.
* [Vehicle sensors](../vehicle-sensors/) — platform-side fuel and other sensor configuration.
* [External and BLE sensors](external-and-ble-sensors.md) — bind device-side sensor channels.
