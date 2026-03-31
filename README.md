# Reconhecimento de Produto por IA

Este projeto utiliza inteligência artificial para reconhecimento de produtos. Ele é construído com FastAPI e inclui um modelo treinado (`best.pt`) para detecção.

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior
- Instalar as dependências (se houver um `requirements.txt`, execute `pip install -r requirements.txt`)

### Iniciar o Servidor
Para iniciar o servidor de desenvolvimento com recarregamento automático, execute o seguinte comando no terminal:

```bash
uvicorn main:app --reload
```

O servidor será iniciado em `http://127.0.0.1:8000`.

### Acessar a Documentação da API
Após iniciar o servidor, acesse o painel interativo da API FastAPI em:

[http://127.0.0.1:8000/docs#](http://127.0.0.1:8000/docs#)

Aqui você pode testar os endpoints disponíveis e visualizar a documentação automática.

## 📁 Estrutura do Projeto
- `main.py`: Código principal da aplicação FastAPI
- `best.pt`: Modelo treinado para reconhecimento
- `.gitignore`: Arquivos ignorados pelo Git

## 🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias ou relatar issues.

## 📄 Licença
Este projeto está sob a licença MIT.