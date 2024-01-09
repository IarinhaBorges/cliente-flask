from users import Users  # Importa a classe Users do arquivo users

# Instancia a classe Users
user = Users()

print("Digite 1 para listar os usuários: ")
print("Digite 2 para criar um usuário: ")
print("Digite 3 para editar um usuário: ")
print("Digite 4 para deletar um usuário: ")
opcao = input()

if opcao == "1":
    
    try:
        users_list = user.list()
        print(users_list)
    except ValueError as e:
        print(f"Erro ao listar usuários: {e}")

elif opcao == "2":
    usuario = {}
    usuario["username"] = input("Digite o username do usuário novo: ")
    usuario["name"] = input("Digite o nome do usuário novo: ")
    usuario["email"] = input("Digite o email do usuário: ")

    try:
        created_user = user.create(usuario)
        print(f"Usuário criado com sucesso: {created_user}")
    except ValueError as e:
        print(f"Erro ao criar usuário: {e}")

elif opcao == "3":
    user_name = input("Digite o nome do usuário que deseja editar: ")
    usuario = {}
    usuario["name"] = input("Digite o novo nome do usuário: ")
    usuario["email"] = input("Digite o novo email do usuário: ")
    usuario["username"] = input("Digite o novo usuário: ")

    try:
        user.update(user_name, usuario)
        print("Usuário atualizado com sucesso")
    except ValueError as e:
        print(f"Erro ao atualizar usuário: {e}")

elif opcao == "4":
    user_name = input("Digite o ID do usuário que deseja deletar: ")

    try:
        user.delete(user_name)
        print("Usuário deletado com sucesso")
    except ValueError as e:
        print(f"Erro ao deletar usuário: {e}")

else:
    print("Opção inválida")