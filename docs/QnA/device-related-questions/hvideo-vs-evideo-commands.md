# HVIDEO vs EVIDEO commands

### Question

What are the differences between HVIDEO and EVIDEO commands (JC400/JC261)?

### Answer

Both commands are used to request video files from the server. Meaning, when you search for a specific video clip, either command can be used to retrieve it.

However, the key difference is where the video is sourced from:

* **HVIDEO** retrieves the video from the camera’s **sub-stream**, which is encoded at a lower quality. Additionally, due to recent firmware updates (FW + 1.6.3), the number of days available through the sub-stream has been reduced.
* **EVIDEO** extracts the video **directly from the SD card**, which provides higher video quality but may require more data consumption during upload.

In summary, **HVIDEO** offers faster, lower-quality retrieval from the sub-stream, while **EVIDEO** provides higher-quality footage directly from the SD card at the cost of increased data usage.
