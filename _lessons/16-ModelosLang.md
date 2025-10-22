---
layout: page
title: Modelos de Linguagem
nav_order: 16
---

# Modelos de Linguagem

### Exercício 1

Considere o seguinte exemplo:

Dados de treino:

```
<s> I am Sam </s>
<s> Sam I am </s>
<s> Sam I like </s>
<s> Sam I do like </s>
<s> do I like Sam </s>
```

Imagine que estamos treinando um modelo de linguagem bi-grama com os
dados de treino mostrados acima.

Probabilidade de cada bi-grama:

$P(Sam| < s >) = \frac{3}{5}$

$P(I| < s >) = \frac{1}{5}$

$P(I|Sam) = \frac{3}{5}$

$P(< /s > |Sam) = \frac{2}{5}$

$P(Sam|am) = \frac{1}{2}$

$P(< /s > |am) = \frac{1}{2}$

$P(am|I) = \frac{2}{5}$

$P(like|I) = \frac{2}{5}$

$P(do|I) = \frac{1}{5}$

$P(Sam|like) = \frac{1}{3}$

$P(< /s > |like) = \frac{2}{3}$

$P(like|do) = \frac{1}{2}$

$P(I|do) = \frac{1}{2}$

Qual seria a próxima palavra mais provável de ser predita pelo modelo
para cada uma das sequências de palavras abaixo?

a)   `<s> Sam ...`

b)   `<s> Sam I do ...`

c)   `<s> Sam I am Sam ...`

d)   `<s> do I like ...`



**Resposta:**

a) “I”.

b) “I” e “like” são igualmente prováveis.

c) “I”.

d) $</s>$.

Observe essas três sentenças:

a) `<s> Sam I do I like </s>`

b) `<s> Sam I am </s>`

c) `<s> I do like Sam I am </s>.`

Qual delas é mais provável de acordo com esse modelo?

**Resposta:**

a: 3/5 × 3/5 × 1/5 × 1/2 × 2/5 × 2/3

b: 3/5 × 3/5 × 2/5 × 1/2

c: 1/5 × 1/5 × 1/2 × 1/3 × 3/5 × 2/5 × 1/2

(b) é a sentença mais provável de acordo com o modelo.

### Exercício 2

Cite as principais desvantagens dos modelos n-grama e possíveis soluções
para esses problemas.

**Resposta:**

Problemas com modelos n-gramas: À medida que n aumenta, é necessário mais memória para armazenar os n-gramas e, além disso, as probabilidades tendem a ser cada vez menores dado o contexto cada vez mais específico. Esparsidade dos dados: a maioria dos n-gramas nunca aparece no corpus, mesmo quando são possíveis (e.g.: e se “estudantes abriram as mochilas” nunca apareceu nos dados?) dessa forma, a probabilidade seria zero.

Algumas maneiras de lidar com esparsidade dos dados são: usar contexto menor (trade-off: modelo menos poderoso); suavizar probabilidades (e.g., adicionando ocorrências imaginárias); prevendo com um ensemble de modelos n-grama com n diferentes; ou utilizar modelos distribuídos.

### Exercício 3

Descreve brevemente como funcionam os modelos neurais de linguagem e
o que são representações *one-hot* e os *embeddings*.

**Resposta:**

Prever a distribuição da próxima palavra dadas as K anteriores é apenas um problema de classificação (multi-classe). Nesse caso, usamos um 1-of-K (one-hot) encoding para palavras, a primeira camada pode ser vista como uma camada com pesos amarrados. *One-hot encoding* são representações esparsas (dimensão: $n_v × 1$, onde $n_v$ é igual ao tamanho do vocabulário) usadas para representar cada palavra do vocabulário. A matriz de pesos age como uma lookup table (seleção de coluna) onde cada coluna é a representação de uma palavra, aka embedding, feature vector ou encoding. *Embeddings* são representações densas (dimensão: $n_e × 1$, onde $n_e$ é igual ao tamanho do embedding escolhido) que enfatizam a localização de uma palavra em um espaço de alta dimensão onde palavras próximas são mais similares semanticamente.
