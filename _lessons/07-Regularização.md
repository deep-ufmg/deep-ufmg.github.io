---
layout: page
---

# Regularização

### Exercício 1

(a) Explique o que é um erro de generalização.

(b) Explique brevemente o que cada método abaixo faz e por que, intuitivamente, ele pode ajudar a resolver um erro de generalização.

1.  Penalização com norma L2.
2.  Data augmentation.
3.  Early stopping.

#### Resposta

a) 

Um erro de generalização ocorre quando um modelo falha em ajustar corretamente aos dados de teste, levando a resultados imprecisos. Um erro de generalização pode ocorrer por ajuste excessivo aos dados de treino (overfitting), ou ajustes insuficientes (underfitting).

b)

1. A penalização L2 é utilizada para reduzir overfitting e, portanto, melhora a generalização de um modelo. Para isso, ela adiciona um termo à função de perda do modelo que penaliza pesos grandes, forçando-os a ficarem mais próximos de 0. Isso impede que certos pesos se sobressaem em relação aos demais e dominem o modelo, o que o tornaria menos complexos.

2. O Data Augmentation é utilizado para aumentar a quantidade e diversidade dos dados de treinamento, criando novas instâncias a partir das existentes. Esse método ajuda a resolver o problema de generalização, pois diversifica os dados de treinamento, fazendo com que o modelo aprenda novos padrões.

3.  O Early Stopping consiste em interromper o treinamento do modelo assim que o desempenho dele no conjunto de validação começa a piorar, ou quando o desempenho não melhora por um número de épocas durante o treinamento. Essa técnica evita que o modelo se ajuste excessivamente aos dados de treino.

### Exercício 2

Considere a seguinte função objetiva de mínimos quadrados regularizada L2 para uma regressão linear:

$$f(w) = ||w”x − y|| + λ||w||^2$$


Como o λ afeta a reta estimada?

#### Resposta

O termo λ adiciona uma penalidade aos coeficientes da reta estimada, forçando-os a serem menores. Quanto maior o valor de λ, maior será a penalidade da reta, o que resultará em um menor ajuste dela aos dados. Por outro lado, quando λ é pequeno ou igual a zero, a penalidade é baixa e a reta estimada pode se ajustar mais aos dados de treinamento. Assim, λ controla o equilíbrio entre o ajuste aos dados de treinamento e a generalização da reta estimada.

### Exercício 3

Suponha que você esteja treinando uma rede com dropout e a probabilidade de um nó ser **mantido** muda de 0.6 para 0.5.
1. O que acontece com o efeito de regularização ao diminuir a probabilidade de um nó ser mantido na rede?
2. Qual o impacto dessa mudança no erro calculado com o conjunto de treino?
3. Durante o treinamento com dropout, a rede é modificada diversas vezes. Alguma modificação deve ser feita na rede em tempo de teste?

#### Resposta

a)

O efeito de regularização tende a aumentar.

b)

Em geral, espera-se que o erro calculado aumente. Isso, pois com a probabilidade menor de se manter um nó, mais neurônios serão desligados durante o treinamento, o que pode levar a uma perda de capacidade de representação dos dados. Como consequência, o modelo pode ter mais dificuldade em ajustar-se aos dados de treinamento, e assim o erro pode aumentar. No entanto, o aumento de erro no treinamento não necessariamente indica um desempenho pior em dados não vistos.

c) 

Em tempo de teste, a rede deve ser utilizada por completo.

### Exercício 4
Considere um caso em que você tem quatro atributos $x_1,...,x_4$ e uma variável dependente $y = 2x_1$. Crie um dataset muito pequeno com 5 exemplos no qual uma regressão linear sem regularização terá um número infinito de soluções para os coeficientes com $w_1 = 0$. Como você acha que este modelo se sairia com novos dados para teste? Regularização ajudaria?

#### Resposta

Basta criar um conjunto de pontos perfeitamente colineares. Com isso, exisitirá um número infinito de soluções válidas, incluindo soluções com $w_1 = 0$. Em um conjunto de testes, os novos dados provavelmente não seriam colineares, de forma que as soluções encontradas pelo nosso modelo não seriam capazes de generalizar bem. Mesmo com regularização, nosso modelo provavelmente ainda não seria capaz de encontrar a solução desejada $y = 2x_1$ dentre as infinitas possibilidades.

### Exercício 5

Suponha que você tenha um modelo que fornece cerca de 80% de precisão no treinamento, bem como nos dados de teste fora da amostra. Você recomendaria aumentar a quantidade de dados ou ajustar o modelo para melhorar a precisão?

#### Resposta

Nesse caso, nosso modelo não está sofrendo de overfitting, e, visto que ainda há uma taxa de erro considerável nos dados de teste, é possível que estejamos em um cenário de underfitting. Nesse caso, aumentar a capacidade do modelo seria importante para garantir que ele fosse potente o suficiente para capturar a nossa base de dados. Aumentar a quanridade de dados poderia ser útil, porém nesse caso aprimorar o modelo provavelmente teria um impacto maior.

### Exercício 6

Flávio dividiu os dados de classificação rotulados em uma parte usada para construção do modelo e outra parte para validação. Flávio então testou 1000 arquiteturas de redes neurais aprendendo parâmetros (backprop) na parte de construção do modelo e testando sua precisão na parte de validação, escolhendo aquele que teve melhor desempenho. Discuta por que o modelo resultante provavelmente produzirá menor precisão nos dados de teste fora da amostra em comparação aos dados de validação, mesmo que os dados de validação não tenham sido usados ​​para aprender parâmetros. Você tem alguma recomendação para Flávio sobre o uso dos resultados de suas 1000 validações?

#### Resposta

Por mais que os dados de validação não tenham sido vistos no treino, eles foram usados para selecionar o melhor modelo encontrado. Dessa forma, a rede escolhida foi uma adequada aos dados de validação, que embora provavelmente seria também boa no teste, obteria métricas certamente menores do que na validação. Em outros termos, ao fazer essa seleção, é como se estivéssemos "overfitando" a rede aos dados de validação. Mesmo assim, o ideal é ainda escolher as redes com as melhores métricas na validação, e descatar as demais. É importante notar que a métrica dessa rede não será as que o modelo encontraria nos testes, então seria ainda necessário testar a rede selecionadas no conjunto de teste para obter as métricas.


