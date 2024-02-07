from passlib.handlers.pbkdf2 import pbkdf2_sha256
from passlib.hash import django_pbkdf2_sha256
from base64 import b64decode
from passlib.utils.binary import ab64_encode

secret = input("Enter secret: ")
hash = 'pbkdf2_sha256$720000$KIzVC7yt8m4w3cLVQ4KQAO$Nr/u2Ikk0jRwrPd3OWcovQIq9wqkxT4DG0TWReDa2Is='
django_pbkdf2_sha256.verify(secret, hash)
if django_pbkdf2_sha256.verify(secret, hash) == False:
    print("The password is not correct")
print(django_pbkdf2_sha256.verify(secret, hash))

rounds = hash.split('$')[1]
salt = hash.split('$')[2]
print(salt)
django_pbkdf2_sha256.hash(secret, rounds=rounds, salt=salt) == hash
print(django_pbkdf2_sha256.hash(secret, rounds=rounds, salt=salt) == hash)


def hashAndCompare(crackedHash):
    crackedChain = crackedHash.split('$')
    # crackedChainDigest = crackedChain[0]
    crackedChainRounds = crackedChain[1]
    crackedChainSalt = crackedChain[2]
    crackedChainSaltPasslibFormat = ab64_encode(crackedChainSalt.encode('utf8')).decode('utf8')
    crackedChainHashData = crackedChain[3].split(':')
    crackedChainHash = crackedChainHashData[0]
    crackedChainHashPasslibFormat = ab64_encode(b64decode(crackedChainHash)).decode('utf8')
    crackedChainData = crackedChainHashData[1]

    passlibHash = pbkdf2_sha256.hash(crackedChainData, rounds=crackedChainRounds, salt=crackedChainSalt.encode('utf8'))
    passlibChain = passlibHash.split('$')
    passlibChainSalt = passlibChain[3]
    passlibChainHash = passlibChain[4]

    print('Passlib: Hash: {0} Salt: {1}\nCracked: Hash: {2} Salt: {3}\n'.format(passlibChainHash, passlibChainSalt,
                                                                                crackedChainHashPasslibFormat,
                                                                                crackedChainSaltPasslibFormat))

hashAndCompare('pbkdf2_sha256$720000$KIzVC7yt8m4w3cLVQ4KQAO$Nr/u2Ikk0jRwrPd3OWcovQIq9wqkxT4DG0TWReDa2Is=:123')