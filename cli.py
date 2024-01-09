import users

user_api = users.Users()

print("digite 1 para listar usuários: ")
print("digite 2 para criar usuário: ")
print("digite 3 para editar usuário: ")
print("digite 4 para remover usuário: ")

opcao = input()

if opcao == "1":
    for usuarios in user_api.list():
        print(usuarios["name"])
        
elif opcao == "2":
    for usuarios in user_api.create():
        print(usuarios["name"])
elif opcao == "3":
    for usuarios in user_api.update():
        print(usuarios["name"])
        
elif opcao == "4":
    for usuarios in user_api.delete():
        print(usuarios["name"])