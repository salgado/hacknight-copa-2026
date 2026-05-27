#!/usr/bin/env python3
"""
Hack Night Rio - Copa do Mundo Edition
Exemplo 02: Ingerir dados do StatsBomb no Elasticsearch

Este script carrega dados de partidas da Copa do Mundo
e indexa no Elasticsearch para uso com o Agent Builder.
"""

import os
import json
from dotenv import load_dotenv
from statsbombpy import sb
from elasticsearch import Elasticsearch, helpers

load_dotenv()

# =============================================================
# 1. Conexão com Elasticsearch
# =============================================================
ELASTIC_ENDPOINT = os.getenv("ELASTIC_ENDPOINT", "https://your-deployment.es.cloud.elastic.co")
ELASTIC_API_KEY = os.getenv("ELASTIC_API_KEY", "your-api-key")

es = Elasticsearch(
    ELASTIC_ENDPOINT,
    api_key=ELASTIC_API_KEY,
)

# Verificar conexão
info = es.info()
print(f"✅ Conectado ao Elasticsearch {info['version']['number']}")

# =============================================================
# 2. Criar índice com mapping otimizado
# =============================================================
INDEX_EVENTS = "hacknight-wc-events"
INDEX_MATCHES = "hacknight-wc-matches"

# Mapping para eventos (copie e cole no Kibana se preferir)
events_mapping = {
    "mappings": {
        "properties": {
            "match_id": {"type": "long"},
            "competition": {"type": "keyword"},
            "season": {"type": "keyword"},
            "team": {"type": "keyword"},
            "player": {"type": "keyword"},
            "type": {"type": "keyword"},
            "timestamp": {"type": "keyword"},
            "minute": {"type": "integer"},
            "second": {"type": "integer"},
            "location": {"type": "float"},
            "pass_end_location": {"type": "float"},
            "shot_statsbomb_xg": {"type": "float"},
            "shot_outcome": {"type": "keyword"},
            "pass_outcome": {"type": "keyword"},
            "pass_recipient": {"type": "keyword"},
            "pass_length": {"type": "float"},
            "pass_height": {"type": "keyword"},
            "dribble_outcome": {"type": "keyword"},
            "under_pressure": {"type": "boolean"},
            "play_pattern": {"type": "keyword"},
            "position": {"type": "keyword"},
        }
    }
}

matches_mapping = {
    "mappings": {
        "properties": {
            "match_id": {"type": "long"},
            "match_date": {"type": "date"},
            "competition": {"type": "keyword"},
            "season": {"type": "keyword"},
            "home_team": {"type": "keyword"},
            "away_team": {"type": "keyword"},
            "home_score": {"type": "integer"},
            "away_score": {"type": "integer"},
            "competition_stage": {"type": "keyword"},
            "stadium": {"type": "keyword"},
            "referee": {"type": "keyword"},
        }
    }
}

for index, mapping in [(INDEX_EVENTS, events_mapping), (INDEX_MATCHES, matches_mapping)]:
    if es.indices.exists(index=index):
        print(f"⚠️  Índice {index} já existe. Pulando criação.")
    else:
        es.indices.create(index=index, body=mapping)
        print(f"✅ Índice {index} criado")

# =============================================================
# 3. Carregar dados da Copa do Mundo
# =============================================================
# FIFA World Cup — ajuste competition_id e season_id conforme necessário
COMPETITION_ID = 43
SEASON_ID = 106  # Verifique com sb.competitions()

print(f"\n📊 Carregando partidas (competition={COMPETITION_ID}, season={SEASON_ID})...")
matches = sb.matches(competition_id=COMPETITION_ID, season_id=SEASON_ID)
print(f"   {len(matches)} partidas encontradas")

# Indexar partidas
match_actions = []
for _, match in matches.iterrows():
    doc = {
        "match_id": int(match["match_id"]),
        "match_date": str(match["match_date"]),
        "competition": match.get("competition", "FIFA World Cup"),
        "season": str(match.get("season", "")),
        "home_team": match["home_team"],
        "away_team": match["away_team"],
        "home_score": int(match["home_score"]),
        "away_score": int(match["away_score"]),
        "competition_stage": match.get("competition_stage", ""),
        "stadium": match.get("stadium", ""),
        "referee": match.get("referee", ""),
    }
    match_actions.append({"_index": INDEX_MATCHES, "_id": doc["match_id"], "_source": doc})

if match_actions:
    helpers.bulk(es, match_actions)
    print(f"✅ {len(match_actions)} partidas indexadas em '{INDEX_MATCHES}'")

# Indexar eventos de cada partida
total_events = 0
for _, match in matches.iterrows():
    match_id = int(match["match_id"])
    print(f"   ⚽ Processando partida {match_id}: {match['home_team']} vs {match['away_team']}...")

    try:
        events = sb.events(match_id=match_id)
    except Exception as e:
        print(f"      ⚠️  Erro: {e}")
        continue

    event_actions = []
    for _, event in events.iterrows():
        doc = {
            "match_id": match_id,
            "competition": "FIFA World Cup",
            "team": event.get("team", ""),
            "player": event.get("player", ""),
            "type": event.get("type", ""),
            "timestamp": event.get("timestamp", ""),
            "minute": int(event["minute"]) if "minute" in event else 0,
            "second": int(event["second"]) if "second" in event else 0,
            "shot_statsbomb_xg": float(event["shot_statsbomb_xg"]) if "shot_statsbomb_xg" in event and event.get("shot_statsbomb_xg") else None,
            "shot_outcome": event.get("shot_outcome", None),
            "pass_outcome": event.get("pass_outcome", None),
            "pass_recipient": event.get("pass_recipient", None),
            "pass_length": float(event["pass_length"]) if "pass_length" in event and event.get("pass_length") else None,
            "pass_height": event.get("pass_height", None),
            "dribble_outcome": event.get("dribble_outcome", None),
            "under_pressure": bool(event.get("under_pressure", False)),
            "play_pattern": event.get("play_pattern", ""),
            "position": event.get("position", ""),
        }
        # Remover campos None para economizar espaço
        doc = {k: v for k, v in doc.items() if v is not None}
        event_actions.append({"_index": INDEX_EVENTS, "_source": doc})

    if event_actions:
        helpers.bulk(es, event_actions)
        total_events += len(event_actions)

print(f"\n🎉 Total: {total_events} eventos indexados em '{INDEX_EVENTS}'")
print("\n✅ Dados prontos! Agora vá para o Agent Builder e comece a hackear!")
