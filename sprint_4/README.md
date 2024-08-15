### Sprint 4: Eigene Daten anbinden
In dieser Übung werden wir die Chainlit App erweitern, indem wir eigene Datenquellen anbinden. Wir konzentrieren uns darauf, die App so zu erweitern, dass sie mit verschiedenen Texttypen umgehen und diese in sinnvolle Abschnitte (Chunks) unterteilen kann. Diese Fähigkeit verbessert die Effizienz der Informationsbeschaffung und die Relevanz der generierten Antworten.

Hier sind die Schritte, die du durchführen musst, um die App weiterzuentwickeln:
- **Verarbeiten von anderen Texttypen und Chunking:** Bearbeite das Code-Skelett in der Datei _vectorstore.py_, um die Fähigkeit zur Verarbeitung verschiedener Texttypen und zum Chunking zu implementieren. Diese Erweiterung ermöglicht es der App, Texte effektiver in der Wissensdatenbank zu speichern und diese für die Beantwortung von Anfragen zu nutzen.
- **App starten und testen:** Nachdem du die neue Funktionalität implementiert hast, starte die App, um sie zu testen. Öffne dafür wieder das Terminal deines Betriebssystems, navigiere zum Ordner _sprint_4/src_ und führe den Befehl ``chainlit run app.py -w`` aus. Teste die App, indem du Fragen stellst, die sich auf die neu eingebundenen Daten beziehen.
- **Evaluation durchführen:** Um die Qualität der neuen Funktionalitäten zu bewerten, führe das Notebook _ragas_evaluation.ipynb_ erneut aus. So kannst du die Leistung der Anwendung mit den neuen Daten messen und potentielle Verbesserungen oder notwendigen Anpassungen ausfindig machen.

**Hinweis:** Alle wichtigen Infos zur Bearbeitung der Aufgaben findest du in Kapitel **4** des Cheetsheets.