---
description: Extend battery life on GPS devices by configuring sleep and power-save conditions and charging modes. Available controls vary by model.
---

# Device power management

## Purpose

For battery-powered devices, these blocks control **how the device sleeps to save power** and **how its battery charges**. Proper power management extends battery life on assets that aren't continuously powered, at the cost of less frequent reporting while asleep.

<!-- SCREENSHOT: example Sleep mode block showing sleep conditions and wake-up interval. Annotate: sleep condition toggles, durations, wake-up interval. -->

## Settings

The controls you may see, depending on the device:

* **Sleep mode conditions** — choose what puts the device to sleep, such as **ignition off**, **no motion**, or **no communication**, with **durations** before light and deep sleep engage and **wake-up intervals** that determine how often the device wakes to report.
* **Light vs deep sleep** — some models distinguish a light sleep (radios partly on) from deep sleep (radios off), sometimes triggered by **voltage thresholds**.
* **Battery charge mode** — control when the backup battery charges, e.g. **on demand**, **only when ignition is on**, or **when ignition is on or charge is low**.

{% hint style="info" %}
Power-save behavior overlaps with the power-save options in [Tracking mode](../location-and-movement/tracking-mode-block.md). On some models the two are configured together; document and tune them as a pair.
{% endhint %}

## Appears when

Appears on battery-powered or power-managed device models that expose sleep or charging controls.

## Gotchas

* Aggressive sleep settings reduce reporting frequency — a device in deep sleep may appear to report rarely or show as not updated. Balance battery life against the tracking detail you need.
* Wake-up intervals and sleep conditions interact with the offline-timeout in [Connection state](../connectivity/connection-state-block.md): set the timeout long enough that a sleeping device isn't shown offline prematurely.

## See also

* [Tracking mode block](../location-and-movement/tracking-mode-block.md) — reporting intervals and power-save modes.
* [Connection state block](../connectivity/connection-state-block.md) — offline-timeout threshold.
