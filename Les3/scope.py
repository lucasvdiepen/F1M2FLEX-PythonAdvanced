class MijnClass:
    varOpenbaar = "Dit is openbaar toegangkelijk"
    __varPrive = "Deze is prive"

    def Voorbeeld(self):
        print(self.__varPrive)

        waardeA = "Tijdelijk"
        print("waardeA is:", waardeA)

    def AndereFunctie(self):
        # waardeA bestaat ALLEEN binnen functie "Voorbeeld"
        # print(waardeA)

        # Vanaf dit punt voeg ik een nieuwe variabele toe aan de instantie van deze class
        self.nieuweVariabele = "Deze variabele is nieuw!"


instClass = MijnClass()
print(instClass.varOpenbaar)
instClass.varOpenbaar = "Veranderd"

instClass.Voorbeeld()
instClass.AndereFunctie()

# Vanaf dit punt bestaat "instClass.nieuweVariabele" wel
print ("Bestaat de variabele 'nieuweVariabele ' al?", instClass.nieuweVariabele)