# Connection setup

This guide explains how to connect to your Cloud Data Warehouse instance, which is built on **Neon PostgreSQL**.

## Connection parameters

When your Cloud Data Warehouse instance is set up, you'll receive these connection parameters via email:

|                   |                                      |
| ----------------- | ------------------------------------ |
| **Parameter**     | Description                          |
| **Host**          | The database server address          |
| **Port**          | The connection port (typically 5432) |
| **Database name** | Your assigned database name          |
| **Username**      | Your database username               |
| **Password**      | Your secure database password        |
| **SSL mode**      | The SSL connection mode              |

## Data architecture

Your Cloud Data Warehouse organizes data in specific schemas:

* **raw\_business\_data** - Contains business data tables (users, objects, tasks, etc.)
* **raw\_telematics\_data** - Contains telematics data from client devices (GPS tracks, sensor readings)

{% hint style="info" %}
When querying data, you must specify both the schema (`raw_business_data`) and table (`objects`) name: `SELECT * FROM raw_business_data.objects LIMIT 10;`
{% endhint %}

## PostgreSQL compatibility

The Cloud Data Warehouse is fully compatible with the PostgreSQL protocol. You can connect using:

* Standard PostgreSQL clients (pgAdmin, DBeaver, etc.)
* Programming languages with PostgreSQL drivers (Python, Java, Node.js)
* Business intelligence tools that support PostgreSQL (Tableau, Power BI)

## Connection string format

For programmatic access, use the standard PostgreSQL connection string format:

```sql
postgresql://username:password@host:port/database?sslmode=ssl_mode
```

Example with placeholders:

{% code overflow="wrap" %}
```sql
postgresql://client_user:your_password@db.example.cloud:5432/client_123_dwh?sslmode=require
```
{% endcode %}

## Connection security

Important security considerations:

* **SSL encryption** - Your data transmission is encrypted according to the specified SSL mode
* **Network configuration** - Your network must allow outbound connections to the provided host and port
* **Credential safety** - Your connection credentials are unique to your instance and should be kept secure

### Best practices for connections

When working with your Cloud Data Warehouse:

* **Manage idle connections** - Close connections when not in use to free up resources
* **Use connection pooling** - For applications with frequent database access
* **Store credentials securely** - Never hardcode credentials in scripts or applications
* **Set appropriate timeouts** - Configure reasonable connection timeouts for your use case

## Connection troubleshooting

If you encounter connection issues:

1. Verify your connection parameters match those in your welcome email
2. Confirm your network allows the connection to the specified host and port
3. Ensure your client supports the required SSL mode

## Next steps

After establishing a connection, proceed to the Schema overview section to learn about the available data structures and tables.
