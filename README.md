# YouTube Video Downloader 🎬

Um downloader de vídeos do YouTube feito em Python que suporta vídeos com restrição de idade e máxima qualidade.

## Recursos ✨

- ✅ Download automático em **máxima qualidade** (melhor vídeo + melhor áudio)
- ✅ Suporte para vídeos com **restrição de idade**
- ✅ Conversão automática para **MP4**
- ✅ Verificação automática de **Node.js**
- ✅ Sistema robusto de **retentativas**
- ✅ Interface simples e amigável

## Requisitos 📋

Antes de usar, certifique-se de que tem instalado:

1. **Python 3.8+** - [Download aqui](https://www.python.org/downloads/)
2. **Node.js** - [Download aqui](https://nodejs.org/) (versão LTS recomendada)

## Instalação 🚀

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Youtube-Video-Downloader.git
cd Youtube-Video-Downloader
```

### 2. Instale as dependências Python

```bash
pip install -r requirements.txt
```

### 3. Verifique as instalações

```bash
# Verificar Python
python --version

# Verificar Node.js
node --version
```

## Como Usar 📺

### Uso Básico

```bash
python youtube_video_download.py
```

Depois é só colar a URL do vídeo e apertar Enter!

### Exemplo

```
Enter the YouTube video URL: https://youtu.be/dQw4w9WgXcQ
✅ Node.js encontrado: v22.14.0
Baixando vídeo...

[youtube] Extracting URL...
✅ Download concluído com sucesso!
```

### Local de Download

Por padrão, os vídeos são salvos em:
```
C:\code\Downloads\
```

Para alterar, edite a linha no `youtube_video_download.py`:
```python
'outtmpl': r'C:\seu\caminho\favorito\%(title)s.%(ext)s',
```

## Vídeos com Restrição de Idade 🔞

Se deseja fazer download de vídeos com restrição de idade:

1. **Abra o Microsoft Edge** e faça login no YouTube
2. **Confirme sua idade** quando o YouTube pedir
3. **Exporte os cookies:**
   - Instale a extensão [Get cookies.txt LOCALLY](https://microsoftedge.microsoft.com/addons/detail/get-cookiestxt-locally/mnlopdejbapmjfpjdbjkfeodijkbnjjp)
   - Visite YouTube.com
   - Clique na extensão e copie os cookies
4. **Salve como `cookies.txt`** na pasta do script
5. Execute o script normalmente - ele detectará o arquivo automaticamente!

## Estrutura do Projeto 📁

```
Youtube-Video-Downloader/
├── youtube_video_download.py    # Script principal
├── requirements.txt              # Dependências Python
├── .gitignore                    # Arquivos ignorados no Git
├── README.md                     # Este arquivo
└── cookies.txt                   # (PRIVADO - não é enviado pro Git)
```

## Troubleshooting 🔧

### "Node.js não foi encontrado"
- Feche o terminal completamente
- Abra um **novo terminal**
- Tente executar `node --version`
- Se funcionar, execute o script novamente

### "Erro: Requested format is not available"
- Pode ser um vídeo deletado ou privado
- Ou o YouTube está bloqueando requisições
- Tente novamente em alguns minutos

### "ERROR: Sign in to confirm your age"
- Você tem um arquivo `cookies.txt`?
- Se sim, ele pode estar expirado - exporte novos cookies
- Se não, siga as instruções da seção "Vídeos com Restrição de Idade"

### "FFmpeg não encontrado"
- Instale FFmpeg: [guia completo](https://ffmpeg.org/download.html)
- No Windows, adicione FFmpeg ao PATH do sistema

## Limitações ⚠️

- O YouTube limita downloads para evitar abuso
- Alguns vídeos podem ter restrições de copyright
- A qualidade disponível varia por vídeo
- Muito recomendado respeitar os direitos autorais

## Disclaimer ⚖️

Este projeto é fornecido "como está". Use por sua conta e risco. Respeite os direitos autorais do YouTube e dos criadores de conteúdo. O autor não é responsável pelo uso indevido desta ferramenta.
