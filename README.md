# Core Systems Lab

This repository is my personal engineering lab for exploring **core system concepts**, **data structures**, and **performance-oriented design**.
Each sub-project focuses on implementing fundamental components from scratch - to deeply understand how things work at a low level, and to experiment with small-scale infrastructure and system-oriented projects.

Topics covered include:
* System Infrastructure and performance benchmarking
* Algorithms and design patterns
* Concurrency primitives and synchronization

---

### Distributed Drone Analyzer (gRPC - C++ & Python)

A **cross-language microservice demo** showing how distributed systems can communicate efficiently between C++ and Python using **gRPC**.

It simulates a **DroneManager** written in C++ that manages a fleet of drones and sends image data to a **Python ImageAnalyzer** service, which returns mock object detection results.

**Highlights:**

* Cross-language communication (C++ ↔ Python) using gRPC and Protocol Buffers  
* Binary and type-safe data transfer over HTTP/2 (faster than JSON / XML)  
* Simple `.proto` contract defining request and response messages  
* Demonstrates distributed design, structured APIs, and clean separation of roles  
* Practical example of service interoperability and real-time data exchange

For full details, setup instructions, and example output, see:  
[`gRPC-distributed-drone/README.md`](./gRPC-distributed-drone/README.md)

---

### Featured Project: Custom Dict (HashMap)

A fully functional **hash-based dictionary** implementation written from scratch in Python.  
It features:

* Linear probing for collision handling  
* Dynamic resizing when load factor exceeds 0.66  
* Lazy deletion via a dedicated `_Deleted` marker  
* Full support for key-value operations (`get`, `set`, `pop`, `update`, `clear`, etc.)

Includes a **benchmark tool** comparing its performance to Python’s built-in `dict`, showing identical average-case complexity (O(1)) while offering an inside view of how hash tables work under the hood.

For details, see:  
[`custom-hash-dictionary-implementation/README.md`](./custom-hash-dictionary-implementation/README.md)

---

### Featured Project: Custom Set (HashSet)

A fully functional **hash-based set** implementation written from scratch in Python.
It includes:

* Linear probing collision resolution
* Dynamic resizing based on load factor
* Lazy deletion using a DELETED marker
* Full support for mathematical set operations and operator overloads

The project also includes a **benchmark tool** comparing its performance to Python’s built-in `set`, demonstrating identical average-case complexity (O(1)) and providing a deeper look into hash table mechanics.

For details, see:
[`custom-hash-set-implementation/README.md`](./custom-hash-set-implementation/README.md)

---

### Bank Queue Manager (C++)

A compact, **production-minded C++ demo** that models a realistic bank counter queue system.
This project demonstrates practical engineering decisions around **ownership**, **polymorphism**, **deterministic scheduling**, and **efficient cancellation semantics** - all implemented in clean, interview-friendly code.

**Overview:**
`BankQueueManager` simulates a queue where clients (Regular / VIP / Business) submit service requests such as deposits, withdrawals, checks, and transfers.
It uses:

* A polymorphic action model (`IServiceAction`)
* Smart ownership with `std::unique_ptr` ("SMRT PTR")
* A `std::set` ordered by a domain-specific comparator ensuring deterministic priority and FIFO order
* Efficient cancellation by storing iterators from `set::insert`, reducing removals to **O(log n)**

For full details, see:
[`bank-queue-manager/README.md`](./bank-queue-manager/README.md)

---

*(Additional projects will be added over time as I continue expanding this lab.)*
