import M2Crypto
import base64
import hashlib
import os


class Rsa(object):
    _rsa = None
    _hash_algo = 'sha1'

    def verify(self, data, signature, useBase64=True):
        """Verify a signature

        Keyword arguments:
        data -- The signed data
        signature -- The signature itself
        useBase64 -- When true, the data string is expected to be base64 encoded (default True)
        """
        if useBase64:
            signature = base64.b64decode(signature)
        try:
            self._rsa.verify(data=data, signature=signature, algo=self._hash_algo)
            return True
        except M2Crypto.RSA.RSAError:
            return False

    def sign(self, data, useBase64=True):
        """Sign data with the key

        Keyword arguments:
        data -- The data to be signed
        useBase64 -- If true, the signature is going to be base64 encoded
        """
        x = self._rsa.sign(data, algo=self._hash_algo)
        if useBase64:
            return base64.b64encode(x)
        return x

    def encrypt(self, data, useBase64=True):
        """Encrypt data with the public key

        Keyword arguments:
        data -- The data to be encrypted
        useBase64 -- If true, the return string is going to be base64 encoded
        """
        x = self._rsa.public_encrypt(data, padding=1)
        if useBase64:
            return base64.b64encode(x)
        return x

    def decrypt(self, data, useBase64=True):
        """Decrypt data with the private key

        Keyword arguments:
        data -- The data to be decrypted
        useBase64 -- If true, the data string is expected to be base64 encoded
        """
        if useBase64:
            data = base64.b64decode(data)
        return self._rsa.private_decrypt(data, padding=1)

    def loadKeypair(self, public, private=None):
        """Load a keypair

        Keyword arguments:
        public -- The public key as string
        private -- The private key as string (default None)
        """
        keyPair = M2Crypto.BIO.MemoryBuffer()
        keyPair.write("%s\n%s" % (public, private))
        self._rsa = M2Crypto.RSA.load_key_bio(keyPair)

    def createKeypair(self, size=2048):
        """Creates a RSA keypair

        Keyword arguments:
        size -- Size of the keypair (default 2048)
        """
        self._rsa = M2Crypto.RSA.gen_key(size, 65537)

    def dumpPrivateKey(self):
        """Get the private key"""
        pri_mem = M2Crypto.BIO.MemoryBuffer()
        self._rsa.save_key_bio(pri_mem, None)
        private_key = pri_mem.getvalue()
        return private_key

    def dumpPublicKey(self):
        """Get the public key"""
        pub_mem = M2Crypto.BIO.MemoryBuffer()
        self._rsa.save_pub_key_bio(pub_mem)
        public_key = pub_mem.getvalue()
        return public_key

    def dumpKeys(self):
        """Get the private and public key"""
        return (self.dumpPublicKey(), self.dumpPrivateKey())

    def getId(self):
        """Get the key id"""
        x = self.dumpKeys()
        return hashlib.sha1(x[0]).hexdigest()

    @staticmethod
    def loadKey(f):
        """Load a key from a file

        Keyword arguments:
        f -- Filepath
        """
        if os.path.isfile(f) and os.access(f, os.R_OK):
            ff = open(f, 'r')
            x = ff.read()
            ff.close()
            return x
        else:
            return None

    @staticmethod
    def storeKey(f, data):
        """Put a key into a file

        Keyword arguments:
        f -- Filepath
        data -- The key as string
        """
        ff = open(f, 'w')
        ff.write(data)
        ff.close()

if __name__ == "__main__":
    x = Rsa()
    x.createKeypair()
    xx = x.dumpKeys()

    y = Rsa()
    y.loadKeypair(xx[0], xx[1])
    e = y.encrypt("Blafasel")
    d = y.decrypt(e)
    signature = y.sign("blafasel")
    print y.verify("blafasel", signature)
    print y.getId()
