
import pandas as pd
from datetime import datetime
import os
import yagmail

# Caminhos
CAMINHO_EXCEL = "C:/Users/keila/OneDrive/Documentos/resumo_vendas_automacao/resumo_vendas_automacao/dados/vendas.xlsx"
CAMINHO_RELATORIO = "C:/Users/keila/OneDrive/Documentos/resumo_vendas_automacao/resumo_vendas_automacao/relatorios/resumo_email.html"

# Leitura do Excel
df = pd.read_excel(CAMINHO_EXCEL)

# Cálculos
df["Total"] = df["Quantidade"] * df["Preço Unitário"]
total_vendido = df["Total"].sum()
produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()
melhor_vendedor = df.groupby("Vendedor")["Total"].sum().idxmax()

# Gerar HTML
html = f"""
<h2>Resumo de Vendas - {datetime.today().strftime('%d/%m/%Y')}</h2>
<ul>
    <li><b>Total vendido:</b> R$ {total_vendido:,.2f}</li>
    <li><b>Produto mais vendido:</b> {produto_mais_vendido}</li>
    <li><b>Melhor vendedor:</b> {melhor_vendedor}</li>
</ul>
"""

# Salvar relatório
os.makedirs("../relatorios", exist_ok=True)
with open(CAMINHO_RELATORIO, "w", encoding="utf-8") as f:
    f.write(html)

print("Relatório gerado com sucesso!")

# Envio de e-mail
EMAIL = "seuemail@gmail.com"
SENHA = "sua_senha_de_app"
DESTINATARIO = "destinatario@exemplo.com"

yag = yagmail.SMTP(EMAIL, SENHA)
yag.send(
    to=DESTINATARIO,
    subject="📈 Resumo de Vendas Diário",
    contents="Segue em anexo o resumo de vendas do dia.",
    attachments=CAMINHO_RELATORIO
)

print("✅ E-mail enviado com sucesso!")
