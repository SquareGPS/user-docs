---
description: Configure power-save sleep conditions on a battery GPS device in Navixy with the Sleep mode block. Available fields depend on the device model.
---

# Sleep mode

## Purpose

The **Sleep mode** block controls how a battery-powered device sleeps to save power. A sleeping device reports less often, which extends battery life on assets that are not continuously powered.

## Settings

The fields depend on the device. You may see:

* **Sleep conditions**: what puts the device to sleep, such as ignition off, no motion, or no communication.
* **Sleep and deep-sleep durations**: how long a condition must hold before light sleep and deep sleep engage.
* **Wake-up intervals**: how often the device wakes to report.
* **Voltage thresholds**: on some models, the voltage levels that trigger light or deep sleep.

## Appears when

Appears on battery-powered device models that expose sleep settings.

## See also

* [Tracking mode block](../../location-and-movement/tracking-mode-block.md): power-save options that overlap with sleep mode.
* [Connection state block](../../connectivity/connection-state-block.md): set the offline timeout long enough that a sleeping device is not shown offline too early.
