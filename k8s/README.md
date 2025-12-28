# Kubernetes Deployment

Das Ausrollen in Kubernetes benötigt vorbereitete Container Images für den Crawl-Job und den eigentlichen MCP-Server. Die Quelle der Images kann ggf. in `production/kustomization.yaml` angepasst werden.

## Schritt 1: Vorbereitung der Daten

Für das Ausrollen des MCP Servers in Kubernetes ist zunächst der Download und die Vorbereitung der Daten erforderlich. Dies wird per Kubernetes-Job mit dem Docker Image "court-decisions-mcp-crawl" realisiert. Dieses schreibt in ein persistentes Volume, welches anschliessend vom "court-decisions-mcp-server" Deployment eingebunden wird.

Die Ausführung des Crawl Jobs erfolgt mit:

`kubectl -n <namespace> apply -k court-decisions-mcp-crawl/production`

Für die Aktualisierung der Daten muss lediglich der Job erneut ausgeführt werden. Name und Registry für das Container Image des Crawl-Jobs können ggf. angepasst werden.

## Schritt 2: Ausrollen des MCP Servers

Der MCP-Server benötigt eine laufende OpenSearch-Instanz:

`kubectl -n <namespace> apply -k opensearch/production`

Anschliessend kann der Server gestartet werden:

`kubectl -n <namespace> apply -k court-decisions-mcp-server/production`

