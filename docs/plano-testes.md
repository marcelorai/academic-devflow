# Plano de Testes 

### 1 Introdução 

#### 1.1 Objetivos 

<p align="justify"> 
Este projeto se trata do desenvolvimento de uma sistema para facilitar o acompanhamento do andamento de Projetos de Software dos discentes nas turmas Engenharia de Software do curso de Bacharelado em Sistemas de Informação do CERES/UFRN. 
</p>

<p align="justify"> 
Este documento descreve o plano de testes para as futuras funcionalidades deste sistema. Dessa forma, o presente plano de testes aborda os seguintes objetivos: 
</p>

- Identificar informações existentes do projeto e o software que deve ser testado.
- Listar os requisitos de teste recomendados (nível alto).
- Recomendar e descrever as estratégias de teste a serem empregadas.
- Identificar os recursos requeridos e fornecer uma estimativa dos esforços de teste.
- Listar os elementos de produto de trabalho das tarefas de teste.

#### 1.2 Escopo

<p align="justify">
Este Plano de Testes descreve os testes de unidade, integração e sistema que serão conduzidos durante o desenvolvimento do projeto. Este projeto será desenvolvido utilizando a filosofia do TDD - Test Driven Developmente ou Desenvolvimento Dirigido por testes, onde os testes são desenvolvidos antes da concepção e implementação das funcionalidades.
</p>

<p align="justify">
A aplicação das técnicas de TDD trazem diversos benefícios para o desenvolvimento do software, um dos benefícios é que, como você vai saber o que o código precisa fazer antecipadamente, você acaba evitando de escrever código demasiadamente complexo ou que não siga os pré-requisitos de negócio. 
</p>

<p align="justify">
Além disso, se você for deixar para testar as funcionalidades do seu código depois, você pode acabar não realizando os testes como deveria. Isso aumenta o risco de, por exemplo, realizarmos alterações no código por conta de testes que não passaram, aumentando substancialmente a possibilidade de introduzirmos problemas com estas alterações. Escrevendo os testes na etapa inicial, pode até parecer que acabamos tendo uma tarefa a mais a ser desempenhada; porém, no fim, seu software terá menos possibilidade de falhas, além de você acabar desenvolvendo código com mais qualidade.
</p>

<p align="justify">
Dessa forma, se busca que os testes cubram todas as funcionalides e módulos do sistema que ainda serão desenvolvidos, com o intuito de produzir um código com uma cobertura de testes alta e garantindo segurança, confiabilidade e qualidade para o sistema. 
</p>

### 2 Requisitos a seres testados 

<p align="justify">
A lista a seguir identifica os itens que foram identificados como alvos do teste. Essa lista representa o que será testado.
</p>

#### 2.1 Testes de unidade 

- Verificar função de conexão com o banco de dados;
- Verificar as funções de query que se comunicam com o banco de dados;
- Verificar o status da aplicação criada; 
- Verificar as funções que se comunicam com a API;
- Verificar as funções de validação dos campos informados e passados por parâmetros;
- Verificar as funções da camada do controlador;
- Verificar as funções da camada de views;
- Verificar as funções da camada de modelos;
- Verificar as funções do módulo de rotas;
- Verificar as funções de autenticação e autorização;

#### 2.2 Testes de integração 

- Verificar a ação de realizar um INSERT no banco de dados;
- Verificar a ação de realizar um SELECT no banco de dados;
- Verificar a ação de realizar um UPDATE no banco de dados;
- Verificar a ação de realizar um DELETE no banco de dados;
- Verificar a ação de realizar um LOGIN no sistema; 
- Verificar a depedência dos módulos do sistema (Testar módulos do sistema que se comunicam com outros módulos);
- Verificar a integração do sistema com sistemas externos;
- Verificar quando se apaga uma tupla de uma tabela que representa uma Foreign Key em outra tabela;
- Verificar quando se realiza uma TRANSACTION que envolve mais de uma tabela;

#### 2.3 Testes de sistema 

<p align="justify">
Os Testes de Sistema estão no escopo da técnica de teste de caixa-preta, e dessa forma não requer conhecimento da estrutura (lógica) interna do sistema. Dessa forma, é um teste mais limitado em relação aos testes de unidade e de integração, se pois se preocupa somente com aspectos gerais do sistema.
</p>

#### 2.4 Teste de Desempenho

- Verificar o tempo de resposta para acesso ao sistema por um usuário arbitrário;
- Verificar o tempo de resposta para puxar os dados da integração com o GitHub;
- Verificar o tempo de resposta para criação dos relatórios de métrica;
- Verificar o tempo de resposta de cadastro de uma nova instância no sistema;
- Verificar o tempo de envio até o recebimento de uma notificação enviada pelo sistema;

#### 2.5 Teste de Interface com o Usuário

- Verificar a facilidade de navegação utilizando um conjunto de amostras de telas;
- Verificar se as telas de amostra estão em conformidade com os padrões da GUI;
- Verificar se a interface é acessível para pessoas com necessidades especias;
- Verificar se a interface se mantém em diferentes dispositivos com tamanhos de tela diferentes;

#### Teste de Segurança e Controle de Acesso

- Verificar o Logon a partir de um PC local;
- Verificar o Logon a partir de um PC remoto;
- Verificar a segurança de Logon por meio de mecanismos de nome de usuário e senha;

### 3 Estratégias e ferramentas 

### 4 Equipe e infra-estrutura 

### 5 Cronograma de atividades

### 6 Documentação complementar 

