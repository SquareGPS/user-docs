# Why my tracker shows LBS location even I've disabled LBS

### Question

Why my tracker shows LBS location even I've disabled LBS

![](<../.gitbook/assets/Unknown image (103)>)

### Answer

Check the update time for this LBS location in the location widget. Most likely this LBS location was saved before you disabled LBS detection and the tracker didn’t provide any GPS points to the platform after it. All LBS starting from the moment of LBS detection saved to 0 meters are filtered.
