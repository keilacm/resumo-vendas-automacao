# 📊 Automação: Resumo de Vendas com Python

Este projeto realiza a automação de um processo de análise e envio de resumo de vendas a partir de um arquivo Excel.

## Funcionalidades

- Leitura de dados de vendas (.xlsx)
- Cálculo de total vendido, produto mais vendido e melhor vendedor
- Geração de relatório HTML com o resumo
- Envio automático por e-mail

## Tecnologias Utilizadas

- Python 3
- Pandas
- yagmail (envio de e-mails)
- openpyxl (leitura de Excel)

## Estrutura do Projeto

```
resumo_vendas_automacao/
├── dados/
│   └── vendas.xlsx
├── relatorios/
│   └── resumo_email.html
├── src/
│   └── automacao.py
├── README.md
└── requirements.txt
```

## Como Executar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure seu e-mail para envio (Gmail recomendado).
3. Execute o script:

```bash
cd src
python automacao.py
```

## ✅ Status do Projeto

✅ Concluído – pronto para uso e personalização.
