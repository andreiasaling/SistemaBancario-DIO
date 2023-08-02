## Desafio: Criando um sistema bancário com Python

**Operação de depósito:**
Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

**Operação de saque:**
O sistema deve permitir realizar 3 saques diários com limite máximos de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

**Operação de extrato:**
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx.
*Exemplo: 1500.45 = R$ 1500.45*

**Versão 2:**
Separar as funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.
- **Saque**: a função saque deve receber os argumentos apenas por nome (keywords only). Sugestão de argumentos; saldo, valor, extrato, limite, numero_saques, limite-saques. Sugestão de retorno: saldo e extrato.
- **Depósito**: a função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo, valor, extrato. Suugestão de retorno: saldo e extrato.
- **Extrato**: a função extrato deve receber os argumentos por posição e nome (positional only e keywords only). Argumentos posicionais: saldo. Argumentos nomeados: extrato.
- **Criar usuário (cliente)**: O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla estado. Deve ser armazenado somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.
- **Criar conta corrente**: O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário.
**Dica**: para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.