# Azure Lab 10

## Objective
Install and run a web server (Nginx) on MyVM.

## Commands Used
ssh azureuser@138.91.117.164
sudo apt update
sudo apt install nginx -y
sudo systemctl start nginx
sudo systemctl status nginx

## Result
Nginx web server successfully installed and running on MyVM.
Successfully served webpage from http://138.91.117.164
NSG attached to network interface to allow HTTP traffic.
