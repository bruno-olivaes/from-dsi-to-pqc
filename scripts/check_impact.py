#!/usr/bin/env python3
"""
Monitor de Impacto Científico (Zenodo API)
Autor: Bruno L. Olivaes
Data: Novembro 2026

Consulta em tempo real as métricas de visualizações e downloads de cada um
dos 5 registros oficiais publicados no CERN/Zenodo.
"""

import json
import urllib.request
import urllib.error
from datetime import datetime

PAPERS = [
    {
        "id": "24124702",
        "doi": "10.5281/zenodo.24124702",
        "name": "00. The Matrioska Protocol (Master Book)",
        "repo": "from-dsi-to-pqc",
    },
    {
        "id": "24121677",
        "doi": "10.5281/zenodo.24121677",
        "name": "01. Planck 2018 DSI (Cosmologia)",
        "repo": "dsi-cosmo-search",
    },
    {
        "id": "24121687",
        "doi": "10.5281/zenodo.24121687",
        "name": "02. Casimir Force (Metrologia)",
        "repo": "casimir-afm-spectroscopy",
    },
    {
        "id": "24121691",
        "doi": "10.5281/zenodo.24121691",
        "name": "03. ESA Euclid (Energia Escura)",
        "repo": "oscillatory-dark-energy-euclid",
    },
    {
        "id": "24121693",
        "doi": "10.5281/zenodo.24121693",
        "name": "04. Qiskit NISQ ZNE (Computação Quântica)",
        "repo": "qiskit-lombscargle-zne",
    },
    {
        "id": "24121695",
        "doi": "10.5281/zenodo.24121695",
        "name": "05. PQC TLS 1.3 (Criptografia)",
        "repo": "pqc-crypto-agility-benchmark",
    },
]

def fetch_record_stats(record_id):
    url = f"https://zenodo.org/api/records/{record_id}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MatrioskaImpactMonitor/1.0 (Bruno Olivaes Portfolio Audit)",
            "Accept": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            stats = data.get("stats", {})
            metadata = data.get("metadata", {})
            return {
                "ok": True,
                "title": metadata.get("title", "N/A"),
                "publication_date": metadata.get("publication_date", "N/A"),
                "views": stats.get("views", 0),
                "unique_views": stats.get("unique_views", 0),
                "downloads": stats.get("downloads", 0),
                "unique_downloads": stats.get("unique_downloads", 0),
            }
    except Exception as e:
        return {"ok": False, "error": str(e)}

def main():
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n" + "=" * 90)
    print(f"🔬 PAINEL DE IMPACTO CIENTÍFICO - ZENODO / CERN (DataCite DOIs)")
    print(f"📅 Consulta realizada em: {now_str} (Horário Local)")
    print("=" * 90)

    header = f"{'#':<3} {'Artigo / Disciplina':<38} {'DOI Zenodo':<28} {'Views':<8} {'Downloads':<10}"
    print(header)
    print("-" * 90)

    total_views = 0
    total_unique_views = 0
    total_downloads = 0
    total_unique_downloads = 0

    for i, paper in enumerate(PAPERS, 1):
        info = fetch_record_stats(paper["id"])
        if info["ok"]:
            v = info["views"]
            uv = info["unique_views"]
            d = info["downloads"]
            ud = info["unique_downloads"]
            total_views += v
            total_unique_views += uv
            total_downloads += d
            total_unique_downloads += ud

            views_str = f"{v} ({uv})"
            dl_str = f"{d} ({ud})"
            print(f"{i:<3} {paper['name']:<38} {paper['doi']:<28} {views_str:<8} {dl_str:<10}")
        else:
            status_txt = "Reservado" if "404" in info.get("error", "") else "ERR"
            print(f"{i:<3} {paper['name']:<38} {paper['doi']:<28} {status_txt:<8} {'--':<10}")

    print("-" * 90)
    print(f"{'TOTAL CONSOLIDADO':<70} {f'{total_views} ({total_unique_views})':<8} {f'{total_downloads} ({total_unique_downloads})':<10}")
    print("=" * 90)
    print("Nota: As contagens entre parênteses indicam visitantes e downloads únicos.")
    print("A API do Zenodo atualiza estatísticas em lotes a cada 1-2 horas.\n")

if __name__ == "__main__":
    main()

