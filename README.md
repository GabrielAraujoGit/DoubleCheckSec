<!-- Banner central -->
<div align="center">
  <img src="https://img.shields.io/badge/DoubleCheckSec-%23000000.svg?style=for-the-badge&logo=python&logoColor=white" height="32"/>
  <img src="https://img.shields.io/badge/2FA%20Security-%23282828.svg?style=for-the-badge&logo=authy&logoColor=white" height="32"/>
  <img src="https://img.shields.io/badge/Open%20Source-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" height="32"/>
</div>

<h1 align="center">DoubleCheckSec</h1>

<p align="center">
  <b>Sistema de Autenticação em Duas Etapas (2FA) com TOTP + QR Code</b><br/>
  Implementação moderna e segura usando Veri2Step, QR Code e criptografia AES (Fernet).
</p>

<div align="center">
  <img src="https://img.shields.io/github/license/GabrielAraujoGit/DoubleCheckSec?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/github/last-commit/GabrielAraujoGit/DoubleCheckSec?style=for-the-badge"/>
  <img src="https://img.shields.io/github/issues/GabrielAraujoGit/DoubleCheckSec?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/GabrielAraujoGit/DoubleCheckSec?style=for-the-badge&color=yellow"/>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white"/>
</div>

# 📌 Sobre o Projeto

**DoubleCheckSec** é um sistema simples e seguro de autenticação em duas
etapas (2FA) usando:

-   **TOTP** compatível com Google Authenticator / Authy\
-   **QR Code automático** para configuração\
-   **Segredo criptografado com AES (Fernet)**\
-   Separação clara entre:
    -   **setup do 2FA** (geração de segredo + QR)
    -   **verificação do código**

Ideal para adicionar 2FA em aplicações Python, APIs ou sistemas
internos.

------------------------------------------------------------------------

# 🔐 Como funciona

## ✔ 1. `setup_2fa.py`

Responsável por:

-   gerar um segredo TOTP
-   criar o **QR Code** para escanear no Google Authenticator
-   criptografar e salvar o segredo em `secret.enc`
-   gerar a chave AES em `secret.key`

📁 Arquivos gerados:

    secret.key     (chave AES – mantenha privada)
    secret.enc     (segredo TOTP criptografado)
    qrcode_2fa.png (QR Code para registrar o 2FA)

------------------------------------------------------------------------

## ✔ 2. `verify_2fa.py`

Responsável por:

-   descriptografar o segredo
-   validar o código TOTP digitado pelo usuário
-   confirmar ou negar a autenticação

------------------------------------------------------------------------

# 🧪 Exemplo de Uso

## 🔧 Inicializar o 2FA

``` bash
python setup_2fa.py
```
