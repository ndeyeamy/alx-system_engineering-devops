What is a server.
A computer server offers services accessible via a network. It can be hardware or software, it is a computer which executes operations following requests made by another computer called a “client”.

The role of the domain name.
According to www.wikipedia.org, the purpose of a domain name is to remember and easily communicate the address of a set of servers (website, email, FTP). For example, wikipedia.org is easier to remember than 208.80.154.224 or 91.198.174.1921.

The DNS record type www is in www.foobar.com.
www.foobar.com uses an A record. This can be verified by running dig www.foobar.com.
Note: Results may be different, but for the infrastructure of this design, an A record is used.
Address mapping record (A record), also called a DNS host record, stores a host name and its corresponding IPv4 address.

The role of the web server.
The web server is software/hardware that accepts requests over HTTP or Secure HTTP (HTTPS) and responds with the content of the requested resource or an error message.

The role of the application server.
Install, operate and host applications and related services for end users, IT departments and organizations and facilitate the hosting and delivery of high-end consumer or business applications.

The role of the database.
Maintain a collection of organized information that can be easily accessed, managed and updated

What the server uses to communicate with the client (user's computer requesting the website).
Communication between the client and the server takes place over the Internet via the TCP/IP protocol suite.

Problems with this infrastructure
There are several SPOFs (Single Point Of Failure) in this infrastructure.
For example, if the MySQL database server is down, the entire site will be down.
