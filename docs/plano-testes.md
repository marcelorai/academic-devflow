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

### 3 Estratégias e ferramentas 

<p align="justify">
  A Estratégia de Teste apresenta a abordagem recomendada para o teste dos aplicativos de software. A seção anterior dos Requisitos de Teste descrevia o que será testado; esta descreve como será testado.
</p>

<p align="justify">
  As principais considerações para a estratégia de teste são as técnicas a serem utilizadas e o critério para saber quando o teste está concluído.
</p>

<p align="justify">
  Além das considerações fornecidas para cada teste a seguir, o teste deve ser executado apenas utilizando bancos de dados conhecidos e controlados, em ambientes protegidos.
</p>

<p align="justify">
  A estratégia de teste a seguir é genérica por natureza e foi desenvolvida para ser aplicada aos requisitos listados na seção 4 deste documento.
</p>

#### 3.1 Tipos de teste

3.1.1 Testes de unidade 

<p align="justify">
Os testes unitários tem por objetivo verificar cada unidade que compõe o software, isoladamente, para determinar se cada uma delas realiza o que foi especificado. A unidade é definida como um componente de software que não pode ser dividido. Nesta fase as categorias de testes aplicáveis são: teste em estruturas internas, teste de funcionalidade, teste de segurança
</p>

- Objetivo do teste: Assegurar que todas as unidades de código possuam o mínimo de verificação.
- Técnica: Implementar um ou mais testes unitários para cada nova funcionalidade utilizando as tecnologias disponíveis para a linguagem de programação escolhida.
- Critérios de Conclusão: Os testes devem passar durante a execução.

3.1.2 Testes de integração

<p align="justify">
  Os testes de integração têm por objetivo encontrar falhas de integração entre as unidades, e não mais em testar as funcionalidades da mesma. Nesta fase as categorias de testes aplicáveis são: testes de interface, testes de dependências entre os componentes.
</p>

- Objetivo do teste: Assegurar que a comunicação entre os módulos do sistema ocorra de forma "correta" e sem a ocorrência de falhas.
- Técnica: Implementar um ou mais testes de integração para cada ação desempenhada pelo sistema e que envolva a conexão entre módulos diferentes.
- Critérios de Conclusão: Os testes devem passar durante a execução.

3.1.3 Testes de sistema 

<p align="justify">
 Os testes de sistema consistem na realização de vários tipos de teste que visam determinar se os componentes de um sistema computacional (envolvendo outros componentes de software e/ou de hardware) se integram bem e realizam as funcionalidades que lhes foram especificadas. Nesta fase as categorias de testes aplicáveis são: testes funcionais e testes não funcionais (performance, instalação, recuperação e carga);
</p>

- Objetivo do teste: Assegurar que o sistema funcione sem a ocorrência de falhas em um contexto real de utilização pelo usuário final.
- Técnica: Submeter o sistema a uma série de situações possíveis de modo a identificar a ocorrência de falhas.
- Critérios de Conclusão: Os testes devem passar durante a execução. 

3.1.4 Testes de desempenho 

<p align="justify">
O teste de desempenho mede tempos de resposta, taxas de transação e outros requisitos sensíveis ao tempo. A meta do teste de Desempenho é verificar e validar se os requisitos de desempenho foram alcançados. O teste de desempenho normalmente é executado várias vezes, cada uma utilizando uma "carga de segundo plano" diferente no sistema. O teste inicial deve ser executado com uma carga "nominal", semelhante à carga normal observada (ou prevista) no sistema de destino. Um segundo teste de desempenho é executado utilizando uma carga de pico.
</p>

- Objetivo do teste: Validar o Tempo de Resposta do Sistema para funções de negócios ou transações designadas sob duas condições: volume normal previsto e volume de pior caso previsto.
- Técnica: Modificar arquivos de dados (a fim de aumentar o número de transações) ou modificar scripts a fim de aumentar o número de iterações ocorrido em cada transação. 
- Critérios de Conclusão: Conclusão com êxito dos scripts de teste sem nenhum defeito e na alocação de tempo esperada.

3.1.5 Testes de interface com o usuário 

<p align="justify">
O teste da Interface com o Usuário verifica a interação de um usuário com o software. A meta do Teste de UI é assegurar que a Interface com o Usuário forneça ao usuário o acesso e a navegação adequados por meio das funções dos aplicativos. Além disso, o Teste de UI assegura que os objetos contidos na UI funcionem conforme esperado e estejam em conformidade com padrões corporativos ou do segmento de mercado.
</p>

- Objetivo do teste:
  - A navegação pelo aplicativo reflete os requisitos e funções de negócios, incluindo a navegação janela a janela, campo a campo e o uso de métodos de acesso (teclas de tabulação, movimentos do mouse e teclas aceleradoras)
  - Objetos e características da janela, tais como menus, tamanho, posição, estado e foco estão em conformidade com os padrões.
- Técnica: Criar / modificar testes para cada janela a fim de verificar a navegação adequada e os estados de objeto para cada janela e objeto do aplicativo.
- Critérios de Conclusão: Verificação com êxito de cada janela permanecer consistente com a versão de benchmark ou dentro do padrão aceitável.

### 4 Equipe e infra-estrutura 

### 5 Cronograma de atividades

### 6 Documentação complementar 

