
def build_getrequest_header_with_Authorization(accesstoken):
    headers={
        "Authorization":f"Bearer {accesstoken}"
        }
    return headers


def build_postrequest_header_with_Authorization(accesstoken):
    headers={
        "Authorization":f"Bearer {accesstoken}",
        "Content-Type":"appplication/json"
        }
    return headers

def build_postrequest_header_without_Authorization():
    headers={
        "Content-Type":"appplication/json"
        }
    return headers
