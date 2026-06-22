---
description: >-
  Device-side anti-theft and security alarms in Navixy: unauthorized movement,
  auto-geofence, no-movement, vibration, impact, and guard modes. Exact controls
  depend on your device model.
---

# Anti-theft and security

## Purpose

These blocks arm the **device itself** to detect tampering, impact, or movement of a parked or guarded vehicle and report events to the platform. They are distinct from — but often paired with — platform-side [Rules](../../events-and-notifications/) such as "Unauthorized movement": these configure detection **on the device**, while rules decide what the platform does with the resulting events.

{% hint style="info" %}
Each control below appears **only on supported hardware**, and the available alarm modes and their fields are vendor-specific. Your device may show a subset under different labels.
{% endhint %}

## What you can configure

The controls you may see, depending on the device:

* **Auto-geofence / unauthorized movement** — when the ignition is off, the device creates a parking zone and reports an event if the vehicle leaves it. You set a **delay after ignition-off** before detection arms and a **radius** for triggering (see below).
* **No-movement alarm** — reports when a device that should be moving stays still (or vice versa), with a timeout and optional pre-alarm.
* **Vibration detection** — uses the device's motion sensor to detect vibration/tampering, with a **sensitivity level** and arm/alarm delays.
* **Impact / accelerometer** — reports a shock above a configured force for a configured duration.
* **Guard / security modes** — vendor "guard" modes that arm sensor and perimeter detection, reporting tampering or displacement.
* **Proximity alarm** — a BLE-based proximity (social-distance) alert on a few models, with a distance and duration threshold.

{% hint style="warning" %}
**Pending product review:** the proximity (social-distance) alarm and some guard/security modes are niche or vendor-specific. Confirm availability and exact behavior for your device with support before relying on them.
{% endhint %}

## Auto-geofence (unauthorized movement)

Auto-geofencing, also known as unauthorized movement detection, is available on many vehicle GPS trackers. When the ignition is off and the device detects coordinates outside a pre-defined auto-geofence zone, it treats the vehicle as leaving its parking area, generates an event, and sends it to the platform, where you can configure notifications.

In the dedicated panel you can:

* **Set the time delay after ignition is switched off** — how long after ignition-off before detection becomes active.
* **Define the radius for triggering** — the distance from the parking location within which movement triggers the event.

![](../../../.gitbook/assets/image-20241118-024806.png)

## Appears when

Appears only on device models whose firmware exposes the corresponding alarm or security mode.

## Gotchas

* Set sensitivity and delays carefully to avoid false alarms; accuracy depends heavily on correct installation and varies by model.
* These device-side alarms are separate from [Tow detection](../location-and-movement/tow-detection-block.md), which is documented as its own block, and from platform-side Rules.

## See also

* [Auto-geofencing](../../events-and-notifications/security/auto-geofencing.md) in Rules and notifications.
* [Tow detection block](../location-and-movement/tow-detection-block.md) — unauthorized-movement detection after engine off.
* [Buttons and keys](buttons-and-keys.md) — SOS buttons and access keys that pair with security modes.
