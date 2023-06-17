'''O sistem de login deve permitir que novoc usuários sejam cadastrados, e que usuários existentes possam fazer o login. O sistema deve alertar caso a senha elogin não estejam corretos'''
# O sistem de login deve permitir que novoc usuários sejam cadastrados
# O sistema não deve permitir que usuários duplicados sejam cadastrados
# Permitir que usuários existentes possam fazer o login
# O sistema deve alertar caso a senha e login não estejam corretos.
'''
1. Quais são os dados de entrada necessários?
- usuário, senha
2. O que devo fazer com estes dados?
- eu devo registrar o usuário e senha que foi digitado.
3. Quais são as restrições deste problema?
- não devo perminir cadastro de usuários já existetes.
4. Qual é o resultado esperado?
- um novo usuario e senha cadastrados.
5. Qual é a sequência de pessoas necessárias para chegar ao resultado final?
- receber o usuário
- receber a senha
- verificar se o usuário já existe
- caso não exista, cadastrar aquele usuário e senha.
'''
# armazenando os usuários existentes
usuarios = ['Amanda', 'Jhon', 'Fernando']
senhas = ['123456', '789def', '12131415']

# recebendo um usuário
usuario_digitado = input('Digite seu usuário: ')
# recebendo uma senha
senha_digitada = input('Digite sua senha: ')
# caso não exista, cadastrar aquele usuário e senha
usuarios.append(usuario_digitado)
senhas.append(senha_digitada)
# confirmar que funcionou
print(usuarios)