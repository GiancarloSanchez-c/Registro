from psycopg2 import connect
import psycopg2
class Connection:

    def __init__(self, table_name):
        self.table_name = table_name

        self.db = connect(host='localhost', user ='postgres',password='Gian23080',
                        database ='Semana_reto2', port = 5433)

        self.cursor = self.db.cursor()

    #Ejecutando consulta

    def execute_query(self, query):

        self.cursor.execute(query)
        self.commit()
        return self.cursor
    
    def insert(self,data):

        try:

            list_values = ""
            for value in data.values():
                if isinstance(value, str):
                    value = f"'{value}'"
                list_values += f'{value},'
                
            # print(list_values)

            query = f'''
                INSERT INTO {self.table_name} ({", ".join(data.keys())}) VALUES ({list_values[:-1]})
            '''            

            self.execute_query(query)
            return True
            
        except psycopg2.Error as e:
            print("Error ",e) 


    def select(self, data=[]):

        try:

            fields = ", ".join(data)
            if not len(data): 
                fields = '*'

            query = f'''
                SELECT {fields} FROM {self.table_name}
            '''
            self.cursor.execute(query)
            return self.cursor.fetchall()

        except psycopg2.Error as e:
            print("Error ",e) 

    def delete(self,id):

        try:
            where_delete = []
            for field_name, field_value in id.items():
                if isinstance(field_value, str):
                    field_value = f"'{field_value}'"
                where_delete.append(f"{field_name} = {field_value}")


            query = f'DELETE FROM {self.table_name} WHERE {" = ".join(where_delete)};'

            self.execute_query(query)

        except psycopg2.Error as e:
            print("Error ",e) 


    def update(self, id, data):
        try:
            list_where = []
            for field_name, field_value in id.items():
                if isinstance(field_value, str):
                    field_value = f"'{field_value}'"
                list_where.append(f"{field_name} = {field_value}")
            
            list_update = []
            for field_name, field_value in data.items():
                if isinstance(field_value, str):
                    field_value = f"'{field_value}'"
                list_update.append(f"{field_name} = {field_value}")

            query = f'''
                UPDATE {self.table_name} SET {', '.join(list_update)}
                WHERE {' AND '.join(list_where)}
            '''

            self.execute_query(query)
            return True

        except psycopg2.Error as e:
            print("Error ",e) 


    def commit(self):

        self.db.commit()

        return True


    def rollback(self):

        self.db.rollback()

        return True