class Documentaire:
    _nombre_objet = 0
    def __init__(self ,title ,date_exit):
        # self._code = code 
        self._title = title
        self._date_exit = date_exit
        Documentaire._nombre_objet +=1

    def GetCodeCount(self):
         return Documentaire._nombre_objet
    
    # def SetCodeCount(self ,NewCode):
    #      self._nombre_objet = NewCode
    
    def GetTitle(self):
        return self._title
    
    def SetTitle(self ,NewTitle):
        self._title = NewTitle
    
    def GetDate_exit(self):
        return self._date_exit
    
    def SetDate_exit(self ,date_exit):
        self._date_exit = date_exit

    def ToString(self):
        return "\nTitle : "+str(self._title)+"\nDate exit : "+str(self._date_exit)+"\ncount : "+"Dev00"+str(Documentaire._nombre_objet)
    
    def Equals(self,doc):
        if(self.GetCodeCount == doc.GetCodeCount):
            return True
        else:
            return False
        
class Exemplaire(Documentaire):
    def __init__(self ,title ,date_exit ,num ,date_achat):
        Documentaire.__init__(self ,title ,date_exit)
        self._num = num
        self._date_achat = date_achat

    def GetNum(self):
        return self._num
    
    def SetNum(self,NewNum):
        self._num = NewNum

    def GetDate_achat(self):
        return self._date_achat
    
    def SetDate_achat(self,NewDatea):
        self._date_achat = NewDatea

    def ToString(self):
        return super().ToString()+"\nNumero : "+self._num+"\nDate d'achat : "+self._date_achat
    
    def Equals(self, numeros):
        return super().Equals(numeros)
    

D1 = Documentaire("Le titre",2025)
print(D1.ToString())

D2 = Exemplaire("Titre2",2026,453,2022)
print(D1.ToString())


    
