---
description: Map a device's SOS and call buttons to phone numbers, control the power-off key, and set digital unlock passwords. Controls vary by model.
---

# Buttons and keys

## Purpose

These blocks map a device's **physical buttons** to actions and control **access keys** — for example, what an SOS press does, which numbers a call button dials, and time-limited unlock codes. They appear only on hardware that has the relevant buttons or key features, and the exact fields vary by model.

<!-- SCREENSHOT: example Buttons & keys block (e.g. SOS button action) showing mode options and phone field. Annotate: action mode selector, phone number entry. -->

## Settings

The controls you may see, depending on the device:

* **SOS button action** — choose what an SOS press does: **send an alert only**, or **make a call to a phone number and send an alert**. When calling is enabled, you set the phone number to dial.
* **Call buttons** — map one or more device buttons (Button #1, #2, …) to phone numbers that are called or alerted when pressed.
* **Switch-off (power-off) button** — enable or disable the device's physical power-off button.
* **Unlocking / digital password** — set a password and use it to unlock the device.
* **Temporary digital password** — issue a **time-limited** unlock code (the validity window is set in minutes, e.g. roughly 10–255 minutes depending on the model).

{% hint style="info" %}
Exact controls depend on your device. A given model shows only the buttons and keys it physically supports, with vendor-specific labels.
{% endhint %}

## Appears when

Appears only on devices whose hardware exposes the corresponding buttons or access-key features.

## Gotchas

* Button-to-phone mappings are stored **on the device**; the number of entries a button supports varies by model.
* A **temporary** password expires automatically when its validity window ends; a standard digital password does not.

## See also

* [Anti-theft and security](anti-theft-and-security.md) — guard and alarm modes that buttons often pair with.
* [Phonebook and authorized numbers](phonebook-authorized-numbers.md) — store the contacts buttons can call.
