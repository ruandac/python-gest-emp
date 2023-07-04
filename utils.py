import os
from PyPDF2 import PdfReader

# Função retorna o diretorio do icone baseado na pasta images conforme o nome do script que está executando a função.
# Ex: Função executada no script "agua.py" retorna a imagem "agua.png" se existir na pasta images 
def iconPath(module_file):
    # Obtém o nome do módulo gerar_relatorio.py
    module_name = os.path.splitext(os.path.basename(module_file))[0]
    
    # Obtém o diretório relativo da pasta "imagens"
    image_dir = 'images'
    
    # Obtém o nome do arquivo de imagem com base no nome do módulo gerar_relatorio.py
    image_name = f"{module_name}.png"
    
    # Verifica se o arquivo de imagem existe
    image_path = os.path.join(image_dir, image_name)
    if os.path.exists(image_path):
        return image_path
    else:
        return None

# Obter dados de um PDF (Em progresso...)
file_name = "pdf-mariot.pdf"
reader = PdfReader(file_name)
page = reader.pages[0]
count = 0

# Coletar o texto
text = page.extract_text().split("\n")
for line in text:
    count += 1
    if ('Total Geral' in line):
        print(text[count+1])