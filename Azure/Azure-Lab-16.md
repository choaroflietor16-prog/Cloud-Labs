# Azure Lab 16

## Objective
Create an Azure Load Balancer to distribute traffic across virtual machines.

## Commands Used
az network public-ip create --name LoadBalancerIP --resource-group MyResourceGroup --sku Standard --location eastus
az network lb create --name MyLoadBalancer --resource-group MyResourceGroup --sku Standard --public-ip-address LoadBalancerIP --frontend-ip-name MyFrontEnd --backend-pool-name MyBackEndPool
az network lb probe create --name MyHealthProbe --resource-group MyResourceGroup --lb-name MyLoadBalancer --protocol Http --port 80 --path /
az network lb rule create --name MyLBRule --resource-group MyResourceGroup --lb-name MyLoadBalancer --protocol Tcp --frontend-port 80 --backend-port 80 --frontend-ip-name MyFrontEnd --backend-pool-name MyBackEndPool --probe-name MyHealthProbe
az network nic ip-config address-pool add --address-pool MyBackEndPool --ip-config-name ipconfigMyVM --nic-name MyVMVMNic --resource-group MyResourceGroup --lb-name MyLoadBalancer

## Result
Load Balancer successfully created and VM added to backend pool.
Traffic on port 80 distributed through the Load Balancer.