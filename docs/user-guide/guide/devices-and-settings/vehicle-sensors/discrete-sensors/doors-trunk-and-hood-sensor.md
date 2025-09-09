# Doors, trunk, and hood sensor



No special configuration is required. However, several factors need to be considered.

First, not all car models transmit this information via the CAN bus. Unfortunately, you can only learn it by testing or requesting detailed documentation from the manufacturer.

Second, due to some peculiarities of the device's data transfer protocol, you will not be able to track the status of doors, etc., until the system receives the **Open** status at least once. For correct operation, we recommend you leave the trunk, hood, and all doors open for several minutes with the engine running.
