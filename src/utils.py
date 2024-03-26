import base64
import hashlib
import json

def parse_multipart(data, decodeBase64=True):
    output = {}

    if decodeBase64:
        data = base64.b64decode(data)

    boundary = data.split(b'\r\n')[0]
    fields = data.split(boundary)

    for f in fields:
        try:
            fNameStart = int(f.find(b'name="'))
            fNameEnd = int(f.find(b'"',fNameStart+6))

            fk = f[fNameStart+6:fNameEnd].decode("utf-8")
            if b'"; filename="' in f:
                fv = f.split(b'\r\n\r\n',1)[1][:-2]
            else:
                fv = f.split(b'\r\n\r\n',1)[1][:-2].decode("utf-8")
            output[fk] = fv
        except:
            pass

    return output

def hash_request(request):
    hash = hashlib.sha256()

    request = {
        k: base64.b64encode(v).decode("utf-8") if isinstance(v, bytes) else v for k,v in request.items()
    }

    hash.update(json.dumps(request, sort_keys=True).encode("utf-8"))

    return hash.hexdigest()

cors_headers = {
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "OPTIONS,POST",
    "Access-Control-Expose-Headers": "X-Amzn-Trace-Id",
}

