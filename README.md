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
