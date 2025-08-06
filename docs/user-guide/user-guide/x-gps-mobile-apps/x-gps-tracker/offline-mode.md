# Offline mode

The X-GPS Tracker has the ability to send a Check-In or Form during a task, even when the device is not connected to the Internet.\
Employees can finish their tasks without having to worry about good GSM connection. Files and forms will be uploaded as soon as connection restores.

### Enabling Offline mode

To enable Offline mode, go to the application settings, the advanced settings tab and toggle the "Offline mode" toggle switch (disabled by default).

![image-20250304-170633.png](attachments/image-20250304-170633.png)

### Offline mode performance details

1. If there is no network connection, data gets placed into a queue. As soon as the network is restored, the application will start uploading files to the server.
2. If the files could not be transferred after reconnection, files will be deleted from the queue and will not be sent.
3. If a photo/file in Check-In or Form could not be uploaded, Check-in or Form will be removed from the queue and will not be sent, and as a result, the task may not be completed.
4. If the user's file storage runs out of space when transferring files and the "Automatically delete files" option is not enabled, the files will not be sent to the server, Check-Ins will not be saved and the tasks will not be executed.

> \[!INFO] If Check-In or Form has been declined by the server or removed from the queue, the notification "Check-In on \[date and time] has been declined" will be shown in the notification bar.
