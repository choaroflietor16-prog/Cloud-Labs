# Azure Lab 06

## Objective
Attach the Network Security Group (NSG) to MySubnet.

## Commands Used
az network vnet subnet update --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --network-security-group MyNSG
az network vnet subnet show --name MySubnet --resource-group MyResourceGroup --vnet-name MyVNet --query networkSecurityGroup

## Result
NSG successfully attached to MySubnet.