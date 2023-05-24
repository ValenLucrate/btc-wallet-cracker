# btc-wallet-cracker

The software works in 2 steps:

1. address and key generation
1) First of all, we will have to start with a private ECDSA key (basically any series of 32 bytes) and this will be our private key
2) Next we will have to generate an uncompressed public key from the private key that we have
3) Next we have to compressed our uncompressed public key
4) Perform SHA-256 hashing on the compressed public key
5) Perform RIPMED-160 hashing on the result of SHA-256
6) Add version byte in front of RIPEMD-160 hash (0x00 for Main Network)
7) Perform SHA-256 hash on the extended RIPEMD-160 result (Below steps are called Base58Check encoding)
8) Perform SHA-256 hash on the result of the previous SHA-256 hash
9) Take the first 4 bytes of the second SHA-256 hash, this is the address checksum
10) Add the 4 checksum bytes from stage 8 at the end of extended RIPEMD-160 hash from stage 5, this is the 25-byte binary Bitcoin Address
11) Convert the result from a byte string into a base58 string using Base58Check encoding, this is the most commonly used Bitcoin Address format

Now we have address and private key.

2. checking the balance
By running a bitcoin node on our servers, we can perform a straightforward query to retrieve information about the address. This enables us to determine whether the address has a balance. If it does, the software saves the address and private key in wif-format to a text file. With this information, you can log in to the wallet and withdraw the btc.
