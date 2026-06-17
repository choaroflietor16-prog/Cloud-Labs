# Azure Lab 13

## Objective
Set up Azure Monitor and create an alert rule for the Virtual Machine.

## Commands Used
az monitor metrics list --resource /subscriptions/0a7c337f-19f9-4b44-8f0c-da333a436896/resourceGroups/MyResourceGroup/providers/Microsoft.Compute/virtualMachines/MyVM --metric "Percentage CPU" --output table
az monitor action-group create --name MyActionGroup --resource-group MyResourceGroup --short-name MyAG
az monitor metrics alert create --name HighCPUAlert --resource-group MyResourceGroup --scopes /subscriptions/0a7c337f-19f9-4b44-8f0c-da333a436896/resourceGroups/MyResourceGroup/providers/Microsoft.Compute/virtualMachines/MyVM --condition "avg Percentage CPU > 80" --action MyActionGroup --description "Alert when CPU exceeds 80%"

## Result
Azure Monitor alert successfully created for MyVM.
Alert triggers when CPU usage exceeds 80%.