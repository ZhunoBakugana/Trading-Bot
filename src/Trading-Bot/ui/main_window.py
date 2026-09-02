#Open the app from here
import sys
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)

# Create a proper, empty window container
window = QMainWindow()
window.setWindowTitle("Trading Hub")
window.resize(400, 300) # Sets an initial width and height

# Show the window directly
window.show()

app.exec()
