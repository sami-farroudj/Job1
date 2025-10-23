# def code(language):
#     if language== "javascript":
#         print("tu es développeur web")
   
#     elif language=="python":
#         print("tu es développeur IA")

#     elif language=="java":
#         print("tu es un développeur logiciel")
    
#     elif language=="reactjs":
#         print("tu es un développeur mobile")
    
#     else: print("un jour,je serais le meilleur développeur")
# (code("python"))

# refaire en mach case

def code(language):
    match language:
        case "javascript":
            print("tu es développeur web")
        case "python":
            print("tu es un développeur ia")
        case "java":
            print("tu es développeur logiciel")
        case "reactjs":
            print("tu es développeur mobile")
        case _ :
            print("un jour je serais le meilleur développeur")

code("javascript")
code("python")
code("java")
code("reactjs")
code("skl")