#!/usr/bin/env python3
"""
Hack Night Rio - Copa do Mundo Edition
Exemplo 01: Explorar dados do StatsBomb

Este script mostra como acessar os dados abertos do StatsBomb
usando a biblioteca statsbombpy.
"""

from statsbombpy import sb
import pandas as pd

# =============================================================
# 1. Listar competições disponíveis
# =============================================================
print("📋 Competições disponíveis:")
competitions = sb.competitions()
print(competitions[['competition_name', 'season_name', 'competition_id', 'season_id']].to_string())
print()

# =============================================================
# 2. Copa do Mundo — buscar partidas
#    competition_id=43 = FIFA World Cup
#    Verifique season_id disponível nos dados acima
# =============================================================
print("⚽ Partidas da Copa do Mundo (verifique a season_id):")
# Exemplo com Copa 2022 (season_id pode variar)
try:
    matches = sb.matches(competition_id=43, season_id=106)
    print(f"   {len(matches)} partidas encontradas")
    print(matches[['match_date', 'home_team', 'away_team', 'home_score', 'away_score']].head(10))
except Exception as e:
    print(f"   Erro: {e}")
    print("   Verifique o season_id correto na tabela de competições acima")
print()

# =============================================================
# 3. Eventos de uma partida
# =============================================================
print("📊 Eventos de uma partida:")
try:
    match_id = matches.iloc[0]['match_id']
    events = sb.events(match_id=match_id)
    print(f"   {len(events)} eventos na partida")
    print(f"   Tipos de evento: {events['type'].unique().tolist()}")
    print()

    # Finalizações
    shots = events[events['type'] == 'Shot']
    print(f"   🎯 Finalizações: {len(shots)}")
    if len(shots) > 0:
        print(shots[['player', 'team', 'shot_outcome', 'shot_statsbomb_xg']].to_string())
except Exception as e:
    print(f"   Erro: {e}")
print()

# =============================================================
# 4. Lineups
# =============================================================
print("👥 Lineups:")
try:
    lineups = sb.lineups(match_id=match_id)
    for team, players in lineups.items():
        print(f"\n   {team}:")
        print(f"   {players[['player_name', 'jersey_number']].to_string()}")
except Exception as e:
    print(f"   Erro: {e}")
