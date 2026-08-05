MODEL: qwen/qwen3.7-max | TASK: 03.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
What are the implications of quantum computing for cybersecurity?

### MODEL RESPONSE
The implications of quantum computing for cybersecurity represent a fundamental paradigm shift, often described as a double-edged sword: it poses an **existential threat** to current encryption standards while simultaneously offering **revolutionary defensive capabilities**.

Here is a detailed breakdown of the implications across three key dimensions:

### 1. The Threat: Breaking Current Cryptography
The most immediate concern is that fault-tolerant quantum computers will render many of today’s public-key infrastructure (PKI) algorithms obsolete.

*   **Asymmetric Encryption Collapse**: Algorithms like **RSA**, **ECC** (Elliptic Curve Cryptography), and **Diffie-Hellman** rely on the mathematical difficulty of factoring large prime numbers or solving discrete logarithm problems. Shor’s algorithm, when run on a sufficiently powerful quantum computer, can solve these problems exponentially faster than classical computers, effectively breaking the trust model of the internet (TLS/SSL, digital signatures, PKI).
*   **Symmetric Encryption Weakening**: Algorithms like **AES** are not broken but are weakened. Grover’s algorithm provides a quadratic speedup for searching unstructured databases, effectively halving the security level. For example, AES-256 would offer the security equivalent of AES-128 against a quantum attack. This is manageable by simply doubling key sizes, unlike the total breakage of asymmetric crypto.
*   **"Harvest Now, Decrypt Later" (HNDL)**: Adversaries may be intercepting and storing encrypted traffic *today* with the intention of decrypting it once quantum hardware matures. This makes long-term data secrecy (e.g., state secrets, medical records, intellectual property) immediately vulnerable, even before a cryptographically relevant quantum computer (CRQC) exists.

### 2. The Defense: Post-Quantum Cryptography (PQC) & Quantum Tech
Cybersecurity is not just a victim of quantum computing; it is also a beneficiary.

*   **Post-Quantum Cryptography (PQC)**: These are new classical algorithms designed to be resistant to both classical and quantum attacks. They rely on mathematical problems believed to be hard for quantum computers, such as:
    *   **Lattice-based cryptography** (e.g., CRYSTALS-Kyber, CRYSTALS-Dilithium)
    *   **Code-based** and **Hash-based** cryptography
    *   *Note*: NIST has already standardized several PQC algorithms, and migration is currently underway across government and industry.
*   **Quantum Key Distribution (QKD)**: This uses the principles of quantum mechanics (specifically the no-cloning theorem and observer effect) to distribute encryption keys. Any attempt to eavesdrop on the key exchange disturbs the quantum state, revealing the intrusion instantly. While currently limited by distance and infrastructure costs, it offers information-theoretic security.
*   **Quantum Random Number Generation (QRNG)**: Classical RNGs are often pseudo-random and predictable. QRNGs leverage inherent quantum indeterminacy to generate truly random numbers, strengthening the foundation of cryptographic key generation.

### 3. Strategic and Operational Implications
The transition to a quantum-safe world requires immediate strategic action:

*   **Crypto-Agility**: Organizations must design systems that allow cryptographic algorithms to be swapped out easily without overhauling entire infrastructures. Hard-coded crypto is a major liability.
*   **Inventory and Risk Assessment**: You cannot protect what you don't know. Organizations need a comprehensive inventory of where cryptography is used, what data has a long shelf life (vulnerable to HNDL), and which vendors support PQC.
*   **Regulatory Compliance**: Governments are beginning to mandate PQC migration (e.g., US CNSA 2.0, EU regulations). Early adopters will face fewer compliance shocks later.
*   **Supply Chain Risk**: The transition depends on hardware vendors, cloud providers, and software libraries updating their stacks. A delay in any link of the chain creates a vulnerability.

### Summary
| Aspect | Classical Era | Quantum Era Implication |
| :--- | :--- | :--- |
| **Public Key Crypto** | Secure (RSA, ECC) | **Broken** (requires PQC replacement) |
| **Symmetric Crypto** | Secure (AES-128/256) |
