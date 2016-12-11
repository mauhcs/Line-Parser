weirdSymbols = ['\n']

#proposicoes
prop = ['de','da','do(s)*', 'em','na','no','para','pra','pro','por']
        
artigos = ['a','as','o','os', 'um','uns','uma','umas']
            
conjuncao = ['e','E','(\")*que','com','q',
         'mas','Mas','se','mais', 'pq','como','\"e']

pronomes = ["(\")*eu", "vc", "ele", "ela","eles","elas",'me','minha','meu','esse','essa','isso','gente','te','quem','você','vocês','vcs','sua','nossa']

negacao = ['nao','não']

verbos = ['é','acho','tem','vou','tava','fazer','tinha','tinha','meio','foi','to','ver','vai','t[aá]','tenho','estou','quero','ser','sei','era','ter','achei','falando','nem','t[oô]','ficar','pode','sou','fico','são','falar','ir','vi','deve','tem','faz','dar','queria','parece','fiquei','é,']

outros = ['né','agora','ja','já','eh','ainda','tb','tambem','também','muito','oq','qdo','pelo','mesmo','só','sem','sem','sobre','então','entao','tão','at[eé]','tod[ao]','lá','(d)*aí','ou','mto','quando','ah','pelo','aqui','ia','bem','assim','você','depois','tua','dai','porque','nunca','sempre','assim','quase','não','assim,','ai','ah,']

def ignoredCharacters(weird=True,
                      props=True,
                      art=True,
                      conj =True,
                      neg = True,
                      verb = True,
                      prono=True,
                      other = True):
    ret = []
    if weird:
        ret.extend(weirdSymbols)
    if props:
        ret.extend(prop)
    if art:
        ret.extend(artigos)
    if conj:
        ret.extend(conjuncao)
    if neg:
        ret.extend(negacao)
    if verb:
        ret.extend(verbos)
    if prono:
        ret.extend(pronomes)
    if other:
        ret.extend(outros)
    ig = '$|'.join(ret)
    return ig
    

marks = [",",".","!","?","\""]
def removeMarks(w):
  y = w
  for m in marks:
    y = y.replace(m,"")
