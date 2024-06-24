# POSTMORTEM
By storyafrika System Admin and Develop team,

Earlier this week users were unable to visit our web servers as most of our servers were down.

The following is an incident report on the outage that occurred on the 29 may 2024, detailing the root cause, the resolution and preventions to mitigate the outage from happening.

The root cause
From 7:15 pm to 8:45 pm users were trying to access storyafrika.com and all its routes, which returned 503 service unavailable messages. Users were unable to access the site, and at its peak other applications were unable to access it api. The root cause was due to a miss configuration of our load balancer as it was routing traffic to a small set of servers to a particular data center, instead of routing the traffic to all servers in all the data centers. Since traffic increased rapidly and servers were small this led to traffic congestion and thus servers failing gradully. 

Timeline ( all time WAT)
April 1 2024(during dev) - load balancer configure (push to production)
7:15 - first server failed
7:15 - monitoring alerts
7:20 - acknowledges alert
7:22 - system was completely down (503)
7:40 - correct configuration of load balancer
7:45 - server restarts
8:00 - 100% traffic back online

Root cause
During development, there was a mis-configuration of the load balancer which passed testing directly to production. The load balancer was configured to route traffic to a specific block of servers in a particular data center; this was deliberate as the software was in production and no thought was taken as to whether the software will scale automatically to huge amounts of traffic as it is the case now. As a result of increased traffic, the available servers could not handle the request anymore as memory usage exceeded their capabalities, leading to the first server crashing at 7:15 PM and eventually all servers were down, resulting in service outage at exactly 7:22 PM.

Resolution and recovery
At exactly 7:15 PM when the server crashed, the monitoring system alerted our engineers who then started working on the issue at 7:20 PM, 2 minutes later all systems were completed down.

After minutes of frustration in finding the issue and looking at log files and inspecting a few of our servers we found out that servers were receiving way more requests than they can handle. So we looked at our load balancer configuration and noticed that the issue was from there. At 7:40 PM correct configuration was made to use the right algorithm for routing traffic and making all our servers visible.

It took some time for our configuration to reflect and we gradually restart the servers at 7:45 PM.
By 7:51PM all servers were up and 100% traffic was restored and routed to all servers.

Corrective and preventive measures
We have completed an intensive and immersive review and analysis on the service outage in the last 3 days. We have concluded on taking the following actions to prevent further outage.
Ensuring that testing is not skipped
Keeping track of deliberate action that may not work in production and change it before pushing
Change debugging to be quicker and faster
Develop mechanism for acknowledge incident alert quickly
Developing with a view of scaling

storyafrika is committed to keep you locked to inspiring african story, we appreciate your patience and again apologize for any impact this may have caused.

sincerely,

Storyafrika Sysadmin and Development team
