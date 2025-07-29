# Configuring Eye Sensor on Teltonika Tracker

The integration of advanced sensors and GPS trackers has become essential for businesses aiming to enhance their operational efficiency and security. Teltonika's Eye Sensor can significantly improve monitoring and data collection capabilities. This article serves as a comprehensive guide for partners who wish to configure these devices for their customers.

By following the step-by-step instructions provided, you will learn how to download and use the Teltonika Eye App, configure the Eye Sensor, and integrate it with Teltonika's GPS trackers and Navixy data retrieval system. Whether you are a seasoned professional or new to these technologies, this guide will ensure a smooth and efficient setup process.

Let's get started on configuring your Teltonika Eye Sensors to maximize their potential for your business needs in 3 steps.

- [1\. Configuration with Mobile APP - Teltonika´s Eye APP](#1-configuration-with-mobile-app-teltonikas-eye-app)
- [2\. Conficugation with Teltonika device configuration for desktop](#2-conficugation-with-teltonika-device-configuration-for-desktop)
- [3\. Setting up an Eye Sensor on Navixy](#3-setting-up-an-eye-sensor-on-navixy)

## 1\. Configuration with Mobile APP - Teltonika´s Eye APP 

Download Teltonika´s Eye App from the Google Store or App Store.

![image-20240819-201555.png](attachments/image-20240819-201555.png)

Get into the Eye Application and turn on Bluetooth. Your mobile device will start scanning any Eye Sensor device around the cellphone. Every device will show the decibels and the distances from the cellphone to the sensors. Select the Eye sensor, which shows the active sensors on the screen, then PIN the code, if it is the first time configuring it, the PIN would be 123456.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdktHNEsaH-N2tmPvi2NXJTp28Y6_L2vs3aQB3KsEr38JXUSxjS6WSZhfq-vEsz4QaNdrusF-qGXFEoVPX8wr-p_VSNO2KZy5YsihJxPxIhAfOuBXG5XPeC9RrgfuEam3kATRXyjh4Ql_EmEAi3utBWVr0O?key=6KHuR2IBwmomxMottXEmGA)

It is important to update the firmware of the device. In this case, the most updated firmware is 1.2.10.

Click on the *configure* button and change the packet setting to *Sensor*, it will display Eye Sensor, and click the *Save* button.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfmqdUk--23DC7qiVYapJkU-hfAjZISIS06ylcIUC6kVILVPRy983MXLXV0_hxHqUCpJk_rvlKbs5cLZKcJS1kH9np3amHr-ANGntbSpVx97rSYw48Xrn1PNvOZC4l4635w3NJIxUKjMAs716P2mZ4oe5Iq?key=6KHuR2IBwmomxMottXEmGA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcdlV7i2Y6miCzjVxNShut77230x1_w2jUe8qiVmwsSRVDzsB8mCtkgOHmabquUkdO0FACRk0nmbm-kbaIR5jfTvb0lZzmShRQ5aQOQex5yPhJQAu-QdFkfvugndzNs0Xlqsv9lP979sGjDu_25Alxnxz_3?key=6KHuR2IBwmomxMottXEmGA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXevSXGMbYt5LZoCMLRNEtptpyQzrdbhFxmdCTYmlrQPhdCv40al-na0osyW3OmM-vlH3O3sn9v1FZYRrqe6bYV1Dl-lfLA8Ezg9BBF7FuPBrudUsUT0AJCxZEF9C6LZ8Vivw0ZgPP4q8Ce8kFnCe5lnFBtU?key=6KHuR2IBwmomxMottXEmGA)

After setting up the Eye sensor, click the upper right button to disconnect. Otherwise, it will not send data to the GPS tracker. 

## 2\. Conficugation with Teltonika device configuration for desktop

Before configuring the Eye sensor, check out how to install the Teltonika Configurator, open the tracker file, and understand the full operation of the sensors with Teltonika’s trackers and Navixy data retrieval:

[https://docs.navixy.com/expert-center/configuring-sensors-on-teltonika-trackers](https://docs.navixy.com/expert-center/configuring-sensors-on-teltonika-trackers)

Click on Bluetooth 4.0 in the left menu. Enable the connection setting and increase the length of the radios. On the sensor settings, click on the Eye Sensor, which will be configured with the MAC number. The Eye sensor connection functionalities will be displayed.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeFVcAbvbHZHlG2CmS2dIggXgCLq3v-7kN4dkpG2Pgd_JbQjRPn6TCuDUnG2bUwph_j3Akz3dLDkHdhKNaNqGs12sw_RSTBPvMnOjl6-f_guX-n1bIcGL9J70ora3TmjUB0sKl77FoVY3SU0T8Ga9NvYSK9?key=6KHuR2IBwmomxMottXEmGA)

The working mode would be an Eye sensor. Type the Eye sensor MAC address in the settings. Select the priority level based on the sensor requirement. In this case, temperature, humidity, magnet, movement, and Eye battery will be the data retrieved from the Eye sensor. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWZy2yg2f8XcyLtejhC_Ns2jSOLgVtSdQh_gfk9fPuE86xXl32MDTtBzxcUaX9-JtOfLlKeyB0kPT8uwt75yMC8HFODKYOwumTag7DbCNf1Rte1kIw-lq1bAeqH5VAFZq-SX3xvg7jFxvH5RyZ_-Rd3gK-?key=6KHuR2IBwmomxMottXEmGA)

Once the device is configured on this tab, go to Status/IO Info. Look up the Eye sensor IO’s selected before, it will show the data from the Eye sensor. You can verify the same data by using the Eye APP. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeK5VLSkdzr05nLP5atJRngf8HoypKpeQWjUPB60lJ6Oe13P_DrZyaMlKAVBFNb3vVvFtuGu0JGMKDs1u_GVm7AHBe5EuWaLZ_nr86ZRmnVw7pxTHubTBImaoJU2XRfqdntk-zam3YuFhB0IAxFmbKj1KRk?key=6KHuR2IBwmomxMottXEmGA)

For this GPS tracker, it is possible to connect up to 4 Eye sensors. 

## 3\. Setting up an Eye Sensor on Navixy 

In this particular case, Teltonika has a Data Sending ID document for FMC130 which is going to be useful to link the Eye sensor values to Navixy. 

In the next link, you can find the complete AVL list:

[https://wiki.teltonika-gps.com/view/FMC130\_Teltonika\_Data\_Sending\_Parameters\_ID](https://wiki.teltonika-gps.com/view/FMC130_Teltonika_Data_Sending_Parameters_ID)

Go to *Device and Settings*, select the device, add a measurement sensor on the *sensor and buttons tap*.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeAR3gyNgRkCsLUoIL57jjBR2Yvq39e4QiyYX76r_YEgwv1MteWxK5fGwYPIHZ3lhc7Y3kbfEbWkLna-eAj72Z9anLLy-ut8WIiXWpFaCBylt9ctzSsDJIfciqLQWypDaP5M4JQrnJFqNZWkqDFymAYM84u?key=6KHuR2IBwmomxMottXEmGA)

Add Temperature, humidity, battery, movement, and Eye sensor battery level value. 

Select AVL Input and the Input Number that corresponds based on Teltonika’s Data document previously mentioned.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXddtkOvKD9YV6gEdUFoOh9TMBFpFiFh6JvZJQKBDXiRtwCfESduESiCACrNle9Vn2jsF0qX4z4rHJEkqX_7YXXfauEBDvpqMMIjG6gSLuiXzn6wqVdYVM1jOffXtIOQ-rWK0s5WgvogCT7wG-L8JqHDKxg?key=6KHuR2IBwmomxMottXEmGA)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXduuuJ1jTrwB5NQB2NUzMK5TNegcRXq3uYMqT_VLpONHg9r2wNaCS8O-9Zunx_pOQq3nXxF4bVL7U4SHtvQF7aF6osMEY2GekRj54XJBI5FXsOlhiTlY4cYfw6dKjFeXdvE1-upZYYru51zKyes3pkjmsYL?key=6KHuR2IBwmomxMottXEmGA)

The magnetic sensor will display automatically. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcqoOZT4DbImQQBcVW9mmvG8eydp1NoI3ixsHo7J0F5h5-cmUK2Q2am5VMYbwkV-1FPL9UiMagaugDrBAHXVcl4GnQz9CM42lwcrajoawtXRDSXCOMxvNbpUJtTMSYMvsauhGcfT6VIoRioVn3JUV3Yk0Dt?key=6KHuR2IBwmomxMottXEmGA)

If it does not appear then it must be created as a measurement sensor as the other sensors, using AVL input #10808.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfZ9ZsysD_zXlJjA9R4wE1_CHACqdhYE7yBvpPCjcN7CrYCSoisNbakv1FqCyht8q5oSC4NJfAofjFIejzGmqTiNEyhxoq1exC3zd-wZNmfnBaAxZwgPMt8_bZ4-E0r5UVrIS8puz-nzz1OcX_L5aP0aMfy?key=6KHuR2IBwmomxMottXEmGA)

Remember to set the decimals of the value in *Calibration/Divisor*.