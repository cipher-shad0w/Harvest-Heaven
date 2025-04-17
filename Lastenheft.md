## 1. Projektübersicht

**Name des Projektes:** Harvest Heaven  
**Entwickler:** Jannis Krija, Jannis Niese, Tobias Lehmann
**Projektziel:** Entwicklung eines Farming-Games als Unterrichtsprojekt  
**Engine:** Unity  
**Programmeirsprache:** C#
**KI-Integration:** Verschiedene LLMs getestet (nicht erfolgreich) 

## 2. Arbeitsaufwand und Tätigkeiten

### 20.01. - 04:00 Jannis K.

- Genereller Aufbau und Rundeinstellungen
- Erstellen der Scene und Importieren der Grafiken
- Zuschneiden und Anpassen der Grafiken

### 21.01. - 02:00 Jannis K.

- Git-Setup (VCS)
- Erstellen eines Jira-Boards mit ersten Aufgaben
- Teamarbeitsstruktur eingerichtet

### 21.01. - 06:00 Jannis K.

- Map erstellt (verschiedene Ebenen)
- Spieler erstellt
- Spielerbewegung implementiert
- Kollision zwischen Spieler und Gegenständen
- Einarbeitung in Unity allgemein

### 25.01. - 03:00 Jannis K.

- Erstellung eines Items zum Einsammeln
- Items können jetzt eingesammelt werden und verschwinden von der Map
- Inventarsystem: Liste, die speichert, wie viele Items man von welcher Sorte hat

### 05.03. - 01:00 Jannis K.

- Erstellung einer Minimap
- Merge-Probleme (05:00)

### 06.03. - 04:00 Jannis K.

- Einarbeitung in KI in Spielen
- Erste Implementierungsversuche (keine funktionierenden Ergebnisse)
- LLM in Python zum Laufen gebracht

### 06.03. - 00:30 Jannis K.

- Erweiterung der Map, damit die Minimap gut aussieht

### 07.03. - 02:00 Jannis K.

- Prompt für das LLM geschrieben, das dem Spieler die Spielmechanik erklären soll

### 13.03. - 03:00 Jannis K.

- LLM-Code geschrieben und eingebunden
- Aufgrund des hohen Zeitaufwands aufgegeben (ging nicht)

### 14.03. - 01:00 Jannis K.

- Minimap wurde beschädigt und gelöscht
- Neue Minimap erstellt

### 15.03. - 02:00 Jannis K.

- Felder neu erstellt
- Pflanzen erstellt
- Spieler kann jetzt Pflanzen auf Feldern platzieren

### 15.03. - 02:00 Jannis K.

- Pflanzen können wachsen
- Spieler kann sie ernten und neu pflanzen
- **Bugs:**
    - Pflanzen können nur neu gepflanzt, aber nicht eingesammelt werden
    - Beim neuen Pflanzen verschieben sich die Pflanzen einige Pixel nach oben
    - Lösung: Pflanze ins Inventar aufnehmen, dann normal pflanzen

## 3. Probleme und Lösungen

### Git und Version Control

- **Problem:** Dateien zu groß für normales Git
- **Lösung:** Erst Unity Version Control System ausprobiert, dann auf Git mit externem Server (LFS) gewechselt

### Mergen der Minimap auf `dev-v1`

- **Problem:** Merge-Prozess hat die `main scene` gelöscht
- **Lösung:** Umständlich rückgängig gemacht und Minimap neu implementiert

### `main scene` mit Git LFS

- **Problem:** Scene-Dateien oft beschädigt, weil LFS nicht gut zu mergen war

### Minimap-Probleme

- **Problem:** Minimap war mit festen Koordinaten platziert → unterschiedliche Monitorgrößen führten zu falscher Platzierung
- **Lösung:** Minimap relativ zur Spielfläche platziert

## 4. Bugs und Lösungen

### Spielerbewegung

- **Problem:** Spieler glitched beim Kollidieren mit Hindernissen
- **Lösung:** Bewegung in blockierte Richtung verhindern

### Pflanzenplatzierung

- **Problem:** Pflanzen erscheinen an falscher Position
- **Lösung:** Pflanze muss erst ins Inventar aufgenommen werden, dann kann sie korrekt platziert werden

### Wasser-Kollision

- **Problem:** Spieler kann einige Pixel ins Wasser laufen
- **Lösung:** Collider vergrößert, sodass Wasser nicht mehr berührt wird

### LLM-Integration

- **Problem:** LLM gibt keine sinnvollen Antworten
- **Lösung:** Debugging-Phase einführen, um bessere UI für Interaktion zu entwerfen

## 5. KI-Planung und Umsetzung

- Idee: NPCs als LLMs, mit denen Spieler interagieren können
- Anfangs sollte ein Spielleiter als LLM das Spiel erklären
- Implementierung mit Flask-Server in Python
- **Problem:** Server hat nicht funktioniert (unbekannter Fehler)

## 6. Projektmanagement und Versionskontrolle

### Arbeitsorganisation

- Jira-Kanban-Board für Aufgabenverwaltung
- Teammitglieder haben selbstständig Issues bearbeitet

### Branching-Modell

1. **Main-Branch (`main`)**
    - Schreibgeschützt, nur für stabile Versionen
    - Merges nur nach vollständigem Review

2. **Development-Branch (`dev-v1`)**
    - Hauptentwicklungszweig
    - Enthält unfertige Features, die später auf `main` gehen

3. **Feature-Branches (`feature/XX-Name`)**
    - Entwickelt neue Features
    - Muss mit Issue verknüpft sein (z. B. `feature/01-Inventarsystem`)
    - Regelmäßiges Pullen von `dev-v1`, um Merge-Konflikte zu vermeiden

4. **Bugfix-Branches (`fix/XX-Name`)**
    - Behebt Bugs während der Entwicklung
    - Falls ein Bug ein Feature betrifft, Fix auf Feature-Branch
    - Allgemeine Fixes gehen direkt auf `dev-v1`
    
5. **Hotfix-Branches (`hotfix/XX-Name`)**
    - Nur für kritische Fehlerkorrekturen auf `main`
    - Kein großes Refactoring, nur minimale Code-Änderungen

### Herausforderungen bei Version Control

- **Problem:** `main scene` wurde mehrfach beschädigt, weil mehrere Entwickler daran arbeiteten
- **Lösung:** PRs und Merges immer von anderen Teammitgliedern überprüfen lassen

## 7. Gameplay-Mechaniken

### Spielerbewegung

- **Steuerung:** WASD oder Pfeiltasten
- **Kamera:** Verfolgt den Spieler
- **Kollisionen:** Spieler interagiert mit Umgebung

### Pflanzen und Felder

- **Platzierung:** Taste drücken, wenn Spieler auf Feld steht
- **Wachstum:** Pflanzen wachsen mit der Zeit
- **Ernte:** Spieler kann reife Pflanzen ernten
- **Inventar:** Geerntete Pflanzen ins Inventar aufnehmen

### Minimap

- **Positionierung:** Oben rechts, skaliert relativ zur Spielfläche

## 8. Verbesserungen und Erkenntnisse

- **Git ist essenziell:** Alles sollte über Git organisiert sein
- **Merge-Prozesse müssen sauber laufen:** Jede PR muss überprüft werden
- **Code-Reviews sind wichtig:** Andere sollten den Code verstehen und prüfen

## 9. Offene Punkte und mögliche Erweiterungen

- **LLM-Integration verbessern:** Debugging des Flask-Servers
- **Mehr Interaktionen mit NPCs:** Quest- oder Dialogsystem einbauen
- **Zusätzliche Features:** Mehr Pflanzensorten, erweiterte Farming-Mechaniken
