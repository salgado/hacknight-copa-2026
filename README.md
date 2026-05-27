# ⚽ Hack Night Rio — Copa do Mundo Edition

**Construa uma solução com IA e dados reais de futebol usando a Stack Elastic!**

📅 **29 de maio de 2026 (sexta-feira)**
📍 **ESPM Rio** — Ladeira da Glória, 26, Glória, Rio de Janeiro
⏰ **16:00 – 22:00**
🎟️ **Gratuito** — 35 vagas

---

## 👋 Bem-vindo!

Neste Hack Night, você vai usar **dados reais de partidas, jogadores e scouts** do [StatsBomb](https://github.com/statsbomb/statsbombpy) combinados com a **stack Elastic** para criar algo incrível em poucas horas.

Pode ser um scout inteligente, um chatbot de Copa, um painel tático, um simulador de resultados — o limite é a sua criatividade!

**Não precisa ter experiência prévia com Elastic.** Teremos mentores circulando para ajudar durante todo o evento.

---

## 📺 Lives Preparatórias

Assista antes do evento para chegar preparado!

| # | Live | Link |
|---|------|------|
| 1 | Introdução ao Elastic Agent Builder | 🔜 Em breve |
| 2 | Setup + Dados StatsBomb na prática | [▶️ Assistir no YouTube](https://youtu.be/UnJ9FiVHp8U) |

---

## 🚀 Prepare-se antes do evento

1. **Crie uma conta gratuita** no [Elastic Cloud](https://cloud.elastic.co/) (trial de 14 dias, sem cartão)
2. **Instale o Python 3.8+** no seu notebook
3. **Clone este repo** e rode o setup:

```bash
git clone https://github.com/salgado/hacknight-copa-2026.git
cd hacknight-copa-2026/starter-kit

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python scripts/check_setup.py
```

Se tudo der ✅, você está pronto!

---

## 🗓️ Agenda do dia

| Horário | Atividade |
|---------|-----------|
| 16:00 – 16:30 | 🍕 Chegada + Networking + Pizza & Bebidas |
| 16:30 – 17:00 | 🎤 Introdução + Demo |
| 17:00 – 20:30 | 💻 Hack Time! |
| 20:30 – 21:30 | 🎬 Apresentação dos projetos + Votação |
| 21:30 – 22:00 | 🏆 Premiação + Encerramento |

---

## 📁 O que tem neste repo

```
├── README.md              ← você está aqui
└── starter-kit/
    ├── README.md          ← guia detalhado de setup + dataset + ideias
    ├── requirements.txt   ← dependências Python
    ├── .env.example       ← template de credenciais Elastic
    ├── scripts/
    │   └── check_setup.py ← verifica se tudo está OK
    └── examples/
        ├── 01_explore_data.py      ← explorar dados do StatsBomb
        ├── 02_ingest_to_es.py      ← ingerir dados no Elasticsearch
        └── mappings/
            └── events_mapping.json ← mapping pronto para usar
```

> 📋 **Regras do desafio, critérios de avaliação e prêmios** serão publicados aqui nos próximos dias. Fique de olho!

---

## 🛠️ Recursos Úteis

- 📖 [Elastic Agent Builder — Documentação](https://www.elastic.co/docs/explore-analyze/ai-features/elastic-agent-builder)
- ⚽ [StatsBomb Python — GitHub](https://github.com/statsbomb/statsbombpy)
- ☁️ [Elastic Cloud — Trial Gratuito](https://cloud.elastic.co/)
- 📊 [ES|QL Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/esql.html)

---

## 🤝 Organização & Parceiros

| | |
|---|---|
| **Elastic Community** | Rio de Janeiro |
| **ACE Laboratory** | PESC/COPPE/UFRJ & Cefet/RJ — [site](https://ace-lab.github.io/) · [LinkedIn](https://www.linkedin.com/company/ace-laboratory/) |
| **ESPM Rio** | Parceiro acadêmico e sede do evento |

---

⚡ *Dúvidas? Abra uma [issue](https://github.com/salgado/hacknight-copa-2026/issues) neste repo ou mande mensagem na [página do evento](https://www.meetup.com/)!*
