# 0x19-postmortem

## Issue Summary

On February 8, 2023, at 10:00 AM EAT, our website experienced an outage that lasted for 2 hours. During the outage, our website was unavailable to users. The outage was caused by a failure in our load balancer.

## Timeline

10:00 AM EAT: Our monitoring system detected that our website was unavailable.
10:05 AM EAT: Our engineers began investigating the issue.
10:15 AM EAT: Our engineers determined that the issue was caused by a failure in our load balancer.
10:30 AM EAT: Our engineers began working to restore our website.
12:00 PM EAT: Our website was restored.

## Root Cause and Resolution

The root cause of the outage was a failure in our load balancer. The load balancer is a device that distributes traffic across multiple servers. When the load balancer failed, it caused all of the traffic to be routed to a single server. This caused the server to become overloaded and unavailable.

![image link](https://blog.pearltrees.com/wp-content/2009/03/interruption1.png)

The issue was resolved by restarting the load balancer. Once the load balancer was restarted, it began distributing traffic across all of the servers again.

## Corrective and Preventative Measures

To prevent future outages, we have taken the following corrective and preventative measures:

We have implemented a new load balancer that is more reliable.
We have increased the capacity of our servers.
We have implemented a new monitoring system that will alert us to potential issues sooner.
