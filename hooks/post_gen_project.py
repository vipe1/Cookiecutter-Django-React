import string
import secrets
import os

list_of_chars = string.ascii_letters + string.digits

def generate_random_credentials(amount=1, length=32, dictionary=list_of_chars) -> str:
    def _main_generator():
        return ''.join(secrets.choice(dictionary) for _ in range(length))

    if amount <= 1:
        return _main_generator()

    creds = []
    for _ in range(amount):
        creds.append(_main_generator())
    return creds


# Generate random database credentials
for stage in ('local', 'production'):
    user, password = generate_random_credentials(2)
    with open(f'./.envs/.{stage}/.postgres', 'a') as file:
        file.write(f'# Auto generated credentials\n')
        file.write(f'POSTGRES_USER={user}\n')
        file.write(f'POSTGRES_PASSWORD={password}\n')


# Generate random Django credentials
production_admin_url = generate_random_credentials()
local_secret, production_secret = generate_random_credentials(2)

divider = '# ' + ('-' * 79)
# Local
with open(f'./.envs/.local/.django', 'a') as file:
    file.write(f'\n# Auto generated credentials\n')
    file.write(f'{divider}\n')
    file.write(f'DJANGO_SECRET_KEY={local_secret}\n')

# Production
with open(f'./.envs/.production/.django', 'a') as file:
    file.write(f'\n# Auto generated credentials\n')
    file.write(f'{divider}\n')
    file.write(f'DJANGO_ADMIN_URL={production_admin_url}\n')
    file.write(f'DJANGO_SECRET_KEY={production_secret}\n')


# Remove file in backend static folder (Read it's content for an explanation)
os.remove('./backend/static/file')