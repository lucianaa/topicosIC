#iris dataset: Conjunto de dados consistem em 3 tipos diferentes de pétalas de íris (Setosa, Versicolour e Virginica) 
#e comprimento da sépala, armazenados em um numpy 150x4.

#dados
from sklearn import datasets
#plot
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data[:, :2]  # as duas primeiras caracteristicas
y = iris.target #classificacao
#0 Comprimento da sépala; 1 Largura da sépala; 2 comprimento da pétala; Largura da pétala 
#setosa, versicolor, virginica
plt.subplots()
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1)
plt.xlabel('Comprimento Sepala')
plt.ylabel('Largura Sepala')
plt.grid(True)
plt.show()