---
layout: page
---

# Otimização

> - Método de Newton
> - Gradiente Descendente

### Exercício 1

Aplique duas iterações do método de Newton para encontrar o ponto máximo da seguinte função:
$$ f(x) = -(x - 3)^4 $$

para $ x_0 = 1 $.

#### Resposta

O método de Newton é dado pela fórmula:
$$
x_{n+1} = x_n - \frac{f'(x_n)}{f''(x_n)},
$$
onde $ f'(x) $ e $f''(x)$ são, respectivamente, a primeira e a segunda derivadas de $f(x)$.

Temos que:
   $$
   f'(x) = -4(x - 3)^3
   $$

   e

   $$
   f''(x) = -12(x - 3)^2
   $$

Agora, aplicamos duas iterações do método de Newton com $x_0 = 1$:

1. Para $x_0 = 1$:
   $$
   f'(1) = -4(1 - 3)^3 = -4(-2)^3 = -4(-8) = 32,
   $$

   e

   $$
   f''(1) = -12(1 - 3)^2 = -12(-2)^2 = -12(4) = -48.
   $$
   Substituímos na fórmula de Newton:
   $$
   \begin{align*}
    x_1 &= x_0 - \frac{f'(x_0)}{f''(x_0)} \\
    &= 1 - \frac{32}{-48} \\
    &= 1 + \frac{2}{3} \\
    &= \frac{5}{3} \\
   \end{align*}
   $$

2. Para $x_1 = \frac{5}{3}$:
   $$
   f'\left(\frac{5}{3}\right) = -4\left(\frac{5}{3} - 3\right)^3 = -4\left(-\frac{4}{3}\right)^3 = -4\left(-\frac{64}{27}\right) = \frac{256}{27},
   $$

   e

   $$
   f''\left(\frac{5}{3}\right) = -12\left(\frac{5}{3} - 3\right)^2 = -12\left(-\frac{4}{3}\right)^2 = -12\left(\frac{16}{9}\right) = -\frac{192}{9} = -\frac{64}{3}.
   $$

   Substituímos na fórmula:

   \begin{align*}
      x_2 &= x_1 - \frac{f'(x_1)}{f''(x_1)} \\
      &= \frac{5}{3} - \frac{\frac{256}{27}}{-\frac{64}{3}} \\
      &= \frac{5}{3} + \frac{256}{576} \\
      &= \frac{5}{3} + \frac{4}{9} \\
      &= \frac{19}{9}
   \end{align*}

Portanto, após duas iterações, $ x_2 = \frac{19}{9} $.

### Exercício 2

Utilizando a mesma função do exercício anterior, aplique o método do gradiente ascendente usando learning rate $ \alpha = 0.01 $ e $ x_0 = 1 $. Compare os dois resultados.

No método do gradiente ascendente, a fórmula é:
$$
x_{n+1} = x_n + \alpha f'(x_n).
$$

1. Para $x_0 = 1$:
   $$
   f'(1) = 32 \quad \text{(calculado anteriormente)},
   $$
   $$
   x_1 = x_0 + \alpha f'(x_0) = 1 + 0.01 \cdot 32 = 1 + 0.32 = 1.32.
   $$

2. Para $x_1 = 1.32$:
   $$
   f'(1.32) = -4(1.32 - 3)^3 = -4(-1.68)^3 = -4(-4.75) = 19.04,
   $$
   $$
   x_2 = x_1 + \alpha f'(x_1) = 1.32 + 0.01 \cdot 19.04 = 1.32 + 0.1904 = 1.5104.
   $$

Portanto, após duas iterações, $x_2 \approx 1.5104$.

**Comparação dos Resultados**

- Pelo método de Newton, o ponto após duas iterações é $x_2 = \frac{19}{9} \approx 2.111$.
- Pelo gradiente ascendente, o ponto após duas iterações é $x_2 \approx 1.5104$.

O método de Newton converge mais rapidamente para o máximo devido à utilização da segunda derivada para ajustar os passos.


### Exercício 3
Considere a função $y(x) = 3x^2$, e ponto inicial $x_0 = -2$. Lembre-se do método atenuado por momentum de descida gradiente:
$$
	x^{(t+1)} = x^{(t)} - \alpha \left( (1-\beta) \nabla L(x^{(t)}) + \beta  \mathbf{V}^{(t-1)}\right).
$$

(a) Esboce o gráfico da função duas vezes. Na primeira, esboce como funcionaria três iterações do método de descida gradiente com $\alpha > 1/3$. Na segunda, esboce como funcionaria três iterações do método de descida gradiente com $\alpha < 1/3$.

(b) Agora, informe qual será o $x_1$ e o $x_2$ encontrados após a primeira e a segunda iterações do método atenuado por momentum de descida gradiente com parâmetros $\alpha = 1/4$, e $\beta = 1/3$.



#### Resposta

(a)

![image.png](08-Otimização_files/image.png)



(b)

**Iteração 1 ($t=1$):**

1. Calcular $\mathbf{V}^{(1)}$:
$$
\mathbf{V}^{(1)} = (1-\beta) \nabla L(x^{(0)}) + \beta \mathbf{V}^{(0)}.
$$
Substituindo:
$$
\mathbf{V}^{(1)} = \left(1 - \frac{1}{3}\right) (6x^{(0)}) + \frac{1}{3} \cdot 0,
$$
$$
\mathbf{V}^{(1)} = \frac{2}{3} \cdot 6 \cdot (-2) = -8.
$$

2. Atualizar \(x^{(1)}\):
$$
x^{(1)} = x^{(0)} - \alpha \mathbf{V}^{(1)}.
$$
Substituindo:
$$
x^{(1)} = -2 - \frac{1}{4} \cdot (-8),
$$
$$
x^{(1)} = -2 + 2 = 0.
$$

---

**Iteração 2 ($t=2$):**

1. Calcular $\mathbf{V}^{(2)}$:
$$
\mathbf{V}^{(2)} = (1-\beta) \nabla L(x^{(1)}) + \beta \mathbf{V}^{(1)}.
$$
Substituindo:
$$
\mathbf{V}^{(2)} = \left(1 - \frac{1}{3}\right) (6x^{(1)}) + \frac{1}{3} \mathbf{V}^{(1)}.
$$
Como \(x^{(1)} = 0\), temos:
$$
\mathbf{V}^{(2)} = 0 + \frac{1}{3} \cdot (-8),
$$
$$
\mathbf{V}^{(2)} = -\frac{8}{3}.
$$

2. Atualizar \(x^{(2)}\):
$$
x^{(2)} = x^{(1)} - \alpha \mathbf{V}^{(2)}.
$$
Substituindo:
$$
x^{(2)} = 0 - \frac{1}{4} \cdot \left(-\frac{8}{3}\right),
$$
$$
x^{(2)} = \frac{2}{3}.
$$

---



Após as iterações:
1. $x_1 = 0$,
2. $x_2 = \frac{2}{3}$.

Portanto:
$$
\boxed{x_1 = 0, \quad x_2 = \frac{2}{3}.}
$$


### Exercício 4

Mostre que se $n$ números são tais que a soma deles é $s$, então a soma dos seus quadrados é minimizada precisamente quando todos eles são iguais a $s/n$ .

#### Resposta


Definimos o Lagrangiano:

$$
\mathcal{L}(x_1, \dots, x_n, \lambda) = \sum_{i=1}^n x_i^2 + \lambda \left( s - \sum_{i=1}^n x_i \right).
$$

Derivando em relação a $x_i$ e $\lambda$:

1. Para $x_i$:
$$
\frac{\partial \mathcal{L}}{\partial x_i} = 2x_i - \lambda = 0 \implies x_i = \frac{\lambda}{2}.
$$

2. Para $\lambda$:
$$
\frac{\partial \mathcal{L}}{\partial \lambda} = s - \sum_{i=1}^n x_i = 0 \implies \sum_{i=1}^n x_i = s.
$$


Como $x_i = \frac{\lambda}{2}$ para todos $i$, segue que:

$$
\sum_{i=1}^n x_i = n \cdot \frac{\lambda}{2} = s \implies \lambda = \frac{2s}{n}.
$$

Logo:

$$
x_i = \frac{\lambda}{2} = \frac{s}{n}, \quad \forall i.
$$



#### Outra Solução

1. Decomponha $ x_i $ como:

$$
x_i = \bar{x} + d_i, \quad \text{onde } \bar{x} = \frac{s}{n} \text{ e } \sum_{i=1}^n d_i = 0.
$$

2. Substitua na soma dos quadrados:

$$
\sum_{i=1}^n x_i^2 = \sum_{i=1}^n (\bar{x}^2 + 2\bar{x}d_i + d_i^2).
$$

3. Simplifique:

- $ \sum_{i=1}^n \bar{x}^2 = n\bar{x}^2 $,
- $ \sum_{i=1}^n 2\bar{x}d_i = 0 $ (pois $ \sum_{i=1}^n d_i = 0 $),
- Resta $ \sum_{i=1}^n x_i^2 = n\bar{x}^2 + \sum_{i=1}^n d_i^2 $.

4. Para minimizar $ \sum_{i=1}^n x_i^2 $, $ \sum_{i=1}^n d_i^2 $ deve ser zero, o que ocorre quando $ d_i = 0 $ para todos $i $.



### Exercício 5

Considere a função quadrática $Q(x) = \frac{1}{2} x^T Ax − bx$, com A uma matriz quadrada não singular de ordem $n$. 

(a) Encontre o gradiente $\nabla Q$;

(b) Escreva a iteração de descida do gradiente;

(c) Encontre o $H_Q$ Hessiano;

(d) Escreva a iteração dada pela fórmula de Newton e calcule seu limite.

(a)

O gradiente da função $Q(x)$ em relação a $x$ é:

$$
\nabla Q(x) = \frac{\partial Q}{\partial x}.
$$

Calculando os termos:
1. O primeiro termo: 
$$
\frac{\partial}{\partial x} \left( \frac{1}{2} x^T A x \right) = A x,
$$
pois $x^T A x$ é uma forma quadrática, e o gradiente resulta em $A x$.
   
2. O segundo termo:
$$
\frac{\partial}{\partial x} (-b^T x) = -b.
$$

Logo, o gradiente é:

$$
\nabla Q(x) = A x - b.
$$

---

(b)

A iteração da descida do gradiente segue a fórmula:

$$
x^{(t+1)} = x^{(t)} - \alpha \nabla Q(x^{(t)}),
$$

onde $\alpha > 0$ é a taxa de aprendizado. Substituindo o gradiente $\nabla Q(x) = A x - b$, temos:

$$
x^{(t+1)} = x^{(t)} - \alpha (A x^{(t)} - b).
$$

---

(c)

O Hessiano da função $Q(x)$ é:

$$
H_Q = \nabla^2 Q(x).
$$

Como $Q(x)$ é uma função quadrática, o Hessiano é constante e igual à matriz $A$:

$$
H_Q = A.
$$

---

(d)

A fórmula de Newton para otimização é:

$$
x^{(t+1)} = x^{(t)} - \big(H_Q\big)^{-1} \nabla Q(x^{(t)}).
$$

Substituindo $H_Q = A$ e $\nabla Q(x) = A x - b$, temos:

$$
x^{(t+1)} = x^{(t)} - A^{-1} (A x^{(t)} - b).
$$

Simplificando:

$$
x^{(t+1)} = x^{(t)} - (x^{(t)} - A^{-1} b),
$$

$$
x^{(t+1)} = A^{-1} b.
$$




### Exercício 6

Seja $A$ uma matriz quadrada não singular de ordem $n$ e $b \in \mathbb{R}^n$ um dado vetor. Considere o sistema linear $Ax = b$. A solução deste sistema pode ser aproximada usando os seguintes passos:

(a) Associe a função de custo $C(x) = ||Ax−b||$. Encontre seu gradiente, $\nabla C(x)$, e o e Hessiano, $H_C(x)$;

(b) Escreva a iteração do algoritmo de descida de gradiente que converge para a
solução do sistema $x$ com o valor inicial $x_0 = 0$;

(c) Escreva a iteração de Newton que converge para a solução do sistema $x$ com o valor inicial $x_0 = 0.$

#### Resposta

(a)

A função de custo associada é:

$$
C(x) = \|Ax - b\|^2 = (Ax - b)^T (Ax - b).
$$

**Gradiente $\nabla C(x)$**

Expandindo $C(x)$:

$$
C(x) = (Ax - b)^T (Ax - b) = x^T A^T A x - 2b^T A x + b^T b.
$$

Derivando em relação a $x$:

1. Primeiro termo:
$$
\frac{\partial}{\partial x} \left(x^T A^T A x \right) = 2 A^T A x.
$$

2. Segundo termo:
$$
\frac{\partial}{\partial x} \left(-2b^T A x \right) = -2 A^T b.
$$

3. Terceiro termo:
$$
\frac{\partial}{\partial x} \left(b^T b \right) = 0 \quad \text{(não depende de \(x\))}.
$$

Logo, o gradiente é:

$$
\nabla C(x) = 2 A^T (A x - b).
$$


**Hessiano $H_C(x)$**

O Hessiano é dado pela derivada do gradiente. Como $\nabla C(x) = 2 A^T A x - 2 A^T b$, temos:

$$
H_C(x) = \nabla^2 C(x) = 2 A^T A.
$$

---

(b)

A iteração da descida de gradiente é:

$$
x^{(t+1)} = x^{(t)} - \alpha \nabla C(x^{(t)}),
$$

onde $\alpha > 0$ é a taxa de aprendizado. Substituindo o gradiente $\nabla C(x) = 2 A^T (A x - b)$:

$$
x^{(t+1)} = x^{(t)} - \alpha \cdot 2 A^T (A x^{(t)} - b).
$$

Simplificando:

$$
x^{(t+1)} = x^{(t)} - 2 \alpha A^T A x^{(t)} + 2 \alpha A^T b.
$$

Com $x_0 = 0$, a iteração converge para a solução $x^* = A^{-1} b$ se $\alpha$ for escolhido adequadamente.

---

(c)

A iteração de Newton é dada por:

$$
x^{(t+1)} = x^{(t)} - (H_C(x^{(t)}))^{-1} \nabla C(x^{(t)}).
$$

Substituímos o Hessiano $H_C(x) = 2 A^T A$ e o gradiente $\nabla C(x) = 2 A^T (A x - b)$:

$$
x^{(t+1)} = x^{(t)} - (2 A^T A)^{-1} \cdot 2 A^T (A x^{(t)} - b).
$$

Simplificando:

$$
x^{(t+1)} = x^{(t)} - (A^T A)^{-1} A^T (A x^{(t)} - b).
$$

Mais simplificado ainda:

$$
x^{(t+1)} = (A^T A)^{-1} A^T b.
$$





```python
#In: 

```
