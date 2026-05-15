# Blocking Tariff Plan - Billing Question

**Question:** If a device is placed under a blocking tariff plan, will it still be billed? Is it possible to view or retrieve historical data?

**Answer:**\
Once a device is assigned to a blocking tariff plan, it will no longer be billable for future billing cycles, provided the blocking plan was applied before the beginning of the new cycle/month.

At the moment the blocking tariff is applied, the platform will stop processing new incoming data for that device. However, all previously stored historical data will remain secure and accessible for review.

Please note that if the device transmitted data to the platform during the current billing cycle before being moved to the blocking tariff plan, the device may still be billed for that period.

**Steps to Configure a Blocking Tariff Plan**

1. Create a new blocking tariff plan.
2. Configure the billing cycle and assign a high tariff value if required for administrative purposes.
3. Complete the remaining tariff plan settings.
4. Set the allowed number of units/devices.
   * If the number of allowed units is set to 0, no devices will be able to operate under that tariff plan.
5. Assign the device(s) to the blocking tariff plan.

**Important Considerations**

If the tariff plan uses a monthly billing cycle, the change may not apply immediately, since devices will remain under the current plan until the billing cycle is completed.

For immediate blocking, we recommend either:

* Creating a **daily blocking tariff plan.**
* Contacting Support so the device plan can be updated manually.

Links: [Blocking Tariff plan](https://navixy.com/docs/admin/plans/suspending-service-for-a-device)
