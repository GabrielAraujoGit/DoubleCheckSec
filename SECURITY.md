<!-- Banner -->
<div align="center">
  <img src="https://img.shields.io/badge/DoubleCheckSec-%23000000.svg?style=for-the-badge&logo=python&logoColor=white" height="32"/>
  <img src="https://img.shields.io/badge/Security%20Policy-%23181717.svg?style=for-the-badge&logo=github&logoColor=white" height="32"/>
  <img src="https://img.shields.io/badge/Dependabot-Active-blue?style=for-the-badge&logo=dependabot" height="32"/>
</div>

<h1 align="center">Política de Segurança</h1>


---

## 🔒 Princípios Gerais

- **Transparência:** qualquer vulnerabilidade identificada será documentada e corrigida publicamente.  
- **Responsabilidade:** não são aceitos testes que prejudiquem usuários, infraestruturas ou terceiros.  
- **Rapidez:** priorizamos correções de segurança em relação a novas features.

---

## 🧠 Boas Práticas Adotadas

- Autenticação segura via **2FA** em todas as contas com acesso de escrita.  
- Tokens e secrets armazenados apenas em **GitHub Actions Secrets**.  
- Dependências monitoradas automaticamente via **Dependabot Security Alerts**.  
- Repositórios protegidos por **branch protection rules** e **assinatura de commits (GPG)**.  
- Política de **revisão obrigatória** para pull requests que modifiquem o core do aplicativo.  

---

## 🧰 Relato de Vulnerabilidades

Se você identificar uma falha de segurança:

1. **Não abra uma issue pública.**  
2. Documente o comportamento inesperado, versão utilizada e possível impacto.  
3. Entre em contato de forma privada (canal de segurança será divulgado futuramente).  

Todas as vulnerabilidades válidas serão analisadas, confirmadas e corrigidas de forma prioritária.  
Agradecemos contribuições responsáveis e éticas.

---

## 🧩 Escopo

Esta política cobre:

- Código-fonte do **Lynx Assistant** e seus módulos oficiais.  
- Scripts e automações incluídos no repositório principal.  
- Fluxos CI/CD e dependências declaradas em `requirements.txt`.

Não cobre:
- Repositórios de terceiros ou forks não oficiais.  
- Implementações externas que utilizem o Lynx sem auditoria de segurança.

---

## 📜 Política de Divulgação

Quando uma vulnerabilidade for confirmada e corrigida:
- A correção será incluída no próximo **release estável**.  
- O changelog refletirá a natureza da atualização (sem detalhes sensíveis).  
- O relatório técnico poderá ser publicado após mitigação completa.

---

## 🔐 Recomendações aos Contribuidores

Antes de contribuir:
- Ative **Two-Factor Authentication (2FA)** na sua conta GitHub.  
- Utilize **chaves SSH (ed25519)** para commits e pushes.  
- Assine commits com **GPG** sempre que possível.  
- Não envie senhas, tokens, nem arquivos confidenciais em commits.  
- Prefira variáveis de ambiente e secrets para qualquer configuração sensível.  

---

<p align="center">
  <b>Lynx Assistant Project</b><br/>
  <i>Construindo ferramentas seguras, abertas e responsáveis.</i>
</p>
