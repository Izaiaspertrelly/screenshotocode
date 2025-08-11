# Como Executar o Projeto "test post code"

Este é uma cópia completa do projeto screenshot-to-code com todas as configurações e chaves de API já incluídas.

## 📋 Pré-requisitos

- Python 3.8+ 
- Poetry (para gerenciamento de dependências Python)
- Node.js 16+
- Yarn (para gerenciamento de dependências JavaScript)

## 🚀 Como Executar

### 1. Backend (FastAPI)

```bash
cd backend
poetry install
poetry run uvicorn main:app --reload --port 7001
```

O backend estará rodando em: http://127.0.0.1:7001

### 2. Frontend (React/Vite)

Em um novo terminal:

```bash
cd frontend
yarn install
yarn dev
```

O frontend estará rodando em: http://localhost:5173

## 🔑 Chaves de API

As seguintes chaves de API já estão configuradas:

- ✅ OpenAI API Key
- ✅ Anthropic API Key (Claude)
- ✅ Grok API Key
- ✅ Gemini API Key

## 📁 Estrutura do Projeto

- `backend/` - Servidor FastAPI com todas as rotas e modelos de IA
- `frontend/` - Interface React com Vite
- `backend/.env` - Chaves de API do backend
- `frontend/.env` - Configurações do frontend
- `.env` - Configurações gerais do projeto

## 🌟 Funcionalidades

- Conversão de screenshots em código HTML/CSS/JS
- Suporte a múltiplos frameworks (React, Vue, HTML+Tailwind, etc.)
- Integração com múltiplos modelos de IA
- Geração de imagens com DALL-E 3
- Interface intuitiva para upload e edição

## 🔧 Solução de Problemas

Se encontrar problemas:

1. Verifique se todas as dependências estão instaladas
2. Confirme se as portas 7001 e 5173 estão livres
3. Verifique se as chaves de API estão válidas
4. Consulte o arquivo `Troubleshooting.md` para mais detalhes

## 📝 Notas

- Este projeto é uma cópia completa e independente
- Todas as configurações já estão prontas para uso
- As chaves de API são as mesmas do projeto original
