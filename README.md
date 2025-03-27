# curso_python

O Curso de Iniciação à Programação em Python para profissionais da Saúde tem uma natureza teórico-prática e é dirigido a pessoas sem conhecimento das linguagens de programação, mas que pretendem desenvolver competências a este nível para incorporarem na sua atividade profissional.

A programação em Python é útil para tratar grandes conjuntos de dados de forma rápida e personalizada, automatizar tarefas de computação ou simular fenómenos biológicos e observar os seus resultados no computador. Embora se privilegie a participação de profissionais da Saúde, a área de atividade dos formandos não é determinante para o sucesso das aprendizagens uma vez que serão dados exemplos da linguagem Python aplicáveis a diferentes domínios. Não se exigem competências prévias de programação, uma vez que os formandos começarão por aprender os conceitos básicos da linguagem Python antes de evoluírem para tarefas mais complexas.  É desejável, no entanto, que tenham uma ideia de como a programação poderá ser útil na sua atividade profissional, por forma a tirarem o máximo partido deste curso. Não se aconselha a utilização de computadores portáteis. 

No final do curso, os formandos deverão ser capazes de construir pequenos programas em Python e de assimilar facilmente outras funcionalidades da linguagem, com vista a desenvolverem as suas capacidades de programação. Os candidatos serão selecionados com base numa carta de motivação, a qual deve sintetizar num só parágrafo os motivos na base da candidatura ao curso.

## Algumas sugestões, notas e conceitos

Atalhos úteis para usar na shell do IDLE

Aceder/percorrer os comandos previamente introduzidos/executados:

```
ALT + p # previous

ALT + n # next
```

Atalho para autocomplete:
```
TAB
```

Para converter uma lista num tuplo, usar função tuple():

```
lista1 = [1,2,3]

tuplo1 = tuple(lista1)
```

Para converter um tuplo numa lista, usar a função list():
```
tuplo2 = (4,5,6)

lista2 = list(tuplo2)
```

Para converver um tuplo numa lista também pode ser usado pex um ciclo "for" para iterar sobre os elementos do tuplo e adicioná-los a uma nova lista usando a função append():

```
tuplo3 = (7,8,9)

lista3 = []

for item in tuplo3:
  lista3.append(item)
```


## É possível efetuar diferentes tipos de cópias de estruturas de objectos, mas é necessário ter especial cuidado no tipo de cópia usada nomeadamente quando se trata de um objecto mutável, pois por vezes é apenas criada uma referência em memória relativa ao objecto original e não uma cópia totalmente nova e independente

Por exemplo, quando se usa a forma mais simples de cópia, estamos a usar o método de "Aliasing":

```
a = [1,2,3]

b = a # Cópia por "aliasing", obtemos nova lista "b" que é igual à "a"

print(b) --> [1,2,3]

b[0] = 5 # Alteração do item com índice zero na nova lista "b", que passará de 1 para 5 (ou seja, agora b = [5,2,3])

print(a) --> [5,2,3] # Mas a lista original "a" também foi alterada! Porque a nova lista "b" é apenas uma referência em memória à lista original "a", quando alteramos "b", alteramos também "a".
```

Usando o método de "Cloning" ou de "Shallow copy", o problema será o mesmo do "Aliasing" se existir uma lista interna dentro da nossa lista:

```
a = [[1,2,3]]

b = a[:] # Cópia por "cloning", obtemos nova lista "b" que é igual à "a"

print(b) --> [[1, 2, 3]]

b[0][0] = 9 # Alteração do primeiro item da lista interna da lista "b", que passará de 1 para 9 (ou seja, agora b = [[9, 2, 3]])

print(a) --> [[9, 2, 3]] # Mas a lista original "a" também foi alterada! Porque a lista interna de "b" é apenas uma referência em memória à lista interna de "a", quando alteramos a lista interna de "b", alteramos também a de "a".

# O mesmo acontece se for usado o método "Shallow copy":

from copy import copy

c = [[4,5,6]]

d = copy(c) # Cópia por "Shallow copy", obtemos nova lista "d" que é igual à "c"

```

Usando o método de "Deepcopy", a cópia será totalmente independente da original, ou seja, tem a sua própria referência em memória, o que significa que quando alteramos uma das listas, não afetamos a outra:

```
from copy import deepcopy

e = [[7,8,9]]

f = deepcopy(e) # Cópia por "Deepcopy", obtemos nova lista "f" que é igual e independente de "e"
```

## Rever conceito de "Função" (inclui docstring e return) e "Procedimento" (sem return e sem garantias na docstring)

## Rever conceito de "Programação por contrato" (docstring) versus "Programação defensiva"


