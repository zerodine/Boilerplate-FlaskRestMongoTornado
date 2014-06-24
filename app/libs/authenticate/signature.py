import hashlib
from authenticate import Authenticate
from app.libs import Rsa
import urllib2
import os


class Signature(Authenticate):
    node_keys = None  # List of allowed key ids
    string_to_verify = None  # Multiple headers concatenated to a string
    signature = None  # The signature given by the node
    key_id = None  # Key id given by the node
    key_url = None  # URL to the public key file of the node
    key_cache_dir = None  # Local keystore
    key = None  # The plaintext public key of the node
    rsa = None  # An instance of RSA

    def __init__(self, node_key_allowed):

        # Just assigning of some variables
        self.node_key_allowed = node_key_allowed

        # Get an instance of RSA
        self.rsa = Rsa()

    def _getKey(self):

        # Generate the filename for local keystore
        f = self.key_cache_dir + self.key_id + ".pub"

        # Check if file exists an is readable
        if not os.path.isfile(f) or not os.access(f, os.R_OK):

            # Get public key from node
            response = urllib2.urlopen(self.key_url)
            key = response.read()

            # Check if key id is right
            if self._check_key_id(key):

                # Save key to store
                ff = open(f, 'w')
                ff.write(key)
                ff.close()

        # Get key from store
        self.key = self.rsa.loadKey(f)

    def _check_key_id(self, key):

        # Generate key id from key
        h = hashlib.sha1()
        h.update(key)
        key_id = h.hexdigest()

        # Check if id is equal to given id
        if key_id == self.key_id:
            return True

        return False

    def verify_key(self):

        # Verify if key id is in defined range of allowed keys
        if self.key_id in self.node_key_allowed:
            return True
        return False

    def verify(self):

        # Verify if key is valid
        if not self.verify_key():
            return False

        # Get key from store
        self._getKey()

        # Load key into RSA instance
        self.rsa.loadPublicKey(self.key)

        # Verify signature
        if self.rsa.verify(self.string_to_verify, self.signature):
            return True

        return False