# Azure Lab 11

## Objective
Create a custom HTML page and serve it via Nginx on MyVM.

## Commands Used
ssh azureuser@138.91.117.164
sudo nano /var/www/html/index.html
sudo systemctl restart nginx

## Result
Custom HTML page successfully served from MyVM at http://138.91.117.164
Page displays: "Welcome to Choaro's Azure VM!"