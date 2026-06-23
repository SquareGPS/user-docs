---
description: Configure the Vibration detection block in Navixy so the device reports vibration after the ignition is off, with a sensitivity level and delays.
---

# Vibration detection

## Purpose

The **Vibration detection** block uses the device's motion sensor to detect vibration or tampering after the ignition is off and report an event to the platform.

## Settings

* **Enable**: turn vibration detection on or off.
* **Sensitivity level**: low, medium, or high.
* **Activation after ignition (seconds)**: how long after ignition off detection arms.
* **Vibration duration (seconds)**: how long vibration must last to count.
* **Waiting ignition (seconds)**: a grace period that ignores vibration around ignition events.

## Appears when

Appears on device models that support vibration detection.

## See also

* [Vibration settings](vibration-settings.md): adjust the motion sensor sensitivity on devices that expose it separately.
