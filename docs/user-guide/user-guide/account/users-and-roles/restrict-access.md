# Restrict Access

Navixy enables organizations to effectively manage access to user-created information, including GPS devices and associated artifacts such as geofences, places, and notification rules. This capability is vital for maintaining data security and operational efficiency, especially in organizations with multiple divisions or business units. This approach ensures that:

* Sensitive information is protected from unauthorized access
* Users can focus on the data and tools relevant to their roles
* Operational efficiency is maintained across different divisions and business units

This document outlines how GPS devices and information created by users are secured and shared with other employees within the organization.

## GPS Devices

When a user adds a GPS device, it is effectively created under the Owner’s account, so even after the user is deleted, the GPS device remains in the organization’s account. The Owner can specify which users can view GPS device data, such as trips or sensor data, ensuring that only authorized individuals can view and manage the device.

![image-20240718-040427.png](attachments/image-20240718-040427.png)

## Associated Artifacts

* **Notification Rules**: Notification rules allow users to set up alerts based on various criteria, such as speeding or leaving a geofence. When a user creates a rule, it is effectively created in the Owner’s account. Other users who have access to the relevant device will also be able to see and use these rules.
* **Places and Geofences**: Users can create Places and Geofences to define specific areas of interest. While these artifacts are managed by the user who created them, they are effectively linked to the Owner’s account. The Owner can grant access to these geofences to other users within the organization. Only users with the appropriate permissions can view and modify these geofences.
