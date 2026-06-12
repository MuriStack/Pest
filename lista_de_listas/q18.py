# 18. Lista de tarefas

# Crie uma lista vazia chamada tarefas.

# Solicite ao usuário 3 tarefas e adicione cada uma delas utilizando append().

# Ao final, exiba todas as tarefas cadastradas.

tarefas = []

for i in range(3):
    tarefas.append(str(input(f"Digite a {i+1}a tarefa: ")))

print(f"Lista de tarefas: {tarefas}")
