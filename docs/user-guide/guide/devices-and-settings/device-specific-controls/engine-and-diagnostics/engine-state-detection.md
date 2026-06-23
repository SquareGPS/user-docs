---
description: Configure the Engine state detection block in Navixy so the device reports engine on and off based on on-board voltage levels and durations.
---

# Engine state detection

## Purpose

The **Engine state detection** block tells the device how to determine that the engine is running, based on on-board voltage. A running engine raises system voltage above the battery's resting level.

## Settings

* **Engine on**: the high voltage level and the duration it must hold to register the engine as on.
* **Engine off**: the low voltage level and the duration it must hold to register the engine as off.

## Appears when

Appears on device models that detect engine state from on-board voltage.

## See also

* [Ignition source](../../location-and-movement/ignition-source.md): choose how the device detects ignition.
