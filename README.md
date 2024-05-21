## RPCW2024-Normal

## João Miguel Ferreira Loureiro - PG53924

## EX 1

Criei as classes Feira(representa feira), Ferramenta (representa o trator e outros utensilios/maquinas), Individuo(pessoas que residem/trabalham numa quinta) donde existem as sub-classes Animal(qualquer animal que la resida seja gado ou que tenha uma função pratica), Dono(dono da quinta e a sua familia direta: filhos e esposo/a) e Trabalhador(trabalhador temporarios), a classe Produto(que representa um produto cultivado na quinta), donde existem as sub-classes Fruta e Vegetal, a classe Quinta (que representa uma quinta) e a classe Tarefa (que representa as varias tarefas que um individuo ou ferramenta possa executar).

Em termos de data properties temos "aloja" que relaciona a quinta a todos os individuos e ferramentas que la residem, "cultiva" relaciona a quinta aos produtos que cultiva, "familia" que relaciona dois individuos da mesma familia, "faz" que relaciona um individuo à tarefa que executa, "troca" dois individuos que troquem entre si, "vende" individuo aos produtos que vende e "vendeEM" indiviudo a feira em que vende.

Os data properties são self-explanatory, mas acrescentei dois que nao sao especificados no texto porque faziam sentido (quantidadeProduto e valorPriduto).

## EX 2

Correr primeiro o med_doencas.py, depois o med_tratamentos.py e por ultimo o med_doentes.py. Como sou o pg53924, usei o ficheiro json com esse nome.

De notar que eu tentei normalizar os nomes para camel case mas alguns nao ficaram com o efeito desejado, pelo o que será um aspeto a melhorar.
