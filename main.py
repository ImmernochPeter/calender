import sys

from PySide2.QtWidgets import QApplication, QLabel, QWidget

# Erstellen einer Anwendung
app = QApplication(sys.argv)

# Erstellen eines Fensters
window = QWidget()
window.setWindowTitle("PySide2 Einsteigertutorial")
window.setGeometry(100, 100, 300, 200)  # Setzen der Fenstergröße und -position

# Erstellen eines Beschriftungselements
label = QLabel(window)
label.setText("Hallo, PySide2!")
label.move(100, 80)  # Verschieben des Labels innerhalb des Fensters

# Anzeigen des Fensters
window.show()

# Ausführen der Anwendungsschleife
sys.exit(app.exec_())
