# Device statuses

Each device in the Navixy platform has a specific status that indicates its current condition. These statuses change based on the duration of time that elapses.

| **Status**                                                                                               | **Default time limit** | **Description**                                                                                                   |
| -------------------------------------------------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------------------------------------------------------------- |
| ![browser\_lrla4GLmVP.png](../../on-premise/on-premise/configuration/attachments/browser_lrla4GLmVP.png) | N/A                    | Data is constantly being received from a device and contains valid coordinates                                    |
| ![browser\_qJjb9CyZAT.png](../../on-premise/on-premise/configuration/attachments/browser_qJjb9CyZAT.png) | 5 minutes              | No valid location data for more than 5 minutes or the device is transmitting data in a time zone other than UTC+0 |
| ![browser\_CHEecmH3nB.png](../../on-premise/on-premise/configuration/attachments/browser_CHEecmH3nB.png) | 10 minutes             | The device does not send any data packets for over set time period                                                |

### Adjusting Timeout Settings

If needed, timeouts in On-Premise instances can be adjusted by modifying the "tcp-server" configuration file. The configuration file is located at the following path

* on Linux: `/home/java/tcp-server/conf/config.properties`
* on Windows: `C:\java\tcp-server\conf\config.properties`

To adjust the timeouts, open the "tcp-server" configuration file for editing and add the following lines:

```
timers.idleTimeout=10m
timers.offlineTimeout=15m
```

In the above example, the timeout value for "GPS not updated" status is set to 10 minutes, while the timeout value for "Offline" status is set to 15 minutes. You can specify any values you need, but make sure to set the first timeout value to be less than the second one. Also, note that it is mandatory to add the letter "m" after the specified timeout value, which means minutes.

After specifying the timeout values, save the configuration file and restart the "tcp-server" to apply the changes.

With these adjustments, the timeout settings can be customized to suit users' needs and ensure optimal device performance on the Navixy platform.
