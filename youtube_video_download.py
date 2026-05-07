from yt_dlp import YoutubeDL
import os
import subprocess
import sys

def find_nodejs():

    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Node.js encontrado: {result.stdout.strip()}")
            return True
    except:
        pass
    
    common_paths = [
        r'C:\Program Files\nodejs\node.exe',
        r'C:\Program Files (x86)\nodejs\node.exe',
        os.path.expandvars(r'%APPDATA%\nvm\node.exe'),
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            print(f"✅ Node.js encontrado em: {path}")
            return True
    
    return False

if not find_nodejs():
    print("⚠️  Node.js não foi encontrado no sistema!")
    print("\n💡 Tente:")
    print("   1. Feche este terminal completamente")
    print("   2. Abra um NOVO terminal (cmd)")
    print("   3. Digite: node --version")
    print("   4. Se aparecer a versão, execute o script novamente")
    print("\n   Se ainda não funcionar, Node.js pode não estar no PATH")
    sys.exit(1)

print()

url = input("Enter the YouTube video URL: ")

cookies_file = os.path.join(os.path.dirname(__file__), 'cookies.txt')

opts = {
    'outtmpl': r'C:\code\Downloads\%(title)s.%(ext)s',
    'format': 'best',
    'merge_output_format': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4'
    }],
    'quiet': False,
    'no_warnings': False,
    'socket_timeout': 30,
    'retries': 5,
}

if os.path.exists(cookies_file):
    opts['cookiefile'] = cookies_file
    print(f"✅ Usando arquivo de cookies: {cookies_file}\n")

try:
    print("Baixando vídeo...\n")
    with YoutubeDL(opts) as ydl:
        ydl.download([url])
    print("\n✅ Download concluído com sucesso!")
except Exception as e:
    print(f"\n❌ Erro ao baixar: {e}")