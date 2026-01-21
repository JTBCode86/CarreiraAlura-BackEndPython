# 🐍 Praticando Python: Listas e Tuplas (Alura) + Algoritmos Avançados

Este repositório contém a resolução das atividades práticas da trilha de Python da Alura, além de módulos bônus para aprofundamento técnico.

## 🏗️ Estrutura do Projeto

Os exercícios da trilha Alura (05 ao 13) foram implementados utilizando **Programação Orientada a Objetos (POO)** e **Clean Architecture**, divididos em:
- **Entities:** Modelagem do domínio e regras fundamentais.
- **Use Cases:** Orquestração da lógica de negócio.
- **Presenters:** Camada de interface CLI (Entrada/Saída).

---

## 📚 Sequência de Atividades (Trilha Alura)

### 05 - Organizando notas de um concurso de redação
* **Objetivo:** Ordenar as notas dos participantes em ordem crescente para premiação.
* **Foco:** Algoritmos de ordenação e proteção de dados na Entidade.

### 06 - Registrando voluntários para uma campanha
* **Objetivo:** Criar um fluxo de cadastro contínuo que encerra ao digitar 'sair'.
* **Foco:** Loops de controle e Inversão de Controle entre Presenter e Use Case.

### 07 - Unindo o relatório de estoques
* **Objetivo:** Unificar dois estoques de mercadorias representados como tuplas.
* **Foco:** Imutabilidade de dados e concatenação de tuplas.

### 08 - Reorganizando uma lista de convidados
* **Objetivo:** Permitir a inserção de novos convidados em posições específicas da lista.
* **Foco:** Manipulação de índices e ajuste de posicionamento para o usuário final.

### 09 - Ordenando os eventos
* **Objetivo:** Corrigir uma lista de eventos que foi registrada na ordem inversa.
* **Foco:** Reversão de coleções (método `reverse`) in-place.

### 10 - Corrigindo posições na lista de uma corrida de atletismo
* **Objetivo:** Localizar um nome incorreto na classificação e substituí-lo pelo correto.
* **Foco:** Busca por valor e atualização de estado na camada de domínio.

### 11 - Removendo o último item de um pedido
* **Objetivo:** Automatizar a remoção do último item inserido por engano em uma comanda.
* **Foco:** Comportamento de Pilha (LIFO) e método `pop`.

### 12 - Calculando a média de notas
* **Objetivo:** Processar notas finais de alunos para gerar a média da turma.
* **Foco:** Operações de agregação e formatação de saída numérica.

### 13 - Registrando dados de alunos
* **Objetivo:** Processar strings complexas (Nome, Idade, Nota) e gerar relatórios individuais.
* **Foco:** Parser de dados brutos para Objetos de Negócio.

---

## 🌟 Módulos Bônus (Algoritmos e Estruturas)

> [!IMPORTANT]
> **Observação:** Os projetos bônus listados abaixo **não seguem a mesma estrutura de pastas** dos exercícios anteriores (Clean Architecture). Eles foram organizados de forma distinta para priorizar o estudo específico de lógica algorítmica e estruturas de dados.

### 14 - Estudo de Recursividade (Bônus I)
* **Objetivo:** Implementar soluções para problemas que se dividem em subproblemas menores.
* **Foco:** Pilha de chamadas, caso base e lógica recursiva aplicada.

### 15 - Preenchimento de Matrizes (Bônus II)
* **Objetivo:** Gerenciar e exibir dados dispostos em grades bidimensionais (linhas e colunas).
* **Foco:** Listas aninhadas e manipulação de coordenadas de matrizes.

---

## 🚀 Como executar
Navegue até a pasta da atividade desejada e execute o ponto de entrada principal:
```bash
python main.py