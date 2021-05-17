import requests
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(
        description="Push user title from Okta into Google Workspace")
    parser.add_argument('-u', '--url', type=str,
                        default='company.okta.com',
                        help='Replace company with the name of your org')
    parser.add_argument('-t', '--token', type=str,
                        default='You did not submit a token',
                        help='API Token from Okta instance')
    parser.add_argument('-a', '--appid', type=str,
                        default='',
                        help='Find this in Okta application General tab')
    args = parser.parse_args()
    return (args.url, args.token, args.appid)

def request_get(url, **kwargs):
    response = requests.get(url, params=kwargs, headers=HEADERS)
    response_data = response.json()
    while response.links.get('next'):
        links = response.links['next']['url']
        response = requests.get(links, headers=HEADERS)
        response_data += response.json()
    return response_data

def get_app_users(url, **kwargs):
    url = f'https://{url}/api/v1/apps/{appid}/users'
    return request_get(url, **kwargs)

def get_okta_users(url, id, **kwargs):
    url = f'https://{url}/api/v1/users/{id}'
    return request_get(url, **kwargs)

if __name__ == '__main__':
    (url, token, appid) = parse_args()

    HEADERS = {
        'Authorization': 'SSWS ' + token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'okta-response': "omitCredentials,omitCredentialsLinks, omitTransitioningToStatus"
    }

    response = get_app_users(url)
    for i in response:
        id = (i['id'])
        userdata = get_okta_users(url, id)
        email = userdata['profile']['email']
        try:
            title = str(userdata['profile']['title'])
        except:
            title = ""
        print(email + ": " + title)

        #gam command
        os.system("$HOME/bin/gam/gam update user "+ email + ' organization title "' + title + '" primary')









