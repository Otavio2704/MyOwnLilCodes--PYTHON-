import os

caminho_imagem = "C:/Users/SeuUsuario/Pictures/wallpaper.jpg"
comando = f'reg add "HKCU\\Control Panel\\Desktop" /v Wallpaper /t REG_SZ /d "{caminho_imagem}" /f'
os.system(comando)
os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
