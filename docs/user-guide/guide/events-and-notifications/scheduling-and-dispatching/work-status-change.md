# Work status change

## Overview

The "Work status change" rule is designed to monitor and track the real-time activities of mobile employees using the X-GPS Tracker app. This rule alerts on employees updating their current status, such as indicating when they are available for a new task or when they have started a new activity.

When the "Work status" rule is active, any changes in an employee’s status will trigger immediate notifications via SMS, email, or pop-up alerts in the User Interface. This functionality ensures that supervisors and dispatchers remain informed about their team’s current activities and availability, enabling better coordination and task management.

## Rule settings

#### Work statuses

Define the specific work statuses that will trigger notifications when selected by employees. Users can choose which statuses to monitor, ensuring that the system only alerts on the most relevant status updates. These statuses are created and assigned through the "Working statuses" widget in the Devices and Settings menu.

For common settings, please refer to [Rules and Notifications](../).

## System operation details

* This rule is specifically designed for use with X-GPS Tracker-enabled devices, meaning that only these devices can be selected as sources for monitoring work status changes.
* The list of work statuses that trigger this rule may vary depending on the custom lists assigned to different trackers. If you modify the list of devices bound to the rule and this alters the list of associated work statuses, the rule will include both the old and new statuses. However, the newly added statuses from the updated list will be unselected by default. You can edit the rule to include these new statuses.
* Unlike many other rules, the "Work status" rule does not have a reset timer, allowing for immediate notification of any status changes.

This setup helps organizations maintain clear communication and effective task management by keeping the team updated on each member’s current work status.
