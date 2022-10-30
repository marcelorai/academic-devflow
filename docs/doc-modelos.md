# Modelo Conceitual e Modelo de Dados

## Descrição

Este documento oferece uma representação visual dos dados da plataforma Academic
Dev Flow. A partir dele é possível entender como se dá a organização dos dados
presentes na plataforma, as entidades que fazem parte do projeto e seu
funcionamento geral.

### Histórico de revisões

| Data       | Versão | Descrição            | Autor                   |
| ---------- | ------ | -------------------- | ----------------------- |
| 02/10/2022 | 1.0    | Documento inicial    | Adriel Faria dos Santos |
| 04/10/2022 | 1.1    | Correção dos modelos | Adriel Faria dos Santos |

## Modelo conceitual

![Modelo conceitual do projeto](./images/modelo-conceitual.png)

### Descrição das entidades

#### **Artefato**

Representa um item qualquer que tenha sido prduzido durante o desenvolvimento de
um _projeto_

#### **Atividade**

Representa uma atividade realizada durante o desenvolvimento de um _projeto_

#### **Coordenador**

_Usuário_ que coordena _membros_, _projetos_ e _equipes_

#### **Equipe**

Conjunto de _membros_ que participa de um _projeto_

#### **Etapa**

Representa uma etapa de um _fluxo_ de desenvolvimento. Seu atributo "NUMERO"
é o responsável por ditar a sua posição no fluxo, ou seja, as etapas de um fluxo
são ordenadas com base nesse atributo, de forma que etapas com o mesmo número
ocorrem simultaneamente

#### **Fluxo**

Representa o fluxo de desenvolvimento escolhido para um determinado _projeto_

#### **Iteração**

Representa uma iteração do processo de desenvolvimento de um _projeto_

#### **Membro**

_Usuário_ que participa no desenvolvimento de _projetos_

#### **Pontuacao**

Representa um acrescimo ou decréscimo de pontuação pela entrega, não entrega ou
atraso de uma _atividade_ ou _artefato_

#### **Projeto**

Representa um projeto que tem deu desenvolvimento acompanhado na plataforma

#### **Release**

Representação de uma release do processo de desenvolvimento de um _projeto_

#### **Usuário**

Contém as informações necessárias para login e realização de ações no sistema

## Modelo de dados

![Modelo de dados do projeto](./images/modelo-dados.png)

## Dicionário de dados

| Entidade    | Atributo   | Limites e restrições                                             |
| ----------- | ---------- | ---------------------------------------------------------------- |
| ARTEFATO    | DESCRICAO  | Campo opcional                                                   |
| ATIVIDADE   | DESCRICAO  | Campo opcional                                                   |
| COORDENADOR | TELEFONE   | Deve considerar DDD                                              |
| ETAPA       | ATIVA      | TPor padrão é False                                              |
| ETAPA       | DESCRICAO  | Campo opcional                                                   |
| ETAPA       | GAMEFICADA | Por padrão é True                                                |
| ETAPA       | NUMERO     | Não pode assumir valores negativos                               |
| FLUXO       | DESCRICAO  | Campo opcional                                                   |
| ITERACAO    | DESCRICAO  | Campo opcional                                                   |
| MEMBRO      | TELEFONE   | Deve considerar DDD                                              |
| PONTUACAO   | COMENTARIO | Campo opcional                                                   |
| PONTUACAO   | PONTOS     | Não pode assumir valores negativos                               |
| PONTUACAO   | PENALIDADE | Por padrão é False                                               |
| PROJETO     | DESCRICAO  | Campo opcional                                                   |
| RELEASE     | DESCRICAO  | Campo opcional                                                   |
| USUARIO     | TIPO       | Pode assumir valores **Administrador**, **Aluno**, **Professor** |

## Referências

[Modelo BSI - Doc 002 - Modelo Conceitual e Modelo de Dados](https://docs.google.com/document/d/1cxzXiWN149Nq5htoB88HZVE0GmWTnHemAwHrNYXif98/edit)
