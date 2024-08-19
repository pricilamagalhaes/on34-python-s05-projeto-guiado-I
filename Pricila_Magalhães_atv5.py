from dataset_alunas import dataset
lista_alunas = dataset

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1: incluir_nova_aluna()
        elif cod_opcao == 2: consultar_lista_alunas()
        elif cod_opcao == 3: consultar_faltas_aluna()
        elif cod_opcao == 4: consultar_notas_aluna()
        elif cod_opcao == 5: consultar_status_aprovacao()
        elif cod_opcao == 6: print("Encerrando o programa..."); break

def obter_opcao():
    codigo_opcao = 0

    while codigo_opcao not in [1, 2, 3, 4, 5]:
        try:
            codigo_opcao = int(input("\nEscolha uma opção:\n"
                                    "1 - Incluir uma nova aluna\n"
                                    "2 - Consultar lista de alunas\n"
                                    "3 - Consultar faltas da aluna\n"
                                    "4 - Consultar notas da aluna\n"
                                    "5 - Consultar status de aprovação\n"
                                    "6 - Sair do sistema\n"
                                    "Opção: "))
                
            if codigo_opcao not in [1, 2, 3, 4, 5]:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 5).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao
    
def incluir_nova_aluna():
#O sistema deve permitir a inclusão de uma nova aluna com os seguintes dados: nome, sobrenome, turma, notas (uma lista de números), presença (uma lista de booleanos indicando 
# a presença em cada aula) e participação (um número representando o nota de participação da aluna).
#OK -Após a inclusão, o sistema deve exibir uma confirmação de que a aluna foi adicionada com sucesso.
#Caso algum dado não seja válido (por exemplo, notas fora do intervalo permitido), o sistema deve informar o usuário sobre o erro e não adicionar a aluna. (opcional)
    print("Insira os seguintes dados: ")
    nome = input("Nome da aluna: ") #Recebo nome da aluna
    sobrenome = input("Sobrenome da aluna: ") #Recebo nome da aluna
    turma = input("Turma da aluna: ") #Recebo nome a turma
    notas = obter_notas() #Chamo a função de pegar as notas para alimentar minha lista "notas"
    presenca = obter_presenca() #Recebo a lista de presença com 'True' ou 'False'
    nota_participacao = float(input("Participação da aluna: ")) #Recebo nota de participação
    salvar_dados(nome,sobrenome,turma,notas,presenca,nota_participacao)
    print(f"Registro salvo com sucesso: {nome}")

    
def consultar_lista_alunas(): 
#O sistema deve exibir a lista de todas as alunas cadastradas, mostrando apenas os nomes.
#A lista deve estar formatada de forma legível para o usuário.
#Caso não haja alunas cadastradas, o sistema deve informar que não há registros. (opcional)

    if len(lista_alunas) > 0: # Verifica se há alunas cadastradas
        print("Lista de alunas cadastradas:")# Mostra a lista de alunas formatada
        for aluna in lista_alunas:
            print(f"{aluna[0]} {aluna[1]}")
    else: # Caso não haja alunas cadastradas
        print("Não há alunas cadastradas.")
    
def consultar_faltas_aluna(): 
#O sistema deve permitir ao usuário buscar as faltas de uma aluna específica.
#O usuário deve informar o nome completo da aluna para realizar a consulta.
#Após a consulta, o sistema deve exibir a quantidade de faltas da aluna
    if len(lista_alunas) > 0: # Verifica se há alunas cadastradas
        nome = input("Nome da aluna que deseja consultar: ") #Recebo nome da aluna
        sobrenome = input("Sobrenome da aluna que deseja consultar: ") #Recebo nome da aluna
        pesquisa_aluno = (nome, sobrenome)    
        if pesquisa_aluno in lista_alunas:
            presenca = mapping(lista_alunas[pesquisa_aluno]["Presença"]) 
            print(f"Nome: {nome} {sobrenome}, Presença: {presenca}")
        else: # Caso não haja alunas cadastradas
            print("Não há alunas cadastradas.")

    
def consultar_notas_aluna(): 
#O sistema deve permitir ao usuário consultar as notas de uma aluna específica.
#O usuário deve informar o nome completo da aluna para realizar a consulta.
#Após a consulta, o sistema deve exibir as notas obtidas pela aluna em cada avaliação.
    if len(lista_alunas) > 0: # Verifica se há alunas cadastradas
        nome = input("Nome da aluna que deseja consultar: ") #Recebo nome da aluna
        sobrenome = input("Sobrenome da aluna que deseja consultar: ") #Recebo nome da aluna
        pesquisa_aluno = (nome, sobrenome)    
        if pesquisa_aluno in lista_alunas:
            notas = lista_alunas[pesquisa_aluno]["Notas"]
            print(f"Nome: {nome} {sobrenome}, Notas: {notas}")
        else: # Caso não haja alunas cadastradas
            print("Não há alunas cadastradas.")

def consultar_status_aprovacao():
    #O sistema deve calcular o status de aprovação de uma aluna com base nas suas notas.
#O usuário deve informar o nome completo da aluna para realizar a consulta.
#O sistema deve calcular a média simples das notas da aluna
#Para o cálculo da aprovação, será considerado: nota de corte, a aluna deve ter pelo menos 80% de presença e nota de participação acima de 6
#Após o cálculo, o sistema deve exibir o status de aprovação da aluna (aprovada ou reprovada) e sua média final
#A nota de corte na escola é 6.
    if len(lista_alunas) > 0: # Verifica se há alunas cadastradas
        nome = input("Nome da aluna que deseja consultar: ") #Recebo nome da aluna
        sobrenome = input("Sobrenome da aluna que deseja consultar: ") #Recebo nome da aluna
        
        pesquisa_aluno = (nome, sobrenome)    
        if pesquisa_aluno in lista_alunas:
            notas = lista_alunas[pesquisa_aluno]["Notas"]
            presenca = lista_alunas[pesquisa_aluno]["Presença"]
            participacao = lista_alunas[pesquisa_aluno]["Participação"]
            print(f"Nome: {nome} {sobrenome}, Notas: {notas} - Presença: {mapping(presenca)} - Participação: {participacao}" )
            
            media_nota = sum(notas)/len(notas) # media simples das notas
            media_final = round((media_nota + participacao) /2,2)
            media_presenca = presenca.count(True)/len(presenca) * 100
            
            if media_presenca >= 80 and media_final > 6:
                print('Aluno Aprovado')
                #print(f"Média Nota: {media_nota}")
                print(f"Média Presença: {media_presenca}")
                print(f"Média Final: {media_final}")
            else:
                print('Aluno Reprovado') 
                #print(f"Média Nota: {media_nota}")
                print(f"Média Presença: {media_presenca}")
                print(f"Média Final: {media_final}")
        else: # Caso não haja alunas cadastradas
            print("Não há alunas cadastradas.")    

def obter_notas(): 
    quantidade_notas = input("Quantidade de notas: ") 
    notas = [] 
    
    for contador in range(int(quantidade_notas)): 
        while True: 
            entrada = input(f"Insira a nota #{contador + 1} do total de {quantidade_notas} :") 
            try: 
                nota = float(entrada) 
                notas.append(nota) 
                break 
            except ValueError: 
                print("Entrada inválida. Por favor, insira um número válido.")

    return notas

def obter_presenca():
    quantidade_aulas = 5 #quantidade_aulas = input("Quantidade de aulas: ") #Recebo a quantidade de aulas
    aulas = [] #Criei uma lista para receber a presença
    for contador in range(int(quantidade_aulas)):
        while True: #Usamos quando não sabemos a quantidade de repetições
            entrada = input(f"Insira a presença da aula #{contador + 1}: do total de {quantidade_aulas}.Letras minusculas e sem acento sim/nao: ")
            try: #Faço uma tentativa de adicionar uma nota na lista
                if entrada == 'sim':
                    aulas.append(True)
                    break
                elif entrada == "nao":
                    aulas.append(False)
                    break
                else:
                    raise ValueError("Entrada inválida. Por favor, insira 'sim' ou 'nao'.")
            except ValueError as e:
                print(f"Error: {e}")
    return aulas

def mapping(lista_booleanos):
    # Define o mapeamento
    mapeamento = {
        False: "Não presente",
        True: "Presente"
    }
    # Aplica o mapeamento usando list comprehension
    lista = [mapeamento[valor] for valor in lista_booleanos]
    
    return lista


def salvar_dados(nome, sobrenome, turma, notas,presenca, nota_participacao): 
    chave = (nome,sobrenome)
    lista_alunas[chave] = {
        "Turma": turma,
        "Notas": notas,
        "Presença": presenca, 
        "Participação": nota_participacao
    }
    
main()