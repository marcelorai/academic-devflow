# Documento Lista de User Stories

## Descrição 

Este documento descreve os User Stories criados a partir da Lista de Requisitos Funcionais no
[Documento de Visão](https://github.com/labens-ufrn/academic-devflow/blob/doc/issue2/docs/doc-visao.md).

## User Story US08 - Manter Usuário

|                              |                                                                                                                                                                                                                       |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Descrição**                | Um usuário tem username, password, tipo de usuário. Os usuários são criados automaticamente no cadastro de cada membro, mas o sistema deve permitir que cada usuário possa visualizar seus dados e também alterá-los. |                                                                         
| **Requisitos envolvidos**    | RF08                                                                                                                                                                                                                  |
| **Estimativa**               | 5 Horas                                                                                                                                                                                                               | 
| **Tempo Gasto (real):**      | ---                                                                                                                                                                                                                   |
| **Prioridades**              | Essencial                                                                                                                                                                                                             |
| **Tamanho Funcional**        | ---                                                                                                                                                                                               |
| **Analista**                 | Guilherme                                                                                                                                                                                                             |
| **Desenvolvedor**            | Não Definido                                                                                                                                                                                                          |
| **Revisor**                  | Não Definido                                                                                                                                                                                                          |
| **Testador**                 | Não Definido                                                                                                                                                                                                          |

## Teste de Aceitação

| **Código**  | **Descrição** |
|-------------|---------------|
| **TA08.01** | O usuário informa, na tela Registrar, todos os dados para registrar-se corretamente, ao clicar em Salvar ele é notificado com uma mensagem de sucesso. Mensagem: Cadastro realizado com sucesso, aguardando ativação do administrado |
| **TA08.02** | O usuário informa, na tela Registrar, os dados para registrar-se incorretamente, ao clicar em Salvar ele é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente. |
| **TA08.03** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é notificado com uma mensagem de erro. Mensagem: Usuário não ativado, aguardando ativação do administrador |
| **TA08.04** | O usuário informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: Login realizado com sucesso. |
| **TA08.05** | No seu perfil, ao usuário clicar alterar, deverá ser capaz de alterar a informação desejada |
| **TA08.06** | No seu perfil, os campos que estão sendo alterados deverão ser atualizados corretamente, ao clicar em Salvar ele é notificado com uma mensagem de sucesso. Mensagem: Alteração realizada com sucesso. |
| **TA08.07** | O usuário informa, durante a alteração do perfil, os dados para registrar-se incorretamente, ao clicar em Salvar ele é notificado com uma mensagem de erro. Mensagem: Atualização não realizada, o campo “xxxx” não foi informado. |
