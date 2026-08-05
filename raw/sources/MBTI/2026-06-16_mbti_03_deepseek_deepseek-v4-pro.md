MODEL: deepseek/deepseek-v4-pro | TASK: 03.txt | SURFACE: api | DATE: 2026-06-16 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
What are the implications of quantum computing for cybersecurity?

### MODEL RESPONSE
Quantum computing's implications for cybersecurity are profound and disruptive. It acts as a double-edged sword: it will catastrophically break much of our current digital security infrastructure while simultaneously enabling new, theoretically unbreakable methods of defense.

The implications can be divided into two main areas: the immense threat and the emerging opportunity.

---

### 1. The Threat: A Cryptographic Apocalypse

The most significant and immediate implication is that a sufficiently powerful quantum computer will render most of today's public-key cryptography obsolete. This is not a theoretical concern; it's a "when, not if" scenario.

#### The Core Problem: Shor's Algorithm

In 1994, mathematician Peter Shor developed an algorithm that a quantum computer can run to efficiently solve two mathematical problems that underpin virtually all modern internet security:

- **Prime Factorization:** The difficulty of factoring a large number into its prime components.
- **The Discrete Logarithm Problem:** The difficulty of solving certain types of logarithms in finite groups.

**The systems at immediate, total risk:**

| Cryptographic System | Used For | Quantum Vulnerability |
| :--- | :--- | :--- |
| **RSA (Rivest–Shamir–Adleman)** | SSL/TLS certificates, digital signatures, email encryption. | Broken completely by Shor's algorithm. |
| **ECC (Elliptic Curve Cryptography)** | Modern websites, mobile devices, cryptocurrencies (e.g., Bitcoin), Signal/WhatsApp messaging. | Broken completely by Shor's algorithm. |
| **Diffie-Hellman (DH/ECDH)** | Key exchange protocols to establish secure sessions (TLS handshake). | Broken completely by Shor's algorithm. |
| **DSA/ECDSA** | Digital signatures for software distribution, code signing, blockchain transactions. | Broken completely by Shor's algorithm. |

The consequence of breaking these is a total loss of confidentiality, integrity, and authenticity for the digital world. An attacker with a Cryptographically Relevant Quantum Computer (CRQC) could:
- **Decrypt any recorded TLS traffic**, exposing banking details, passwords, corporate secrets, and state secrets.
- **Forge digital signatures**, allowing them to impersonate anyone, push malicious software updates, and authorize fraudulent blockchain transactions.
- **Undermine trust** in the entire internet, as the fundamental mechanisms for secure communication would cease to function.

#### The "Harvest Now, Decrypt Later" (HNDL) Threat

This is an active and current threat. Sophisticated state-level adversaries are believed to be intercepting and storing massive amounts of encrypted internet traffic today. They cannot decrypt it now, but they are banking on the arrival of a CRQC in the next 10-20 years. When that happens, they will retroactively decrypt data that remains valuable, such as long-lived government secrets, industrial blueprints, or personal health records. Any data that needs to remain secret for decades is already at risk.

#### Impact on Symmetric Cryptography: Grover's Algorithm

Symmetric cryptography (like AES) used for bulk data encryption is not broken in the same catastrophic way. Grover's algorithm provides a quadratic speedup for brute-force searching. The implication is simple: **double the key size**.
- AES-128 will offer the security equivalent of
