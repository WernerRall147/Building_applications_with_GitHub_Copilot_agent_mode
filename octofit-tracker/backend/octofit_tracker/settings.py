INSTALLED_APPS = [
    # ...existing apps...
    'octofit',
    'corsheaders',
]

# Ensure the database engine djongo is properly configured
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
    }
}

# Enable CORS
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']