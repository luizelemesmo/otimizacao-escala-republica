# Otimização de Escalas de Tarefas Domésticas em Repúblicas Estudantis

Este repositório contém a implementação de uma solução computacional para o problema
de alocação de tarefas domésticas em repúblicas estudantis, desenvolvida no contexto da
**Avaliação 02** da disciplina **BCC325 – Inteligência Artificial**, do curso de Ciência da
Computação da **Universidade Federal de Ouro Preto (UFOP)**.

O problema é modelado como um **Problema de Satisfação de Restrições (CSP)** e resolvido
por meio de um algoritmo exato de **busca em profundidade (backtracking)** com **poda por
custo (Branch and Bound)**.

---

## 🧠 Descrição do Problema

A convivência em repúblicas estudantis exige uma organização justa e eficiente das
tarefas domésticas, como a limpeza de cômodos. A atribuição manual dessas tarefas pode
resultar em sobrecarga de alguns moradores, repetição excessiva de atividades e
desconsideração de indisponibilidades individuais.

O objetivo deste projeto é gerar uma **escala de limpeza viável e equilibrada**, alocando
moradores a diferentes tarefas ao longo de um conjunto de semanas, respeitando um
conjunto de restrições rígidas e minimizando um custo associado à alocação.

---

## ⚙️ Técnica de Inteligência Artificial Utilizada

A abordagem adotada baseia-se em técnicas clássicas de Inteligência Artificial, em
especial:

- **Problema de Satisfação de Restrições (CSP)**  
- **Busca em Profundidade (Backtracking)**  
- **Poda por Custo (Branch and Bound)**  

Além disso, é utilizada uma **heurística de penalidade** para desestimular a alocação de
um mesmo morador em semanas consecutivas, quando possível, melhorando a qualidade da
solução final.

---

## 📐 Modelo do Problema

O problema considera:
- um conjunto de moradores;
- um conjunto de semanas;
- um conjunto de cômodos (tarefas);
- dificuldades associadas a cada tarefa;
- indisponibilidades individuais ao longo das semanas.

As principais restrições incluem:
- cada morador pode realizar, no máximo, uma tarefa por semana;
- um morador não pode repetir a mesma tarefa ao longo do horizonte de planejamento;
- todas as demandas de cada cômodo devem ser atendidas;
- indisponibilidades devem ser respeitadas.

O objetivo é minimizar o custo total da escala, considerando dificuldade das tarefas,
indisponibilidade dos moradores e penalidades por trabalho consecutivo.

---

## 🗂 Estrutura do Repositório

```text
.
├── src/
│   └── republica_solver.py
├── txt/
│   └── relatorio.pdf
└── README.md
```

- `src/`: contém a implementação do algoritmo em Python  
- `txt/`: contém o relatório técnico do trabalho em formato PDF  
- `README.md`: documentação geral do projeto  

▶️ **Execução**

O código foi desenvolvido em **Python 3** e não depende de bibliotecas externas.

Um exemplo simplificado de uso é apresentado a seguir:

```python
from republica_solver import RepublicaSolver

solver = RepublicaSolver(
    moradores=[...],
    semanas=[...],
    comodos=[...],
    dificuldades={...},
    indisponibilidades={...},
    vagas_por_semana=...
)

solucao = solver.resolver()
```

A solução retornada corresponde à melhor escala encontrada de acordo com o modelo e as
restrições definidas.

---

## 📊 Resultados

Para instâncias de pequeno e médio porte, típicas de repúblicas estudantis, o algoritmo é
capaz de encontrar soluções ótimas em tempo viável. A utilização da poda por custo é
fundamental para reduzir o espaço de busca e evitar a explosão combinatória.

Resultados experimentais e análises detalhadas podem ser encontrados no relatório
técnico.

---

## 📄 Relatório Técnico

O relatório completo do projeto, contendo:

- definição do problema;
- modelo matemático;
- descrição da implementação;
- análise de resultados;

está disponível na pasta `txt/`.

---

## 👨‍🎓 Autores

- Fernanda Alves Andrade  
- Hugo Augusto Silva de Faria  
- Luiz Henrique de Carvalho  
- Marcos Vinício Euzébio  
- Nicole Bertolino Lamounier Santos  

Curso de Ciência da Computação  
Universidade Federal de Ouro Preto – UFOP  

---

## 📌 Observação

Este repositório tem finalidade acadêmica e foi desenvolvido exclusivamente para fins
educacionais, no contexto da disciplina **BCC325 – Inteligência Artificial**.
