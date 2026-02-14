# SeqAlignX - Alinhamento Global

## Descrição

O **SeqAlignX** é uma implementação educacional do algoritmo **Needleman-Wunsch** para alinhamento global de sequências biológicas. Este algoritmo é fundamental em bioinformática para comparar sequências de DNA, RNA ou proteínas e identificar similaridades.

### O que é Alinhamento Global?

O alinhamento global busca encontrar a melhor correspondência entre **duas sequências completas**, introduzindo gaps (espaços) quando necessário. É diferente do alinhamento local, que busca apenas regiões similares.

**Aplicações:**
- Comparação de genes homólogos entre espécies
- Identificação de mutações
- Filogenia e estudos evolutivos
- Análise de variantes

## Funcionalidades

- **Implementação Completa**: Algoritmo Needleman-Wunsch puro em Python
- **Matriz de Pontuação**: Visualização da matriz de programação dinâmica
- **Cálculo de Score**: Pontuação do melhor alinhamento possível
- **Sem Dependências**: Usa apenas Python padrão

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Nenhuma dependência externa necessária!

### Instalação

```bash
git clone https://github.com/FellypeMelo/seqalignx.git
cd seqalignx
```

Pronto! Não precisa instalar nada mais.

## Como Usar

### Execução Básica

```bash
python main.py
```

### Personalizando Sequências

Edite as sequências no final do arquivo `main.py`:

```python
seq1 = "GATTACA"
seq2 = "GCATGCU"
```

### Exemplo de Saída

```
============================================================
SeqAlignX - Alinhamento Global (Needleman-Wunsch)
============================================================

Sequência 1: GATTACA
Sequência 2: GCATGCU

Score de Alinhamento: 0

Matriz de Pontuação:
       G   C   A   T   G   C   U
   0  -1  -2  -3  -4  -5  -6  -7
G -1   1   0  -1  -2  -3  -4  -5
A -2   0   0   1   0  -1  -2  -3
T -3  -1  -1   0   2   1   0  -1
T -4  -2  -2  -1   1   1   0  -1
A -5  -3  -3   0   0   0   0  -1
C -6  -4  -2  -1  -1  -1   1   0
A -7  -5  -3  -1  -2  -2   0   0

Alinhamento concluído!
```

## Algoritmo Needleman-Wunsch

### Passo 1: Inicialização

Cria-se uma matriz de (m+1) × (n+1), onde m e n são os comprimentos das sequências.

- Primeira linha: 0, -1, -2, -3, ... (penalidades de gap)
- Primeira coluna: 0, -1, -2, -3, ... (penalidades de gap)

### Passo 2: Preenchimento

Para cada célula (i, j), calculamos:

```
match = matriz[i-1][j-1] + (1 se seq1[i-1] == seq2[j-1] senão -1)
delete = matriz[i-1][j] + (-1)  # Gap na sequência 2
insert = matriz[i][j-1] + (-1)  # Gap na sequência 1

matriz[i][j] = max(match, delete, insert)
```

### Passo 3: Traceback (Não implementado ainda)

Partindo do canto inferior direito, retrocedemos para reconstruir o alinhamento.

### Sistema de Pontuação

| Operação | Score | Descrição |
|----------|-------|-----------|
| **Match** | +1 | Bases iguais (A=A, T=T, etc.) |
| **Mismatch** | -1 | Bases diferentes (A≠T, etc.) |
| **Gap** | -1 | Inserção ou deleção |

## Estrutura do Projeto

```
seqalignx/
├── main.py              # Implementação completa
├── requirements.txt     # Sem dependências
└── README.md           # Documentação
```

## Guia de Desenvolvimento

### Milestones do Projeto

#### Milestone 1: Algoritmo Básico ✅
- [x] Criar e inicializar matriz de pontuação
- [x] Implementar preenchimento da matriz
- [x] Calcular score final
- [x] Visualização da matriz
- [x] Documentação

#### Milestone 2: Traceback e Alinhamento 🚧
- [ ] Implementar traceback para reconstruir o alinhamento
- [ ] Exibir alinhamento com gaps (ex: G-ATTACA)
- [ ] Salvar alinhamento em arquivo
- [ ] Análise de múltiplos alinhamentos ótimos

#### Milestone 3: Melhorias de Algoritmo 📊
- [ ] Matriz de substituição (BLOSUM, PAM)
- [ ] Penalidades de gap variáveis (gap open, gap extend)
- [ ] Alinhamento de múltiplas sequências (progressivo)
- [ ] Otimização com espaço linear (Hirschberg)

#### Milestone 4: Funcionalidades Avançadas 🔄
- [ ] Leitura de arquivos FASTA
- [ ] Alinhamento local (Smith-Waterman)
- [ ] Busca em bancos de dados
- [ ] Visualização gráfica do alinhamento
- [] Benchmark com ferramentas existentes (BLAST)

### Tarefas para Contribuidores

**Nível Iniciante:**
1. Adicionar argparse para input via CLI
2. Criar função para ler sequências de arquivo
3. Implementar matriz BLOSUM62 simples

**Nível Intermediário:**
1. Implementar traceback completo
2. Adicionar penalidade de gap affine
3. Criar visualização do alinhamento

**Nível Avançado:**
1. Implementar alinhamento múltiplo (ClustalW-style)
2. Otimização com numpy
3. Algoritmo de alinhamento local

## Conceitos Importantes

### Programação Dinâmica
O algoritmo usa programação dinâmica para evitar recalcular subproblemas. A complexidade é O(m×n).

### Alinhamento Global vs Local
- **Global**: Alinha sequências completas (Needleman-Wunsch)
- **Local**: Encontra melhores sub-regiões (Smith-Waterman)

### Matrizes de Substituição
- **BLOSUM**: Baseada em blocos conservados
- **PAM**: Baseada em mutações aceitas
- **Simples**: +1 match, -1 mismatch (usado aqui)

### Penalidade de Gap
- **Linear**: Cada gap custa o mesmo
- **Affine**: Gap opening ≠ Gap extension

## Exemplos de Aplicação

### 1. Identificação de Homologia
```
Humano:    GATTACA
Chimpanzé: GATTACA  (100% similaridade)
Rato:      GCTTACA  (86% similaridade)
```

### 2. Detecção de Mutações
```
Referência: GATTACA
Paciente:   GCTTACA  (Mutação A→C na posição 2)
```

### 3. Comparação Evolutiva
Alinhar genes homólogos entre espécies para construir árvores filogenéticas.

## Limitações Atuais

- Não reconstrói o alinhamento (apenas calcula score)
- Sistema de pontuação simples (+1/-1)
- Penalidade de gap linear
- Sem suporte a arquivos de entrada
- Apenas duas sequências

## Próximos Passos Recomendados

1. **Implementar Traceback**: Reconstruir o alinhamento ótimo
2. **Adicionar Input FASTA**: Ler sequências de arquivo
3. **Matrizes de Substituição**: Implementar BLOSUM/PAM
4. **Penalidade Affine**: Diferenciar gap open e gap extend
5. **Comparação**: Mostrar alinhamento lado a lado

## Exercícios Sugeridos

### Exercício 1: Traceback Básico
Implemente a função de traceback que reconstrói o caminho na matriz.

### Exercício 2: Comparação de Sequências
Compare duas sequências de DNA reais e identifique as diferenças.

### Exercício 3: Gap Affine
Modifique o algoritmo para usar penalidade de gap diferente para abrir vs estender.

## Referências

- [Needleman-Wunsch Algorithm](https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm)
- [Sequence Alignment](https://en.wikipedia.org/wiki/Sequence_alignment)
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [BLAST Algorithm](https://en.wikipedia.org/wiki/BLAST_(biotechnology))
- [BLOSUM Matrix](https://en.wikipedia.org/wiki/BLOSUM)

## Licença

MIT License - veja arquivo LICENSE

## Contato

Abra uma issue para dúvidas ou sugestões.

---

**Status**: 🟡 Funcional Básico - Requer traceback para alinhamento completo