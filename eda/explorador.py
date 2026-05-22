import pandas as pd
from matplotlib import pyplot as plt

class Explorador:
    def __init__(self, df):
        self.data = df

    def descripcion(self):
        salida = self.data.describe().T
        salida["Nulos"] = self.data.isnull().sum()
        salida["Tipos"] = self.data.dtypes
        return salida
    
    def perdidos(self):
        import seaborn as sns
        sns.heatmap(self.data.isnull(), cbar=False, cmap='viridis')
        plt.show()

    def perdidos_juntos(self):
        # Calcular la cantidad de valores perdidos por columna
        suma_perdidos = self.data.isnull().sum()

        # Visualizar el diagrama de barras de valores perdidos
        plt.figure(figsize=(10, 6))
        # Es el mismo tipo de gráfico que hemos usado para ver los valores únicos de las columnas categóricas
        suma_perdidos.plot(kind='bar', color='lightcoral')
        plt.title('Diagrama de Barras de Valores Perdidos', fontsize=16)
        plt.xlabel('Columnas', fontsize=12)
        plt.ylabel('Cantidad de Valores Perdidos', fontsize=12)
        plt.show()


if __name__ == '__main__':
    datos = pd.read_csv("data/Ejemplo_valores_perdidos.csv")
    explorador = Explorador(datos)
    explorador.perdidos_juntos()
    plt.savefig("imagenes/grafica_perdidos_barras.png")
    explorador.perdidos()
    plt.savefig("imagenes/grafica_perdidos.png")
    print(explorador.descripcion())