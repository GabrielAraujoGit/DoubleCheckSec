<!-- Banner central -->
<div align="center">
  <img src="https://img.shields.io/badge/DoubleCheckSec-%23000000.svg?style=for-the-badge&logo=python&logoColor=white" height="32"/>
  <img src="https://img.shields.io/badge/2FA%20Security-%23282828.svg?style=for-the-badge&logo=authy&logoColor=white" height="32"/>
  <img src="https://img.shields.io/badge/Open%20Source-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" height="32"/>
</div>

<h1 align="center">DoubleCheckSec</h1>

<p align="center">
  <b>Sistema de Verificação em Duas Etapas com PyOTP</b><br/>
  Adiciona uma camada extra de segurança às suas aplicações com autenticação 2FA simples e eficaz.
    
</p>

<div align="center">
  <img src="https://img.shields.io/github/license/gabriel-araujo-git/DoubleCheckSec-?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/github/last-commit/gabriel-araujo-git/DoubleCheckSec-?style=for-the-badge"/>
  <img src="https://img.shields.io/github/issues/gabriel-araujo-git/DoubleCheckSec-?style=for-the-badge"/>
  <img src="https://img.shields.io/github/stars/gabriel-araujo-git/DoubleCheckSec-?style=for-the-badge&color=yellow"/>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB.svg?style=for-the-badge&logo=python&logoColor=white"/>
</div>


## Funções Principais

### `gerar_segredo()`

Esta função gera um segredo exclusivo para o usuário. O segredo é uma sequência aleatória de caracteres base32 que deve ser compartilhada com um aplicativo de autenticação, como o Google Authenticator. O segredo é essencial para gerar e verificar os códigos de verificação.

### `gerar_token(segredo)`

Esta função recebe um segredo como entrada e retorna um token de verificação atual gerado com base no segredo fornecido. O token é um código de uso único que expira após um curto período de tempo.

### `verificar_token(segredo, token)`

Esta função recebe o segredo do usuário e o token de verificação inserido pelo usuário e verifica se o token é válido. Se o token estiver correto e dentro do período de validade, a função retornará `True`, indicando que a autenticação em duas etapas foi bem-sucedida. Caso contrário, a função retornará `False`.

## Exemplo de Uso

```python
if __name__ == "__main__":
    # Passo 1: Gerar um segredo para o usuário
    segredo = gerar_segredo()
    print("Passo 1: Compartilhe este segredo com o aplicativo de autenticação:", segredo)

    # Passo 2: Obter o token de verificação do usuário (gerado pelo aplicativo)
    token = input("Passo 2: Digite o token gerado pelo aplicativo de autenticação: ")

    # Passo 3: Verificar o token
    if verificar_token(segredo, token):
        print("Token válido. Autenticação em duas etapas bem-sucedida!")
    else:
        print("Token inválido. Autenticação em duas etapas falhou.")
```

## Contribuindo

Se você quiser contribuir para o projeto DoubleCheckSec, sinta-se à vontade para abrir uma "Issue" ou enviar um "Pull Request" com suas melhorias ou correções de bugs.

## Licença

Este projeto está licenciado sob a licença MIT. Leia o arquivo [LICENSE](LICENSE) para obter mais detalhes.

## Contato

Para qualquer dúvida ou sugestão relacionada a este projeto, entre em contato através do email ga2951057@gmail.com

---

Agradecemos por utilizar o DoubleCheckSec para aumentar a segurança em seus sistemas e contas de usuário. Esperamos que este projeto seja útil para suas necessidades de verificação em duas etapas!
