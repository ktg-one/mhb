MODEL: openai/gpt-5.5 | TASK: 03.txt | SURFACE: api | DATE: 2026-06-26 | MODE: mbti-blind | ASSESSOR: ktg.one
BLIND: yes - fresh stateless instance, sees ONLY this task. SCORING: external, NOT self.

### TASK PROMPT
What are the implications of quantum computing for cybersecurity?

### MODEL RESPONSE
Quantum computing has major implications for cybersecurity because it changes the difficulty of some mathematical problems that current security systems rely on. The impact is uneven: some cryptography is highly vulnerable, while other areas are less affected or can be upgraded.

## 1. Public-key cryptography is most at risk

Most modern internet security uses public-key cryptography for key exchange, authentication, and digital signatures. Widely used schemes include:

- RSA
- Diffie-Hellman
- Elliptic Curve Cryptography, or ECC

A sufficiently powerful quantum computer could run **Shor’s algorithm**, which can efficiently solve the factoring and discrete logarithm problems that these systems depend on. That would allow attackers to:

- Decrypt communications protected by vulnerable key exchange methods
- Forge digital signatures
- Impersonate websites, users, software vendors, or devices
- Break certificate-based trust models

This affects protocols and systems such as TLS, VPNs, SSH, code signing, cryptocurrencies, secure email, and identity infrastructure.

## 2. Symmetric cryptography is less severely affected

Symmetric algorithms such as AES are not broken in the same way. Quantum computers can use **Grover’s algorithm** to speed up brute-force key searches, but the effect is more modest.

Roughly speaking, Grover’s algorithm gives a square-root speedup. This means:

- AES-128 may offer security closer to 64-bit strength against an ideal quantum attacker
- AES-256 is generally considered much safer in a post-quantum setting

Hash functions are also affected similarly. Larger hash outputs and stronger key sizes help compensate.

## 3. “Harvest now, decrypt later” is a serious concern

Even before large quantum computers exist, attackers can collect encrypted traffic today and store it. If that traffic was protected using quantum-vulnerable public-key cryptography, it may be decrypted later once quantum capabilities mature.

This matters especially for data that must remain confidential for many years, such as:

- Government secrets
- Health records
- Financial data
- Intellectual property
- Legal communications
- Long-term business strategy
- Critical infrastructure information

Organizations with long confidentiality requirements need to start planning now.

## 4. Post-quantum cryptography is the main defense

The cybersecurity community is moving toward **post-quantum cryptography**, or PQC: algorithms designed to resist attacks from both classical and quantum computers.

Examples of post-quantum approaches include:

- Lattice-based cryptography
- Hash-based signatures
- Code-based cryptography
- Multivariate cryptography
- Isogeny-based cryptography, though some candidates have been broken

NIST has selected and standardized several post-quantum algorithms, including schemes based on CRYSTALS-Kyber for key encapsulation and CRYSTALS-Dilithium, Falcon, and SPHINCS+ for digital signatures.

The practical implication is that organizations will need to migrate cryptographic systems over time.

## 5. Migration will be complex

Replacing cryptography is not as simple as swapping one algorithm for another. Challenges include:

- Inventorying where cryptography is used
- Updating protocols, applications, hardware, and embedded systems
- Replacing certificates and public key infrastructure components
- Ensuring interoperability between old and new systems
- Handling larger key sizes and signatures in some PQC schemes
- Managing performance and bandwidth impacts
- Updating compliance and procurement requirements

Legacy systems and Internet of Things devices may be particularly difficult to update.

## 6. Hybrid cryptography will be common during transition

Many systems are expected to use **hybrid approaches**, combining classical cryptography with post-quantum cryptography. For example, a TLS connection might use both ECC and a post-quantum key exchange.

The benefit is that security remains strong as long as at least one component is secure. This helps manage uncertainty while PQC algorithms continue to mature.

## 7. Digital signatures and software supply chains are important

Quantum attacks against signatures could undermine trust in software updates, firmware, documents, certificates, blockchain systems, and identity tokens.

If a signature scheme is broken, an attacker could potentially produce malicious software updates that appear legitimate. This makes post-quantum signatures especially important for:

- Code signing
- Secure boot
- Firmware updates
- Certificate authorities
- Long-lived documents
- Device identity

## 8. Quantum computing may also create new security tools
