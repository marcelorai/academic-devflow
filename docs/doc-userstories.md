# Documento Lista de User Stories

## Descrição 

Este documento descreve os User Stories criados a partir da Lista de Requisitos Funcionais no
[Documento de Visão](https://github.com/labens-ufrn/academic-devflow/blob/doc/issue2/docs/doc-visao.md).

### User Story US03 - Manter Fluxo de desenvolvimento

|           |           |
| --------- | --------- |
| **Descrição:** | Um fluxo de desenvolvimento tem código, nome, descrição, quantidade de etapas. O sistema deve permitir o cadastro de um novo fluxo de desenvolvimento para cada projeto, assim como a alteração e visualização deste. |
| **Requisitos Envolvidos** | RF03 | Manter Fluxo de desenvolvimento |
| **Prioridade**            | Essencial |
| **Estimativa**            | 8h |
| **Tempo Gasto (real):**   | --- |
| **Tamanho Funcional**     | --- |
| **Analista**              | Joan (responsável por especificar/detalhar o US) |
| **Desenvolvedor**         | Adriel (responsável por implementar e realizar testes de unidade e testes de integração) |
| **Revisor**               | Joan (responsável por avaliar a implementação e executar os testes de unidade e testes de integração) |
| **Testador**              | Guilherme (responsável por executar os Testes de Aceitação e fazer o relatório de testes) |


### **Testes de Aceitação (TA)**

| **Código**  | **Descrição** |     
| ----------- | ------------- |
| **TA03.01** | O usuário deseja cadastrar um novo fluxo de desenvolvimento, então o usuário clica no botão inserir fluxo de desenvolvimento. O usuário preenche todos os campos de modo correto e clica em Salvar/Cadastrar, recebendo uma notificação em tela de sucesso, como "Fluxo de desenvolvimento cadastrado com sucesso". |
| **TA03.02** | O usuário deseja cadastrar um novo fluxo de desenvolvimento, então o usuário clica no botão inserir fluxo de desenvolvimento. O usuário preenche algum campo ou todos os campos de modo incorreto e clica em Salvar/Cadastrar, o usuário é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente. |
| **TA03.03** | O usuário deseja alterar o fluxo de desenvolvimento, então o usuário clica no botão editar fluxo de desenvolvimento. O usuário altera os campos que deseja de modo correto e clica em Editar/Salvar, recebendo uma notificação em tela de sucesso, como "Fluxo de desenvolvimento alterado com sucesso". |                                                     
| **TA03.04** | O usuário deseja alterar o fluxo de desenvolvimento, então o usuário clica no botão editar fluxo de desenvolvimento. O usuário altera algum campo ou todos os campos de modo incorreto e clica em Editar/Salvar, o usuário é notificado com uma mensagem de erro. Mensagem: A operação falhou, o campo “xxxx” não foi informado corretamente. | 
| **TA03.05** | O usuário deseja excluir o fluxo de desenvolvimento, o usuário clica no botão excluir, caso o fluxo de desenvolvimento já possua etapas cadastradas, o sistema deve informar ao usuário e perguntar se realmente deseja excluir o fluxo de desenvolvimento, caso o usuário confirme, o sistema envia o fluxo para a lixeria e notifica ao usuário com uma mensagem de sucesso. Mensagem: "Fluxo de desenvolvimento excluído com sucesso".   Caso o usuário não confirme, ele deve ser notificado com uma mensagem informando que nenhuma mudança ocorreu. |          

