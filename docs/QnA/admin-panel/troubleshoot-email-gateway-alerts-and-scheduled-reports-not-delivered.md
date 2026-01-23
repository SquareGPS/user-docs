# Troubleshoot email gateway (alerts and scheduled reports not delivered)

### Question

How can I troubleshoot when no emails are being received (alerts, scheduled reports)?

### Answer

To troubleshoot, send a test email while the browser DevTools is open.

1. Admin Panel → Account management → Email gateways.
2. Open DevTools (F12) → Network tab.
3. Clear the Network tab call history (optional, but makes the next steps easier).
4. Click **Send test email**.
5. Find the `send_email` network request.
6. Check the **Response**.

If successful, you should see `success:true`.

If you see an error, it usually points to wrong SMTP credentials or server settings.

Screenshots from the original workflow:

![](<../.gitbook/assets/Unknown image (138)>)

![](<../.gitbook/assets/Unknown image (139)>)

![](<../.gitbook/assets/Unknown image (140)>)

Successful response example:

![](<../.gitbook/assets/Unknown image (141)>)

Also check spam and allow up to **5 minutes** for delivery.

If you performed the steps above and still can’t identify why emails are not being delivered, contact Support.
