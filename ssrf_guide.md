# SSRF

## What is SSRF?

SSRF (Server-Side Request Forgery) is a web application vulnerability that enables attackers to send unauthorized requests from the server to other internal or external systems. SSRF occurs when an application accepts user-supplied input, such as URLs or network requests, and uses it to construct server-side requests without proper validation or authentication.

An attacker can exploit SSRF to send requests to internal or external systems that the application would normally have no access to, potentially leading to data breaches, privilege escalation, or other serious consequences. SSRF attacks are particularly dangerous in cloud environments, where multiple services and resources are interconnected, and attackers can use the vulnerability to move laterally within the infrastructure.

## Example

An example use case of SSRF is a web application that allows users to fetch data from a third-party API by submitting a URL. If the application does not validate or sanitize the user-supplied input, an attacker can inject a malicious URL that points to an internal server or a private network resource, and trigger a server-side request from the application to that resource.

For instance, an attacker can inject a URL like http://192.168.0.10/admin, where 192.168.0.10 is the IP address of an internal server that hosts sensitive data or administrative interfaces. The application will process this URL and send a request to the internal server, potentially revealing sensitive data or allowing the attacker to take control of the system.

A real-world example of SSRF occurred in 2018 when a vulnerability was discovered in the Google App Engine (GAE) that allowed attackers to make unauthorized requests to internal Google services. The vulnerability was due to the way GAE handled certain types of URL fetch requests, which could be manipulated by attackers to send requests to Google's internal services, such as Google Cloud Metadata API. This allowed attackers to extract sensitive information, such as access tokens and private keys, and launch further attacks against Google's infrastructure.

The vulnerability was patched by Google, but it highlighted the severity and impact of SSRF vulnerabilities, especially in cloud environments where multiple services and resources are interconnected.