def arrondir_notes(notes):
     notes_arrondi=[]
     for note in notes:
          if note>=40:
               multiple=((note// 5)+1)*5
               difference= multiple - note

               if difference < 3:
                    note = multiple
     notes_arrondi.append(note)   
     if note <40:
          print(f"la note est de{notes_arrondi}, test échoué ")
     else:
        print(f"la note est de {notes_arrondi}, test réussi ")
     
     
     return notes_arrondi
arrondir_notes([82])







# def test(note):
#     if note<40:
#          print("test échoué")
#     else:
#          print("test réussi")
# test(12)

