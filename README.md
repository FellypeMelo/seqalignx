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

- **Implementação Completa**: Algoritmo Needleman-Wunsch puro em Python (incluindo Traceback)
- **Suporte a FASTA**: Carregamento automático de sequências de arquivos `.fasta`
- **Interface CLI**: Controle total via linha de comando para arquivos e pontuações
- **Visualização de Alinhamento**: Exibição clara com barras verticais para matches
- **Matriz de Pontuação**: Visualização opcional da matriz de programação dinâmica
- **Sem Dependências Externas**: Usa apenas a biblioteca padrão do Python

## Estrutura de Dados

### 📁 `test_data/` - Dados Sintéticos (Commitados)
Contém **55+ pares de sequências** com similaridade conhecida:
- ✅ **Commitados no GitHub**
- 🎯 **Similaridade controlada** (idênticas 100%, alta 80-95%, média 50-70%, baixa 20-40%)
- 📊 **Casos especiais** (com gaps, complementar reversa, proteínas)
- 🧪 **Validação precisa** (score esperado conhecido)

### 📁 `data/` - Dados Reais (Gitignored)
Para dados reais de pesquisa:
- 🚫 **Ignorado pelo Git**
- 🧬 **Sequências reais** do NCBI

## Instalação

### Pré-requisitos

- Python 3.7 ou superior
- Nenhuma dependência externa necessária!

### Instalação

```bash
git clone https://github.com/FellypeMelo/seqalignx.git
cd seqalignx
```

## Como Usar

### Execução Básica

O SeqAlignX agora exige arquivos de entrada via CLI:

```bash
python main.py --seq1 test_data/seqalignx_test_01_identical.fasta --seq2 test_data/seqalignx_test_01_identical.fasta
```

### Argumentos Disponíveis

- `--seq1`: Caminho para o arquivo FASTA da primeira sequência (Obrigatório)
- `--seq2`: Caminho para o arquivo FASTA da segunda sequência (Obrigatório)
- `--match`: Pontuação para match (Padrão: 1)
- `--mismatch`: Pontuação para mismatch (Padrão: -1)
- `--gap`: Penalidade de gap (Padrão: -1)
- `--quiet`: Não exibe a matriz de pontuação (útil para sequências longas)

### Exemplo de Saída

```
============================================================
SeqAlignX - Alinhamento Global (Needleman-Wunsch)
============================================================

Sequência 1: test_data/seqalignx_test_01_identical.fasta (Tamanho: 120)
Sequência 2: test_data/seqalignx_test_01_identical.fasta (Tamanho: 120)

Score de Alinhamento: 120

Alinhamento Reconstruído:
G G G G A G T G G A C T A G C G A T C C A A A C T C C A G C G A C A A G T A C A G T T C G A G A G A C A A C C T A C A G T A T C A A C A A A T T T G C T G C C T A G G A G T T G G G A G A C G C A C T C G A G A T G C T T A A T C G T A G A T G
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
G G G G A G T G G A C T A G C G A T C C A A A C T C C A G C G A C A A G T A C A G T T C G A G A G A C A A C C T A C A G T A T C A A C A A A T T T G C T G C C T A G G A G T T G G G A G A C G C A C T C G A G A T G C T T A A T C G T A G A T G

Alinhamento concluído!
```

## Algoritmo Needleman-Wunsch

O algoritmo utiliza três etapas:
1. **Inicialização**: Criação da matriz com penalidades de gap acumuladas.
2. **Preenchimento**: Cálculo de scores baseados em match, mismatch e gaps.
3. **Traceback**: Reconstrução do caminho ótimo do fim ao início para gerar o alinhamento visual.

## Estrutura do Projeto

```
seqalignx/
├── main.py              # Implementação completa e CLI
├── test_fasta.py        # Testes unitários para o parser
├── test_cli.py          # Testes unitários para a interface
├── test_traceback.py    # Testes unitários para o algoritmo
├── test_integration.py  # Testes de integração (E2E)
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

#### Milestone 2: Traceback e Alinhamento ✅
- [x] Implementar traceback para reconstruir o alinhamento
- [x] Exibir alinhamento com gaps e marcações visuais
- [x] Interface CLI com argparse
- [x] Suporte a arquivos FASTA

#### Milestone 3: Melhorias de Algoritmo 📊
- [ ] Matriz de substituição (BLOSUM, PAM)
- [ ] Penalidades de gap variáveis (gap open, gap extend)
- [ ] Alinhamento de múltiplas sequências (progressivo)
- [ ] Otimização com espaço linear (Hirschberg)

#### Milestone 4: Funcionalidades Avançadas 🔄
- [ ] Alinhamento local (Smith-Waterman)
- [ ] Busca em bancos de dados
- [ ] Visualização gráfica do alinhamento (Plotly/Matplotlib)

### Testes (TDD)

O projeto segue rigorosamente o desenvolvimento guiado por testes. Para rodar todos os testes:

```bash
python -m unittest discover .
```

## Licença

MIT License - veja arquivo LICENSE

## Contato

Abra uma issue para dúvidas ou sugestões.

---

**Status**: 🟢 Funcional e Completo (Algoritmo Needleman-Wunsch)
