import veri2step
from cryptography.fernet import Fernet
import os


SECRET_FILE = "secret.enc"
FERNET_KEY_FILE = "secret.key"

def load_fernet():
    with open(FERNET_KEY_FILE, "rb") as f:
        key = f.read()
    return Fernet(key)

def load_secret():
    if not os.path.exists(SECRET_FILE):
        raise FileNotFoundError("Arquivo secret.enc não encontrado. Execute setup_2fa.py primeiro.")

    if not os.path.exists(FERNET_KEY_FILE):
        raise FileNotFoundError("Arquivo secret.key não encontrado. Não é possível descriptografar.")

    f = load_fernet()
    with open(SECRET_FILE, "rb") as f_in:
        encrypted_secret = f_in.read()

    secret = f.decrypt(encrypted_secret).decode()
    return secret

def main():
    secret = load_secret()

    verifier = veri2step.Verifier(
        algorithm="totp",
        secret=secret
    )

    user_otp = input("Digite o código do Google Authenticator: ")

    if verifier.verify(user_otp):
        print("✔ Autenticado com sucesso!")
    else:
        print("✘ Código inválido.")

if __name__ == "__main__":
    main()
