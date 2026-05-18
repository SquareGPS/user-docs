# Why does my tracker show LBS location even though I've disabled LBS?

## Question

Why does my tracker show LBS location even though I've disabled LBS?

![](<../.gitbook/assets/Unknown image (16)>)

## Answer

Check the update time for this device's LBS location in the location block. Most likely, this LBS location was saved before you disabled LBS detection, and the tracker didn't provide any GPS points to the platform afterward. All LBS locations starting from the moment the LBS detection is set to 0 meters are filtered.
