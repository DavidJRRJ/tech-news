# Tech News

## Descrição do Projeto

O projeto **Tech News** foi desenvolvido em Python com o objetivo de fornecer consultas em notícias sobre tecnologia, obtidas através da raspagem do blog da Trybe. Este projeto visa aprimorar habilidades específicas, como o uso do terminal interativo do Python, escrita de módulos personalizados, aplicação de técnicas de raspagem de dados, extração de conteúdo HTML e armazenamento dos dados em um banco de dados.

## Habilidades Trabalhadas

1. **Utilização do Terminal Interativo do Python:**
   - O projeto utiliza o terminal interativo do Python para interações eficientes e execução de scripts.

2. **Escrita de Módulos Personalizados:**
   - Vários módulos foram escritos para modularizar o código, promovendo uma organização eficaz e reutilização de código.

3. **Raspagem de Dados:**
   - Técnicas de raspagem de dados foram aplicadas para extrair informações relevantes do blog da Trybe.

4. **Extração de Conteúdo HTML:**
   - O projeto faz uso de técnicas avançadas para extrair dados específicos do conteúdo HTML das páginas do blog.

5. **Armazenamento em Banco de Dados:**
   - Os dados obtidos são armazenados em um banco de dados para facilitar o acesso e a consulta posterior.

## Como Utilizar

### Pré-requisitos:

- Certifique-se de ter o Docker e o Docker Compose instalados em seu ambiente.

### Execução:

1. **Construir a imagem:**
   - Navegue até o diretório do projeto no terminal.
   - Execute o seguinte comando para construir a imagem Docker:

     ```bash
     docker-compose build
     ```

2. **Executar o container:**
   - Após a construção bem-sucedida, execute o seguinte comando para iniciar o container:

     ```bash
     docker-compose up
     ```

   - O projeto estará acessível no endereço http://localhost:PORTA, onde "PORTA" é a porta especificada no arquivo `docker-compose.yml`.

3. **Parar o container:**
   - Para parar o container, utilize o comando:

     ```bash
     docker-compose down
     ```

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

- `src/`: Contém os módulos e scripts principais.
- `data/`: Armazena o banco de dados ou arquivos de dados gerados.
- `requirements.txt`: Lista as dependências necessárias.

---

**Tech News** é um projeto desenvolvido para aprimorar habilidades em Python e raspagem de dados. Esperamos que seja útil para manter-se atualizado sobre as últimas notícias de tecnologia!
