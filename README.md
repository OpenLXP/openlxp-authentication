# OpenLXP-Authentication

This is a Django package built on the social-auth-app-django package to allow additional authentication options for the OpenLXP project.

Currently this package adds support for storing SAML configurations in the database used by Django, to allow for site administrators to set SAML configurations through the admin app.


## Required Settings 

### JSONFIELD_ENABLED

The JSONFIELD_ENABLED setting is required as it allows storing the attribute mapping as JSON in the database.

```ini
JSONFIELD_ENABLED = True
```

### USER_MODEL

The USER_MODEL setting sets what model should be used when authenticating a User.

```ini
USER_MODEL = 'core.XDSUser'
```

### SP_ENTITY_ID

The SP_ENTITY_ID setting sets Entity ID that IDPs should use for identifying the service.  This settings should be unique to your service.

```ini
SP_ENTITY_ID = 'http://localhost:8000'
```

## Optional Settings

### SESSION_EXPIRATION

The SESSION_EXPIRATION setting has the Django session expiration match an experiation supplied by the IDP.

```ini
SESSION_EXPIRATION = True
```

### LOGIN_REDIRECT_URL

The LOGIN_REDIRECT_URL setting is used by the application to redirect the user upon a successful login.

```ini
LOGIN_REDIRECT_URL = 'http://www.google.com'
```

### STRATEGY

The STRATEGY setting is required if using the OVERIDE_HOST setting.  OpenLXP-Authentication provides a strategy but custom solutions can be created and referenced in this setting.

```ini
STRATEGY = 'openlxp_authentication.models.SAMLDBStrategy'
```


USER_MODEL = 'core.XDSUser'
SESSION_EXPIRATION = True
LOGIN_REDIRECT_URL = 'http://www.bbc.com'
SP_ENTITY_ID = 'http://localhost:8000'
OVERIDE_HOST = 'http://localhost:8000'
BAD_HOST = 'http://localhost'
SP_PUBLIC_CERT = "******"
SP_PRIVATE_KEY = "******"
ORG_INFO = {
    "en-US": {
        "name": "example",
        "displayname": "Example Inc.",
        "url": "http://localhost",
    }
}
TECHNICAL_CONTACT = {
    "givenName": "Tech Gal",
    "emailAddress": "technical@localhost.com"
}
SUPPORT_CONTACT = {
    "givenName": "Support Guy",
    "emailAddress": "support@localhost.com",
}
USER_ATTRIBUTES = ["user_permanent_id",
        "first_name",
        "last_name",
        "email"]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'openlxp_authentication.models.SAMLDBAuth',
)
