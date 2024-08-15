### Sprint 2: Erweiterung der App mit RAG
In dieser Übung erweitern wir die Chainlit App um Retrieval-Augmented Generation (RAG) Funktionalitäten. Damit ermöglichen wir es der App, relevante Informationen aus einer Wissensdatenbank zu suchen und zu nutzen, um präzisere und kontextreichere Antworten zu generieren.

Hier sind die erforderlichen Schritte, um mit der Entwicklung fortzufahren:

- **Vectorstore anlegen:** Fülle das vorgegebene Code-Skelett in der Datei _vectorstore.py_ aus, um einen Vectorstore anzulegen. Dieser wird verwendet, um die Wissensdatenbank für die RAG-Funktionalität zu speichern und zu durchsuchen.
- **Code der Chainlit App erweitern:** Ergänze das vorgegebene Code-Skelett in der Datei _app.py_, um die RAG-Funktionalität in die Chainlit App zu integrieren. Dies umfasst das Einbinden des Vectorstores und die Anpassung der Kommunikation mit dem LLM.
- **App starten:** Starte die App, indem du wie zuvor
  - den Terminal deines Betriebssystems öffnest, 
  - in den Ordner sprint_2/src wechselst,
  - den Befehl ```chainlit run app.py -w``` ausführst.
- **Umgebungsvariablen ergänzen:** Beim ersten Start der App wirst du aufgefordert den Namen des Deployments für das Embedding Modell zu hinterlegen. Kopiere diesen aus Azure und speichere ihn.
- **Optional - Speichern der Konversationshistorie:** Ergänze den Code der App, sodass der Chatverlauf gespeichert wird. Dies ermöglicht es, den Verlauf der Interaktionen zu dokumentieren und bei Bedarf wieder abzurufen. Dadurch können Benutzer auf frühere Nachrichten Bezug nehmen und dazu Rückfragen stellen.

**Hinweis:** Alle wichtigen Infos zur Bearbeitung der Aufgaben findest du in Kapitel **2** des Cheetsheets.