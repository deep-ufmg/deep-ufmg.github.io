---
layout: page
---


# Regressão Linear

> Regressão Linear e seus possíveis problemas práticos.
>
> Algumas questões dessa lista são bastante desafiadoras! Não se desanime se não conseguir respondê-las.


## 1. Suponha que temos alguns dados $x_1, \ldots, x_n \in \mathbb{R}$. Nosso objetivo é encontrar uma constante $b$ tal que $\sum_i (x_i - b)^2$ seja minimizada.

   1. Encontre uma solução analítica para o valor ótimo de $b$.
   2. Como este problema e sua solução se relacionam com a distribuição normal?
   3. O que acontece se mudarmos a perda de $\sum_i (x_i - b)^2$ para $\sum_i |x_i - b|$? Você consegue encontrar a solução ótima para $b$?


## Respostas

1

Para encontrar o valor de $b$ que minimiza $\sum_i (x_i - b)^2$, derivamos a função de perda em relação a $b$ e igualamos a zero:

$
\frac{\partial}{\partial b} \sum_i (x_i - b)^2 = -2 \sum_i (x_i - b) = 0.
$

Resolvendo para $b$:

$
\sum_i (x_i - b) = 0 \quad \implies \quad b = \frac{\sum_i x_i}{n}.
$

Portanto, o valor ótimo de $b$ é a média dos valores $x_i$:

$
b = \bar{x}.
$

---

2

Minimizar o erro quadrático médio como fazemos aqui é equivalente a maximizar a log-versossimilhança da distribuição normal.

A normal é dada pela seguinte fórmula:
$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)
$$

> - $ \mu $ é a média,
> - $ \sigma $ é o desvio padrão,
> - $ x $ é a variável aleatória.

Podemos definir a verossimilhança da normal da seguinte forma:

$$
L(\mu, \sigma^2 \mid x_1, x_2, \dots, x_n) = \prod_{i=1}^n \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right)
$$

Tirando o log, chegamos na log-verossimilhança, dada pela seguinte fórmula:

$$
\ell(\mu, \sigma^2 \mid x_1, x_2, \dots, x_n) = -\frac{n}{2} \log(2\pi) - \frac{n}{2} \log(\sigma^2) - \frac{1}{2\sigma^2} \sum_{i=1}^n (x_i - \mu)^2
$$

Repare que os termos inicias não dependem de x, podemos, portanto, considerar apenas o termo final:

$$ \sum_{i=1}^n (x_i - \mu)^2$$

Que é justamente o erro quadrático!






---

3


Ao usar o erro absluto médio, em vez do erro quadrático médio, a nossa função de custo deixa de ser diferenciável. Desta forma, não podemos encontrar a solução ótima da mesma forma como fizemos no exercício 1.

Ainda assim, é possível encontrar uma solução ótima analiticamente, que, neste caso, é a mediana dos nossos dados. Intuitivamente, podemos pensar que como a mediana divide os dados no meio, teremos a mesma quantidade de pontos sendo menores e maiores que ela, o que a torna o ponto que minimiza a distância absoluta.

Para se convencer da validade desse resultado, derive a distância absoluta com relação a b em dois intervalos distintos: para $x \leq b$ e $ x > b$.



## 2. Lembre-se de que uma das condições para que o problema de regressão linear seja solucionável é que a matriz de design $\mathbf{X}^\top \mathbf{X}$ tenha posto completo.

   1. O que acontece se isso não for o caso?
   2. Como você poderia corrigir isso? O que acontece se você adicionar uma pequena quantidade de ruído Gaussiano independente, coordenada por coordenada, a todas as entradas de $\mathbf{X}$?
   3. Qual é o valor esperado da matriz de design $\mathbf{X}^\top \mathbf{X}$ neste caso?
   4. O que acontece com o gradiente estocástico descendente quando $\mathbf{X}^\top \mathbf{X}$ não tem posto completo?


1

Caso a matriz não tenha posto completo, ela não é inversível, e logo não podemos encontrar a solução dos mínimos quadrados pelo método analítico normal, $ \hat\beta=(X^⊤X)^{−1}X^⊤y$.

---

2

Adicionar um ruído gaussiano independente é uma forma de corrigir este problema. Ao adicionar pequenas perturbações em nossos dados, eles (muito provavelmente) deixam de ser colineares. Com isso, nossa matriz ruidosa terá posto completo, será inversível, e, portanto, podemos usar o método tradicional nela.

---

3

Se adicionarmos ruído de média 0 e desvio padrão $\sigma$ à nossa entrada, o valor de cada elemento será acrescido independentemente de um ruído aleatório. Ao fazermos a multiplicação $X^⊤X$, toda a diagonal da matriz resultante terá seu valor acrescido de $\sigma^2$ (note que a diagonal contém o quadrado dos elementos de x). Em contrapartida, o VALOR ESPERADO dos elementos fora da diagonal não será alterado, uma vez que o ruído é centrado em zero, e logo, na média, as perturbações se cancelarão. Assim temos que:

$$E(X'^⊤X') = X^⊤X + n\sigma^2I$$

onde $I$ é a matriz identidade, e $n$ o número de amostras.

---

4

O gradiente descendente não é afetado, visto que ele não depende da inversibilidade da matriz. O fato do posto não ser completo, no entanto, indica que o espaço contém direções redundantes, o que pode dificultar a convergência do SGD.

## 7. O que acontece se você quiser usar regressão para estimar realisticamente preços de casas ou ações?

   1. Mostre que a suposição de ruído Gaussiano aditivo, isto é, $y = \mathbf{X}\boldsymbol{\beta} + \epsilon$, com $\epsilon \sim \mathcal{N}(0, \sigma^2)$, não é apropriada.
Dica: Considere se é possível termos preços negativos devido ao ruído. Como as flutuações nos preços realmente se comportam?
> A suposição do ruído aditivo diz que nossos dados vem de uma combinação linear de nossas features + um ruído gaussiano $\epsilon$.
   2. Por que a regressão no logaritmo do preço seria muito melhor, isto é, $y = \log(\text{preço})$?
   3. O que você precisa considerar ao lidar com penny stocks, isto é, ações com preços muito baixos? Dica: é possível negociar a todos os preços? Por que isso é um problema maior para ações baratas? Para mais informações, revise o famoso modelo de Black-Scholes para precificação de opções (Black and Scholes, 1973).


1

No caso de preçoes de ativos, essa suposição não é válida por alguns motivos.

1. Ao adicionar um ruído gaussiano, o preço poderia ficar negativo, o que não é válido.
2. Na prática, variações no preço são relativas ao preço base. Uma ação barata pode variar em alguns centavos, enquanto uma casa varia em milhares de reais. Além disso, mesmo considerando o mesmo ativo, a variação positiva e negativa tem impactos diferentes. Imagine uma ação de $R\$100$. Um aumento de $R\$50$ no preço e uma queda de $R\$50$ tem impactos bastante diferentes.

---

2

Ao tirar o log do preço, nós temos algumas vantagens para o nosso modelo.

1. O modelo agora prevê apenas preços positivos, já que a função log não está definida para números negativos.
2. As flutuações da previsão passam a ser relativas ao preço.
> se y = 1, o preço = 10. Se y = 2, o preço = 100, se y = 3, o preço = 1000. note que uma mudança linear na previsão resulta numa mudança multiplicativa no preço.

---

3

Existe um incremento mínimo que o preço de uma ação pode ter (1 centavo por exemplo). Assim, ao tratarmos de ações muito baratas, nós saímos de um cenário contínuo, e passamos para um discreto, em que os preços podem assumir apenas alguns poucos valores pré-determindos.

> É claro, para ações mais caras o cenário real também é discreto, mas nas penny stocks, esse variação mínima representa um percentual grande do preço, e é bem mais problemática. Para ações mais caras, podemos assumir que os dados são contínuos na prática.

## 8. Suponha que queremos usar regressão para estimar o número de maçãs vendidas em uma mercearia.

   1. Quais são os problemas com um modelo de ruído aditivo Gaussiano? Dica: você está vendendo maçãs, não petróleo.
   2. A **distribuição de Poisson** captura distribuições sobre contagens. Ela é dada por

      $p(k \mid \lambda) = \frac{\lambda^k e^{-\lambda}}{k!}$.

      Aqui, $\lambda$ é a taxa esperada, e $k$ é o número de eventos observados. Prove que $\lambda$ é o valor esperado das contagens $k$.
   3. Projete uma função de perda associada à distribuição de Poisson.
   4. Projete uma função de perda para estimar $\log \lambda$ em vez de $\lambda$.


1

Os problemas surgem por que vendemos poucas maçãs, e, além disso, o número de maçãs vendidas é discreta. Os problemas são similares aos descritos no exercício acima.

---

2

A distribuição de Poisson é dada por:

$$p(k \mid \lambda) = \frac{\lambda^k e^{-\lambda}}{k!},$$

onde $k \in {0, 1, 2, \dots}$ é o número de eventos, e $\lambda > 0$ é a taxa esperada.

Queremos provar que $\mathbb{E}[k] = \lambda$.

O valor esperado de $k$ é definido como:

$$\mathbb{E}[k] = \sum_{k=0}^\infty k \cdot p(k \mid \lambda).$$

Substituímos $p(k \mid \lambda)$ na equação:

$$\mathbb{E}[k] = \sum_{k=0}^\infty k \cdot \frac{\lambda^k e^{-\lambda}}{k!}.$$


Reescrevemos $k \cdot \frac{\lambda^k}{k!}$ como:

$$k \cdot \frac{\lambda^k}{k!} = \frac{\lambda^k}{(k-1)!}.$$

Alteramos o índice de somação ($k \to k+1$) para já que o fatorial não está definido para números negativos. (Repare que, no somatório original, quando $k=0$, o valor também era 0, assim esse primeiro termo pode ser cortado)

$$\mathbb{E}[k] = \sum_{k=1}^\infty \frac{\lambda^k}{(k-1)!} e^{-\lambda}.$$

Definimos $j = k-1$, o que implica $j = 0, 1, 2, \dots$. Assim, a equação torna-se:

$$\mathbb{E}[k] = \lambda \sum_{j=0}^\infty \frac{\lambda^j}{j!} e^{-\lambda}.$$

O termo $\sum_{j=0}^\infty \frac{\lambda^j}{j!}$ é a expansão da série de Taylor de $e^\lambda$, portanto:

$$\sum_{j=0}^\infty \frac{\lambda^j}{j!} = e^\lambda.$$

Substituímos isso na equação:

$$\mathbb{E}[k] = \lambda e^{-\lambda} \cdot e^\lambda.$$

Como $e^{-\lambda} \cdot e^\lambda = 1$, temos:

$$\mathbb{E}[k] = \lambda.$$

Portanto, o valor esperado de $k$ é $\lambda$.

---

3

Podemos construir uma função de perda baseada na verossimilhança (usaremos a Negative Log-Likelihood, ou NLL) da distribuição de Poisson. Nosso objetivo aqui será que o nosso modelo aprenda o parâmetro $\lambda$, que define a Poisson.

Para a distruibuição de Poisson, a NLL é dada pela seguinte expressão:

$$NLL = -\sum_i log(p(k_i | \lambda_i)) = -\sum_i(k_ilog(\lambda_i) - \lambda_i - log(k_i!))$$

> Para encontrar essa fórmula, basta tirar o log da PDF de Poisson.

Como $log(k_i!)$ é constante em relação a $\lambda_i$, podemos ignorá-lo. Logo, chegamos em:

$$NLL = \sum_i(\lambda_i - k_ilog(\lambda_i))$$

---

4

Por simplicidade, denotemos $\mu_i = log(\lambda_i)$. Logo, temos também que $\lambda_i = e^{\mu_i}$. Basta substituir na equação anterior.

$$NLL = \sum_i(e^{\mu_i} - k_i \mu_i)$$



Referências:

https://d2l.ai/chapter_linear-regression/linear-regression.html


```python
#In: 

```
