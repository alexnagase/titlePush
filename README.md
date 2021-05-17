# titlePush
Pushes an Okta user profile title to Google Workspace without having to enable attribute sync. Allows groups and membership to push from Google to Okta and attributes to sync from Okta to Google. Can be modified to push other attributes as well. 

Requires GAM to be installed. https://github.com/jay0lee/GAM

## Instructions

Run file with Parameters:

**-u, --url**

company.okta.com (replace company with your Okta Tenant URL)

**-t, --token**

Use admin token generated from Okta Admin Console

**-a, --appid**

Find the appid of Google Workspace in your Okta tenant. Can be found Google Workspace app's general tab.
