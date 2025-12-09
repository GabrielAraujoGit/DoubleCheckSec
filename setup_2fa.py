import veri2step
from cryptography.fernet import Fernet
import qrcode
import os

SECRET_FILE = "secret.enc"
FERNET_KEY_FILE = "secret.key"

def generate_fernet_key():
    key = Fernet.generate_key()
    with open(FERNET_KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_fernet():
    if not os.path.exists(FERNET_KEY_FILE):
        key = generate_fernet_key()
    else:
        with open(FERNET_KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

def main():
    # Cria segredo TOTP randômico
    secret = veri2step.generate_random_secret()
    print("Segredo TOTP gerado (não compartilhe):", secret)

    # Cria URI padrão Google Authenticator
    uri = veri2step.generate_totp_uri(
        secret,
        account_name="gabriel@example.com",   # você pode ajustar
        issuer="MinhaAplicacao"
    )

    print("\nURI TOTP:", uri)

    # Criar QR Code
    img = qrcode.make(uri)
    img.save("qrcode_2fa.png")
    print("QR Code salvo como: qrcode_2fa.png")

    # Armazenar segredo de forma criptografada
    f = load_fernet()
    encrypted = f.encrypt(secret.encode())

    with open(SECRET_FILE, "wb") as f_out:
        f_out.write(encrypted)

    print("\nSegredo criptografado salvo em:", SECRET_FILE)

if __name__ == "__main__":
    main()
