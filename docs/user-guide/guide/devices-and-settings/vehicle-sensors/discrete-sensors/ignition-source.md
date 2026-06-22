---
description: Configure the ignition source for GPS devices that use virtual ignition detection via motion sensor or voltage instead of a direct ignition cable connection.
---

# Ignition source

## Purpose

This page covers creating an **ignition sensor** on the platform for devices that use **virtual ignition** — derived from the motion sensor or on-board voltage — instead of a direct ignition-cable connection.

{% hint style="info" %}
This is the **platform-side sensor**. To choose *how the device itself* detects ignition (digital input, on-board voltage, or motion), use the [Ignition source block](../../location-and-movement/ignition-source-block.md) under Location and movement.
{% endhint %}

## How virtual ignition works

Some devices do not allow connecting the ignition cable to the device input to transmit the ignition status. Instead, they use virtual ignition based on the motion sensor readings or the vehicle's onboard voltage.

When the engine is running, the vehicle's power supply is provided by the vehicle's generator, which typically has a higher voltage than the battery. The voltage is higher and allows the ignition status to be determined.

The ignition detection by the movement sensor is convenient if the device is not connected to the vehicle's onboard electrical system. However, when the vehicle is towed, the ignition will also be detected as the vehicle moves, although the engine will not start.

## Settings

The ignition source is selected from a drop-down list. If the ignition source is the onboard power supply voltage, the range of values in which the ignition is considered switched on must be selected.

## Appears when

Available on devices that expose a suitable input or support virtual ignition.

## See also

* [Ignition source block](../../location-and-movement/ignition-source-block.md) — set the device-side ignition detection mode.
* [Engine hours block](../../location-and-movement/engine-hours-block.md) — can use an ignition sensor as its data source.
