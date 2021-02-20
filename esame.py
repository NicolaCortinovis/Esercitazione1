# Esercitazione 1 del corso Laboratorio di Programmazione data 12/01/2021
# Nicola Cortinovis

class ExamException(Exception):
    pass


class MovingAverage():

    # Costruttore della classe MovingAverage, l'unico parametro e' la dimensione della
    # finestra con cui calcolare la media mobile

    def __init__(self,window):

        self.window = window # La dimensione della finestra
        # window <= 0 ?
        if(self.window <= 0):
            raise ExamException('Errore, il parametro window "{}" risulta essere < o = a 0'.format(self.window))
        # Si puo' convertire a float?
        try:
            float(self.window)
        except:
            raise ExamException('Errore,il parametro window "{}", non e\' convertibile a float'.format(self.window))
        
        # Se window e' un float, arrotondalo
        if isinstance(self.window,float):
            # print('Era float ho arrotondato')
            self.window = round(self.window)
        
        # Se window e' una stringa convertibile, convertila
        elif isinstance(self.window,str):
            # print('Era str convertibile ho convertito')
            # Se self.window e' una stringa, convertimela a float e poi arrotondamela così vengono gestiti entrambi i casi della stringa contente un float o un int
            self.window = float(self.window)
            self.window = round(self.window)


    # Metodo compute, data una lista in input il metodo andra' a calcolare la media mobile
    # di tutta la lista sulla base della dimensione della finestra ritornando a fine
    # esecuzione una lista contenente i valori della media mobile


    def compute(self,lista):

        # La lista che ritornero' a fine esecuzione
        lista_media_mobile = []

        # La lista passata e' una lista?
        if not isinstance(lista,list):
            raise ExamException('Errore, il parametro lista "{}" passato nella funzione compute della classe MovingAverage non e\' di tipo list'.format(lista))
        
        # La lista passata contiene interi o float?  Se riesci converti tutto a float e arrotonda
        for item in lista:
            try:
                float(item)
            except:
                raise ExamException('Errore, il parametro "{}" della lista "{}" passata nella funzione compute della classe MovingAverage non e\' convertibile a float e quindi non e\' valido'.format(item,lista))

        # Convertimi tutti gli elementi a float
        lista = [float(item) for item in lista]

        # Leggo tutti gli elementi della lista
        for i in range(len(lista)):

            # Skip degli elementi fino a quando ho a sinistra della i un numero
            # sufficiente di elementi per calcolarmi la prima media mobile, self.window - 1
            # perche' partiamo da 0
            if(i < (self.window - 1)):
                continue
            
            # Dove mi salvo i valori estratti dalla lista per calcolarmi la media mobile
            # viene inizializzata a vuota per ogni ciclo for, cioe' per ogni finestra
            # esaminata
            lista_appoggio = []

            # Indice j che indica l'i-esimo elemento e che andremo a decrementare ed un indice counter per controllare quanti elementi ho messo nella lista_appoggio
            j = i
            counter = 0
            # Finche' counter e' minore della finestra
            while(counter < self.window):
                # Inserisco nella lista d'appoggio l'elemento j-esimo, incremento counter e decremento j
                lista_appoggio.append(lista[j])
                counter += 1
                j -= 1
            
            # Variabile dove salvarmi la somma degli elementio della lista_appoggio
            somma = 0

            # Sommo tutti gli elementi della lista_appoggio
            for element in lista_appoggio:
                somma += element

            # Valore che salvero' nella lista_media_mobile
            media_mobile = somma / self.window

            # Lo salvo nella lista_media_mobile
            lista_media_mobile.append(media_mobile)

        # Ritorno la lista_media_mobile con tutti i valori calcolati
        return lista_media_mobile

########## Parte di soft testing del programma, cancellami/commentami alla fine ##########

#testing_list = [2,"3.5",6,8,10,12,14,16]
#testing_obj = MovingAverage(2)
#testing_mob_avg = testing_obj.compute(testing_list)

#expected_list = [3,5,7,9,11,13,15]
#print(expected_list)
#print(testing_mob_avg)

###########################################################################################

# Voto testato: 25
# Note:
# Quando vado a fare dei test non cercare di risolvere problemi facendo delle conversioni,semplicemente alza l'eccezione e la storia finisce lì. Nel testing il mio programma non gestiva il caso None con un'eccezione perchè evidentemente e' convertibile a float e provava a lavorarci, non gestiva con un' eccezione il caso in cui window era un float perche' lo convertiva e provava a lavorarci e quindi altro "errore". L'unico errore "vero" ed abbastanza grave e' che non ho effettuato un check sulla lunghezza della lista passata e window, cioè chiaramente window non puo' mai essere piu' grande della lunghezza della lista. Tutto sommato un'esercitazione molto utile per capire quello che il prof vuole venga fatto