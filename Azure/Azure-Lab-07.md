# Azure Lab 07

## Objective
Create a Virtual Machine (VM) inside MyVNet and MySubnet in Azure using the CLI.

## Commands Used
az vm create --name MyVM --resource-group MyResourceGroup --location eastus --image Canonical:ubuntu-24_04-lts:server-arm64:latest --vnet-name MyVNet --subnet MySubnet --admin-username azureuser --generate-ssh-keys --size Standard_B2pls_v2

## Result
Virtual Machine successfully created inside MyResourceGroup.
Successfully SSHed into VM from MacBook.
Public IP: 138.91.117.164
Private IP: 10.0.1.4 (inside MySubnet)
Note: Required quota increase request and ARM64 compatible image.
Virtual Machine successfully created inside MyResourceGroup.
Successfully SSHed into VM from MacBook.
Public IP: 138.91.117.164
Private IP: 10.0.1.4 (inside MySubnet)
Note: Required quota increase request and ARM64 compatible image.