from hashids import Hashids
from django.conf import settings

hashids = Hashids (
    salt=settings.SALT,
    min_length=8,
)

def encode_id(id):
    return hashids.encode(id)

def decode_id(id):
    decoded = hashids.decode(id)
    return decoded[0] if decoded else None