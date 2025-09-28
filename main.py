'''receitas = [
    {
        "nome": "brigadeiro",
        "ingredientes": ["1 caixa de leite condensado", "1 colher (sopa) de margarina sem sal", "7 colheres (sopa) de achocolatado ou 4 colheres (sopa) de chocolate em pó", "chocolate granulado"],
        "utensilios": ["panela", "espatula", "copo medidor", "prato raso"],
        "modo_preparo": "Em uma panela funda, acrescente o leite condensado, a margarina e o chocolate em pó.
Cozinhe em fogo médio e mexa até que o brigadeiro comece a desgrudar da panela.
Deixe esfriar e faça pequenas bolas com a mão passando a massa no chocolate granulado."
    },
    {
        "nome": "torta",
        "ingredientes": ["3 ovos", "1 xícara de leite", "2 xícaras de farinha"],
        "utensilios": ["liquidificador", "forma"],
        "modo_preparo": "Bata tudo no liquidificador e asse por 30 minutos."
    },
    {
        "nome": "cocada",
        "ingredientes": ["400 g de coco fresco ralado grosso", "-1 e 1/2 xícara (chá) de água", "óleo, o quanto baste para untar",
             "2 e 1/2 xícaras (chá) de açúcar"
              "1/4 xícara (chá) de leite condensado"],
        "utensilios": ["colher de pau", "espatula", "panela", "ralador"],
        "modo_preparo": "Unte uma assadeira grande com óleo.
Reserve
Coloque a água e o açúcar numa panela e leve ao fogo alto.
Despeje o coco na panela com a calda e mexa.
Acrescente o leite condensado e continue mexendo até que comece a desprender do fundo da panela.
Retire a cocada do fogo e coloque as colheradas sobre a assadeira untada.
Espere endurecer um pouco e retire as cocadas da assadeira com uma espátula.
Se quiser guardar a cocada, deixe esfriar bem e guarde num recipiente com tampa."
    }
]
  [
 {
        "nome": "chocolate quente",
        "ingredientes": ["1 xícara (chá) de leite", "1 colher (café) de açúcar", "1 colher (chá) rasa de amido de milho", "1/2 colher (café) de canela em pó", "1 colher (sopa) de chocolate em pó"],
        "utensilios": ["caneca", "leiteira", "espatula"],
        "modo_preparo": "Misture o açúcar, o chocolate, a canela, parte do leite e leve ao fogo.
Dissolva o amido de milho no restante do leite para que ele não empelote quando for adicionado ao restante dos ingredientes.
Adicione o leite com amido à mistura e mexa com uma colher até engrossar e ferver.
Sirva quente."
    },
    {
        "nome": "palha italiana",
        "ingredientes": ["1 caixa de leite condensado", "1/2 colher (sopa) de margarina sem sal", "8 colheres (sopa) de chocolate em pó", "1 pacote de biscoito maisena"],
        "utensilios": ["panela", "pincel", "colhaer de pau", "travessa", "faca"],
        "modo_preparo": "Pique o biscoito em pedacinhos pequenos e reserve.
Com o leite condensado, a margarina e o chocolate em pó, faça um brigadeiro.
Assim que o brigadeiro começar a soltar do fundo da panela, misture o biscoito picado até formar uma massa, retire do fogo.
Unte uma bancada de mármore, ou alguma superfície lisa, com margarina e despeje essa massa.
Abra a massa, batendo com a palma das mãos.
Deixe esfriar e corte em quadradinhos.,"
    }
    {
        "nome": "mousse de maracujá",
        "ingredientes": ["1 lata de leite condensado", "1 lata de creme de leite", "suco de maracujá"],
        "utensilios": ["liquidificador"],
        "modo_preparo": "Bata tudo no liquidificador e leve à geladeira."
    }
]
  
]'''
from fastapi import FastAPI

from pydantic import BaseModel
from typing import List
class receita(BaseModel):
    nome : str
    ingredientes : List[str]
    modo_de_preparo : str

receitas: List[receita] = []

app = FastAPI(title='API de Ana júlia')

@app.get("/")
def title():
    return {"title": "livro de receitas"}

@app.get("/receita")
def get_receita():
    return{"/"}

@app.get("/receitas/{nome_receita}")
def get_receita_by_name(nome_receita: str):
    for receita in receitas:
        if receita.nome == nome_receita:
          return receita

    return {"receita não encontrada"}

receitas: List[receita] = []

@app.get("/receitas/")
def get_todas_receitas():
    return receitas

@app.post("/receitas")
def create_receita(dados: receita):
    nova_receita = dados

    receitas.append(nova_receita)
    return nova_receita

from fastapi import FastAPI
app = FastAPI()
receitas = []

@app.post("/receitas/")
def criar_receita(nome: str, descricao: str):
     for r in receitas:
          if r[0] == nome:
               return "uma receita ja tem esse nome"
          receitas.append((nome, descricao))
          return "receita {nome} criada"
     
class CreateReceita(BaseModel):
        nome: str
        ingredientes: List[str]
        modo_de_preparo: str

class Receita(BaseModel):
        id: int
        nome: str
        ingredientes: List[str]
        modo_de_preparo: str

from fastapi import FastAPI
app = FastAPI()

receitas = []
ultimo_id = 0

@app.post("/receitas")
def criar_receita(nome: str , ingredientes: str , modo_de_preparo: str):
     ultimo_id[0] += 1
     receita = (ultimo_id[0], nome,ingredientes, modo_de_preparo)
     receitas.append(receita)
     return receita

from fastapi import FastAPI
app = FastAPI()

receitas = [
     {"id":1, "nome": "mousse de maracuja", "ingredientes":["1 lata de leite condensado", "1 lata de creme de leite", "suco de maracujá"]},
     {"id":2, "nome": "brigadeiro", "ingredientes":["1 caixa de leite condensado", "1 colher (sopa) de margarina sem sal", "7 colheres (sopa) de achocolatado ou 4 colheres (sopa) de chocolate em pó", "chocolate granulado"]},
]

@app.get("/receitas/id/{id}")
def get_receita_por_id(id:int):
    for receita in receitas:
     if receita["id"] == id:
          return receita
     return{"mensagem": "receita nao encontrada"}

     from fastapi import FastAPI

app = FastAPI()

@app.get("/receitas/id/{id}")
def get_receita(id: int):
    if id == 1:
        return {"id": 1, "nome":  "mousse de maracuja", "ingredientes":["1 lata de leite condensado", "1 lata de creme de leite", "suco de maracujá"]}
    if id == 2:
        return {"id": 2, "nome": "brigadeiro", "ingredientes":["1 caixa de leite condensado", "1 colher (sopa) de margarina sem sal", "7 colheres (sopa) de achocolatado ou 4 colheres (sopa) de chocolate em pó", "chocolate granulado"]}
    return {"mensagem": "Receita não encontrada"}

@app.post("/receitas")
def criar_receita(nome: str, ingredientes: list):
    if nome == "" or nome[1:] == "" or nome[50:]:
        return {"mensagem": "Nome inválido"}
    if ingredientes == [] or ingredientes[20:]:
        return {"mensagem": "Quantidade inválida de ingredientes"}
    if nome == "Bolo de Chocolate" or nome == "Brownie":
        return {"mensagem": "Receita já existe"}
    return {"mensagem": "Receita criada"}

@app.put("/receitas{id}")
def update_receita(id: int, dados: CreateReceita):
    for i in range(len(receitas)):
        if receitas[i].id == id:
            receita_atualizada = Receita(
                id=id,
                nome=dados.nome,
                ingredientes=dados.ingredientes,
                modo_de_preparo=dados.modo_de_preparo,
            )

            receitas[i] = (receita_atualizada)
            return receita_atualizada
        return{"mensagem": "Receita não encontrada"}
    
    receita = ["brigadeiro", "torta", "cocada", "chocolate quente", "mousse de maracuja", "palha italiana"]

    def editar_nome(nome_atual, nome_alterado):
        if nome_alterado in receitas:
            return {"já existe"}
        for i in range (len(receitas)): 
            if receitas[i] == nome_atual:
                receitas[i] == nome_alterado
                return {"nome modificado"}
            return{"receita não encontrada"}
        
        def editar_receita(nome, ingredientes, modo_de_preparo):
            if nome == "" or ingredientes == "" or modo_de_preparo == "":
                return {"campos vazios não são salvos"}
            return {"receita foi editada"}      

        @app.delete("/receitas/{id}") 
        def deletar_receita(id: int):

            for i in range(len(receitas)):
                if receitas[i].id == id:
                    receitas.pop(i)
                    return {"mensagem": "receita deletada"}
                return{"mensagem : " "receita não encontrada"}
            
            from fastapi import FastAPI

            app = FastAPI()
            receitas = ["brigadeiro", "torta", "cocada", "chocolate quente", "mousse de maracuja", "palha italiana"]

            @app.delete("/deletar/{nome}")
            def deletar_receita(nome: str):
                if not receitas:
                    return {"mensagem": "não existe receitas para excluir"}
                if nome in receitas:
                    receitas.remove(nome)
                    return {"mensagem": "deletando receita de '{nome}'"}
                else:
                    return {"mensagem": "não existe a receita de {nome} na lista"}