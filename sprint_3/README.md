### Sprint 3: Evaluierung der RAG-Anwendung
In dieser Übung konzentrieren wir uns auf die Evaluierung der Retrieval-Augmented Generation (RAG) Funktionalitäten, die wir in der Chainlit App implementiert haben. Ziel ist es, die Leistung der App zu messen und Einblicke in die internen Prozesse während der Interaktion mit dem Language Model zu gewinnen.

Folge diesen Schritten, um mit der Evaluierung zu beginnen:
- **Observability-Komponente Phoenix einbauen:** Erweitere das Code-Skelett in der Datei _app.py_, um die Observability-Komponente Phoenix zu integrieren. Dies ermöglicht eine detaillierte Einsicht in die Hintergrundprozesse während der Interaktionen mit dem LLM. Teste es gerne, indem du zunächst die App wie zuvor startest
  - Terminal deines Betriebssystems öffnen 
  - in den Ordner sprint_24/src wechseln,
  - den Befehl ```chainlit run app.py -w``` ausführen.

Stelle nun ein paar Fragen an den Chatbot und beobachte, was mit Phoenix dazu aufgezeichnet wird. Alle wichtigen Infos zur Bearbeitung der Aufgaben findest du im Abschnitt _Phoenix_ in Kapitel 3 des Leitfadens.
- **Chainlit Server herunterfahren:** Stoppe den Chainlit Server, indem du ``STRG C`` im terminal ausführst.
- **Evaluationsdatensatz aufbauen:** Erstelle einen aussagekräftigen Evaluationsdatensatz, indem du die vorhandenen Testfragen in _testdata.csv_ mit mind. 5 eigenen Fragen ergänzt. Achte darauf, dass die Fragen vielfältig und repräsentativ für die Anwendung sind.
- **Konfigurationsdatei anlegen:** Erstelle eine Datei namens _.env_ im Ordner _sprint_3_ und fülle sie mit den erforderlichen Umgebungsvariablen. Verwende dazu die Vorlage aus der Datei _.env_template_ und ergänze die Werte wie in den vorigen Übungen.
- **Evaluation mit Ragas implementieren:** Vervollständige das Code-Skelett im Notebook _ragas_evaluation.ipynb_, um die Evaluierung der RAG-Anwendung durchzuführen. Alle wichtigen Infos zur Bearbeitung der Aufgaben findest du im Abschnitt _RAGAS_ in Kapitel 3 des Leitfadens.
- **Notebook ausführen und Ergebnisse festhalten:** Führe das Notebook aus, indem du
  - einen Jupyter Lab Server mit dem Befehl ```jupyter lab```startest
  - in der Jupyter Lab-Oberfläche in deinem Webbrowser zur Datei _ragas_evaluation.ipynb_ navigierst
  - und die einzelnen Zellen des Notebooks nacheinander ausführst, um die Evaluation durchzuführen.
  
  Wo liefert die Anwendung gute Ergebnisse? Wo eher unzureichende? Analysiere die Metriken und überlege, welche zusätzlichen Metriken oder Anpassungen sinnvoll sein könnten, um ein umfassenderes Bild der App-Leistung zu erhalten.