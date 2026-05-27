#!/usr/bin/env python3
"""
Hack Night Rio - Copa do Mundo Edition
Script de verificação de setup

Execute: python scripts/check_setup.py
"""

import sys

def check_python():
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"  ✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"  ❌ Python {version.major}.{version.minor} — precisa 3.8+")
        return False

def check_statsbomb():
    try:
        from statsbombpy import sb
        comps = sb.competitions()
        print(f"  ✅ statsbombpy instalado ({len(comps)} competições disponíveis)")
        return True
    except ImportError:
        print("  ❌ statsbombpy não instalado — pip install statsbombpy")
        return False
    except Exception as e:
        print(f"  ⚠️  statsbombpy instalado mas erro ao acessar dados: {e}")
        return True

def check_elasticsearch():
    try:
        import elasticsearch
        print(f"  ✅ elasticsearch-py {elasticsearch.__version__}")
        return True
    except ImportError:
        print("  ❌ elasticsearch não instalado — pip install elasticsearch")
        return False

def check_pandas():
    try:
        import pandas
        print(f"  ✅ pandas {pandas.__version__}")
        return True
    except ImportError:
        print("  ❌ pandas não instalado — pip install pandas")
        return False

def main():
    print()
    print("⚽ Hack Night Rio – Verificação de Setup")
    print("=" * 45)
    print()

    checks = [
        ("Python", check_python),
        ("statsbombpy", check_statsbomb),
        ("elasticsearch-py", check_elasticsearch),
        ("pandas", check_pandas),
    ]

    results = []
    for name, check_fn in checks:
        print(f"  Verificando {name}...")
        results.append(check_fn())
        print()

    print("=" * 45)
    if all(results):
        print("  🎉 Tudo pronto! Você está preparado para o Hack Night!")
    else:
        print("  ⚠️  Alguns itens precisam de atenção. Corrija e rode novamente.")
    print()

if __name__ == "__main__":
    main()
