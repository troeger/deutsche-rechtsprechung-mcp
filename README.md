# Rechtsprechung MCP Server

Ein [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/spec) Server, der die Daten von [Rechtsprechung im Internet](https://www.rechtsprechung-im-internet.de) (Entscheidungen des Bundesverfassungsgerichts, der obersten Gerichtshöfe des Bundes sowie des Bundespatentgerichts ab dem Jahr 2010) durchsuchbar und für LLMs (Large Language Models) zugänglich macht.

## Projektübersicht

Dieses Projekt stellt eine Schnittstelle bereit, über die KI-Agenten und Anwendungen auf eine umfangreiche Datenbank deutscher Rechtsprechung zugreifen können. Es besteht aus drei Hauptkomponenten:

1.  **MCP Server**: Der Kern des Projekts. Ein FastMCP-Server, der Tools zur Suche und zum Abruf von Volltexten bereitstellt.
2.  **Data Preprocessing**: Eine Pipeline, um Urteile von "Rechtsprechung im Internet" herunterzuladen, zu bereinigen und in ein durchsuchbares Format zu konvertieren.
3.  **Beispiel-Agent**: Ein Google ADK Agent, der demonstriert, wie man den MCP Server nutzen kann, um juristische Fragestellungen zu beantworten.

## 1. MCP Server

Der Server läuft in einem Docker-Container und nutzt OpenSearch als Backend für schnelle und flexible Volltextsuchen.

### Funktionen (Tools)

*   `search_decisions(query: str, limit: int)`: Sucht nach Urteilen basierend auf Text, Aktenzeichen oder Normen.
*   `get_decision_by_doknr(doknr: str)`: Ruft den vollständigen Text (Leitsätze, Gründe, Metadaten) eines spezifischen Urteils ab.

### Technologie

*   **Python**: Implementierung des Servers mit `mcp.server.fastmcp`.
*   **OpenSearch**: Speicherung und Indizierung der Urteile.
*   **Docker Compose**: Orchestrierung von Server und Datenbank.

### Starten des Servers

```bash
cd mcp
docker-compose up --build
```

Der Server ist anschließend unter `http://localhost:8002/mcp` erreichbar. Die Datenbank wird beim ersten Start automatisch initialisiert (siehe `src/ingest.py`).

## 2. Data Preprocessing

Bevor der Server nützlich ist, müssen Daten ingestiert werden. Die Skripte im Ordner `prepare_data/` kümmern sich um die Beschaffung und Aufbereitung.

*   **Quelle**: [Rechtsprechung im Internet](https://www.rechtsprechung-im-internet.de/) (Open Data).
*   **Prozess**:
    1.  Links extrahieren (`extract_links.py`).
    2.  XML-Daten herunterladen (`download_files.py`).
    3.  Entpacken (`extract_zips.py`).
    4.  Konvertierung zu Markdown für optimale LLM-Lesbarkeit (`convert_all_to_md.py`).

Detaillierte Anweisungen finden sich in `prepare_data/README.md`.

## 3. Beispiel-Agent (Google ADK)

Im Ordner `google-adk-agent/` befindet sich ein Referenz-Agent, der zeigt, wie man den MCP-Server in eine Anwendung integriert.

*   **Framework**: Google Agent Development Kit (ADK).
*   **Modell**: Gemini 2.5 Flash / Gemini 3 Pro Preview.
*   **Funktion**: Der Agent analysiert Sachverhalte, sucht selbstständig passende Urteile und gibt eine rechtliche Einschätzung ab.

Siehe `google-adk-agent/agent/README.md` für Details zur Einrichtung.

## Voraussetzung

*   Docker & Docker Compose
*   Python 3.10+ (für lokale Entwicklung/Preprocessing)
*   Zugriff auf Gemini API (für den Agenten)

## Lizenz

Dieses Projekt ist unter der [MIT License](LICENSE) lizenziert. Die Daten stammen vom Bundesministerium der Justiz und dem Bundesamt für Justiz.
