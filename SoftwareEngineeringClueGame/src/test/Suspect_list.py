import sys
from PyQt5.QtWidgets import QApplication, QListWidget, QListWidgetItem, QLabel, QDialog

class Suspect_list(QListWidget):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        
        suspects = ['Scarlett', 'Mustard', 'Orchid', 'Green', 'Peacock', 'Plum']
        
        for suspect in suspects:
            self.addItem(suspect)
            
        self.itemClicked.connect(self.launchPop_up)
            
    def launchPop_up(self, item):
        pop = Pop_up(item.text(), self)
        pop.show()
            
class Pop_up(QDialog):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.resize(600, 300)
        self.label = QLabel(name, self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    demo = Suspect_list()
    demo.show()
    
    sys.exit(app.exec_())