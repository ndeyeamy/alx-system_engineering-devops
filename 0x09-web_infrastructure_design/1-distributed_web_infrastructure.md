The load balancer (HAproxy):
The HAProxy load balancer is configured with the Round Robin distribution algorithm. A round robin is an arrangement of choosing all elements of a group equally in a rational order, usually from the top to the bottom of a list, then starting again at the top of the list and so on.
The configuration enabled by the load balancer.
The HAProxy load balancer allows an active-passive configuration rather than an active-active configuration. In an active-passive configuration, not all nodes will be active (able to receive workloads at any time). In the case of two nodes for example, if the first node is already active, the second node must be passive or on standby. The second or subsequent passive node can become an active node if the previous node is inactive.
How a primary-replica (master-slave) database cluster works.
A primary replica configuration configures one server to act as the primary server and the other server to act as a replica of the primary server. However, the primary server is capable of performing read/write requests while the replica server is only capable of performing read requests. Data is synchronized between the primary and replica servers each time the primary server performs a write operation.
The difference between the master node and the replication node with respect to the application.
The primary node is responsible for all write operations that the site requires while the replication node is able to handle read operations, decreasing read traffic to the primary node.
Problems with this infrastructure
There are several SPOF (Single Point Of Failure).
For example, if the main MySQL database server is down, the entire site will not be able to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the main database server are also SPOFs.
Security issues.
Data transmitted over the network is not encrypted using an SSL certificate so that hackers can spy on the network. There is no way to block unauthorized IP addresses since there is no firewall installed on any server.
No surveillance.
We have no way of knowing the status of each server since they are not monitored
