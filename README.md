ZeroMQ Publisher-Subscriber for CSV Data
========================================

This repository contains a Python implementation of a ZeroMQ publisher-subscriber pattern for streaming data from a CSV file over a network.

Features
--------

-   Publishes data from a CSV file using ZeroMQ.
-   Allows subscribers to connect and receive data in real-time.
-   Configurable to work over local networks and the internet.

Requirements
------------

-   Python 3.6 or higher
-   ZeroMQ library (pyzmq)
-   Pandas library

Installation
------------

1.  Clone the repository by running the following commands in your terminal:

    git clone <https://github.com/yourusername/ZeroMQ_Publisher_Subscriber.git> cd ZeroMQ_Publisher_Subscriber

2.  Install the required Python packages by running the following command:

    pip install zmq pandas

Usage
-----

### Publisher

1.  Modify the publisher script:

    Update the `csv_file_path` with the path to your CSV file and set the `internal_ip` to the internal IP address of your publisher laptop.

    Example modifications in publisher.py:

    Set the path to your CSV file as: csv_file_path = 'path/to/your/data.csv'

    Set the internal IP address of the publisher laptop as: internal_ip = "192.168.1.x" (Replace with your actual internal IP)

2.  Run the publisher script by executing:

    python publisher.py

### Subscriber

1.  Modify the subscriber script:

    Update the `public_ip` with the public IP address of the publisher laptop.

    Example modifications in subscriber.py:

    Set the public IP address of the publisher laptop as: public_ip = "39.33.241.27" (Use your actual public IP address)

2.  Run the subscriber script by executing:

    python subscriber.py

Configuration
-------------

### Firewall and Port Forwarding

-   Ensure the firewall on the publisher laptop allows incoming connections on port 5555.
-   Set up port forwarding on the router of the publisher laptop to forward traffic on port 5555 to the internal IP address of the publisher laptop.

### Testing Locally

-   To test the setup on a local network, use the internal IP addresses of the publisher and subscriber laptops.
