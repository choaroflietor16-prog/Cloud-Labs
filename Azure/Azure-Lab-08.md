# Azure Lab 08

## Objective
Stop and deallocate the Virtual Machine to preserve free credits.

## Commands Used
az vm deallocate --name MyVM --resource-group MyResourceGroup
az vm show --name MyVM --resource-group MyResourceGroup --query powerState

## Result
VM successfully deallocated and stopped.