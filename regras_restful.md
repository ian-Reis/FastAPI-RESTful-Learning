# 🚀 Guia de Aprendizagem: REST e RESTful

Este documento reúne de forma simples e direta os conceitos fundamentais sobre arquitetura **REST** e sistemas **RESTful**.

---

## 📌 1. Conceito Básico

A diferença entre os dois termos é simples de entender:
* **REST (Representational State Transfer)**: É o conjunto de regras, princípios e restrições de arquitetura para a criação de sistemas na web.
* **RESTful**: É o nome dado ao sistema, aplicação ou API que consegue aplicar todas as regras do REST na prática.

### 🧩 A Analogia do Restaurante
Para entender como uma API (Interface de Programação de Aplicação) funciona, imagine que você está em um restaurante:
* **Você (O Cliente / Navegador)**: Quer fazer um pedido de comida.
* **A Cozinha (O Servidor)**: Guarda todos os ingredientes e prepara os pratos (os dados).
* **O Garçom (A API REST)**: Leva o seu pedido anotado até a cozinha e traz o prato pronto de volta para você.

---

## 🚦 2. Os 4 Pilares das Requisições HTTP

Uma API RESTful usa "verbos" do protocolo HTTP para indicar qual ação deve ser feita com um determinado dado (chamado tecnicamente de **recurso**). Pense neles como as ações básicas de um sistema de cadastro:

| Verbo HTTP | Ação Equivalente | Exemplo Prático |
| :--- | :--- | :--- |
| **`GET`** | Buscar / Ler | Ver a lista de produtos de uma loja ou os dados de um perfil. |
| **`POST`** | Criar / Inserir | Cadastrar um novo usuário ou enviar uma nova publicação. |
| **`PUT` ou `PATCH`** | Editar / Atualizar | `PUT` altera o cadastro inteiro do produto. `PATCH` altera só o preço. |
| **`DELETE`** | Excluir / Apagar | Remover um produto do estoque ou deletar uma conta. |

---

## 📦 3. O Formato dos Dados: JSON

As APIs RESTful modernas conversam utilizando um formato de texto muito leve e fácil de ler chamado **JSON** (*JavaScript Object Notation*). Ele organiza as informações usando um sistema de **Chave: Valor** dentro de chaves `{}`.

**Exemplo de um dado em JSON:**
```json
{
  "id": 125,
  "nome": "Notebook Gamer",
  "preco": 4200.00,
  "disponivel": true
}
```

---

## 📋 4. As 6 Regras de Ouro (Restrições do REST)

Para que uma API ganhe o selo de "RESTful", ela precisa respeitar seis regras de design:

1. **Cliente-Servidor (Client-Server):** O aplicativo (tela) e o banco de dados (servidor) devem ser separados. Isso permite que você mude o visual do aplicativo sem mexer nas regras de negócio do servidor.
2. **Sem Estado (Stateless):** O servidor não guarda memória de conversas passadas. Cada nova mensagem enviada pelo cliente precisa conter todas as informações necessárias para ser entendida sozinha.
3. **Cache:** A API deve dizer claramente se os dados enviados podem ser guardados na memória do computador do cliente. Isso evita buscas repetidas e deixa o sistema mais rápido.
4. **Interface Uniforme:** A estrutura das URLs (os endereços da API) e os comandos devem seguir sempre o mesmo padrão lógico (ex: `/usuarios`, `/produtos`).
5. **Sistema em Camadas (Layered System):** O cliente não precisa saber se está falando direto com o servidor final ou se a mensagem passou por computadores de segurança e distribuição no caminho.
6. **Código Sob Demanda (Opcional):** O servidor pode enviar pedaços de código de programação (como scripts) para rodar direto no computador do cliente se for necessário.

---

## 🛠️ 5. Ferramentas e Prática

Para começar a testar e entender o funcionamento na prática, utilizam-se duas ferramentas principais:

* **[Postman](https://postman.com)**: O programa ideal para simular um cliente. Com ele, você pode enviar comandos `GET`, `POST`, `PUT` e `DELETE` para qualquer API e ver a resposta na tela.
* **[JSONPlaceholder](https://typicode.com)**: Uma API pública e gratuita usada exclusivamente para testes. Você pode enviar requisições para lá e treinar seus códigos sem precisar criar um servidor do zero.
