# Lab 01 — VLAN & Inter-VLAN Routing (Router-on-a-Stick)

## Topology
![Network Topology](topology.png)

## Objective
Design and configure a network with three VLANs and enable communication between them using a single router interface (Router-on-a-Stick).

## Network Design

| VLAN | Name           | Network          | Gateway        |
|------|----------------|------------------|----------------|
| 10   | Administration | 192.168.10.0/24  | 192.168.10.1   |
| 20   | Sales          | 192.168.20.0/24  | 192.168.20.1   |
| 30   | IT             | 192.168.30.0/24  | 192.168.30.1   |

## Devices
- 1 x Cisco 2911 Router
- 1 x Cisco 2960 Switch
- 6 x PCs (2 per VLAN)

## Configuration Summary

### Switch
- VLANs 10, 20, 30 created
- Access ports assigned per VLAN
- Fa0/7 configured as 802.1Q trunk to router

### Router (Router-on-a-Stick)
- G0/0.10 — encapsulation dot1Q 10 — 192.168.10.1
- G0/0.20 — encapsulation dot1Q 20 — 192.168.20.1
- G0/0.30 — encapsulation dot1Q 30 — 192.168.30.1

## Fault Encountered & Diagnosed
Inter-VLAN communication was failing for VLAN 20 and VLAN 30 PCs. Systematic troubleshooting revealed:

- VLANs configured correctly ✅
- Trunk working correctly ✅
- Router subinterfaces up/up ✅
- **Root cause: Default gateways missing on PCs in VLAN 20 and VLAN 30**

Once default gateways were assigned (192.168.20.1 and 192.168.30.1), full inter-VLAN communication was restored.

## Result
✅ All three VLANs communicating successfully through the router.

## Tools Used
Cisco Packet Tracer