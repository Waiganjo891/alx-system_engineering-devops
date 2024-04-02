Web stack debugging
Filename: 0-nginx_likes_port_80
Task
Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.
Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
Write a Bash script that configures a server to the above requirements

Filename: 1-debugging_made_short
Task
Your Bash script must be 5 lines long or less
There must be a new line at the end of the file
You must respect usual Bash script requirements
You cannot use ;
You cannot use &&
You cannot use wget
You cannot execute your previous answer file (Do not include the name of the previous script in this one)
service (init) must say that nginx is not running ← for real
