# Importando a classe ConexaoMySQL do arquivo database.py
import database as db

# Classe Estado que representa um estado.
class Estado:
    
    # Construtor da classe Estado que inicializa os atributos.
    def __init__(self):
        self.id = 0
        self.nome = ""
        self.sigla = ""
        
        # Inicializa uma instância da classe ConexaoMySQL para gerenciar a conexão com o banco de dados.
        self.db = db.ConexaoMySQL()
        
# Método para salvar um estado no banco de dados.
    def salvar(self):
        conn = self.db.abrir()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "INSERT INTO estado (nome, sigla) VALUES (%s, %s);"
                    cursor.execute(sql, (self.nome, self.sigla))
                    conn.commit()
                    self.id = cursor.lastrowid
                    print("Salvo com sucesso!")
            except Exception as e:
                print(f"Erro ao salvar estado: {e}")
            finally:
                self.db.fechar()
                
# Método para listar todos os estados cadastrados no banco de dados.
    def listar(self):
        conn = self.db.abrir()
        estados = []
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "SELECT id, nome, sigla FROM estado;"
                    cursor.execute(sql)
                    estados = cursor.fetchall()
            except Exception as e:
                print(f"Erro ao listar estados: {e}")
            finally:
                self.db.fechar()
        return estados
    
# Método para atualizar os dados de um estado existente no banco de dados.
    def atualizar(self):
        conn = self.db.abrir()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "UPDATE estado SET nome = %s, sigla = %s WHERE id = %s;"
                    cursor.execute(sql, (self.nome, self.sigla, self.id))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Atualizado com sucesso!")
                    else:
                        print("Nenhum estado encontrado com o ID informado.")
            except Exception as e:
                print(f"Erro ao atualizar estado: {e}")
            finally:
                self.db.fechar()
                
# Método para excluir um estado do banco de dados pelo ID.
    def excluir(self):
        conn = self.db.abrir()
        if conn:
            try:
                with conn.cursor() as cursor:
                    sql = "DELETE FROM estado WHERE id = %s;"
                    cursor.execute(sql, (self.id,))
                    conn.commit()
                    if cursor.rowcount > 0:
                        print("Excluído com sucesso!")
                    else:
                        print("Nenhum estado encontrado com o ID informado.")
            except Exception as e:
                print(f"Erro ao excluir estado: {e}")
            finally:
                self.db.fechar()