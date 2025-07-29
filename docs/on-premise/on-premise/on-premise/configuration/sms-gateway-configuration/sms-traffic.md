# SMS Traffic

[SMS traffic](https://www.smstraffic.ru/en/) is a well-known telecommunications company based in Russia, and is particularly well-suited for messaging in Russia and Kazakhstan.

## Navixy JSON configuration for SMS Traffic

```
 provider: smstraffic
 type: transceiver
 params:
 {
 "login": <login>, //login to SMS Traffic
 "password":<password>, //password to SMS Traffic
 "urls": <array of URLs>, //e.g. ["https://www.smstraffic.ru/multi.php", "https://www2.smstraffic.ru/multi.php"]
 "override_originator": null //allows replacing sender's phone number, null means no override
 }
```

For example, here is an SQL query that can be used to add a new SMS gateway to the **'sms\_gates'** table in the **'google'** database:

```
INSERT INTO google.sms_gates (type, provider, params, enabled, class_filter) VALUES ('transceiver', 'smstraffic', '{"login":"$LOGIN", "password":"$PASSWD","urls": ["https://www.smstraffic.ru/multi.php"]}', 1, '*');
```

To use the SQL query above, simply replace the placeholders '`$LOGIN`' and '`$PASSWD`' with your own login and password credentials.

Enabling an SMS gateway requires an additional SQL query, which can be executed separately to update the 'enabled' parameter for the desired gateway in the 'sms\_gates' table of the 'google' database:

```
UPDATE google.dealers SET master_phone="$SMS_FROM", from_sms="$SMS_FROM" WHERE dealer_id=1;
```

## Inbound messages

The SMS Traffic gateway can process inbound messages without requiring any additional settings.