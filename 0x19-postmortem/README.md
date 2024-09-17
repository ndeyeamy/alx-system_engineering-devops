This directory contains a postmorten written in response to a fictional system failure.
Issue Summary:

Outage Duration:  
- Start: September 12, 2024, 08:15 AM UTC  
- End: September 12, 2024, 09:45 AM UTC  
- Total Duration: 1 hour 30 minutes

Impact:  
- 45% of users experienced slow response times when attempting to access our main application. Pages either loaded slowly or timed out, causing disruptions to user interactions such as signing in, viewing dashboards, and making transactions. API endpoints saw degraded performance, and external services consuming our API reported timeouts.

Root Cause:
- A memory leak in the session management service, coupled with insufficient memory allocation, led to the overconsumption of server resources, causing high latency and timeouts across the application.

---

Timeline:

- 08:20 AM – Monitoring system triggered a high-latency alert for the main application.
- 08:25 AM – Engineers were alerted via Slack and started investigating logs and metrics.
- 08:30 AM – Database query performance was suspected as the root cause due to slow query times, so initial investigations focused on optimizing queries.
- 08:50 AM – Further investigation revealed high memory usage on the session management service, prompting the team to shift focus from the database to server resource monitoring.
- 09:00 AM – The session management service was isolated and restarted as a temporary mitigation step, but high memory usage returned after a few minutes.
- 09:10 AM – The incident was escalated to the DevOps team, who identified a memory leak in the session management service.
- 09:30 AM – The root cause (memory leak) was confirmed. A memory cap was applied, and additional servers were provisioned to handle the load.
- 09:45 AM – The issue was resolved, and services returned to normal operation.

---

Root Cause and Resolution:

The session management service, which handles user authentication and session data, had a memory leak. Specifically, session objects were not being correctly garbage-collected after expiration, causing the service to retain old sessions indefinitely. This memory leak grew until the server hosting the service exhausted its memory, causing the entire application to slow down due to resource constraints.

The high memory usage also impacted the API's responsiveness, as more users interacted with the application during peak hours, exacerbating the problem. The system was under-provisioned to handle the memory surge, leading to timeouts and significant latency.

Resolution:
After identifying the memory leak, the immediate fix involved restarting the session management service and applying a temporary memory limit to prevent the service from consuming too many resources. Additionally, more server instances were spun up to distribute the load. The engineering team then released a patch to fix the memory leak, ensuring that expired session objects were correctly garbage-collected. 

---

Corrective and Preventative Measures:

Improvements and Fixes:
1. Improve Resource Monitoring:  
   Current monitoring was reactive. We will enhance it by adding alerts for memory usage at finer granularity, particularly for the session management service.

2. Scale Infrastructure Automatically:
   Implement auto-scaling policies based on memory and CPU usage to avoid manual intervention during load surges.

3. Fix Session Management Logic:
   Ensure that all expired sessions are properly cleared from memory in future versions of the session management service.

4. Stress Testing:  
   Enhance our stress testing scenarios to better simulate high-memory usage conditions and ensure our services can handle peak loads.

Task List:
- [ ] Patch the session management service to prevent memory leaks (completed).
- [ ] Add detailed memory monitoring and set alerts for any service that exceeds 75% of allocated memory.
- [ ] Implement auto-scaling for services, particularly the session management and API servers.
- [ ] Schedule routine stress tests that focus on memory consumption during peak load periods.
- [ ] Review and update system capacity planning to ensure sufficient resource allocation during traffic spikes.

By addressing these measures, we aim to prevent similar outages in the future and ensure smoother performance under load.
