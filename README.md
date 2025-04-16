
# 📊 Plataforma Interna de Métricas e Produtividade - Fleximedical

Este projeto foi desenvolvido sob demanda para a **Fleximedical**, com o objetivo de **monitorar indicadores de produtividade, andamento de projetos e performance da equipe**, tudo por meio de uma interface web segura e intuitiva criada com Streamlit.

---

## 🚀 Visão Geral

A aplicação permite que diferentes tipos de usuários (admin e normal) acessem funcionalidades específicas, como:

- 📝 Preenchimento de formulários com dados de atividades
- 📂 Visualização de base de dados consolidada
- 📈 Geração de gráficos e indicadores sobre produtividade e andamento de projetos
- 📊 Análise do planejado versus realizado
- 🔒 Controle de acesso com autenticação segura via arquivo `secrets.toml`

---

## 👥 Perfis de Usuário

- **Admin**  
  Tem acesso total às análises e banco de dados da aplicação.

- **Normal**  
  Pode preencher o formulário de atividades, mas não acessa dados gerenciais.

---

## 🧠 Tecnologias Utilizadas

- **Python 3.9+**
- **Streamlit** – Interface web reativa e leve
- **Streamlit Navigation** – Controle de navegação entre múltiplas páginas
- **Secrets Management** – Armazenamento seguro de credenciais de usuários

---

## 🔐 Segurança

A autenticação é baseada em credenciais protegidas por meio do arquivo `secrets.toml`, o que garante sigilo e controle de acesso:

```toml
# Exemplo do arquivo .streamlit/secrets.toml
[credenciais]
senha_ronaldo = "sua_senha_segura"
senha_felipe = "outra_senha_segura"
```

---

## 📁 Estrutura do Projeto

```
📦 projeto/
│
├── main.py                 # Script principal com sistema de login e navegação
├── homepage.py             # Página de entrada de dados (formulário)
├── tabela.py               # Visualização da base de dados
├── indicadores.py          # Indicadores de produtividade
├── graficos.py             # Gráficos de distribuição por área
├── planejadoxreal.py       # Comparativo planejado vs. real
└── .streamlit/
    └── secrets.toml        # Credenciais dos usuários
```

---

## ▶️ Como Rodar o Projeto

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Crie o arquivo de credenciais**
```bash
mkdir .streamlit
nano .streamlit/secrets.toml
```

3. **Adicione o conteúdo com as senhas dos usuários**
```toml
[credenciais]
senha_ronaldo = "123456"
senha_felipe = "654321"
```

4. **Instale as dependências**
```bash
pip install -r requirements.txt
```

5. **Execute a aplicação**
```bash
streamlit run main.py
```

---

## 💼 Impacto na Fleximedical

✅ Centralização dos dados de produtividade  
✅ Visibilidade clara do desempenho da equipe  
✅ Relatórios automatizados sem uso de planilhas manuais  
✅ Interface acessível via navegador, sem necessidade de instalação  
✅ Base sólida para decisões estratégicas e operacionais  

---

## 👨‍💻 Autor

Desenvolvido por **Vitor Alves**  
📧 vitoralves20112011@gmail.com  
💼 [linkedin.com/in/vit0ralves(https://linkedin.com/in/vit0ralves)

---

## ⭐ Considerações Finais

Este projeto é um exemplo real de como aliar **desenvolvimento ágil, automação e visualização de dados** para resolver problemas reais em ambientes corporativos. Se você busca alguém que saiba entregar soluções funcionais, com segurança e foco no usuário — **vamos conversar!**
