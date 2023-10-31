The purpose of firewalls.
A firewall1,2 (from the English firewall3) is software and/or hardware used to enforce the network security policy, which defines what types of communications are authorized on this computer network. It monitors and controls applications and data flows (packets).
The SSL certificate is used to encrypt traffic between web servers and the external network to prevent man-in-the-middle (MITM) attacks and network sniffers from detecting traffic, which could expose valuable information. SSL certificates guarantee confidentiality, integrity and identification.
HTTPS is HTTP with TLS encryption. HTTPS uses TLS (SSL) to encrypt normal HTTP requests and responses, making it safer and more secure. A website that uses HTTPS has https:// at the beginning of its URL.
The purpose of customer monitoring.
Monitoring clients are used to monitor servers and the external network. They analyze server performance and operations, measure overall health, and alert administrators if servers are not performing as expected. The monitoring tool observes servers and provides administrators with key metrics about server operations. It automatically tests server accessibility, measures response time, and alerts for errors like corrupted/missing files, security vulnerabilities/violations, and many other issues.
Problems with this infrastructure
Terminating SSL at the load balancer would leave traffic between the load balancer and the web servers unencrypted.
Having a MySQL server is a problem because it is not scalable and can serve as a single point of failure for web infrastructure.
Having servers with all the same components would force the components to compete for server resources such as CPU, memory, I/O, etc., which can lead to poor performance and also make it difficult to locate the source of the problem. A setup like this is not easily scalable.
