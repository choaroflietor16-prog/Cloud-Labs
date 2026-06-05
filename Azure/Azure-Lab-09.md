# Azure Lab 09

## Objective
Start the deallocated Virtual Machine and reconnect via SSH.

## Commands Used
az vm start --name MyVM --resource-group MyResourceGroup
az vm show --name MyVM --resource-group MyResourceGroup --query powerState
ssh azureuser@138.91.117.164

## Result
VM successfully started and SSH connection established.