---
layout: page
title: Stride e Padding
nav_order: 10
---

# Stride e Padding

### Exercício 1

Dado uma imagem em preto e branco de tamanho 8 × 8 pixels e um filtro
de tamanho 3 × 3, indique as dimensões da matriz resultado da convolução e o tamanho do padding que deverá ser utilizado em cada um dos casos:

a) Valid padding

b) Same padding

**Resposta:**

a) Dimensão do resultado: 6 × 6, padding: $p$ = 0

b) Dimensão do resultado: 8 × 8, padding: $p$ = 1

### Exercício 2

Repita o exercício acima utilizando stride igual a 2.

**Resposta:**

a) Dimensão do resultado: 3 × 3, padding: $p$ = 0

b) Dimensão do resultado: 8 × 8, padding: $p$ = 4.5 $p$ = (n ∗ s − n + f − s) / 2

(Note que quando $p$ não é um valor inteiro significa que o padding no lado esquerdo e direito da matriz terão tamanhos diferentes. No nosso caso, seriam adicionados 4 zeros na esquerda e 5 na direita, ou vice-versa).

### Exercício 3

Explique como o tamanho do filtro de convolução pode não causar impacto no número de aplicaçãoes (ou seja, o número de vezes que seu filtro irá multiplicar o volume de entrada) ao usar o Same Padding.

**Resposta:**

Ainda que filtros maiores sejam aplicados menos vezes em uma mesma
entrada, no Same Padding, o tamanho da entrada é proporcional ao tamanho do filtro (por causa do padding). Portanto, a quantidade de aplicações do filtro permanece inalterada.

### Exercício 4

O Valid Padding sempre produz uma imagem de saída com dimensões
2D menores do que a entrada. Estritamente falando, este não é sempre o caso. Especifique o caso (não muito interessante) onde esta afirmação é falsa.

**Resposta:**

Quando o filtro tem tamanho 1 × 1. Assumindo que não haverá padding e stride igual a 1, dado uma imagem n × n, ao aplicar um filtro 1 × 1, o resultado obtido terá dimensão igual a:

(n − f + 1) × (n − f + 1) = n × n.

## 2. Convoluções sobre volumes

### Exercício 5

Suponha uma entrada de tamanho 63 x 63 x 16. Ao aplicar uma convolução nessa entrada com 32 filtros de tamanho 7 x 7, usando stride igual a 2 e sem padding. Qual será o volume de saída?

**Resposta:**

29 x 29 x 32

### Exercício 6

Suponha uma entrada de tamanho 15 x 15 x 8. Usando a operação de padding igual 2, qual é a dimensão do dado de saída após o padding?

**Resposta:**

19 x 19 x 8

### Exercício 7

Dado uma entrada de dimensão 63 x 63 x 16 e uma convolução com 32 filtros de dimensão 7 x 7 cada e um stride igual a 1, qual deverá ser o tamanho do padding utilizado para que você obtenha uma saída com o mesmo tamanho da entrada (same padding)?


**Resposta:**

$p$ = 3
