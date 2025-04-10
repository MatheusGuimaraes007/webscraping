# 📊 Pesquisa de Mercado - Notebooks no Saldão da Informática

Este projeto realiza a coleta de dados de notebooks no site [Saldão da Informática](https://www.saldaodainformatica.com.br/) usando **Scrapy**, armazena os dados em um banco de dados **SQLite** e exibe insights por meio de um dashboard interativo feito com **Streamlit**.

---

## 🚀 Tecnologias Utilizadas

- Python
- Scrapy
- Pandas
- NumPy
- SQLite3
- Streamlit

---

## ⚙️ Passo a passo para rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/MatheusGuimaraes007/webscraping.git
cd webscraping
```
### 2 Crie um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```
### 3 Instale as dependências

```bash
pip install -r requirements.txt
```

### 4 Execute o crawler para coletar os dados

```bash
scrapy runspider notebook.py -o data/data.jsonl
```

### 5 Execute o crawler para coletar os dados

```bash
python main.py
```

### 6 Inicie o dashboard com Streamlit

```bash
streamlit run app.py
```


### Bônus

## 🛠️ Visualizando o Banco de Dados com SQLite Viewer

Se quiser inspecionar o conteúdo do banco `saldaodainformatica.db` sem instalar ferramentas no seu computador, você pode usar a ferramenta online:

🔗 [SQLite Viewer (alexcvzz)](https://inloop.github.io/sqlite-viewer/)

### Como usar:

1. Acesse o link: [https://inloop.github.io/sqlite-viewer/](https://inloop.github.io/sqlite-viewer/)
2. Clique em **"Choose file"** e selecione o arquivo `data/saldaodainformatica.db` gerado pelo projeto.
3. O site carregará automaticamente todas as tabelas e seus dados.
4. Você pode:
   - Visualizar os registros
   - Rodar consultas SQL direto no navegador
   - Exportar dados para CSV

> Essa ferramenta é muito útil para quem está testando ou validando a saída de projetos que utilizam **SQLite** como banco local.

---
