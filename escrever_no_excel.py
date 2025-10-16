import pandas as pd

# Ler
df = pd.read_excel("dados.xlsx")

# Modificar
df["Total"] = df["Quantidade"] * df["Preço"]

# Salvar
df.to_excel("dados_atualizados.xlsx", index=False)
    