---
description: Detect unauthorized movement of a parked vehicle with the device's motion sensor, and report a tow event after the ignition switches off.
---

# Tow detection block

## Purpose

**Tow detection** detects **unauthorized movement** of a parked vehicle using the device's built-in motion sensor. After the ignition is switched off, the sensor arms and monitors for vibration, impact, or movement; if detected, the device sends an event to the platform, which can notify you via [Rules and notifications](../../events-and-notifications/security/unauthorized-movement.md).

![](../../../.gitbook/assets/image-20240815-214358.png)

## Settings

* **Enable / disable** — turn tow detection on or off.
* **Sensitivity** — motion-sensor sensitivity (e.g. high / medium / low; lower = less sensitive).
* **Delay after engine off** — how long after ignition-off before detection arms.
* **False-alarm (fake-tow) delay** — a short delay that filters out brief movements so they don't trigger a false tow event.

## Appears when

Appears on devices that support tow detection (vendor variants exist — e.g. Queclink, Teltonika).

## Gotchas

* Set sensitivity carefully to avoid false alarms; accuracy depends heavily on correct installation and varies by model.
* This is device-side detection. It's related to, but distinct from, the platform-side [Unauthorized movement](../../events-and-notifications/security/unauthorized-movement.md) rule and the other [anti-theft and security](../device-specific-controls/anti-theft-and-security.md) modes.

## See also

* [Anti-theft and security](../device-specific-controls/anti-theft-and-security.md) — other device-side alarm modes.
* [Unauthorized movement](../../events-and-notifications/security/unauthorized-movement.md) — the platform rule for movement alerts.
