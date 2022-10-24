#1. Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. As tabelas devem compreender as seguintes funcionalidades:
#a. As tarefas devem ser divididas em “categorias”;
#b. Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
#c. As restrições/relacionamentos devem fazer sentido.

import sqlite3
conexao = sqlite3.connect('tabela_exercicios')

cursor = conexao.cursor()
#cursor.execute ('DROP TABLE tarefas')
#cursor.execute('CREATE TABLE categorias(id_categoria INT NOT NULL, nome VARCHAR(100), gênero VARCHAR(50), PRIMARY KEY (id_categoria));')
#cursor.execute('CREATE TABLE tarefas(id_tarefas INT NOT NULL, nome VARCHAR(100), data VARCHAR(50), status VARCHAR(50), id_categoria INT NOT NULL, PRIMARY KEY (id_categoria), FOREIGN KEY (id_tarefas) REFERENCES categorias(id_categoria));')

conexao.commit()
conexao.close