# Data2Day Workshop - Bring your own Data: Hands-on Enterprise AI Assistants in der Cloud

Herzlich Willkommen zum Workshop!

In den nächsten Stunden werden wir Schritt für Schritt eine eigene Retrieval-Augmented Generation-Anwendung (RAG) entwickeln.
Dabei werden wir nicht nur die Anwendung gemeinsam aufbauen, sondern auch ihre Leistungsfähigkeit evaluieren.
Ein besonderes Augenmerk legen wir auf die Integration eurer persönlichen Daten, um das System präzise auf eure spezifischen Fragestellungen anzupassen und individuelle Antworten zu generieren.

Alle im Workshop verwendeten Code-Beispiele findest du in diesem Repository. Es dient als Basis, um die erworbenen Kenntnisse auch nach dem Workshop anzuwenden und weiter zu vertiefen.
## Getting started

### Setup Development-Environment
1. Erstelle eine virtuelle Entwicklungsumgebung

```bash
python3 -m venv name_of_virtualenv
source name_of_virtualenv/bin/activate
```

2. Installiere die benötigten Python-Pakete

```bash
pip install -r requirements.txt
```

### Get Azure Credentials

Die benötigten Zugangsdaten zu unserer Azure Instanz findest du in XY.

## Build your (first) Chatbot-App
In [Sprint 1](sprint_1/README.md) werden wir eine grundlegende Chainlit App entwickeln, die als Grundlage für eine spätere RAG-Anwendung dient und die Interaktion mit einem Large Language Model (LLM) ermöglicht. 

## Connect your App to the Data
Im [zweiten Sprint](sprint_2/README.md) erweitern wir die Chainlit App mit RAG-Funktionalitäten, indem wir einen Vectorstore anlegen und die App modifizieren, sodass sie fähig ist, gezielt Wissen aus einer Datenbank zu extrahieren und fundierte Antworten auf Fragen mit spezifischem Kontext zu liefern.

## Evaluation
[Sprint 3](sprint_3/README.md) beschäftigt sich mit der Evaluierung der RAG-Funktionalitäten in unserer Chainlit App. Wir integrieren die Observability-Komponente [Phoenix](https://docs.arize.com/phoenix), erstellen einen Evaluationsdatensatz und führen eine umfassende Analyse mithilfe des Evaluationsframeworks [ragas](https://docs.ragas.io/en/stable/) durch, um die Leistung der App zu messen und zu verstehen, wo sie gut funktioniert und wo Verbesserungen nötig sind.

## Add your Own Data
In unserem [letzten Sprint](sprint_4/README.md) werden wir eure eigenen Daten an die App anbinden.
