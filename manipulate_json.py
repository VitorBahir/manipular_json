import json

filename = 'config.json'

try:
    with open(filename, 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    config = {}
    with open(filename, 'w') as file:
        json.dump(config, file)

print("Escolha a opção:")
print("1 - Ler configuração")
print("2 - Escrever configuração")
opcao = input("Opção: ")

if opcao == '1':
    if not config:
        print("O arquivo não contém informações.")
    else:
        print("Conteúdo do arquivo:")
        print(json.dumps(config, indent=2))
elif opcao == '2':
    config['server_name'] = input("1 - Informe o nome do servidor: ")
    config['server_ip'] = input("2 - Informe o IP do servidor: ")
    config['server_password'] = input("3 - Informe a senha do servidor: ")

    with open(filename, 'w') as file:
        json.dump(config, file, indent=2)

    print("Informações salvas com sucesso no arquivo.")
    print("Conteúdo do arquivo:")
    print(json.dumps(config, indent=2))
else:
    print("Opção inválida.")
