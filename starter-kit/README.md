# ⚽ Hack Night Rio – Copa do Mundo Edition

> Construa uma solução com IA e dados reais de futebol usando a Stack Elastic!

📅 **29 de maio de 2026** | 📍 **ESPM Rio** | ⏰ **16:00–22:00**

---

## 🚀 Setup Rápido (faça ANTES do evento!)

### 1. Elastic Cloud (trial gratuito)

1. Acesse [cloud.elastic.co](https://cloud.elastic.co/)
2. Crie uma conta (trial de 14 dias, sem cartão de crédito)
3. Crie um deployment (escolha a região mais próxima)
4. Guarde suas credenciais (endpoint, API key)

### 2. Ambiente Local

```bash
# Python 3.8+ necessário
python --version

# Clone este repo
git clone https://github.com/<org>/hacknight-copa-2026.git
cd hacknight-copa-2026

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instale as dependências
pip install -r requirements.txt
```

### 3. Verifique o Setup

```bash
python scripts/check_setup.py
```

Se tudo estiver ✅, você está pronto!

---

## 📊 O Dataset: StatsBomb

Usaremos dados do [StatsBomb Open Data](https://github.com/statsbomb/statsbombpy) — um dos datasets mais completos de futebol mundial, com:

- **Eventos de partidas** (passes, finalizações, dribles, faltas...)
- **Lineups e escalações**
- **Dados de competições** (Copas do Mundo, ligas europeias, etc.)
- **Estatísticas de jogadores** (scout completo)

### Explorar os dados

```python
from statsbombpy import sb

# Listar competições disponíveis
competitions = sb.competitions()

# Partidas da Copa do Mundo 2022
matches = sb.matches(competition_id=43, season_id=106)

# Eventos de uma partida específica
events = sb.events(match_id=3869685)

# Lineups
lineups = sb.lineups(match_id=3869685)
```

Veja mais exemplos em [`examples/`](./examples/).

---

## 🤖 Elastic Agent Builder

O Agent Builder é a ferramenta principal do desafio. Com ele você pode criar agentes de IA que:

- Consultam dados no Elasticsearch usando linguagem natural
- Executam análises e geram insights automaticamente
- Combinam múltiplas fontes de dados

📖 [Documentação do Agent Builder](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder)

📺 **Live Preparatória** — Assista à gravação: (link em breve)

---

## 💡 Ideias de Projetos

| Projeto | Descrição | Dificuldade |
|---------|-----------|-------------|
| 🔍 Scout Inteligente | Agente que recomenda jogadores por posição/estilo | ⭐⭐ |
| 📊 Painel Tático | Dashboard com análise de partidas e heatmaps | ⭐⭐ |
| 🗣️ Chatbot de Copa | Assistente que responde sobre jogos e seleções | ⭐ |
| 📰 Gerador de Análises | Relatórios automáticos pré/pós-jogo | ⭐⭐ |
| 🏆 Simulador de Resultados | Previsões baseadas em dados históricos | ⭐⭐⭐ |
| ⚡ Detector de Padrões | Identificar padrões táticos em jogadas | ⭐⭐⭐ |

> 💡 Estes são apenas exemplos! Use sua criatividade.

---

## 📁 Estrutura do Repo

```
├── README.md                  # Você está aqui
├── requirements.txt           # Dependências Python
├── datasets/
│   ├── README.md              # Descrição dos datasets pré-processados
│   └── load_data.py           # Script para carregar dados no Elasticsearch
├── docs/
│   ├── setup-elastic.md       # Guia detalhado de setup do Elastic Cloud
│   ├── agent-builder-101.md   # Intro ao Agent Builder
│   └── statsbomb-guide.md     # Guia dos dados StatsBomb
├── examples/
│   ├── 01_explore_data.py     # Explorar dados do StatsBomb
│   ├── 02_ingest_to_es.py     # Ingerir dados no Elasticsearch
│   ├── 03_agent_builder.md    # Passo a passo do Agent Builder
│   └── mappings/
│       └── events_mapping.json # Mapping pronto para copiar/colar
└── scripts/
    └── check_setup.py         # Verificar se tudo está configurado
```

---

## 🛠️ Recursos Úteis

- [StatsBomb Python Docs](https://github.com/statsbomb/statsbombpy)
- [Elastic Agent Builder Docs](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder)
- [Elastic Cloud](https://cloud.elastic.co/)
- [ES|QL Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/esql.html)
- [ACE Laboratory](https://ace-lab.github.io/)

---

## 🤝 Organização & Parceiros

- **Elastic Community** – Rio de Janeiro
- **ACE Laboratory** – PESC/COPPE/UFRJ & Cefet/RJ
- **ESPM Rio**

---

⚡ *Dúvidas? Abra uma issue neste repo ou mande mensagem na página do evento!*
