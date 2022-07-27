from datetime import datetime

def log(...):
        #! Hay que cambiar el contenido de esta funcion
    "La idea seria que esta funcion nos diga que es lo que fue haciendo el codigo."
    "Y lo guarde en un logger"
    file= open('logger.txt', 'w')
    content =f'... ... ... ...'
    for i in ...:
            actual_time = datetime.now()
            content = content + f'[{actual_time}]:       ... ... ...'
    file.write(content)
    file.close()
    pass