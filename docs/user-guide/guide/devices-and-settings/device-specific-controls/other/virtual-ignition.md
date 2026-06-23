---
description: Configure the Virtual ignition block in Navixy so the device derives ignition from on-board voltage or motion instead of an ignition wire.
---

# Virtual ignition

## Purpose

The **Virtual ignition** block lets the device derive ignition state from on-board voltage or motion when the ignition wire is not connected.

## Settings

* **Mode**: derive ignition from board voltage or from the motion sensor.
* **Ignition-on voltage**: the voltage above which ignition counts as on, in voltage mode.
* **Rest duration to off**: how long without motion before ignition counts as off, in motion mode.
* **Motion duration to on**: how long motion must last before ignition counts as on, in motion mode.

## Appears when

Appears on device models that support virtual ignition.

## See also

* [Ignition source block](../../location-and-movement/ignition-source-block.md): the main block for choosing the ignition detection mode.
