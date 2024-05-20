            self.checkboxes = []
            self.GOSTS = getGOST()
            self.GOSTTP = requests.get('http://127.0.0.1:8000/Связь%20ГОСТ%20и%20ТП/').json()
            self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_3)
            for i in range(len(self.GOSTS)):
                isTRUE = 0
                checkbox = QCheckBox(self.GOSTS[i]['gostName'], self.scrollAreaWidgetContents_3)
                checkbox.setObjectName(f"checkBox_{i}")

                for j in range(len(self.GOSTTP)):
                    if self.GOSTTP[j]['idDOCK'] == self.dataThisTP['id']:
                        if self.GOSTTP[j]['idGOST'] == self.GOSTS[i]['id']:
                            isTRUE = 1
                            break
                
                if (isTRUE == 1):
                    checkbox.setChecked(True)
                else:
                    checkbox.setChecked(False)
                isTRUE = 0
                self.checkboxes.append(checkbox)
                self.verticalLayout.addWidget(checkbox)