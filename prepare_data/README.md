# Pipeline zur Datenaufbereitung

Dieses Verzeichnis enthält Skripte zum Herunterladen, Entpacken und Konvertieren deutscher Gerichtsurteile von "Rechtsprechung im Internet" in ein Format, das für den MCP-Server geeignet ist.

## Übersicht

Die Pipeline umfasst die folgenden Schritte:
1. **Inhaltsverzeichnis herunterladen & Links extrahieren**: Lädt das Master-XML-Inhaltsverzeichnis herunter und extrahiert alle Download-Links.
2. **Zip-Dateien herunterladen**: Lädt die einzelnen Fallarchive herunter.
3. **Zips entpacken**: Entpackt die XML-Dateien aus den heruntergeladenen Archiven.
4. **In Markdown konvertieren**: Verarbeitet die XML-Dateien und konvertiert sie in strukturiertes Markdown für die Indizierung.

## Voraussetzungen

- Python 3.12+
- Abhängigkeiten: `pip install -r requirements.txt`

## Nutzung

Führen Sie die Skripte in der folgenden Reihenfolge aus:

### 1. Links extrahieren
```bash
python extract_links.py
```
- **Aktion**: Lädt `rii-toc.xml` nach `data/` herunter (falls nicht vorhanden) und erstellt `data/links.txt`.

### 2. Dateien herunterladen
```bash
python download_files.py
```
- **Aktion**: Lädt alle in `data/links.txt` aufgelisteten Zip-Dateien in das Verzeichnis `data/downloads/` herunter.
- **Hinweis**: Verwendet einen Thread-Pool und beinhaltet ein einfaches Rate-Limiting.

### 3. ZIPs entpacken
```bash
python extract_zips.py
```
- **Aktion**: Entpackt alle Dateien aus `data/downloads/` nach `data/extracted/`.

### 4. In Markdown konvertieren
```bash
python convert_all_to_md.py
```
- **Aktion**: Konvertiert XML-Dateien in `data/extracted/` in Markdown-Dateien im Verzeichnis `../mcp/markdown/`.
- **Hinweis**: Nutzt prozessbasierte Parallelisierung für eine schnellere Konvertierung.

## Datenstruktur

- `data/rii-toc.xml`: Das Quell-Inhaltsverzeichnis.
- `data/links.txt`: Liste der herunterzuladenden URLs.
- `data/downloads/`: Rohdaten als ZIP-Dateien.
- `data/extracted/`: Entpackte XML-Dateien.
- `../mcp/markdown/`: Finale Markdown-Dateien, bereit für den OpenSearch-Import.

## Docker

Der Download und das Parsen der Daten kann auch durch ein Docker Image ausgeführt werden. Im Gegensatz zur direkten Ausführung der Skripte werden die Markdown-Daten ebenfalls im `data`-Ordner gespeichert:

`docker build . -t court-decisions-mcp-crawl`
`docker run -v ./data/:/app/data/ court-decisions-mcp-crawl`
