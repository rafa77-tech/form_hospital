# Escopo do Projeto #

## 1. Objetivo Geral ##

Desenvolver um webapp simples em Python, utilizando um framework minimalista (como Flask ou FastAPI), para gerenciar um formulário de informações hospitalares. O aplicativo irá:

- Exibir um campo de seleção de hospital a partir de uma lista carregada via CSV.
- Ao selecionar um hospital, exibir um formulário com campos já preenchidos (dados oriundos do CSV) e campos vazios que o usuário precisará completar.
- Não permitir a edição dos campos já preenchidos.
- Ao finalizar o preenchimento de todos os campos, o hospital selecionado será removido da lista de hospitais pendentes.

## 2. Funcionalidades Principais ##

- Carregamento de Dados a partir de CSV:

- Ler um arquivo CSV contendo informações parciais de hospitais.
- Armazenar esses dados em memória ou em uma estrutura de dados simples para rápido acesso (por exemplo, um dicionário em Python).

- Seleção do Hospital:

- Exibir um dropdown (select) com todos os hospitais disponíveis no CSV.
- Ao escolher um hospital, o formulário deve ser atualizado.

- Formulário Dinâmico:

Ao selecionar um hospital, o front deve exibir um conjunto de campos:
Campos já preenchidos (vindos do CSV) e não editáveis (read-only).
- Campos em branco (não presentes no CSV) que devem ser preenchidos pelo usuário.
- O formulário será simples, composto por campos de texto, possíveis selects ou textareas, conforme a necessidade.

- Validação do Formulário:

- Todos os campos obrigatórios devem ser preenchidos.
- Exibir mensagens de erro ou destaque em vermelho caso falte algo antes do envio.

- Envio do Formulário:

- Ao enviar, o backend valida se todos os campos obrigatórios estão preenchidos.
- Uma vez completo, remover o hospital selecionado da lista de pendências (ou seja, atualizar a lista em memória e opcionalmente gravar um novo CSV ou marcar no CSV original que este hospital já foi finalizado).

- Atualização da Lista de Hospitais:

- Após o envio bem-sucedido dos dados, o dropdown inicial não deve mais conter o hospital que já teve o formulário completado.

## 3. Estrutura dos Dados no CSV ##

O CSV conterá colunas como, por exemplo:

hospital_id (identificador único do hospital)
NO_FANTASIA	NO_LOGRADOURO = Nome do hospital
EMPRESA_RESP_PSA = Empresa responsável pelo pronto-socorro adulto
EMPRESA_RESP_PSI = Empresa responsável pelo pronto-socorro infantil
EMPRESA_RESP_UTIA = Empresa responsável pela UTI adulto
EMPRESA_RESP_UTIPED = Empresa responsável pela UTI pediatrica
EMPRESA_RESP_ANESTESIA = Empresa responsável pelo serviço de anestesiologia
EMPRESA_RESP_UIA = Empresa responsável pela unidade de internação adulto
EMPRESA_RESP_UIP = Empresa responsável pela unidade de internação infantil
NO_BAIRRO = Nome do bairro
NU_ENDERECO = Endereço completo
CO_CEP = CEP
NU_TELEFONE = Telefone	

- Alguns campos podem já estar preenchidos no CSV (por exemplo, nome_hospital, campo1), enquanto outros podem estar vazios.

- O CSV pode ser estruturado de forma que campos obrigatórios sem informação venham como strings vazias ("").

## 4. Fluxo do Usuário ##

- O usuário acessa a página principal.
- Na página inicial, vê um dropdown com a lista de hospitais pendentes (ele pode digitar o nome do hospital para selecionar mais facilmente)
- O usuário seleciona um hospital.
- O frontend faz uma requisição (via AJAX ou redirecionamento) para o backend, obtendo os dados do hospital.
- O frontend pré-preenche os campos existentes e deixa em branco os campos não preenchidos.
- O usuário completa os campos em branco.
- O usuário clica em "Enviar".
- O backend valida os dados e, se tudo certo, remove o hospital da lista de pendências.
- O frontend redireciona o usuário de volta para a página inicial, agora com o hospital removido do dropdown (apenas do dropdown, não do CSV).

## 5. Tecnologias Backend ##

- Linguagem: Python (3.10+ recomendado)
- Framework Web: Flask
- Leitura de CSV: Biblioteca pandas do Python
- Armazenamento de Dados: Inicialmente, apenas em memória (listas/dicionários) carregados do CSV. Ao finalizar um hospital, atualizar o CSV

## 6. Tecnologias Frontend ##

- HTML/CSS/JS: Estrutura básica.
- Bootstrap:
Uso de componentes prontos para forms, dropdown, botões, alertas de validação.

- Integração:

- Possivelmente uma pequena requisição AJAX quando um hospital for selecionado, para retornar os dados via JSON.
- Ou, alternativamente, recarregar a página enviando o hospital_id selecionado para o backend e renderizando o template já com os dados preenchidos (uma abordagem mais simples, porém menos dinâmica).

## 7. Layout das Páginas ##

- Página Inicial (/):

- Título do projeto
- Dropdown com lista de hospitais pendentes
- Botão "Carregar Formulário"

- Página do Formulário (/formulario/<hospital_id>):

- Título com nome do hospital
- Campos de formulário (input text, selects, etc.)
- Campos já preenchidos aparecem como readonly
- Campos vazios aparecem como input text editáveis
- Botão "Enviar"

- Página de Confirmação (após envio):

- Mensagem de sucesso
- Link de volta para a página inicial

## 8. Lógica do Backend Passo a Passo ##

- Startup do servidor:

- Ler o CSV.
- Gerar uma estrutura de dados (por exemplo, um dicionário com hospital_id como chave e outro dicionário com os campos como valor).
- Filtrar apenas hospitais pendentes (se houver a necessidade de status).

- Rota Principal (GET /):

- Renderizar template da página inicial.
- Passar a lista dos hospitais pendentes para o template (nome e hospital_id).

- Rota do Formulário (GET /formulario/<hospital_id>):

- Obter do dicionário em memória os dados do hospital.
- Identificar quais campos estão preenchidos e quais não.
- Renderizar o template do formulário, marcando campos preenchidos como readonly e campos vazios como editáveis.

- Rota de Submissão do Formulário (POST /formulario/<hospital_id>):

- Receber os dados do formulário.

- Validar se todos os campos obrigatórios estão presentes agora.
- Se válido:

- Atualizar a memória (remover hospital da lista pendente).
- Opcional: atualizar o CSV marcando o hospital como completado ou removendo-o.
- Redirecionar para página de confirmação/sucesso.
- Se inválido:

- Retornar ao formulário com mensagens de erro.

## 9. Testes e Validação ##

- Testes Manuais:

- Carregar a página inicial, verificar a lista de hospitais.
- Selecionar um hospital com alguns campos já preenchidos.
- Preencher os campos faltantes e enviar.
- Verificar se o hospital saiu da lista na página inicial.

- Testes Automatizados (Opcional):

- Testar a rota de leitura do CSV.
- Testar a geração da lista de hospitais pendentes.
- Testar a submissão correta e incorreta do formulário.
