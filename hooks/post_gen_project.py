import string
import secrets

list_of_chars = string.ascii_letters + string.digits


def generate_random_credentials(length=32, dictionary=list_of_chars) -> str:
    return ''.join(secrets.choice(dictionary) for _ in range(length))


user = generate_random_credentials()
password = generate_random_credentials()

with open('./.envs/.local/.postgres', 'a') as file:
    file.write(f'POSTGRES_USER={user}\n')
    file.write(f'POSTGRES_PASSWORD={password}\n')
