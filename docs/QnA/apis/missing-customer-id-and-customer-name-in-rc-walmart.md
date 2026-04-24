# Missing Customer ID and Customer Name in RC-Walmart

**Question: Why are the Customer ID and Customer Name not appearing in Walmart?**\
Answer: A likely reason is that both devices are configured with the same External ID. When an External ID is duplicated, it can create conflicts in Walmart’s system, which typically expects a unique identifier per device. As a result, the platform may overwrite or misassociate incoming data, preventing fields like Customer ID and Customer Name from being displayed correctly. Assigning a unique External ID to each device ensures proper data mapping and visibility.

**Reference:** [Waltmart RC blogpost](https://www.navixy.com/es/blog/ayudando-a-transportistas-logisticos-a-cumplir-con-el-cumplimiento-de-recurso-confiable-de-walmart-superando-desafios-de-transmision-de-datos)

