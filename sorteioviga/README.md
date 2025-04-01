# 🎯 Sorteio Viga – API em Spring Boot

Projeto desenvolvido em sala de aula para praticar os fundamentos de **Java com Spring Boot**, utilizando uma arquitetura em camadas com boas práticas de desenvolvimento.

## 🚀 Tecnologias utilizadas

- Java 17
- Spring Boot
- Spring Data JPA
- Spring Validation
- Lombok
- PostgreSQL
- Swagger (OpenAPI)
- Maven

---

## 📁 Estrutura do Projeto

- `usuario`: módulo de gerenciamento de usuários
- `bilhete`: módulo de bilhetes vinculados a usuários
- `exception`: tratamento de erros com exceções personalizadas
- `config`: configuração do Swagger/OpenAPI

---

## ✅ Funcionalidades já implementadas

### 🧑‍💼 Usuário

| Método | Endpoint             | Descrição                         |
|--------|----------------------|-----------------------------------|
| `POST` | `/usuarios`          | Cadastra novo usuário             |
| `GET`  | `/usuarios/todos`    | Lista todos os usuários           |
| `GET`  | `/usuarios/{id}`     | Busca usuário por ID              |
| `PUT`  | `/usuarios/{id}`     | Atualiza dados do usuário         |
| `DELETE`| `/usuarios/{id}`    | Exclui um usuário                 |

**Validações e regras aplicadas:**
- E-mail e CPF únicos
- Validação de formato de telefone
- Data de nascimento não pode ser futura

---

### 🎟️ Bilhete

| Método | Endpoint                       | Descrição                                |
|--------|--------------------------------|------------------------------------------|
| `POST` | `/usuarios/{id}/bilhetes`      | Cria um bilhete para um usuário existente |

**Estrutura:**
- Cada bilhete tem um número (`Integer`) e está vinculado a um `Usuario` (`@ManyToOne`)

**DTO criado:**
- `BilheteRequest`: recebe apenas o número do bilhete como JSON

---

## 🧪 Exemplo de requisição para criar um usuário

```http
POST /usuarios
Content-Type: application/json

{
  "nome": "João da Silva",
  "email": "joao@email.com",
  "cpf": "12345678900",
  "telefone": "+5511988887777",
  "dataNascimento": "1995-04-20"
}
