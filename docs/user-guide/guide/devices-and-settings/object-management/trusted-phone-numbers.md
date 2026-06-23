---
description: Control which phone numbers may send SMS and USSD commands to a GPS device, protecting it from unauthorized configuration. Up to five numbers.
---

# Trusted phone numbers

## Purpose

**Trusted phone numbers** are the numbers allowed to send **SMS/USSD commands** to the device. Restricting command sources protects the device from unauthorized configuration or control. This setting is part of the device's general object settings.

<!-- SCREENSHOT: Object settings, Trusted phone numbers field (multi-entry). Annotate: add/remove number control, the 5-number limit. -->

## Settings

* **Trusted numbers**: A list of phone numbers permitted to send commands to the device. Add up to **5 numbers**. Each entry is validated as a phone number.

## Appears when

Available for devices on accounts where the trusted-numbers feature is enabled, and only for non-blocked devices.

## Gotchas

* The limit is **5 numbers** per device.
* Trusted numbers can be **copied to many devices at once**, along with label, group, and tags.
* This controls **who may command the device by SMS/USSD**: It does not change how the device reports (see [Tracking mode](../location-and-movement/tracking-mode-block.md)) or its SIM settings (see [Phone number block](phone-number-block.md)).

## See also

* [Phone number block](phone-number-block.md), the device's SIM and APN settings.
* [Object label block](object-label-block.md), label, group, and tags.
