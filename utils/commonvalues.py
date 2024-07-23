import bcrypt
import jwt

key = "secret"
POST = "POST"
GET = "GET"
NOTFOUND_CODE = 400
SUCCESS_CODE = 200
SERVER_ERROR = 500

# example password
password = 'passwordabc'

# converting password to array of bytes


print(hash)


def hasingTheText(text):
    bytes = text.encode('utf-8')
    # generating the salt
    salt = bcrypt.gensalt()
    # Hashing the password
    hash = bcrypt.hashpw(bytes, salt)
    # Decode the byte object to a string
    hash_str = hash.decode('utf-8')
    print(hash_str)
    return hash_str


def jwtd(value):
    text = jwt.encode(value, key=key, algorithm="HS256")
    print(text)
    return text
