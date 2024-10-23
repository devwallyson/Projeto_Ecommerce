
# W Store  E-commerce

**W Store** é um projeto de e-commerce desenvolvido durante a disciplina de Orientação a Objetos, utilizando os princípios fundamentais da orientação a objetos (Encapsulamento, Herança e Polimorfismo) com **Python** e **Django** como ferramentas de desenvolvimento. Além disso, o projeto faz uso de funcionalidades do **Bootstrap** para a criação de uma interface responsiva e amigável.

## Descrição do Projeto

A **W Store** é uma loja virtual onde os usuários podem visualizar produtos, adicionar itens ao carrinho de compras, realizar o checkout e gerenciar suas contas por meio de um sistema de login e registro. O foco do projeto foi aplicar os três pilares da orientação a objetos, garantindo um código organizado, reutilizável e facilmente escalável.

### Pilares da Orientação a Objetos Aplicados

1. **Encapsulamento**;

2. **Herança**;
   
3. **Polimorfismo**.

## Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento da aplicação.
- **Django**: Framework utilizado para o back-end, que facilitou a construção da aplicação web, incluindo sistema de autenticação de usuários, gerenciamento de modelos e templates.
- **Bootstrap**: Framework CSS utilizado para criar uma interface moderna e responsiva. Elementos como navegação, botões e layout foram estilizados usando componentes do Bootstrap.

## Funcionalidades Implementadas

- Listagem de produtos
- Adição de produtos ao carrinho de compras
- Gerenciamento de carrinho (visualização e remoção de itens)
- Sistema de registro e login de usuários
- Checkout e simulação de métodos de pagamento
- Interface responsiva com design moderno, utilizando Bootstrap

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/wstore.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd wstore
   ```

3. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute as migrações:
   ```bash
   python manage.py migrate
   ```

6. Inicie o servidor local:
   ```bash
   python manage.py runserver
   ```

7. Acesse o projeto no navegador através do endereço: `http://127.0.0.1:8000`




