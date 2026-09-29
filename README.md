# Identificacao de Objetos para minha IC


### 1. Clonar o repositorio

```
git clone https://github.com/23Viegas/ic-identificacao-objetos
```

### 2. Entrar na pasta

```
cd ic-identificacao-objetos
```

### 3. Criar o ambiente virtual

```
python -m venv .venv
```

### 4. Ativar o ambiente virtual

```
.\.venv\Scripts\activate
```

### 5. Instalar as dependencias

```
python -m pip install opencv-python
python -m pip install ultralytics
```

### Treinamento de imagem passo a passo:

### 1. Site para fazer o treinamneto das imagens

https://universe.roboflow.com/

### 2. Tirar foto do objeto em várias posições e fundos e fazer o quadrado completo no objeto

### 3. Baixar o codigo e substituir no projeto:
   # 3.1 Colocar no data.yml

   ```
   train: train/images
   val: train/images

   nc: 1
   names: ['alicate']
   ```

### Executar o arquivo treinar.py
   ### Apos executar, substituir no main.py:

   ```
   modelo_objeto = YOLO("runs/detect/train-(numero da versao do treino)/weights/best.pt")
   ```


### Tutorial GitHub:
   # inicializa o git na pasta do projeto

   ```
   git init
   ```  

   # seleciona todos os arquivos para enviar

    ```
    git add .
    ```

   # salva um ponto de checkpoint com uma mensagem

    ```
    git commit -m "primeiro commit"
    ```

   # conecta sua pasta local ao repositório do GitHub

    ```
    git remote add origin https://github.com/23Viegas/ic-identificacao-objetos
    ```

   # envia tudo para o GitHub

    ```
    git push 
    ``` 

   # Baixa as atualizações mais recentes do GitHub para o seu computador
   
    ```
    git pull 
    ```  
     
