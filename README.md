# 🔐 HTTP vs HTTPS: Wireshark & Simulation-Based Comparison

## 📌 Overview
This project explores and compares HTTP and HTTPS protocols using real-world tools like **Wireshark**, **Cisco Packet Tracer**, and a **local server demo**. We highlight the security risks of HTTP and how HTTPS protects sensitive data like usernames and passwords during transmission.

---

## 📚 Table of Contents
- [1. Theory: HTTP vs HTTPS](#1-theory-http-vs-https)
- [2. Wireshark Demo – HTTP](#2-wireshark-demo--http)
- [3. Wireshark Demo – HTTPS](#3-wireshark-demo--https)
- [4. Cisco Packet Tracer Simulation](#4-cisco-packet-tracer-simulation)
- [5. Local HTTPS Server Demo](#5-local-https-server-demo)
- [6. Conclusion](#6-conclusion)
- [7. References](#7-references)

---

## 1. Theory: HTTP vs HTTPS

| Feature               | HTTP                          | HTTPS                             |
|----------------------|-------------------------------|------------------------------------|
| Protocol             | HyperText Transfer Protocol   | HyperText Transfer Protocol Secure |
| Port                 | 80                            | 443                                |
| Encryption           | ❌ None                       | ✅ TLS/SSL encryption              |
| Authentication       | ❌ No                         | ✅ Certificate-based               |
| Data Visibility      | ✅ Plaintext in transit       | ❌ Encrypted end-to-end            |

---

## 2. Wireshark Demo – HTTP

### 🎯 Objective
Demonstrate how HTTP POST data (like usernames and passwords) can be intercepted and read using Wireshark.

### 🛠 Tools Used
- Python HTTP server
- HTML login form
- Wireshark

### 🔍 Details
Submitted:
- username=hello123
- password=thisisapassword


### 📸 Screenshot  
> ![image](https://github.com/user-attachments/assets/2d3db346-68b9-456d-ba81-8a364abc2adf)


### 🧠 Analysis
HTTP transmits data in plaintext. Any attacker with access to the network (or a packet capture) can easily read sensitive information like login credentials.

---

## 3. Wireshark Demo – HTTPS

### 🎯 Objective
Show that HTTPS encrypts traffic, preventing attackers from reading POST data.

### 🛠 Tools Used
- Python HTTPS server with self-signed certificate
- Wireshark

### 🔐 What You See in Wireshark
- TLS Handshake
- `Encrypted Application Data` instead of visible POST content

### 📸 Screenshot  
> ![image](https://github.com/user-attachments/assets/c59d9246-f2fa-4657-9ed6-2b089b8c9ff0)

### 🧠 Analysis
The same login form is used, but the data is encrypted. Wireshark cannot show the username or password, proving HTTPS prevents sniffing attacks.

---

## 4. Cisco Packet Tracer Simulation

### 🎯 Objective
Simulate how HTTP and HTTPS behave in a network environment.

### 🛠 Setup
- Devices: PC, Switch, Web Server, DNS Server
- Protocols: HTTP and symbolic HTTPS
- Ports: 80 (HTTP), 443 (HTTPS)

### 📸 Screenshots  
- HTTP server:
![image](https://github.com/user-attachments/assets/4fed20b2-0c76-4c9d-b2c4-252e8ac7f5b4)



- HTTPS setup:
![image](https://github.com/user-attachments/assets/76892746-a22c-4078-ba1d-d09d196483a9)

### 🧠 Notes
Cisco Packet Tracer doesn't simulate real TLS encryption, but it allows you to show protocol differences and port usage visually.

---

## 5. Local HTTPS Server Demo

### 🎯 Objective
Run a secure HTTPS server locally using Python and a self-signed SSL certificate to demonstrate encrypted traffic.

### 🛠 Steps
1. Generate certificate:
```bash
openssl req -new -x509 -keyout cert.key -out cert.pem -days 365 -nodes
```

2. Run Python script:
```bash
python secure_server.py
```

3. Open in browser:
```
https://localhost:4443
```

Self-certifcate warning:
![image](https://github.com/user-attachments/assets/c4b0d46d-dc74-4d2e-a82f-854669dbbb5a)

Wireshark TLS traffic:
![image](https://github.com/user-attachments/assets/1cbd1f31-3542-4107-90fd-be3caafec55c)

### 🧠 Outcome
Data submitted via HTTPS is not readable in Wireshark. The form and credentials are protected by encryption—even with a self-signed certificate.

---
# 6. Conclusion
-  HTTP is insecure: Anyone can intercept and read data.
-  HTTPS is essential: It encrypts data and validates server identity.
-  Wireshark clearly shows the difference: one is open, the other locked down.
-  Even in basic demos, the security benefits of HTTPS are clear and measurable.
-   _Always use HTTPS for any form-based or sensitive interactions._
---
# 7. References
- 🔗 [Wireshark User Guide](https://www.wireshark.org/docs/)
- 🔗 [Python HTTP Server Docs](https://docs.python.org/3/library/http.server.html)
- 🔗 [TLS 1.3 – RFC 8446](https://datatracker.ietf.org/doc/html/rfc8446)
- 🔗 [HTTP 1.1 – RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616)
- 🔗 [Cisco Packet Tracer](https://www.netacad.com/courses/packet-tracer)
