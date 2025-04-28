---
layout: page
title: Regressão Logística e SVM
nav_order: 3
---

# Regressão Logística e SVM

> - Regressão Logística
> - SVM

## Regressão Logística

### Exercício 1

No modelo de regressão logística com um regressor apenas, a probabilidade é definida como:

$$ P(Y_i = 1) = p(x_i) = \frac{1}{1 + \exp(-b - w_1 x_i)}. $$

Deduza que a log-verossimilhança de $ \theta = (b, w_1) $ no caso do modelo logístico com um único regressor é dada por:

$$
l(\theta) = b \sum_{i=1}^n y_i + w_1 \sum_{i=1}^n x_i y_i - \sum_{i=1}^n \log(1 + e^{b + w_1 x_i}).
$$


**Resposta:**

Para deduzir a expressão da log-verossimilhança $ l(\theta) $ no modelo de regressão logística com um regressor, começamos pela definição da função de verossimilhança para variáveis aleatórias Bernoulli. Cada observação $ Y_i $ pode assumir os valores 0 ou 1, com probabilidades $ 1 - p_i $ e $ p_i $, respectivamente, onde:

$$
p_i = P(Y_i = 1) = \frac{1}{1 + \exp(-b - w_1 x_i)}.
$$

A função de verossimilhança é dada por:

$$
L(\theta) = \prod_{i=1}^n p_i^{y_i} (1 - p_i)^{1 - y_i}.
$$

Tomando o log da verossimilhança, obtemos a log-verossimilhança:

$$
l(\theta) = \sum_{i=1}^n  y_i \log(p_i) + (1 - y_i) \log(1 - p_i) .
$$

Agora, expressamos $ \log(p_i) $ e $ \log(1 - p_i) $ em termos do bias $ b $ e do peso $ w_1 $:

$$
\begin{align*}
p_i &= \frac{e^{b + w_1 x_i}}{1 + e^{b + w_1 x_i}} \\
\log(p_i) &= (b + w_1 x_i) - \log(1 + e^{b + w_1 x_i}) \\
\log(1 - p_i) &= -\log(1 + e^{b + w_1 x_i})
\end{align*}
$$

> Repare que $log(e^x) = x$

Substituindo essas expressões na log-verossimilhança:

$$
\begin{align*}
l(\theta) &= \sum_{i=1}^n  y_i ((b + w_1 x_i) - \log(1 + e^{b + w_1 x_i})) + (1 - y_i)( -\log(1 + e^{b + w_1 x_i}))  \\
&= \sum_{i=1}^n  y_i (b + w_1 x_i) - \log(1 + e^{b + w_1 x_i})
\end{align*}
$$

Separando os somatórios, temos:

$$
l(\theta) = b \sum_{i=1}^n y_i + w_1 \sum_{i=1}^n x_i y_i - \sum_{i=1}^n \log(1 + e^{b + w_1 x_i}).
$$


### Exercício 2

No modelo logístico com um regressor apenas, mostre que o vetor gradiente da log-verossimilhança $ l(\theta) $ é dado por:

$$
\nabla l(\theta) =
\begin{bmatrix}
\frac{\partial l}{\partial b} \\
\frac{\partial l}{\partial w_1}
\end{bmatrix}
=
\begin{bmatrix}
\sum_{i=1}^n y_i - p_i \\
\sum_{i=1}^n x_i y_i - p_i x_i
\end{bmatrix},
$$

onde $ p_i = p(x_i) $.



**Resposta**


Para encontrar o vetor gradiente da log-verossimilhança $ l(\theta) $, calculamos as derivadas parciais em relação a $ b $ e $ w_1 $:

**Derivada parcial em relação a $ b $:**


\begin{align*}
\frac{\partial l}{\partial b} &= \sum_{i=1}^n \left[ y_i - \frac{e^{b + w_1 x_i}}{1 + e^{b + w_1 x_i}} \right] * \\
&= \sum_{i=1}^n \left( y_i - p_i \right)
\end{align*}


> *Olhe a questão acima para ver essa derivação de $p_i$

**Derivada parcial em relação a $w_1$:**


\begin{align*}
\frac{\partial l}{\partial w_1} &= \sum_{i=1}^n \left[ y_i x_i - \frac{e^{b + w_1 x_i}}{1 + e^{b + w_1 x_i}} x_i \right] \\
&= \sum_{i=1}^n \left( y_i x_i - p_i x_i \right) \\
&= \sum_{i=1}^n x_i \left( y_i - p_i \right).
\end{align*}


Portanto, o vetor gradiente é:

$$
\nabla l(\theta) =
\begin{bmatrix}
\sum_{i=1}^n \left( y_i - p_i \right) \\
\sum_{i=1}^n x_i \left( y_i - p_i \right)
\end{bmatrix}.
$$


### Exercício 3

Ainda no modelo logístico com um regressor apenas, mostre que a matriz Hessiana da log-verossimilhança $l(\theta) $ é dada por:

$$
H(l(\theta)) =
- \begin{bmatrix}
\frac{\partial^2 l}{\partial b^2} & \frac{\partial^2 l}{\partial b \partial w_1} \\
\frac{\partial^2 l}{\partial b \partial w_1} & \frac{\partial^2 l}{\partial w_1^2}
\end{bmatrix}
=
- \begin{bmatrix}
\sum_{i=1}^n p_i (1 - p_i) & \sum_{i=1}^n p_i (1 - p_i) x_i \\
\sum_{i=1}^n p_i (1 - p_i) x_i & \sum_{i=1}^n p_i (1 - p_i) x_i^2
\end{bmatrix}.
$$

**Resposta**

Para determinar a matriz Hessiana da log-verossimilhança $l(\theta)$, calculamos as segundas derivadas parciais:

**Derivada segunda em relação a $b$:**


\begin{align*}
\frac{\partial^2 l}{\partial b^2} &= -\sum_{i=1}^n \frac{e^{b + w_1 x_i}}{(1 + e^{b + w_1 x_i})^2} \\
&= -\sum_{i=1}^n p_i (1 - p_i).
\end{align*}


**Derivada mista em relação a $b $ e $w_1$:**


\begin{align*}
\frac{\partial^2 l}{\partial b \partial w_1} &= -\sum_{i=1}^n \frac{e^{b + w_1 x_i}}{(1 + e^{b + w_1 x_i})^2} x_i \\
&= -\sum_{i=1}^n p_i (1 - p_i) x_i.
\end{align*}


**Derivada segunda em relação a $w_1$:**


\begin{align*}
\frac{\partial^2 l}{\partial w_1^2} &= -\sum_{i=1}^n \frac{e^{b + w_1 x_i}}{(1 + e^{b + w_1 x_i})^2} x_i^2 \\
&= -\sum_{i=1}^n p_i (1 - p_i) x_i^2.
\end{align*}


Assim, a matriz Hessiana é:

$$
H(l(\theta)) =
- \begin{bmatrix}
\sum_{i=1}^n p_i (1 - p_i) & \sum_{i=1}^n p_i (1 - p_i) x_i \\
\sum_{i=1}^n p_i (1 - p_i) x_i & \sum_{i=1}^n p_i (1 - p_i) x_i^2
\end{bmatrix}.
$$

## SVM

### Exercício 4

Quais as principais diferenças entre o SVM e uma Regressão Linear?

**Resposta**

Existem duas principais diferenças entre o SVM e a Regressão Linear.

1. Enquanto a regressão linear encontra uma fronteira de decisão apenas minimizando o erro quadrático, o SVM tenta encontrar o melhor separador, para isso maximizando a margem entre os vetores de suporte.

2. O Truque do Kernel possibilita que o SVM encontre soluções de problemas não lineares. Embora possamos usar features polinomiais na regressão linear, o truque do kernel nos permite atingir o mesmo resultado sem calcular diretamente as features no espaço com mais dimensões, de forma que os cálculos são mais rápidos e eficientes.

### Exercício 5

No SVM, quais são os tipos de kernels mais comuns? Como eles são definidos? Em quais situações usamos cada um deles?

**Resposta**

1. **Kernel Linear**:
  - Definição:
  $$ K(x, x') = x \cdot x'$$
  - Usado para problemas linearmente separáveis.
2. **Kernel Polinomial**:
  - Definição:
  $$ K(x, x') = (x \cdot x' + c)^d$$
  - Bom para dados com características polinomiais. É muito flexível, uma vez que podemos alterar o parâmetro $d$, porém um $d$ grande pode ser bastante custoso.

3. **Radial Basis Function (RBF)**

  - Definição:
  $$K(x, x') =  \exp(- \frac {||x - x'||^2}{2σ^2})$$
  - Muito usado na prática. Mapeia os dados para um espço complexo com dimensões infinitas, possibilitando que ele modelo dados muito difíceis.

4. **Kernel Sigmoid**
  - Definição:
  $$K(x, x') = tanh(αx ⋅ x' + c)$$
  - Menos comum, útil em algumas poucas situações. Pode apresentar problemas de convergência, a depender dos valores de $\alpha$ e $c$.


De forma geral, o kernel a ser usado depende da natureza dos dados a serem processados. Escolher o melhor deles para o seu problema cegamente é difícil, e, na prática, é melhor testar várias opções e ver qual se encaixou melhor.

### Exercício 6

O que é uma *Soft Margin* em um SVM? Por que ela é usada nos SVMs?

A Soft Margin no SVM possibilita que o modelo encontre uma margem não estrita, isso é, com alguns pontos dentro dela, ou até classificados erroneamente. Ela é controlada pelo parâmetro c, quanto mais baixo, mais relaxada a margem será. O ajuste da soft margin é essencial no uso do SVM, já que, na prática, os problemas com os quais lidamos não são perfeitamente separáveis. Assim, para garantir que o modelo encontre uma fronteire de decisão boa, que seja capaz de generalizar para novos dados, precisamos permitir que ele 'abandone' alguns pontos ao definir a margem.


```python
#In: 

```
