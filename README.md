
# Bithub Proxy Server

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Limitations](#limitations)
4. [Technologies Used](#technologies-used)
5. [Usage](#usage)
6. [Resources](#resources)
7. [License](#license)

## Introduction

This Proxy Server is a powerful tool designed to facilitate seamless HTTP request handling and caching for users and administrators alike. By providing complete and fail-proof parsing of request and response headers, it ensures compatibility with a wide range of HTTP versions. Users can send HTTP requests directly from their browsers without the need for client-side applications. With features such as persistent disk caching, an efficient LRU caching algorithm, and a user-friendly graphical interface, this Proxy Server enhances performance and usability. Additionally, it offers secure admin account authentication and robust control over server operations, making it an essential resource for managing web traffic effectively.


## Features

- **Complete and Fail-Proof Parsing**: 
  - Parses request and response headers into dedicated Request and Response header objects.
  - Supports a wide range of header fields found in both modern and legacy HTTP requests with their correct corresponding types.
  - Facilitates easier reception and manipulation of various forms of requests and responses.

- **Direct HTTP Request Sending**: 
  - Allows users to send HTTP requests directly from browsers without the need for a client-side application.

- **Persistent Disk Caching**: 
  - Caches data directly onto the computer disk, persisting the cache between proxy sessions.

- **Efficient Caching Algorithm**: 
  - Implements the Least Recently Used (LRU) caching algorithm using a minimum-heap and a dictionary for optimized performance.

- **Admin Account Authentication**: 
  - Requires administrators to create an account and authenticate their sign-in using a secure hashing system for security.

- **Proxy Server Control**: 
  - Allows admins to run and terminate the proxy server without needing terminal or command line interference.

- **File Type Handling**: 
  - Capable of handling various file types, including HTML, GIF, CSS, and any binary object.

- **Cache Control Management**: 
  - Manages cache control directives such as `no-cache` and `no-store`.

- **Reception Type Handling**: 
  - Handles different reception types including chunked transfers, content-length specified transfers, and default timeout cases.

- **Graphical User Interface (GUI)**: 
  - Features a user-friendly graphical interface that displays all required and additional information.
 
## Limitations
  - A maximum of 50 global concurrent connections at a time.
  - A maximum of 5 connections per host at a time.
  - Supports up to 10 hosts using the server simultaneously.

## Technologies Used

- **Python**: Version 3.11
- **Libraries**: 
  - `tkinter` and `customtkinter` for GUI
  - `os`, `time`, `datetime`, `socket`, `threading`, `pickle` for core functionality

## Usage

Run the proxy server and access it through your web browser to handle requests.

## Resources

- [Validating URLs in Python](https://scribe.rip/@miguendes/how-to-check-if-a-string-is-a-valid-url-in-python-fb0584aab549)
- [Creating Directories in Python](https://note.nkmk.me/en/python-os-mkdir-makedirs/)
- [Modifying File Timestamps](https://www.tutorialspoint.com/python/os_utime.htm)
- [Grouping Constants in Python](https://stackoverflow.com/questions/29792189/grouping-constants-in-python)
- [Implementing Min-Heap in Python](https://www.geeksforgeeks.org/min-heap-in-python/)
- [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/)
- [Python Socket Programming](https://builtin.com/data-science/python-socket)
- [MDN Web Docs - HTTP Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)

## License

This project is licensed under the MIT License.
