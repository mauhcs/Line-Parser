weirdSymbols = ['\n']

#proposicoes
prop = ['de','da','do',
        'em','na','no',
        'para','pra','pro']
        
artigos = ['a','as','o','os',
            'um','uns','uma','umas']
            
conjuncao = ['e','E','que','com','q',
             'mas','Mas','se','mais']

negacao = ['nao','não']

verbos = ['é']

outros = ['né']

def ignoredCharacters(weird=True,
                      props=True,
                      art=True,
                      conj =True,
                      neg = True,
                      verb = True,
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
    if other:
        ret.extend(outros)
    return ret
