# Sistema de Controle de Almoxarifado  🛠️

Este projeto é o backend de um sistema de gestão de ferramentas e equipamentos, desenvolvido para a disciplina de Práticas Extensionistas Integradoras V, dos cursos de Engenharia do 5° período da Universidade de Vassouras. O sistema utiliza **Django** para gerenciar o banco de dados e fornecer uma API que se comunica com dispositivos **ESP32** via RFID.

## 🚀 Funcionalidades Atuais
- **Cadastro de Colaboradores:** Registro de usuários autorizados a retirar equipamentos.
- **Gestão de Ativos:** Cadastro de ferramentas com controle de status automático (Disponível/Em Uso).
- **Registro de Movimentações:** Log completo de retiradas e devoluções com carimbo de data/hora.
- **Automação de Status:** O sistema altera o status do ativo automaticamente ao registrar uma nova movimentação.

## 🛠️ Tecnologias Utilizadas
- **Python 3.x**
- **Django 5.x**
- **Django Rest Framework** (Pronto para integração)
- **SQLite** (Banco de dados de desenvolvimento)
- **Python-Decouple** (Gestão de variáveis de ambiente)

## 🔧 Como Rodar o Projeto Localmente

Siga os passos abaixo para configurar o ambiente em sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/rafaela-barbosa/projeto_automacao_almo.git
   cd backend
2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   # No Windows:
   .\venv\Scripts\activate
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
4. **Configure as variáveis do ambiente:**
   Crie um arquivo .env na raiz do projeto seguindo o modelo do .env.example
5. **Rode as migrações do banco de dados:**
   ```bash
   python manage.py migrate
6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
  Acesse o sistema em: http://127.0.0.1:8000/admin

### Equipe Infinity Engineers
* Amanda Da Silva Diniz Nogueira
* Bernardo Dos Santos Pinto Rodrigues
* Hildon 
* Lívia Araujo Speranza
* Mirella Aparecida Do Carmo
