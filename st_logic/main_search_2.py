from st_logic.st_util import Util
import st_root
from operator import itemgetter

json_data = Util.json_chats_load()

listado_chats = {}
consolidado_terminos = {}
cont_chats = 0

banklist = []
infile = open(st_root.ROOT_DIR + '/st_data/input/' + 'list - bank.txt', 'r', encoding='utf-8')
for line in infile:
    banklist.append(line.strip().split('\n')[0])

infile.close()

for jchat in json_data:
    cont_chats = cont_chats + 1
    id_chat = jchat['id_conversation']
    textos_chat = ""

    for jtext in jchat['messages_all']:
        textos_chat = textos_chat + " " + jtext['text'] + " "

    if textos_chat == "":
        listado_chats[id_chat] = ""
    else:
        terms = []
        for term in banklist:
            count = textos_chat.count(term)

            if count>0:
                terms.append((term,count))

        terms_sorted = sorted(terms, key=itemgetter(1), reverse=True)
        listado_chats[id_chat] = terms_sorted

        for words in terms_sorted:
            if words[0] in consolidado_terminos:
                consolidado_terminos[words[0]] = consolidado_terminos[words[0]] + words[1]
            else:
                consolidado_terminos[words[0]] = words[1]


Util.export_cvs("total_terminos",consolidado_terminos)
Util.export_cvs("terminos_x_chat",listado_chats)