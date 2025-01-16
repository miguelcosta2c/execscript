# ExecScript

## Descrição

ExecScript é uma aplicação robusta para execução segura de arquivos criptografados em um banco de dados Oracle. Ideal para proteger seus scripts contra alterações indesejadas.

**Nota:** Recomenda-se o uso do projeto irmão, **CriptoScript**, para a criação e manipulação dos arquivos criptografados utilizados nesta aplicação.

Desenvolvido com **PySide6**, **oracledb** e **cryptography**, o ExecScript garante um ambiente controlado para execução de arquivos sensíveis.

## Funcionalidades

- **Descriptografia e Execução de Arquivos SQL:** Realize a execução segura de scripts armazenados de forma criptografada.
- **Interface Gráfica Intuitiva:** Facilita a interação do usuário com o sistema.
- **Integração com OracleDB:** Conexão direta e eficiente com bancos de dados Oracle.

## Pré-requisitos

1. **Python 3.9 ou superior**
2. Instalação das seguintes dependências:
   - PySide6
   - oracledb
   - cryptography
3. **Banco de Dados Oracle** configurado e acessível.
4. Arquivos necessários:
   - `.enc`: Arquivo criptografado.
   - `.key`: Chave de descriptografia, gerada pelo projeto CriptoScript.

## Como Usar

1. **Testar Conexão:**
   - Antes de iniciar, clique em "Testar Conexão" para verificar o acesso ao banco de dados.

2. **Enviar Arquivo:**
   - Carregue o arquivo `.enc` e a chave `.key` necessários para a descriptografia.

3. **Executar Arquivo:**
   - Após o envio, execute o script descriptografado diretamente no banco de dados Oracle.

4. **Converter em Executável:**
   - Utilize o arquivo `.spec` incluso para gerar um executável (.exe) com o PyInstaller:
     ```bash
     pyinstaller ExecScript.spec
     ```

## Licença

Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo `LICENSE`.

---

Feito com dedicação por Miguel Cosme Costa.

