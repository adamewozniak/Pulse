import json
import requests

URL = 'https://api.fitbit.com'

def getHeaders():

    readToken = open("lib/api/refreshToken.rt","r")
    refreshToken = readToken.read()
    GET_BEARER = '/oauth2/token'
    api_url = URL + GET_BEARER

    headers = {
        'Authorization': 'Basic MjJDWUNQOmRhZTc3OGUxM2IzNDE2NjJmM2JjYmM5NDMzMDQ0NmU1',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    args = {
        'grant_type' : 'refresh_token',
        'refresh_token' : refreshToken
    }

    response = requests.post(api_url,
        headers=headers,
        params=args)

    responseObj = json.loads(response.content)

    try:
        newRefreshToken = responseObj['refresh_token']
        saveToken = open("lib/api/refreshToken.rt","w")
        saveToken.write(newRefreshToken)
    except:
        return responseObj

    return {
        'Authorization': ('Bearer {0}').format(responseObj['access_token'])
    }

def apiRequest(uri, opts, reqType):

    uri = uri.format_map(opts)
    headers = getHeaders()

    print("\nPOST TO : " + uri)
    #print("HEADERS : " + json.dumps(headers))
    print("ARGS : " + json.dumps(opts) + "\n")
        
    postUrl = URL + uri

    if(reqType == "POST"):
        response = requests.post(postUrl,
            headers = headers, 
            params = opts)
    elif(reqType == "GET"):
        response = requests.get(postUrl,
            headers = headers, 
            params = opts)

    else :
        return {'success':False}

    return json.loads(response.content)

# Collection of API URLS
GET_HEART = '/1/user/-/activities/heart/date/{date}/1d/{detail-level}/time/{start-time}/{end-time}.json'

#getHeart method
#opts.date (today)
#opts.detail-level (1sec)
#opts.start-time (00:00)
#opts.end-time (00:01)
def getHeart(opts):
    return apiRequest(
        GET_HEART,
        opts, "GET"
    )