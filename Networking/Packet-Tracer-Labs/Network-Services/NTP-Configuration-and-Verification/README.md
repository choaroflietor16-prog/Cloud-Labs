# NTP Configuration and Verification

This Cisco Packet Tracer activity covers using Network Time Protocol (NTP) to synchronise network device clocks. Consistent timestamps help correlate events across devices during troubleshooting.

## Open the lab

Download [the Packet Tracer activity](NTP-Configuration-and-Verification.pka) and open it in Cisco Packet Tracer. Use the activity instructions to identify the NTP source and the devices that need to synchronise.

## Verify synchronisation

On Cisco IOS devices that support them, use:

```text
show clock detail
show ntp associations
show ntp status
```

Check that each client has a reachable NTP source and reports a synchronised clock. If it does not synchronise, verify IP reachability and the configured NTP server address, then allow time for the association to establish.
