---
description: Store name and phone contacts on a GPS device for SMS commands and alerts. The maximum number of entries depends on the device model.
---

# Phonebook and authorized numbers

## Purpose

The **phone book** stores **name + phone** contacts **on the device** so it can send SMS alerts to, or accept commands from, known numbers. This is configured on the device itself, separate from the platform-side [Trusted phone numbers](../object-management/trusted-phone-numbers.md) setting.

<!-- SCREENSHOT: Phone book block — table of name/phone entries with add/edit/remove. Annotate: Name column, Phone column, add button. -->

## Settings

* **Contacts** — a list of entries, each with a **Name** and a **Phone** number. Add, edit, and remove entries as needed.
* **SMS channel usage** *(some models)* — controls how the device uses its SMS channel, for example a low-battery alert mode.

## Appears when

Appears on devices that maintain an on-device phonebook. The **maximum number of entries depends on the model** — for example, around 3 contacts on some models and up to 20 on others.

## Gotchas

* This phonebook lives **on the device**; it is distinct from platform-side [Trusted phone numbers](../object-management/trusted-phone-numbers.md), which control who may command the device by SMS/USSD.
* The entry limit is model-specific.

## See also

* [Trusted phone numbers](../object-management/trusted-phone-numbers.md) — platform-side list of numbers allowed to command the device.
* [Buttons and keys](buttons-and-keys.md) — map buttons to the numbers they call.
