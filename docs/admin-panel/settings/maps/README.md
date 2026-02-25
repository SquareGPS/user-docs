---
description: >-
  Choose which maps users can access, set the default map view, and configure
  GIS providers, including Google Maps.
---

# Map preferences

This page describes the **Maps preferences** page of Admin panel settings. It consists of two parts: [Available maps](./#how-to-select-maps) and [Map default settings](./#default-map-view).

<figure><img src="../../.gitbook/assets/image (38).png" alt="Map preferences page"><figcaption><p>Map preferences page</p></figcaption></figure>

## Cartography in Navixy

To make GPS data easy to understand, the Navixy GPS-tracking platform utilizes digital maps and Geographic Information Services (GIS).

* **Maps** enable users to identify their current location, view the location of events recorded in reports (such as fuel filling or draining), and see where specific events occurred (like pressing the SOS button).
* **GIS** provides additional information such as the exact address of a current location, estimated time and length for building routes, taking into account streets and traffic, and street view in any selected area. It is an essential feature for efficient fleet management and helps businesses make informed decisions.

## Making maps available to your users

To enhance the user experience of your service, you have the option to set default list of maps, map center point, and scale that will be used when logging into the platform for the first time. This allows for a more customized and streamlined experience for your users.

### How to select maps

You can define the list of available maps for your users by checking the boxes the **Available maps** block. To add maps that are commonly used in your region, please contact our Customer Success team.

### Default map view

By setting the default map view, map center location and map zoom parameter, you can improve experience for your users when they log into the platform for the first time. These settings will be applied both to web interface and mobile apps.

Please note that the map position stays where the user last left it. The default settings only apply on the first login or after clearing cookies.

## Using different maps and GIS with Navixy

With Navixy, you are free to choose from a variety of licensed maps and GIS services, including Geocoding, Street View, Directions, Distance Matrix, and more. Your preferences may vary depending on your region and local demand. Here are just a few of the popular available options:

* Google Maps
* OpenStreetMaps
* Bing Maps
* Mapbox
* Yandex Maps

### Adding Google Maps to your service

Google Maps services remain one of the most popular choices for premium maps and GIS worldwide. If you're interested in using Google Maps services with Navixy, you have two options available to you:

1. Activate Navixy's **Premium GIS** package (recommended)
2. Provide your Google Maps license key

#### **How to activate Navixy Premium GIS**

To activate and upgrade to the Navixy Premium GIS Package, simply contact our customer success team. This package includes not only fully licensed Google Maps services, but also advanced GIS services from Navixy including a set of additional licensed maps, algorithms for routing and distance calculation, LBS/Cell-ID databases. Our team will guide you through the process and ensure a smooth upgrade experience, so you can start taking advantage of all the benefits that come with the Premium GIS Package.

#### **How to use your own map license form Google**

If you prefer using the license purchased from Google, you can integrate Google Maps and its API with Navixy. Simply provide our team with the necessary information, and we'll take care of the rest. To learn how to create a key, see [Set up the Geocoding API](https://developers.google.com/maps/documentation/geocoding/get-api-key) page on Google's website. Once you've created the key, send it to Navixy's technical support team along with your domain name information. For security purposes, we recommend creating two Google API keys and restricting them as follows:

* Google API key #1: Restrict it to the following APIs: Google Maps JavaScript API and Google Street View Image API.
* Google API key #2: Restrict it to the following APIs: Google Maps Geocoding API, Google Maps Geolocation API, and Google Maps Directions API.

Please note that if you change your domain name, you will need to create new keys and provide our team with the updated information. This will ensure that your maps and API continue to function properly with Navixy.

#### Adding other Maps and GIS

Activating additional Maps and GIS services with Navixy is a straightforward process. Just follow these steps:

1. Contact our customer success team to learn about the available options for additional maps and GIS services.
2. Select the services you want to activate and let our team know which ones you've chosen.
3. Our team will provide you with the necessary instructions and help you activate the services.
4. Once activated, you can start using the new maps and GIS services right away.

For more information about deploying your own tile server, see [Map tile servers](https://docs.navixy.com/on-premise/custom-maps).

Please note that maps and GIS services that you deploy locally or in the cloud may require separate licenses or paid subscriptions. Our team will help you navigate this process and ensure that you have everything you need to take full advantage of Navixy's offers.
