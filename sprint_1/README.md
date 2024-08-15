### Sprint 1: Grundlegende Chainlit App
In dieser ersten Übung legen wir das Fundament für eine RAG-Anwendung, auf dem wir in den kommenden Übungen aufbauen werden. Dazu legen wir uns als Erstes eine simple Chainlit App an, mit der wir mit einem LLM kommunizieren können.

Hier sind die erforderlichen Schritte, um mit der Entwicklung loszulegen:
- **Gitlab Repository klonen**: Klone das Gitlab Repository zur Übung mit dem folgenden Befehl in einen Ordner deiner Wahl
```git clone https://gitlab.inovex.de/jheinz2/data2day-rag-workshop.git```
- **Erforderliche Python-Pakete installieren:** Installiere die benötigten Python-Pakete, indem du im Terminal den Befehl ```pip install -r requirements.txt``` ausführst.
- **Code-Skelett vervollständigen:** Fülle das vorgegebene Code-Skelett in der Datei _app.py_ aus. Alle dazu benötigten Informationen kannst du im ersten Kapitel des Cheatsheet finden oder auch die [Dokumentation von Chainlit](https://docs.chainlit.io) nutzen, falls du etwas genauer nachlesen möchtest.
- **App starten:** Starte das Skript der App, indem du
  - den Terminal deines Betriebssystems öffnest,
  - in den Ordner _sprint_1/src_ wechselst,
  - und den Befehl ```chainlit run app.py -w``` ausführst. Der Parameter ```-w``` sorgt dabei dafür, dass die App bei Änderungen des Codes automatisch neu geladen wird.
- **Optional - Einstellungsmöglichkeiten ergänzen:** Chainlit bietet die Möglichkeit, verschiedene Einstellungsmöglichkeiten in der Oberfläche vorzunehmen. Ergänze den Code der App, sodass z.B. die Temperature des LLMs flexibel eingestellt werden kann. 
