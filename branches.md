Branching Strategie für Unity-Projekt
1. Main-Branch (main)
🔒 Schreibgeschützt → Niemand pusht direkt auf main.
✅ Ziel: Enthält nur geprüfte, stabile Versionen.
📌 Zusammenführung: Nur durch Merge Request (MR) nach vollständiger Absegnung aller Teammitglieder.
👨‍💻 Wer darf mergen? Alle, aber erst nach Team-Approval.

2. Development-Branch für nächste Version (dev-v1)
✍️ Hauptentwicklungszweig → Hier entsteht die Version, die später abgegeben wird.
✅ Ziel: Nach Fertigstellung geht dieser Branch nach Review auf main.
📌 Zusammenführung: Feature- und Fix-Branches werden über Merge Requests in dev-v1 zusammengeführt.
👨‍💻 Wer darf mergen? Ein zugewiesenes Teammitglied muss absegnen.

3. Feature-Branches (feature/01-Name)
✍️ Neue Features werden hier entwickelt.
✅ Ziel: Nach Fertigstellung gehen sie auf dev-v1.
📌 Regeln:

Muss mit einem Issue verknüpft sein! (feature/01-InventarSystem)
Regelmäßiges Pullen von dev-v1, um Merge-Konflikte zu vermeiden.
Kleinere Features bevorzugt! Falls ein Feature zu groß wird, lieber in kleinere unterteilen (feature/01a-UI, feature/01b-Logik).
👨‍💻 Wer darf mergen? Entwickler des Features nach Code-Review.
4. Bugfix-Branches (fix/01-Name)
🛠 Fixes für Bugs während der Entwicklung.
✅ Ziel: Beheben von Problemen, bevor dev-v1 fertig ist.
📌 Regeln:

Muss mit einem Issue verknüpft sein! (fix/02-Kollisionserkennung)
Fixes für ein Feature gehen auf den zugehörigen Feature-Branch!
Allgemeine Fixes (die mehrere Bereiche betreffen) gehen auf dev-v1
👨‍💻 Wer darf mergen? Entwickler des Fixes oder Feature-Besitzer nach Review.
5. Hotfix-Branches (hotfix/01-Name)
🔥 Dringende Fehlerkorrekturen für die Hauptversion.
✅ Ziel: Kleine, kritische Fixes direkt auf main anwenden.
📌 Regeln:

Nur für Notfälle! (z. B. Crashes oder Gamebreaking-Bugs)
Kein großes Refactoring, nur minimaler Code-Änderungsumfang!
👨‍💻 Wer darf mergen? Entwickler nach Absprache mit Team.
