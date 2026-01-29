# Send data from a non-integrated device (Navixy Generic Protocol)

### Question

How can I send data to the platform from a non-integrated device?

### Answer

If your specific device isn’t integrated on our platform, you are able to use our Navixy Generic Protocol to do so. This is a universal protocol allowing you to send the specific data you need to our platform without waiting or paying for the costs associated with device integration. Once you have your device data, you will need to "convert" it to our accepted JSON format as shown in our documentation. Then all you have to do is send the data over HTTP/HTTPS to our platform and your device data will display.

The minimum required JSON is like so:

| { "message\_time": "...", "device\_id": "..." } |
| ----------------------------------------------- |

### Links

* [Navixy Generic Protocol](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-generic-protocol)
* [Message structure and attributes](https://app.gitbook.com/s/tx3J5BxnWyPV0nP2xr0z/technologies/navixy-generic-protocol/navixy-generic-protocol-10/message-structure-and-attributes)
