# No livestreaming video on the platform (JC261)

### Question

Why is my JC261 camera not livestreaming?

### Answer

There are two main possible root causes for the lack of live streaming on the platform:

1.  **RSERVICE configuration**

    Make sure the camera is configured with the correct RSERVICE command for live streaming:

    `RSERVICE,rtmp.x-gpsmail.com:1935/encoder`

    If the server is not set correctly, the customer will not be able to view the live stream.
2.  **SIM / data plan / connectivity**

    Even when it may look like a platform issue, poor signal strength or an insufficient SIM card data plan can prevent the camera from uploading the stream with the required quality.

    We recommend checking the SIM plan and verifying that the connection is stable and working properly.
