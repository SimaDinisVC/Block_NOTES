def encoder(frase):
    frasedes = []
    for c in frase:
        frasedes.append(c)
    Normal = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    normal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Codificacao = ["E", "X", "W", "R", "O", "T", "P", "S", "U", "D", "Q", "G", "H", "J", "I", "K", "L", "Z", "M", "C", "Y", "B", "N", "F", "A", "V"]
    codificacao = ['e', 'x', 'w', 'r', 'o', 't', 'p', 's', 'u', 'd', 'q', 'g', 'h', 'j', 'i', 'k', 'l', 'z', 'm', 'c', 'y', 'b', 'n', 'f', 'a', 'v']
    numNormal = ['1','2','3','4','5','6','7','8','9','0']
    CodifiNum = ['!','"','#','$','%','&','/','(',')','=']
    codificado = ""
    for i in range(len(frasedes)):
        if frasedes[i] in Normal:
            codificado = codificado + codificacao[Normal.index(frasedes[i])]
        elif frasedes[i] in normal:
            codificado = codificado + Codificacao[normal.index(frasedes[i])]
        elif frasedes[i] in numNormal:
            codificado = codificado + CodifiNum[numNormal.index(frasedes[i])]
        else:
            codificado = codificado + frasedes[i]
    return codificado

def addNEWusr(user,passw):
    newuser = "'{0}':['{1}', 10, 0]".format(user,passw)
    fileread = open('datauser.py', 'r')
    data = str(fileread.read())
    fileread.close()
    filewrite = open('datauser.py', 'w')
    add = data.index("}")
    if 'login = {}' in data:
        line = data[:add] + newuser + data[add:]
    else:
        line = data[:add] + ", " + newuser + data[add:]
    filewrite.write(line) 
    filewrite.close()