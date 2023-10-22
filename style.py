toolbarStyle = """
            QToolBar {
                background-color: #121212; /* Arka plan rengi - koyu gri */
                border: none;
            }
            QToolButton {
                background-color: #121212; /* Düğme arka plan rengi - koyu gri */
                border: none;
                color: white; /* Düğme metin rengi - beyaz */
                padding: 10px 14px; /* Düğme iç içe olma mesafesi */
            }
            QToolButton:hover {
                background-color: #1e1e1e; /* Fare üzerine geldiğinde arka plan rengi - biraz daha açık gri */
            }
            QToolButton:checked {
                background-color: #171717; /* Seçili düğme arka plan rengi - mavi */
                color: white; /* Seçili düğme metin rengi - beyaz */
            }
            QToolButton:checked:hover {
                background-color: #6600cc; /* Tıklı ve fare üzerindeyken arka plan rengi - mor */
            }
        """
infoButtonStyle = """
                color: white;
                selection-color: white;
                selection-background-color: white;
            """
