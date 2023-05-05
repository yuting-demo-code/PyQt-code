from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

app = QApplication([])

main_widget = QWidget()
main_layout = QVBoxLayout()
main_widget.setLayout(main_layout)
button_texts = ["btn"+str(i) for i in range(5)]

def set_label_text(i):
    print(i)

for i, text in enumerate(button_texts):
    button = QPushButton(text)
    button.clicked.connect(lambda checked, i=i: set_label_text(i))
    main_layout.addWidget(button)


main_widget.show()
app.exec_()
