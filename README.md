<h1 align="center">Projeto opportunity API | Django FULL STACK </h1>

## 🖥️ Descrição do projeto / Project description

O sistema giram em torno de uma necessidade vista por mim (Kawhan) em ajudar os professores que disponibilizam oportunidades de bolsas, emprego, mestrado e etc, voltado para os alunos do Campus IV. Então, vendo essa oportunidade, criei uma API para gerenciar cadastro de informações de vagas e permitir que os alunos se inscrevam em uma determinada vaga, além de disponibilizar end-poins para o contato direto de várias informações. Planejo também deixar o projeto open source caso algum aluno deseje criar algo que consuma a api ou melhorar cada vez mais a ideia inicial, criando oportunidade de contrinbuir com a oportunidade open source e também incentivando os alunos para que utilizem do conhecimento que tem para gerar soluções viaveis para faculdade em que estudam.

The system revolves around a need seen by me (Kawhan) in helping professors who provide opportunities for scholarships, jobs, master's degrees, etc., aimed at Campus IV students. So, seeing this opportunity, I created an API to manage vacancy information registration and allow students to enroll in a given vacancy, in addition to providing end-points for direct contact of various information. I also plan to leave the project open source in case any student wants to create something that consumes the api or increasingly improve the initial idea, creating an opportunity to contribute to the open source opportunity and also encouraging students to use the knowledge they have to generate solutions viable for the college where they study.

---

## 📌 Funcionalidades
- Verificação de cadastro por e-mail
- Cadastro de vagas do CAMPUS IV


---
## 🚢 Using Docker
```
docker-compose up --build
docker-compose up 
```
## 🛠️ Usabilidade do código do sistema / system code usability

- Criação do ambiente virtual:
```
python -m venv 
venv\Scripts\activate                            //Ativar ambiente virtual (cmd)
python -m pip install --upgrade pip             //Atualizar pip
pip install -r requirements.txt                //Instalar dependências
python manage.py migrate                      //Sincronizar database
python manage.py createsuperuser             //Criar um super usuário
python manage.py runserver                  //Iniciar o servidor

```
---

## ✔️ Tecnologias utilizadas | Práticas utilizadas | Technologies used | Practices used

- Python (Django)
- JWT Auth 
- HTLML 5
- CSS 3
- Clean code and Design Patters
- REST API
- Swagger
- Redis Cache 
- Docker

---

## 🚩 Contribuidores | contributors

| [<img src="https://avatars.githubusercontent.com/u/69232156?v=4" width=115><br><sub>Kawhan Laurindo de Lima</sub>](https://github.com/Kawhan) | 
| :---: | 
