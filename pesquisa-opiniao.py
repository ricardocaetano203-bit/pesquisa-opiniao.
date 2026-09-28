# Programa de Pesquisa de Opinião - TudoWeb
# Agenda 08 - Desenvolvimento de Sistemas I

qtd_excelente = 0
qtd_ruim = 0
total_entrevistados = 50

for i in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {i} ---")
    
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    print("Opções de opinião:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    
    # Validação com while para evitar dados incorretos
    opiniao = int(input("Digite o código da opinião (1, 2 ou 3): "))
    while opiniao != 1 and opiniao != 2 and opiniao != 3:
        print("Opção inválida! Digite novamente.")
        opiniao = int(input("Digite o código da opinião (1, 2 ou 3): "))
    
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1

print("\n--- RESULTADO FINAL DA PESQUISA ---")
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
