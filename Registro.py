from config.connection import Connection

class Persona():

    def __init__(self,nombre,apellido):

        self.nombre = nombre
        self.apellido =apellido
class Docente(Persona):

    def __init__(self,nombre,apellido,Dni,telefono,correo):
        Persona.__init__(self,nombre,apellido)

        self.edad = telefono
        self.Dni = Dni
        self.correo = correo


class Alumno(Persona):

    def __init__(self,nombre,apellido,grado, seccion):
        Persona.__init__(self,nombre,apellido)
        self.grado = grado
        self.seccion = seccion

class Curso:
    
    def __init__(self,curso):
        self.curso = curso

class Notas():

    def __init__(self,alumnos_id, cursos_id,Nota_1,Nota_2, Nota_3, Nota_4):
        self.alumnos = alumnos_id
        self.curso = cursos_id
        self.Nota_1 = Nota_1
        self.Nota_2 = Nota_2
        self.Nota_3 = Nota_3
        self.Nota_4 = Nota_4

class Seccion():

    def __init__(self,  grado, seccion):

        self.grado = grado
        self.seccion = seccion

class Registro():

    def menu(self):
        while True:
            print('''
                Bienvenido al registro de alumnos y docentes : 
                ¿Que desea hacer?
                1) Registrar alumno 
                2) Registrar docente
                3) Actualizar datos del alumno
                4) Actualizar datos del docente
                5) Ingresar notas al alumno
                6) Actulizar notas y curso del alumno
                7) Ingresar un nuevo curso
                8) Actualizar cursos
                9) Ver alumnos registrados
                10) Ver alumnos,grado,sección y notas
                11) Ver profesores registrados
                12) Borrar datos de profesor
                13) Borrar datos del alumno
                14) Borrar curso
                15) Salir del Programa.
            ''')

            opcion = input("> ")

            if opcion == "1":
                
                self.create_table_alumno()
                self.insert_alumnos()
                
            elif opcion == "2": 

                self.create_table_prof()
                self.insert_prof()

            elif opcion == "3":
                
                self.update_alumnos()

            elif opcion == "4":

                self.update_docente()

            elif opcion == "5":

                self.create_table_nota()
                self.insert_notas()

            elif opcion == "6":

                self.update_notas()


            elif opcion == "7":

                self.insert_curso()

            elif opcion == "8":

                self.update_curso()

            elif opcion == "9":

                self.all_alumnos()

            elif opcion == "10":
                
                self.all_registro()

            elif opcion == "11":
                
                self.all_profes()

            elif opcion == "12":

                self.delete_profes()
            
            elif opcion == "13":
                
                self.delete_alum()

            elif opcion == "14":

                self.delete_curso()

            elif opcion == "15":
                print("\nGracias por usar el programa")
                quit()

            else:
                print("\nIntroduciste una opcion incorrecta")


    #CREANDO TABLA DE ALUMNO, INSERTANDO ALUMNOS, ACTULIZANDO DATOS DEL ALUMNOS

    def create_table_alumno(self):

        try:
            conn = Connection('alumnos')
            query = '''
                CREATE TABLE IF NOT EXISTS alumnos(
                    id SERIAL PRIMARY KEY NOT NULL,
                    Nombre VARCHAR (50) NOT NULL,
                    Apellido VARCHAR (50) NOT NULL,
                    Edad INTEGER NOT NULL,
                    DNI INTEGER NOT NULL,
                    grado VARCHAR (20),
                    Seccion INTEGER
                );
            '''

            conn.execute_query(query)
            conn.commit()
        
        except Exception as e:
            conn.rollback()
            print(e)

    def insert_alumnos(self):
        
        try:
            conn = Connection('alumnos')
            conn.insert({
                'Nombre': input('Ingrese el nombre del alumno: '),
                'Apellido':input('Ingrese el apellido del alumno: '),
                'Edad': int(input('Ingrese la edad del alumno: ')),
                'DNI': int(input('Ingrese el DNI del alumno: ')),
                'Grado': input('Ingrese el grado del alumno'),
                'Seccion': input('Ingrese la sección del alumno: ')
            })
            print('---------------------------')
            print('Se registro con éxito')
            print('---------------------------')

        except Exception as e:
            print(e)

    def update_alumnos(self):   
        while True:
            print('''¿Qué datos desea actualizar:
                1) Nombre
                2) Apellido
                3) Edad
                4) Grado
                5) Seccion
                6) Salir.
            ''')
            opcion = input('--> ')

            if opcion == "1":
                try:
                    conn = Connection('alumnos')
                    conn.update({
                        'Nombre': input('Ingrese el nombre del alumno que desea actualizar: ')
                    }, {
                        'Nombre':input('Ingrese el nuevo nombre del alumno: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            if opcion == "2":
                try:
                    conn = Connection('alumnos')
                    conn.update({
                        'Apellido': input('Ingrese el Apellido del alumno que desea actualizar: ')
                    }, {
                        'Apellido':input('Ingrese el nuevo Apellido del alumno: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e) 
            
            if opcion == "3":
                try:
                    conn = Connection('alumnos')
                    conn.update({
                        'Edad': input('Ingrese la edad del alumno que desea actualizar: ')
                    }, {
                        'Edad':input('Ingrese la nueva edad del alumno: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            if opcion == "4":
                try:
                    conn = Connection('alumnos')
                    conn.update({
                        'Grado': input('Ingrese el grado del alumno que desea actualizar: ')
                    }, {
                        'Grado':input('Ingrese el nuevo grado del alumno: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)



            if opcion == "5":
                try:
                    conn = Connection('alumnos')
                    conn.update({
                        'Seccion': input('Ingrese la secció del alumno que desea actualizar: ')
                    }, {
                        'Seccion':input('Ingrese la nueva sección del alumno: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            elif opcion == "6":
                print("\nGracias por usar el programa")
                quit()

            else:
                print("\nIntroduciste una opcion incorrecta")



    def delete_alum(self):
        try:
            conn = Connection('alumnos')
            conn.delete({
                'id': input('Ingrese el Id del alumno que desea eliminar: ')
            })

            print('---------------------------')
            print('Se eliminó el ID con éxito')
            print('---------------------------')
            
        except Exception as e:
            print(e)



    def all_alumnos(self):
        try: 
            conn = Connection('alumnos')
            alumnos = conn.select([])
            for lista_alum in alumnos:
                print(f'\nID: {lista_alum[0]}')
                print(f'Nombre: {lista_alum[1]}')
                print(f'Apellido: {lista_alum[2]}')
                print(f'Edad: {lista_alum[3]}')
                print(f'DNI: {lista_alum[4]}')
                print(f'Grado: {lista_alum[5]}')
                print(f'Seccion: {lista_alum[6]}\n')
                print('-----------------------------------')
        except Exception as e:
            print(e)

    alumno = Alumno('nombre', 'apellido','grado','seccion')


    ##CREANDO TABLA DE PROFESOR, INSERTANDO PROFESORES, ACTULIZANDO DATOS DE LOS PROFESORES

    def create_table_prof(self):

        try:
            conn = Connection('Profesor')
            query = '''
                CREATE TABLE IF NOT EXISTS profesor(
                    id SERIAL PRIMARY KEY NOT NULL,
                    nombre VARCHAR(50) NOT NULL,
                    apellido VARCHAR(50) NOT NULL,
                    DNI INTEGER NOT NULL,
                    Correo VARCHAR (50) NOT NULL,
                    Telefono INTEGER NOT NULL
                );
            '''
            conn.execute_query(query)
            conn.commit()
        
        except Exception as e:
            conn.rollback()
            print(e)


    def insert_prof(self):
        
        try:
            conn = Connection('Profesor')
            conn.insert({
                'Nombre': input('Ingrese el nombre del profesor: '),
                'Apellido':input('Ingrese el apellido del profesor: '),
                'DNI': int(input('Ingrese el DNI del profesor: ')),
                'Correo': input('Ingrese el correo del profesor: '),
                'Telefono': input('Ingrese el teléfono del profesor: ')
            })

            print('---------------------------')
            print('Se actulizó con éxito')
            print('---------------------------')

        except Exception as e:
            print(e)

    profesor = Docente('nombre', 'apellido', 'DNI','Correo','Telefono')

    def update_docente(self):  

        while True:
            print('''¿Qué datos desea actualizar:
                1) Nombre
                2) Apellido
                3) DNI
                4) Correo
                5) Teléfono
                6) Salir.
            ''')

            opcion = input('--> ')

            if opcion == "1":
                try:
                    conn = Connection('Profesor')
                    conn.update({
                        'Nombre': input('Ingrese el nombre del profesor que desea actualizar: ')
                    }, {
                        'Nombre':input('Ingrese el nuevo nombre del profesor: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            if opcion == "2":
                try:
                    conn = Connection('Profesor')
                    conn.update({
                        'Apellido': input('Ingrese el Apellido del profesor que desea actualizar: ')
                    }, {
                        'Apellido':input('Ingrese el nuevo Apellido del profesor: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e) 
            
            if opcion == "3":
                try:
                    conn = Connection('Profesor')
                    conn.update({
                        'DNI': input('Ingrese el DNI del profesor que desea actualizar: ')
                    }, {
                        'DNI':input('Ingrese el nuevo DNI del profesor: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            if opcion == "4":
                try:
                    conn = Connection('Profesor')
                    conn.update({
                        'Correo': input('Ingrese el correo del alumno que desea actualizar: ')
                    }, {
                        'Correo':input('Ingrese el nuevo correo del alumno: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            if opcion == "5":
                try:
                    conn = Connection('Profesor')
                    conn.update({
                        'Telefono': input('Ingrese el Telefono del alumno que desea actualizar: ')
                    }, {
                        'Telefono':input('Ingrese el nuevo Telefono del alumno: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            elif opcion == "6":
                print("\nGracias por usar el programa")
                quit()

            else:
                print("\nIntroduciste una opcion incorrecta")



    
    def delete_profes(self):
        try:
            conn = Connection('Profesor')
            conn.delete({
                'id': input('Ingrese el Id del profesor que desea eliminar: ')
            })

            print('---------------------------')
            print('Se eliminó el ID con éxito')
            print('---------------------------')

        except Exception as e:
            print(e)


    def all_profes(self):
        try: 
            conn = Connection('Profesor')
            profe = conn.select([])
            for lista_profe in profe:
                print(f'\nID: {lista_profe[0]}')
                print(f'Nombre: {lista_profe[1]}')
                print(f'Apellido: {lista_profe[2]}')
                print(f'DNI: {lista_profe[3]}')
                print(f'Correo: {lista_profe[4]}')
                print(f'Telefono: {lista_profe[5]}\n')
                print('-----------------------------------')
        except Exception as e:
            print(e)


    
    # CREANDO TABLA DE CURSO. INSERTANDO NUEVOS CURSOS , ACTUALIZANDO CURSOS 

    def create_table_curso(self):

        try:
            conn = Connection('curso')
            query = '''
                    CREATE TABLE IF NOT EXISTS curso(
                        id SERIAL PRIMARY KEY NOT NULL,
                        curso VARCHAR(50) NOT NULL
                    );
                '''
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            print(e)
    
    def insert_curso(self):
        try:
            conn = Connection('curso')
            conn.insert({
                'Curso': input('Qué curso desea ingresar: ')
            })

            print('Se ingreso el curso con éxito')

        except Exception as e:
            print(e)
    
    def update_curso(self):  

        while True:
            print('¿Qué curso desea actualizar')

            try:
                conn = Connection('curso')
                conn.update({
                    'Curso': input('Ingrese el curso que desea actualizar: ')
                }, {
                    'Curso':input('Ingrese el curso nombre del alumno: ')

                })

                print('---------------------------')
                print('Se actulizó con éxito')
                print('---------------------------')

            except Exception as e:
                print(e)


    def delete_curso(self):

        try:
            conn = Connection('curso')
            conn.delete({
                'id': input('Ingrese el Id del curso que desea eliminar: ')
            })

            print('---------------------------')
            print('Se eliminó el ID con éxito')
            print('---------------------------')
            
        except Exception as e:
            print(e)
    curso = Curso('Curso')


    #CREANDO TABLA DE NOTA DEL ALUMNO, INGRESANDO NOTAS DEL ALUMNO, ACTUALIZANDO NOTAS DEL ALUMNOS

    def create_table_nota(self):

        try:
            conn = Connection('nota')
            query = '''
                    CREATE TABLE IF NOT EXISTS nota(
                        id SERIAL PRIMARY KEY NOT NULL,
                        alumno_id integer NOT NULL,
                        curso_id integer NOT NULL,
                        Nota_1 real NOT NULL,
                        Nota_2 real NOT NULL,
                        Nota_3 real NOT NULL,
                        Nota_4 real NOT NULL
                    );
                '''
            conn.execute_query(query)
            conn.commit()

        except Exception as e:
            conn.rollback()
            print(e)


    def insert_notas(self):
        
        try:
            conn = Connection('nota')
            conn.insert({
                'alumno_id': int(input('Ingrese el ID del alumno: ')),
                'curso_id': int(input('Ingrese el Id del curso: ')),
                'Nota_1': int(input('Ingrese la primera nota del alumno: ')),
                'Nota_2': int(input('Ingrese la segunda nota del alumno: ')),
                'Nota_3': int(input('Ingrese la tercera nota del alumno: ')),
                'Nota_4': int(input('Ingrese la cuarta nota del alumno: '))
            })

            print('---------------------------')
            print('Se ingresó con éxito')
            print('---------------------------')

        except Exception as e:
            print(e)




    def all_registro(self):
        try:
            conn = Connection('nota')
            query = '''
                SELECT a."id",a."nombre" as "Nombre del alumno" ,
                    a."apellido" as "Apellido",
                    a."edad" as "Edad",
                    a."dni" as "DNI",
                    s."grado" as "Grado",
                    s."seccion" as "Seccion",
                    c."curso" as "Curso",
                    n."nota_1" as "Nota 1",
                    n."nota_2" as "Nota 2",
                    n."nota_3" as "Nota 3",
                    n."nota_4" as "Nota 4"
                    FROM "alumnos" a, "curso" c , 
                    "nota" n, "seccion" s
                    WHERE a."id" = n."id" and
                    c."id" = n."id"
            '''
            cursor = conn.execute_query(query)
            nota = cursor.fetchall()
            for notas in nota:
                print('---------------------------')
                print(f'\nID: {notas[0]}')
                print(f'Nombres del alumno: {notas[1]} {notas[2]}')
                print(f'Edad: {notas[3]}')
                print(f'DNI: {notas[4]}')
                print(f'Grado: {notas[5]}')
                print(f'Seccion: {notas[6]}')
                print(f'Curso: {notas[7]}')
                print(f'Nota 1: {notas[8]}')
                print(f'Nota 2: {notas[9]}')
                print(f'Nota 3: {notas[10]}')
                print(f'Nota 4: {notas[11]}\n')
                print('----------------------------------')

        except Exception as e:
            print(e)

    def update_notas(self):

        while True:
            print('''¿Qué datos desea actualizar?
                1) Nota 1
                2) Nota 2
                3) Nota 3
                4) Nota 4
                5) Curso
                6) Salir.
            ''')

            opcion = input('--> ')

            if opcion == "1":
                try:
                    conn = Connection('nota')
                    conn.update({
                        'alumno_id': input('Ingrese el ID del alumno: '),
                        'Nota_1': input('Ingrese la nota actual: ')
                    }, {
                        'Nota_1':input('Ingrese la nueva nota: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)
            
            if opcion == "2":
                try:
                    conn = Connection('nota')
                    conn.update({
                        'alumno_id': input('Ingrese el ID del alumno: '),
                        'Nota_2': input('Ingrese la nota actual: ')
                    }, {
                        'Nota_2':input('Ingrese la nueva nota: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            if opcion == "3":
                try:
                    conn = Connection('nota')
                    conn.update({
                        'alumno_id': input('Ingrese el ID del alumno: '),
                        'Nota_3': input('Ingrese la nota actual: ')
                    }, {
                        'Nota_3':input('Ingrese la nueva nota: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            if opcion == "4":
                try:
                    conn = Connection('nota')
                    conn.update({
                        'alumno_id': input('Ingrese el ID del alumno: '),
                        'Nota_4': input('Ingrese la nota actual: ')
                    }, {
                        'Nota_4':input('Ingrese la nueva nota: ')

                    })

                    print('---------------------------')
                    print('Se actulizó con éxito')
                    print('---------------------------')

                except Exception as e:
                    print(e)

            elif opcion == "5":
                try:
                    conn = Connection('nota')
                    conn.update({
                        'alumno_id': input('Ingrese el ID del alumno que desea para actualizar el curso: '),
                    }, {
                        'curso_id': input('Ingrese el ID del curso nuevo: ')
                    })
                except Exception as e:
                    print(e)

            elif opcion == "6":
                print("\nGracias por usar el programa")
                quit()

            else:
                print("\nIntroduciste una opcion incorrecta")    

    calificaciones = Notas('alumnos_id', 'cursos_id','Nota_1','Nota_2', 'Nota_3', 'Nota_4')

    def create_table_seccion(self):

        try:
            conn = Connection('seccion')
            query = '''
                CREATE TABLE IF NOT EXISTS seccion(
                    id SERIAL PRIMARY KEY NOT NULL,
                    grado VARCHAR (50) NOT NULL,
                    seccion VARCHAR (10) NOT NULL
                );
            
            '''
            conn.execute_query(query)
            conn.commit()
        
        except Exception as e:
            conn.rollback()
            print(e)

    def insert_grado_seccion(self):

        try:
            conn = Connection('seccion')
            conn.insert({
                'Grado': input('Ingrese el grado del alumno: '),
                'Seccion':input('Ingrese la sección del alumno: ')
            })

            print('---------------------------')
            print('Se ingresó con éxito')
            print('---------------------------')

        except Exception as e:
            print(e)



class Inicio(Registro):

    def __init__(self):

        try:
            
            self.menu()
            
            
        
        except KeyboardInterrupt:

            print("\nAplicacion Interrumpida")


Inicio()