# Missing Customer ID and Customer Name in RC-Walmart

**Question: Why are the Customer ID and Customer Name not appearing in Walmart?**

\
**Answer**: The main reason why the Customer ID and Customer Name are not being included in the Walmart retransmission is due to an incorrect configuration of the External ID field.

For this type of integration, it is necessary to follow the standard Recurso Confiable format:\
License Plate | Route ID | Company ID | Company Name

It is important to note that the configuration must follow the Trusted Resource documentation. If only a single number is entered in the External ID field, the system will not be able to transmit all the required information, which results in missing fields such as Customer ID and Customer Name.

<figure><img src="../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

**Links:**&#x20;

[Waltmart RC blogpost](https://www.navixy.com/es/blog/ayudando-a-transportistas-logisticos-a-cumplir-con-el-cumplimiento-de-recurso-confiable-de-walmart-superando-desafios-de-transmision-de-datos)&#x20;

[Recurso Confiable](https://www.navixy.com/docs/user/guide/devices-and-settings/data-forwarding/recurso-confiable)

