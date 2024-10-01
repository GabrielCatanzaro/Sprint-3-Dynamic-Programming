# Matrizes para armazenar os dados
usuarios = []  # Cada usuário será armazenado como [id_usuario, nome, especialidade, experiencia]
treinamentos = []  # Cada treinamento será [id_treinamento, id_usuario, procedimento, tempo_execucao, pontuacao]
desempenho = []  # Cada desempenho será [id_desempenho, id_treinamento, precisao, erros_cometidos]

# Função para gerar IDs automáticos
def gerar_id(lista):
    if lista:
        return lista[-1][0] + 1  # O próximo ID será o último + 1
    return 1

# Função para registrar um novo usuário
def registrar_usuario(nome, especialidade, experiencia):
    id_usuario = gerar_id(usuarios)
    usuarios.append([id_usuario, nome, especialidade, experiencia])
    print(f"Usuário {nome} registrado com ID {id_usuario}")
    return id_usuario

# Função para iniciar um treinamento
def iniciar_treinamento(id_usuario, procedimento):
    id_treinamento = gerar_id(treinamentos)
    # O tempo_execucao e a pontuação são armazenados mais tarde
    treinamentos.append([id_treinamento, id_usuario, procedimento, None, None])
    print(f"Treinamento para o procedimento '{procedimento}' iniciado com ID {id_treinamento}")
    return id_treinamento

# Função para salvar o desempenho
def salvar_desempenho(id_treinamento, precisao, erros_cometidos):
    id_desempenho = gerar_id(desempenho)
    desempenho.append([id_desempenho, id_treinamento, precisao, erros_cometidos])
    print(f"Desempenho salvo com ID {id_desempenho}")
    return id_desempenho

# Função para registrar o tempo de execução e a pontuação
def finalizar_treinamento(id_treinamento, tempo_execucao):
    for treino in treinamentos:
        if treino[0] == id_treinamento:
            pontuacao = calcular_pontuacao(tempo_execucao, treino)
            treino[3] = tempo_execucao
            treino[4] = pontuacao
            print(f"Treinamento {id_treinamento} finalizado. Tempo: {tempo_execucao} Pontuação: {pontuacao}")
            return pontuacao
    print(f"Treinamento {id_treinamento} não encontrado.")
    return None

# Função para calcular a pontuação final (tempo e erros afetam negativamente, precisão aumenta a pontuação)
def calcular_pontuacao(tempo_execucao, treino):
    for record in desempenho:
        if record[1] == treino[0]:  # Se o desempenho corresponder ao treinamento
            precisao = record[2]
            erros_cometidos = record[3]
            pontuacao = (precisao * 100) - (erros_cometidos * 5) - (tempo_execucao * 2)
            return max(pontuacao, 0)  # A pontuação mínima é 0
    return 0

# Função para exibir o relatório de um treinamento
def exibir_relatorio(id_treinamento):
    for treino in treinamentos:
        if treino[0] == id_treinamento:
            id_usuario = treino[1]
            for user in usuarios:
                if user[0] == id_usuario:
                    nome = user[1]
                    procedimento = treino[2]
                    tempo_execucao = treino[3]
                    pontuacao = treino[4]
                    print(f"Relatório para {nome} no procedimento {procedimento}:")
                    print(f" - Tempo de execução: {tempo_execucao}")
                    print(f" - Pontuação: {pontuacao}")
                    return
    print(f"Treinamento {id_treinamento} não encontrado.")

# Função para exibir o histórico de todos os treinamentos de um usuário
def exibir_historico_usuario(id_usuario):
    print(f"Histórico de Treinamentos para o Usuário {id_usuario}:")
    for treino in treinamentos:
        if treino[1] == id_usuario:
            print(f" - Treinamento {treino[0]}: Procedimento {treino[2]}, Tempo {treino[3]}, Pontuação {treino[4]}")

# Função para listar todos os usuários
def listar_usuarios():
    print("Lista de Usuários:")
    for user in usuarios:
        print(f"ID: {user[0]}, Nome: {user[1]}, Especialidade: {user[2]}, Experiência: {user[3]}")

# Função para listar todos os treinamentos
def listar_treinamentos():
    print("Lista de Treinamentos:")
    for treino in treinamentos:
        print(f"ID: {treino[0]}, Usuário: {treino[1]}, Nome: {usuarios[treino[1]-1][1]}, Procedimento: {treino[2]}, "
              f"Tempo: {treino[3]}, Pontuação: {treino[4]}")


# Exemplo de uso do sistema para treinamento ou registro de médico
id_usuario = registrar_usuario("Dr. João", "Cirurgia Geral", 5)
id_treinamento = iniciar_treinamento(id_usuario, "Apendicectomia")
id_desempenho = salvar_desempenho(id_treinamento, precisao=0.95, erros_cometidos=2)
finalizar_treinamento(id_treinamento, tempo_execucao=15.5)

id_treinamento2 = iniciar_treinamento(id_usuario, "Esplenectomia ")
id_desempenho2 = salvar_desempenho(id_treinamento2, precisao=1.1, erros_cometidos=3)
finalizar_treinamento(id_treinamento2, tempo_execucao=18.25)

id_usuario2 = registrar_usuario("Dr. Pedro", "Nefrologista", 6)
id_treinamento3 = iniciar_treinamento(id_usuario2, "Cirurgia das glândulas suprarrenais ")
id_desempenho3 = salvar_desempenho(id_treinamento3, precisao=1.2, erros_cometidos=2)
finalizar_treinamento(id_treinamento3, tempo_execucao=16.6)

# Relatório
print('--------------')
exibir_relatorio(id_treinamento)
print('--------------')
# Listagem de todos os usuários e treinamentos
listar_usuarios()
listar_treinamentos()
print('--------------')
# Listagem de histórico de treinamentos por usuário
exibir_historico_usuario(id_usuario)