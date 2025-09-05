import matplotlib.pyplot as plt

# Dados ficiticios - Vendas ao longo dos meses

meses = ["jan", "fev", "mar", "abr", "jun", "jul"]
vendas = [150, 200, 100, 300, 250, 400]

# 2- criando um gráfico de linhas

plt.figure(figsize= (8, 5))
plt.plot(
    meses, 
    vendas,
    marker="o",
    linestyle = "-",
    color = "blue",
    label = "Vendas"
    )

#3- Adicionando rótulos e títulos ao gráfico

plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.title("Vendas dos últimos 6 meses")
plt.legend()
plt.grid(True)
	
# 4- Exibindo gráfico

plt.show()