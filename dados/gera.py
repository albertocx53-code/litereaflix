"""Gera src/data/catalogo.json da LiteraFlix. Rode: python3 dados/gera.py"""
import json, os

def yt(i): return 'https://www.youtube.com/watch?v=' + i

N, BE, MN, U, TVB, RV, AA = 'Professor Noslen', 'Brasil Escola', 'Prof. Marcelo Nunes', 'Univesp (série Literatura Fundamental)', 'TV Brasil (Caminhos da Reportagem)', 'TV Cultura (Roda Viva)', 'Prof. Átila Almada'

CAPAS = {
    'escola': [('#1d3b2a', '#081a10'), ('#14213d', '#070d1b'), ('#3b1f3f', '#160a18'), ('#0f3b3f', '#05181a'), ('#5a1a22', '#1c070b'), ('#6b4a12', '#221704'), ('#2b3340', '#0c0f14')],
    'autor': [('#5a1a22', '#1c070b'), ('#2b3340', '#0c0f14'), ('#3b1f3f', '#160a18'), ('#1d3b2a', '#081a10')],
    'obra': [('#14213d', '#070d1b'), ('#6b4a12', '#221704'), ('#0f3b3f', '#05181a'), ('#5a1a22', '#1c070b'), ('#1d3b2a', '#081a10'), ('#3b1f3f', '#160a18')],
    'universal': [('#232a3a', '#0a0d14'), ('#3a2a1a', '#140d07'), ('#1e3340', '#091219')],
    'trilha': [('#3a0f18', '#120408'), ('#0e2a33', '#040f13'), ('#2e2a10', '#100e04')],
    'documentario': [('#402018', '#140906'), ('#183028', '#07120e')],
}
OURO, COBRE, PRATA = '#e3b45a', '#e09a6a', '#d6dbe2'
_cont = {}
def capa(area, motif, kicker, autor=None, accent=OURO):
    lista = CAPAS[area]; k = _cont.get(area, 0); _cont[area] = k + 1
    c1, c2 = lista[k % len(lista)]
    a = {'motif': motif, 'c1': c1, 'c2': c2, 'accent': accent, 'kicker': kicker}
    if autor: a['autor'] = autor
    return a

def ficha(porque, ideias, nomes, objetivos, perguntas, leitura, atividades=(), dicas=(), refs=()):
    return {
        'porQue': porque, 'conceitos': list(ideias), 'pensadores': list(nomes), 'objetivos': list(objetivos), 'perguntas': list(perguntas),
        'plano': [
            {'etapa': 'Pergunta de abertura', 'tempo': '10 min', 'descricao': f'Lance a pergunta "{perguntas[0]}" e anote as respostas da turma no quadro.'},
            {'etapa': 'Vídeo', 'tempo': '15 a 25 min', 'descricao': 'Assista ao vídeo com a turma e pause nos pontos-chave para os alunos anotarem as ideias principais.'},
            {'etapa': 'Leitura comentada', 'tempo': '15 min', 'descricao': leitura},
            {'etapa': 'Debate e síntese', 'tempo': '10 min', 'descricao': 'Retome as respostas do início e peça que cada aluno escreva, em três linhas, o que aprendeu.'},
        ],
        'atividades': [{'nome': a, 'descricao': d} for a, d in atividades],
        'roteiro': [], 'dicas': list(dicas), 'referencias': list(refs),
    }

T = []
def add(slug, tipo, area, titulo, sinopse, arte, videos, temas, fontes, ano=None, chamada=None, ficha_=None, pop=50, generos=(), elenco=()):
    T.append({
        'slug': slug, 'tipo': tipo, 'titulo': titulo, 'tituloOriginal': None, 'chamada': chamada, 'sinopse': sinopse,
        'ano': ano, 'duracao': None, 'pais': None, 'idiomas': ['Português'], 'generos': list(generos), 'disciplinas': [area],
        'faixa': ['Ensino Médio', 'Enem e vestibulares'], 'arte': arte, 'destaque': False, 'ordemDestaque': None, 'popularidade': pop,
        'direcao': list(fontes), 'elenco': list(elenco), 'temas': list(temas), 'ondeAssistir': [], 'slides': [], 'materiais': [],
        'videos': [{'titulo': t, 'url': yt(i)} for t, i in videos], 'ficha': ficha_,
    })

# ======================= ESCOLAS LITERÁRIAS =======================
E = lambda *a, **k: add(*a[:2], 'escola', *a[2:], **k)
E('linha-do-tempo-das-escolas', 'videoaula', 'Linha do Tempo das Escolas Literárias',
  'O mapa da literatura em língua portuguesa: o que é uma escola literária, como cada época responde à anterior e a ordem que você precisa saber para o Enem e os vestibulares.',
  capa('escola', 'livro', 'Comece por aqui'), [('Introdução à Literatura: linha do tempo das escolas literárias', 'WGZFBePibF0')],
  ['introducao', 'enem', 'literatura-brasileira', 'literatura-portuguesa'], [N], ano=1100, chamada='Antes de tudo, o mapa.', pop=88,
  ficha_=ficha('Dá à turma a visão do todo antes de entrar em cada época, o que facilita perceber continuidades e rupturas.',
    ['Estilo de época', 'Contexto histórico', 'Ruptura e continuidade', 'Literatura e sociedade'], ['Gil Vicente', 'Camões', 'Machado de Assis', 'Mário de Andrade'],
    ['Reconhecer a sequência das escolas literárias', 'Relacionar cada escola ao seu contexto histórico', 'Entender que uma escola reage à anterior'],
    ['Por que a literatura muda de uma época para outra?', 'Toda mudança literária é uma ruptura completa?', 'Qual época você acha que mais se parece com a nossa?'],
    'Monte com a turma uma linha do tempo no quadro, com uma data, uma escola e um autor para cada época.',
    [('Linha do tempo ilustrada', 'Em grupos, os alunos fazem uma linha do tempo em cartolina com uma imagem e um trecho de cada escola.')]))

E('trovadorismo', 'videoaula', 'Trovadorismo',
  'As cantigas medievais galego-portuguesas: de amor, de amigo, de escárnio e de maldizer. Poesia feita para ser cantada nas cortes e nas vilas, ponto de partida da literatura em português.',
  capa('escola', 'louro', 'Escola literária', 'séculos XII a XV'), [('Trovadorismo: contexto histórico', 'N8aCwmWgVyA')],
  ['trovadorismo', 'literatura-portuguesa', 'poesia', 'enem'], [N], ano=1189, chamada='Quando a poesia era cantada.', pop=64,
  ficha_=ficha('Mostra a origem da língua literária portuguesa e ajuda a turma a perceber como amor, sátira e música andavam juntos.',
    ['Cantiga de amor', 'Cantiga de amigo', 'Cantiga de escárnio', 'Cantiga de maldizer', 'Vassalagem amorosa', 'Coita amorosa'], ['Paio Soares de Taveirós', 'D. Dinis', 'Martim Codax'],
    ['Diferenciar as cantigas líricas das satíricas', 'Identificar o eu lírico feminino da cantiga de amigo', 'Relacionar as cantigas ao contexto feudal'],
    ['Quem fala na cantiga de amigo, se quem escrevia era homem?', 'O que as cantigas de escárnio têm em comum com os memes?', 'Que músicas de hoje lembram a coita amorosa?'],
    'Leia uma cantiga de amigo de Martim Codax e identifique, com a turma, quem fala e para quem.',
    [('Cantiga de hoje', 'Os alunos reescrevem uma cantiga de escárnio sobre um tema atual da escola, sem citar pessoas reais.')]))

E('humanismo', 'videoaula', 'Humanismo',
  'A transição da Idade Média para o Renascimento em Portugal: as crônicas de Fernão Lopes e o teatro de Gil Vicente, que ri da sociedade inteira.',
  capa('escola', 'mascara', 'Escola literária', 'séculos XV e XVI'), [('Humanismo', 'TaiiIil8-Ow'), ('"Auto da barca do inferno", de Gil Vicente: videoaula', 'Yg8P9y14EDk')],
  ['humanismo', 'literatura-portuguesa', 'teatro', 'gil-vicente'], [N, MN], ano=1434, chamada='O teatro que critica todo mundo.', pop=60,
  ficha_=ficha('Gil Vicente é cobrado com frequência e ajuda a discutir crítica social com humor.',
    ['Teatro popular', 'Auto e farsa', 'Crítica social', 'Teocentrismo em crise', 'Crônica histórica'], ['Gil Vicente', 'Fernão Lopes'],
    ['Caracterizar o Humanismo como época de transição', 'Reconhecer a crítica social no teatro de Gil Vicente', 'Identificar tipos sociais representados'],
    ['Quem seria julgado hoje se houvesse uma barca do inferno?', 'O humor pode ser uma forma de crítica?', 'Por que Gil Vicente usa personagens-tipo?'],
    'Leia a cena do Fidalgo no Auto da barca do inferno e discuta o que ele leva consigo e por quê.'))

E('quinhentismo', 'videoaula', 'Quinhentismo',
  'Os primeiros textos escritos sobre o Brasil: a Carta de Pero Vaz de Caminha, os relatos de viajantes e a literatura de catequese dos jesuítas.',
  capa('escola', 'caravela', 'Escola literária', 'século XVI', PRATA), [('Quinhentismo', 'WULOzFYZ30g')],
  ['quinhentismo', 'literatura-brasileira', 'enem'], [N], ano=1500, chamada='O Brasil visto de fora.', pop=58,
  ficha_=ficha('Permite discutir o olhar do colonizador e a visão sobre os povos indígenas, tema frequente no Enem.',
    ['Literatura informativa', 'Literatura de catequese', 'Olhar eurocêntrico', 'Carta de achamento'], ['Pero Vaz de Caminha', 'Padre José de Anchieta', 'Pero de Magalhães Gândavo'],
    ['Reconhecer os textos informativos do século XVI', 'Analisar a visão do europeu sobre a terra e os povos indígenas', 'Diferenciar texto informativo e texto de catequese'],
    ['Como os povos indígenas aparecem na Carta de Caminha?', 'Quem não teve voz nesses textos?', 'Como seria a mesma cena contada por um indígena?'],
    'Leia o trecho da Carta em que Caminha descreve os indígenas e marque as palavras que revelam o olhar do europeu.',
    [('Outra versão da chegada', 'Os alunos reescrevem o encontro de 1500 do ponto de vista indígena.')]))

E('classicismo', 'videoaula', 'Classicismo',
  'O Renascimento em Portugal: a medida nova, o soneto, o equilíbrio e a epopeia Os Lusíadas, de Luís de Camões.',
  capa('escola', 'caravela', 'Escola literária', 'século XVI'), [('Classicismo', 'yUx7vExUi4k')],
  ['classicismo', 'literatura-portuguesa', 'poesia', 'camoes'], [N], ano=1527, chamada='Camões e a medida nova.', pop=62,
  ficha_=ficha('Camões é base para entender o soneto e a épica, e aparece em muitas questões de interpretação.',
    ['Antropocentrismo', 'Medida nova', 'Soneto', 'Epopeia', 'Racionalismo', 'Neoplatonismo amoroso'], ['Luís de Camões', 'Sá de Miranda'],
    ['Reconhecer características do Classicismo', 'Analisar um soneto de Camões', 'Identificar a estrutura de Os Lusíadas'],
    ['O amor pode ser explicado pela razão?', 'Por que os navegadores viraram heróis de epopeia?', 'O que fica de fora da história contada em Os Lusíadas?'],
    'Leia "Amor é fogo que arde sem se ver" e mostre como Camões usa antíteses para definir o amor.'))

E('barroco', 'videoaula', 'Barroco',
  'A arte do contraste: fé e pecado, corpo e alma, luz e sombra. No Brasil, a poesia de Gregório de Matos e os sermões do Padre Antônio Vieira.',
  capa('escola', 'barroco', 'Escola literária', 'século XVII'),
  [('Barroco no Brasil', '1FN2jCxgnt0'), ('Barroco em Portugal', 'zGVONzNXGSo'), ('"Sermão da Sexagésima", do Padre Antônio Vieira: análise', 'egh2tDx-JMw')],
  ['barroco', 'literatura-brasileira', 'literatura-portuguesa', 'poesia', 'enem'], [N], ano=1601, chamada='A arte dos contrastes.', pop=66,
  ficha_=ficha('As figuras de linguagem do Barroco ajudam a turma a ler poemas e textos argumentativos com mais atenção.',
    ['Cultismo', 'Conceptismo', 'Antítese e paradoxo', 'Fusionismo', 'Carpe diem', 'Sátira'], ['Gregório de Matos', 'Padre Antônio Vieira'],
    ['Identificar cultismo e conceptismo', 'Reconhecer antíteses e paradoxos', 'Relacionar o Barroco à Contrarreforma'],
    ['Por que o homem barroco vive em conflito?', 'A sátira de Gregório de Matos ainda faria sentido hoje?', 'Um sermão pode ser um texto argumentativo?'],
    'Leia um soneto de Gregório de Matos e peça que os alunos sublinhem as antíteses.'))

E('arcadismo', 'videoaula', 'Arcadismo',
  'O retorno à simplicidade: pastores, campos, vida bucólica e razão iluminista. No Brasil, a poesia ligada à Inconfidência Mineira.',
  capa('escola', 'louro', 'Escola literária', 'século XVIII', COBRE),
  [('Arcadismo no Brasil: contexto histórico e autores', 'leb7oRjtsO8'), ('Arcadismo: contexto histórico e características', 'svEGlGf5Zo4'), ('Arcadismo em Portugal', 'Yadx1nAvgyo')],
  ['arcadismo', 'literatura-brasileira', 'poesia'], [BE, N], ano=1768, chamada='Fugir para o campo.', pop=55,
  ficha_=ficha('Mostra como a literatura dialoga com o Iluminismo e com a história de Minas Gerais.',
    ['Bucolismo', 'Fugere urbem', 'Locus amoenus', 'Aurea mediocritas', 'Pastoralismo', 'Inutilia truncat'], ['Tomás Antônio Gonzaga', 'Cláudio Manuel da Costa', 'Basílio da Gama', 'Bocage'],
    ['Reconhecer as convenções árcades', 'Relacionar o Arcadismo ao Iluminismo', 'Ler liras de Marília de Dirceu'],
    ['Por que poetas da cidade fingiam ser pastores?', 'Fugir da cidade ainda é um desejo atual?', 'Que relação há entre os poetas árcades e a Inconfidência?'],
    'Leia uma lira de Marília de Dirceu e identifique os elementos do cenário bucólico.'))

E('romantismo', 'videoaula', 'Romantismo',
  'Sentimento, nacionalismo e liberdade. O indianismo, o ultrarromantismo e a poesia social de Castro Alves; na prosa, os romances de José de Alencar.',
  capa('escola', 'flor', 'Escola literária', 'século XIX'),
  [('Romantismo no Brasil: poesia', 'M7okFxuX8fM'), ('Romantismo no Brasil: prosa', 'HoaCn9VnY2w'), ('Primeira geração do Romantismo (poesia)', '0J5gUbsYpjw'),
   ('Segunda geração do Romantismo (poesia)', '6doyaptYpQg'), ('Romantismo em Portugal', 'MUvd5BJiGI4')],
  ['romantismo', 'literatura-brasileira', 'poesia', 'prosa', 'enem', 'jose-de-alencar'], [N, BE], ano=1836, chamada='Sentir é preciso.', pop=82,
  ficha_=ficha('É a escola mais cobrada no Enem e ajuda a discutir a construção da identidade nacional.',
    ['Nacionalismo', 'Indianismo', 'Subjetivismo', 'Idealização da mulher', 'Mal do século', 'Condoreirismo'], ['Gonçalves Dias', 'Álvares de Azevedo', 'Castro Alves', 'José de Alencar', 'Joaquim Manuel de Macedo'],
    ['Diferenciar as três gerações românticas', 'Analisar a idealização do indígena', 'Reconhecer a poesia social de Castro Alves'],
    ['Por que o indígena virou herói nacional no Romantismo?', 'Quem ficou de fora da identidade nacional romântica?', 'Que traços românticos você vê nas músicas e séries de hoje?'],
    'Compare "Canção do exílio", de Gonçalves Dias, com um trecho de "O navio negreiro", de Castro Alves.',
    [('Paródia da Canção do exílio', 'Os alunos escrevem uma "Canção do exílio" sobre o próprio bairro.')]))

E('realismo-naturalismo', 'videoaula', 'Realismo e Naturalismo',
  'A literatura que desconfia do sentimento: a ironia de Machado de Assis, a análise psicológica e o determinismo do romance naturalista de Aluísio Azevedo.',
  capa('escola', 'olho', 'Escola literária', 'fim do século XIX'),
  [('Realismo no Brasil', 'iCXp_ic4p_E'), ('Naturalismo no Brasil', '0ca0bBqnxE4'), ('Naturalismo em Portugal', 'FAzWo39rMYY')],
  ['realismo', 'literatura-brasileira', 'prosa', 'enem', 'machado-de-assis'], [N], ano=1881, chamada='Olhar a sociedade sem véus.', pop=84,
  ficha_=ficha('Machado de Assis é o autor mais cobrado nos vestibulares e o Realismo ensina a ler a ironia.',
    ['Objetividade', 'Análise psicológica', 'Ironia', 'Crítica à burguesia', 'Determinismo', 'Zoomorfização'], ['Machado de Assis', 'Aluísio Azevedo', 'Raul Pompeia', 'Eça de Queirós'],
    ['Diferenciar Realismo e Naturalismo', 'Reconhecer a ironia machadiana', 'Relacionar o Naturalismo às teorias científicas do século XIX'],
    ['O meio determina quem somos?', 'Por que Machado usa narradores pouco confiáveis?', 'O que mudou do romance romântico para o realista?'],
    'Leia o capítulo "O delírio" ou "Das negativas", de Memórias póstumas, e discuta o tom do narrador.'))

E('parnasianismo', 'videoaula', 'Parnasianismo',
  'A arte pela arte: forma perfeita, rimas raras, sonetos de métrica rigorosa e temas da Antiguidade. Olavo Bilac, Raimundo Correia e Alberto de Oliveira.',
  capa('escola', 'louro', 'Escola literária', 'fim do século XIX', PRATA),
  [('Parnasianismo no Brasil', 'JKmrUc1PhuE'), ('Parnasianismo', 'OmiZrv3DBns'), ('Parnasianismo em Portugal', 'iqP66FxK0h4')],
  ['parnasianismo', 'literatura-brasileira', 'poesia', 'olavo-bilac'], [N, BE], ano=1882, chamada='A busca da forma perfeita.', pop=52,
  ficha_=ficha('Ajuda a ensinar métrica e soneto, e prepara a turma para entender a reação modernista.',
    ['Arte pela arte', 'Culto da forma', 'Soneto', 'Métrica e rima rica', 'Objetividade', 'Temas clássicos'], ['Olavo Bilac', 'Raimundo Correia', 'Alberto de Oliveira'],
    ['Reconhecer o soneto parnasiano', 'Fazer a escansão de um verso', 'Entender por que os modernistas criticaram os parnasianos'],
    ['A forma de um poema importa tanto quanto o conteúdo?', 'Por que os modernistas debocharam dos parnasianos?', 'Rima rica deixa o poema melhor?'],
    'Leia "Profissão de fé", de Olavo Bilac, e compare com "Os sapos", de Manuel Bandeira.'))

E('simbolismo', 'videoaula', 'Simbolismo',
  'Musicalidade, mistério e espiritualidade. A poesia que sugere em vez de dizer, com Cruz e Sousa e Alphonsus de Guimaraens.',
  capa('escola', 'lua', 'Escola literária', 'fim do século XIX', PRATA),
  [('Simbolismo no Brasil', 'rVjVUTXHocQ'), ('Simbolismo', 'Tt99uuF1-Bk'), ('Cruz e Sousa', '_lpDA9i-q9E')],
  ['simbolismo', 'literatura-brasileira', 'poesia', 'cruz-e-sousa', 'vozes-negras'], [N, BE], ano=1893, chamada='Sugerir, não dizer.', pop=54,
  ficha_=ficha('Trabalha a sonoridade do poema e apresenta Cruz e Sousa, poeta negro fundamental da literatura brasileira.',
    ['Musicalidade', 'Sinestesia', 'Aliteração', 'Misticismo', 'Subjetividade', 'Obsessão pelo branco'], ['Cruz e Sousa', 'Alphonsus de Guimaraens', 'Camilo Pessanha'],
    ['Reconhecer recursos sonoros do Simbolismo', 'Identificar sinestesias', 'Conhecer a trajetória de Cruz e Sousa'],
    ['Um poema pode ser como uma música?', 'Que relação há entre a obsessão pelo branco e o racismo vivido por Cruz e Sousa?', 'O que um poema ganha quando sugere em vez de explicar?'],
    'Leia em voz alta "Violões que choram", de Cruz e Sousa, e peça que a turma identifique as aliterações.'))

E('pre-modernismo', 'videoaula', 'Pré-Modernismo',
  'O Brasil real entra na literatura: Os sertões de Euclides da Cunha, a crítica de Lima Barreto, o Jeca Tatu de Monteiro Lobato e a poesia de Augusto dos Anjos.',
  capa('escola', 'sertao', 'Período literário', 'início do século XX', COBRE),
  [('Pré-Modernismo', 'UBxq1C4jVLE'), ('Pré-Modernismo: características e autores', 'CYnvT0jr6h4'), ('Lima Barreto', 'O7tA6_gtoQ0')],
  ['pre-modernismo', 'literatura-brasileira', 'prosa', 'enem', 'lima-barreto'], [N, BE], ano=1902, chamada='O Brasil que não aparecia nos livros.', pop=70,
  ficha_=ficha('Conecta literatura, história da Primeira República e questões sociais muito cobradas no Enem.',
    ['Denúncia social', 'Regionalismo', 'Linguagem jornalística', 'Nacionalismo crítico', 'Guerra de Canudos'], ['Euclides da Cunha', 'Lima Barreto', 'Monteiro Lobato', 'Augusto dos Anjos', 'Graça Aranha'],
    ['Entender o Pré-Modernismo como período de transição', 'Relacionar as obras à Primeira República', 'Reconhecer a denúncia social'],
    ['Que Brasil esses autores mostraram?', 'Policarpo Quaresma era herói ou ingênuo?', 'Os sertões de hoje ainda são esquecidos?'],
    'Leia o trecho "O sertanejo é, antes de tudo, um forte", de Os sertões, e discuta a visão do autor.'))

E('modernismo-1922', 'videoaula', 'Modernismo: a geração de 1922',
  'A Semana de Arte Moderna e a ruptura com o passado: verso livre, humor, linguagem coloquial e a busca de uma identidade brasileira com Mário e Oswald de Andrade.',
  capa('escola', 'estrela', 'Escola literária', 'a partir de 1922'),
  [('Modernismo: 1ª geração', 'WmOICqpg4Rg'), ('Primeira fase do Modernismo', 'ULrYkCAQlHc')],
  ['modernismo', 'literatura-brasileira', 'poesia', 'enem', 'mario-de-andrade'], [N, BE], ano=1922, chamada='Destruir para construir.', pop=90,
  ficha_=ficha('O Modernismo é o período mais cobrado no Enem e conversa diretamente com a cultura brasileira de hoje.',
    ['Semana de Arte Moderna', 'Verso livre', 'Antropofagia', 'Linguagem coloquial', 'Poema-piada', 'Nacionalismo crítico'], ['Mário de Andrade', 'Oswald de Andrade', 'Manuel Bandeira', 'Anita Malfatti', 'Tarsila do Amaral'],
    ['Compreender a ruptura modernista', 'Analisar o Manifesto Antropófago', 'Reconhecer o verso livre e o humor'],
    ['O que significa "devorar" a cultura estrangeira?', 'Por que a Semana de 22 causou tanto escândalo?', 'Que artistas de hoje fazem antropofagia?'],
    'Leia "Pronominais", de Oswald de Andrade, e discuta a diferença entre a norma da escola e a fala do povo.',
    [('Manifesto da turma', 'Em grupos, os alunos escrevem um manifesto de cinco frases sobre a arte que querem ver na escola.')]))

E('geracao-de-30', 'videoaula', 'Modernismo: a geração de 1930',
  'O romance que denuncia a seca, a fome e a desigualdade, com Graciliano Ramos, Rachel de Queiroz e Jorge Amado, e a poesia madura de Drummond, Cecília e Vinicius.',
  capa('escola', 'sertao', 'Escola literária', 'de 1930 a 1945'),
  [('Modernismo: 2ª geração (prosa)', 'YlqUollEjyo'), ('Modernismo: 2ª geração (poesia)', 'PyojY1qM9pU')],
  ['modernismo', 'literatura-brasileira', 'prosa', 'poesia', 'enem', 'graciliano-ramos'], [N], ano=1930, chamada='A literatura que olha para o sertão.', pop=80,
  ficha_=ficha('Une literatura e questões sociais do Brasil, temas centrais da redação e das provas de Linguagens.',
    ['Romance regionalista', 'Denúncia social', 'Seca e migração', 'Poesia reflexiva', 'Engajamento'], ['Graciliano Ramos', 'Rachel de Queiroz', 'Jorge Amado', 'José Lins do Rego', 'Carlos Drummond de Andrade', 'Cecília Meireles'],
    ['Caracterizar o romance de 30', 'Relacionar literatura e realidade social', 'Reconhecer a poesia de Drummond e Cecília'],
    ['Por que a seca virou tema central da literatura?', 'A literatura pode mudar a realidade?', 'O que a família de Fabiano diz sobre o Brasil de hoje?'],
    'Leia o capítulo "Baleia", de Vidas secas, e discuta a humanização da cachorra.'))

E('geracao-de-45', 'videoaula', 'Modernismo: a geração de 1945',
  'A invenção da linguagem: o sertão-mundo de Guimarães Rosa, a introspecção de Clarice Lispector e a poesia construída de João Cabral de Melo Neto.',
  capa('escola', 'olho', 'Escola literária', 'a partir de 1945', COBRE),
  [('Modernismo: 3ª geração (prosa)', 'fUqkhFQvYNE'), ('Modernismo: 3ª geração (poesia)', 'bQiS0HlnuX4'), ('Terceira fase do Modernismo', 'OTuzZKLA2kA')],
  ['modernismo', 'literatura-brasileira', 'prosa', 'poesia', 'clarice-lispector', 'guimaraes-rosa'], [N, BE], ano=1945, chamada='Reinventar a palavra.', pop=78,
  ficha_=ficha('Apresenta três autores que mudaram a língua literária brasileira e aparecem sempre nas provas.',
    ['Experimentação da linguagem', 'Fluxo de consciência', 'Epifania', 'Regionalismo universal', 'Neologismos', 'Poesia objetiva'], ['Guimarães Rosa', 'Clarice Lispector', 'João Cabral de Melo Neto'],
    ['Reconhecer a renovação da linguagem', 'Identificar epifania em contos de Clarice', 'Analisar neologismos de Guimarães Rosa'],
    ['Inventar palavras é permitido na literatura?', 'O que é uma epifania?', 'Por que se diz que o sertão de Rosa é o mundo?'],
    'Leia o conto "Amor", de Clarice Lispector, e localize o momento de epifania de Ana.'))

E('literatura-contemporanea', 'videoaula', 'Literatura Contemporânea',
  'Do fim do Modernismo até hoje: a poesia marginal, a prosa urbana, a literatura negra, indígena e periférica e as novas vozes que estão nas provas.',
  capa('escola', 'cidade', 'Período literário', 'de 1960 até hoje', PRATA),
  [('Literatura contemporânea', 'dWmGwQCl32s'), ('Palavras ancestrais: reflexões sobre literatura indígena', 'uXaKHzroJXs')],
  ['contemporanea', 'literatura-brasileira', 'enem', 'vozes-negras'], [N, TVB], ano=1960, chamada='As vozes de agora.', pop=74,
  ficha_=ficha('Aproxima a literatura da realidade dos alunos e apresenta autores que entraram recentemente nas listas de vestibular.',
    ['Pluralidade de vozes', 'Literatura periférica', 'Escrevivência', 'Poesia marginal', 'Literatura indígena', 'Prosa urbana'], ['Conceição Evaristo', 'Carolina Maria de Jesus', 'Ailton Krenak', 'Paulo Leminski', 'Rubem Fonseca'],
    ['Reconhecer tendências da literatura contemporânea', 'Valorizar vozes antes silenciadas', 'Relacionar literatura e identidade'],
    ['Quem tem direito de contar a própria história?', 'O que é escrevivência?', 'Que autores de hoje deveriam estar nas provas?'],
    'Leia um poema de Conceição Evaristo ou de Leminski e discuta a linguagem e o tema.',
    [('Sarau da turma', 'Organize um sarau com poemas de autores contemporâneos escolhidos pelos alunos.')]))

# ======================= AUTORES =======================
A = lambda *a, **k: add(*a[:2], 'autor', *a[2:], **k)
A('machado-de-assis', 'videoaula', 'Machado de Assis',
  'Neto de escravizados alforriados, menino pobre do Morro do Livramento, fundador da Academia Brasileira de Letras e o maior escritor brasileiro. A vida e a obra de quem inventou a ironia nacional.',
  capa('autor', 'pena', 'Autor', '1839 – 1908'), [('Machado de Assis', 'Q5dtkkUun2I'), ('Realismo no Brasil', 'iCXp_ic4p_E')],
  ['machado-de-assis', 'realismo', 'literatura-brasileira', 'vozes-negras', 'enem'], [BE, N], ano=1839, chamada='O bruxo do Cosme Velho.', pop=94,
  ficha_=ficha('Machado é presença garantida em vestibulares e permite discutir racismo, ascensão social e ironia.',
    ['Ironia', 'Narrador não confiável', 'Análise psicológica', 'Crítica à elite', 'Metalinguagem'], ['Memórias póstumas de Brás Cubas', 'Dom Casmurro', 'Quincas Borba', 'Contos'],
    ['Conhecer a trajetória de Machado de Assis', 'Reconhecer marcas do estilo machadiano', 'Discutir o apagamento da negritude de Machado'],
    ['Por que Machado foi retratado como branco por tanto tempo?', 'O que torna a ironia de Machado tão atual?', 'Capitu traiu Bentinho?'],
    'Leia o conto "Pai contra mãe" e discuta a escravidão no texto.'))

A('clarice-lispector', 'videoaula', 'Clarice Lispector',
  'Nascida na Ucrânia e criada no Recife, Clarice transformou a introspecção em linguagem. Uma aula sobre a autora de A hora da estrela, A paixão segundo G.H. e Laços de família.',
  capa('autor', 'estrela', 'Autora', '1920 – 1977'), [('Literatura Fundamental 63: Clarice Lispector, com Marília Librandi', '267TNFtoxHc'), ('A hora da estrela', 'gt3nX23qmNI')],
  ['clarice-lispector', 'modernismo', 'literatura-brasileira', 'autoras', 'enem'], [U, BE], ano=1920, chamada='Escrever é procurar.', pop=89,
  ficha_=ficha('Clarice é muito cobrada e ensina a ler o que acontece dentro das personagens.',
    ['Fluxo de consciência', 'Epifania', 'Introspecção', 'Metalinguagem', 'Condição feminina'], ['A hora da estrela', 'Laços de família', 'A paixão segundo G.H.', 'Perto do coração selvagem'],
    ['Conhecer a trajetória de Clarice', 'Reconhecer a epifania', 'Ler um conto de Laços de família'],
    ['O que muda quando a ação acontece dentro da personagem?', 'Macabéa existe ainda hoje?', 'Por que Clarice é considerada difícil?'],
    'Leia o conto "Felicidade clandestina" e discuta o desejo da menina pelo livro.'))

A('guimaraes-rosa', 'videoaula', 'Guimarães Rosa',
  'Médico, diplomata e inventor de palavras. Guimarães Rosa fez do sertão de Minas um mundo inteiro em Grande sertão: veredas, Sagarana e Primeiras estórias.',
  capa('autor', 'sertao', 'Autor', '1908 – 1967'), [('Literatura Fundamental 42: Grande sertão: veredas, com Willi Bolle', 'Jcfpbm7owCo'), ('"Campo geral" (1964), de Guimarães Rosa', 'tHZ3SI5LIao')],
  ['guimaraes-rosa', 'modernismo', 'literatura-brasileira', 'enem'], [U, MN], ano=1908, chamada='O sertão é o mundo.', pop=80,
  ficha_=ficha('Rosa mostra como a língua pode ser reinventada, e o sertão como lugar de grandes perguntas humanas.',
    ['Neologismos', 'Regionalismo universal', 'Oralidade', 'Travessia', 'Bem e mal'], ['Grande sertão: veredas', 'Sagarana', 'Primeiras estórias', 'Campo geral'],
    ['Conhecer a obra de Guimarães Rosa', 'Analisar neologismos', 'Ler um conto de Primeiras estórias'],
    ['O que é "viver é muito perigoso"?', 'Por que inventar palavras?', 'O sertão de Rosa existe de verdade?'],
    'Leia "A terceira margem do rio" e discuta o que significa o pai na canoa.'))

A('graciliano-ramos', 'videoaula', 'Graciliano Ramos',
  'Prefeito de Palmeira dos Índios, preso na ditadura Vargas e mestre da frase seca. O autor de Vidas secas, São Bernardo e Angústia.',
  capa('autor', 'sertao', 'Autor', '1892 – 1953', COBRE), [('"Vidas secas" (1938), de Graciliano Ramos: videoaula', 'iDLUv-IHEk8'), ('"Angústia" (1936), de Graciliano Ramos', 'ewNvd8ZfOa8')],
  ['graciliano-ramos', 'modernismo', 'literatura-brasileira', 'prosa', 'enem'], [MN], ano=1892, chamada='Escrever como as lavadeiras de Alagoas.', pop=76,
  ficha_=ficha('Graciliano ensina concisão e permite discutir seca, poder e desigualdade.',
    ['Linguagem seca', 'Denúncia social', 'Análise psicológica', 'Opressão', 'Memória'], ['Vidas secas', 'São Bernardo', 'Angústia', 'Memórias do cárcere'],
    ['Conhecer a vida e a obra de Graciliano', 'Reconhecer a linguagem enxuta', 'Discutir a denúncia social'],
    ['Por que Graciliano corta tanto as palavras?', 'Fabiano tem voz no romance?', 'O que é a "palavra seca"?'],
    'Leia o trecho em que Graciliano compara a escrita ao trabalho das lavadeiras.'))

A('lima-barreto', 'videoaula', 'Lima Barreto',
  'Jornalista, servidor público e escritor negro que expôs o racismo e o ridículo da Primeira República. Autor de Triste fim de Policarpo Quaresma.',
  capa('autor', 'cidade', 'Autor', '1881 – 1922'), [('Lima Barreto', 'O7tA6_gtoQ0'), ('"Triste fim de Policarpo Quaresma" (1915): videoaula', 'hh8-PfGpTTA')],
  ['lima-barreto', 'pre-modernismo', 'literatura-brasileira', 'vozes-negras', 'enem'], [BE, MN], ano=1881, chamada='O cronista do subúrbio.', pop=72,
  ficha_=ficha('Lima Barreto une crítica social, racismo e humor, temas muito presentes no Enem.',
    ['Crítica social', 'Racismo', 'Subúrbio carioca', 'Nacionalismo ingênuo', 'Linguagem jornalística'], ['Triste fim de Policarpo Quaresma', 'Recordações do escrivão Isaías Caminha', 'Clara dos Anjos'],
    ['Conhecer a trajetória de Lima Barreto', 'Relacionar sua obra à Primeira República', 'Discutir o racismo na literatura'],
    ['Por que Lima Barreto ficou tanto tempo esquecido?', 'Policarpo é herói ou louco?', 'O subúrbio aparece nos livros de hoje?'],
    'Leia o requerimento de Policarpo pedindo o tupi como língua oficial.'))

A('carolina-maria-de-jesus', 'documentario', 'Carolina Maria de Jesus',
  'Catadora de papel na favela do Canindé, em São Paulo, Carolina escreveu o diário que virou best-seller mundial em 1960. Uma reportagem sobre a vida e o legado da autora de Quarto de despejo.',
  capa('documentario', 'raiz', 'Documentário', '1914 – 1977'),
  [('Carolina de Jesus é o tema do Caminhos da Reportagem', '4UdObZw8Jjw'), ('"Quarto de despejo: diário de uma favelada" (1960)', 'WYbcq__ObU4')],
  ['carolina-maria-de-jesus', 'contemporanea', 'literatura-brasileira', 'vozes-negras', 'autoras', 'enem'], [TVB, MN], ano=1914, chamada='A fome escrita em diário.', pop=91,
  generos=['Reportagem'],
  ficha_=ficha('Carolina entrou nas listas de vestibular e permite discutir fome, racismo e o direito de escrever.',
    ['Diário', 'Fome', 'Favela', 'Racismo', 'Literatura de testemunho', 'Escrita como resistência'], ['Quarto de despejo', 'Casa de alvenaria', 'Diário de Bitita'],
    ['Conhecer a trajetória de Carolina', 'Ler trechos de Quarto de despejo', 'Discutir quem tem voz na literatura'],
    ['Por que a "cor da fome" é amarela para Carolina?', 'Um diário pode ser literatura?', 'Por que Carolina foi esquecida depois do sucesso?'],
    'Leia o trecho de 15 de julho de 1955, o aniversário da filha Vera Eunice.',
    [('Diário de uma semana', 'Os alunos escrevem um diário de três dias sobre o bairro onde vivem.')]))

A('conceicao-evaristo', 'entrevista', 'Conceição Evaristo',
  'Escritora mineira que criou o conceito de escrevivência: a escrita que nasce da vida das mulheres negras. Ela fala sobre seu processo criativo no Roda Viva.',
  capa('documentario', 'raiz', 'Entrevista', 'nascida em 1946'), [('"Escrevivência": Conceição Evaristo fala sobre seu processo criativo no Roda Viva', 'PppP5_TQjQE')],
  ['conceicao-evaristo', 'contemporanea', 'literatura-brasileira', 'vozes-negras', 'autoras', 'enem'], [RV], ano=1946, chamada='Escrever a partir da própria vida.', pop=86,
  generos=['Entrevista'],
  ficha_=ficha('Conceição Evaristo está entre as autoras mais lidas nas escolas e o conceito de escrevivência rende ótimos debates.',
    ['Escrevivência', 'Memória', 'Mulher negra', 'Ancestralidade', 'Literatura afro-brasileira'], ['Ponciá Vicêncio', 'Olhos d\'água', 'Becos da memória', 'Poemas da recordação'],
    ['Compreender o conceito de escrevivência', 'Conhecer a obra de Conceição Evaristo', 'Relacionar literatura e identidade'],
    ['O que é escrevivência?', 'A experiência de quem escreve muda o que é escrito?', 'Que histórias da sua família mereciam virar livro?'],
    'Leia o poema "Vozes-mulheres" e acompanhe as gerações que aparecem nele.',
    [('Vozes da minha família', 'Inspirados em "Vozes-mulheres", os alunos escrevem um poema com as vozes de três gerações da família.')]))

A('lygia-fagundes-telles', 'entrevista', 'Lygia Fagundes Telles',
  'A dama da literatura brasileira em entrevista ao Roda Viva, em 1997, e duas aulas sobre o romance As meninas e o conto "Eu era mudo e só".',
  capa('documentario', 'flor', 'Entrevista', '1918 – 2022'),
  [('Roda Viva com Lygia Fagundes Telles, em 1997', '1pLcCM5ztN8'), ('"As meninas" (1973): videoaula', '68xmwnwlt-o'), ('"Eu era mudo e só": videoaula', '4TKAlI_AARM')],
  ['lygia-fagundes-telles', 'contemporanea', 'literatura-brasileira', 'autoras', 'prosa'], [RV, MN], ano=1918, chamada='Ouvir a autora.', pop=68,
  generos=['Entrevista'],
  ficha_=ficha('Lygia escreveu sobre o mundo feminino e a ditadura com sutileza, e seus contos são ótimos para aulas curtas.',
    ['Conto psicológico', 'Memória', 'Condição feminina', 'Ditadura', 'Mistério'], ['As meninas', 'Ciranda de pedra', 'Antes do baile verde', 'Seminário dos ratos'],
    ['Conhecer a obra de Lygia', 'Analisar um conto psicológico', 'Relacionar As meninas ao contexto da ditadura'],
    ['O que uma entrevista revela que o livro não mostra?', 'Por que As meninas foi lido como crítica à ditadura?', 'Qual é o mistério de "Venha ver o pôr do sol"?'],
    'Leia o conto "Venha ver o pôr do sol" e peça que a turma preveja o final antes da última página.'))

A('cruz-e-sousa', 'videoaula', 'Cruz e Sousa',
  'Filho de escravizados, nascido em Desterro, hoje Florianópolis, Cruz e Sousa é o maior poeta simbolista brasileiro, o "Cisne Negro".',
  capa('autor', 'lua', 'Autor', '1861 – 1898', PRATA), [('Cruz e Sousa', '_lpDA9i-q9E'), ('Simbolismo no Brasil', 'rVjVUTXHocQ')],
  ['cruz-e-sousa', 'simbolismo', 'literatura-brasileira', 'poesia', 'vozes-negras'], [BE, N], ano=1861, chamada='O Cisne Negro.', pop=58,
  ficha_=ficha('Cruz e Sousa permite discutir racismo e a força da poesia simbolista.',
    ['Musicalidade', 'Sinestesia', 'Dor e transcendência', 'Racismo', 'Emparedado'], ['Broquéis', 'Missal', 'Faróis', 'Últimos sonetos'],
    ['Conhecer a vida de Cruz e Sousa', 'Analisar recursos sonoros', 'Discutir a experiência do racismo em sua obra'],
    ['O que é ser "emparedado"?', 'Como o racismo aparece na poesia de Cruz e Sousa?', 'Por que o branco é tão presente em seus versos?'],
    'Leia um trecho de "Emparedado" e discuta a sensação de prisão que o texto cria.'))

A('olavo-bilac', 'videoaula', 'Olavo Bilac',
  'O Príncipe dos Poetas, mestre do soneto parnasiano e autor da letra do Hino à Bandeira. Uma aula sobre sua vida e obra.',
  capa('autor', 'louro', 'Autor', '1865 – 1918', PRATA), [('Olavo Bilac', '4B3pEL52vk0'), ('Parnasianismo no Brasil', 'JKmrUc1PhuE')],
  ['olavo-bilac', 'parnasianismo', 'literatura-brasileira', 'poesia'], [BE, N], ano=1865, chamada='O Príncipe dos Poetas.', pop=50,
  ficha_=ficha('Bilac é o modelo do soneto parnasiano e ajuda a ensinar métrica.',
    ['Soneto', 'Culto da forma', 'Lirismo amoroso', 'Patriotismo'], ['Poesias', 'Via Láctea', 'Tarde'],
    ['Conhecer Olavo Bilac', 'Analisar um soneto', 'Comparar o Bilac parnasiano e o lírico'],
    ['"Ora (direis) ouvir estrelas!" é um verso racional?', 'Forma perfeita garante emoção?', 'Por que os modernistas atacaram Bilac?'],
    'Leia o soneto XIII de Via Láctea, "Ora (direis) ouvir estrelas!".'))

A('manuel-bandeira', 'videoaula', 'Manuel Bandeira',
  'O poeta do cotidiano, do verso livre e da "vida inteira que podia ter sido e que não foi". Uma aula sobre os poemas mais cobrados.',
  capa('autor', 'estrela', 'Autor', '1886 – 1968'), [('Manuel Bandeira: seleção de poemas', '0jGwgfB2wXc'), ('Modernismo: 1ª geração', 'WmOICqpg4Rg')],
  ['manuel-bandeira', 'modernismo', 'literatura-brasileira', 'poesia', 'enem'], [MN, N], ano=1886, chamada='A poesia do cotidiano.', pop=73,
  ficha_=ficha('Bandeira é acessível, emocionante e presença certa nas provas.',
    ['Verso livre', 'Cotidiano', 'Humor', 'Morte', 'Memória da infância'], ['Libertinagem', 'Estrela da vida inteira', 'Carnaval'],
    ['Conhecer a poesia de Bandeira', 'Reconhecer o verso livre', 'Analisar temas do cotidiano'],
    ['Por que ir embora pra Pasárgada?', 'Um poema pode nascer de uma notícia de jornal?', 'O que é "a vida inteira que podia ter sido"?'],
    'Leia "Poema tirado de uma notícia de jornal" e compare com a notícia original imaginada pela turma.'))

A('cecilia-meireles', 'videoaula', 'Cecília Meireles',
  'Poeta, professora e educadora, Cecília escreveu o Romanceiro da Inconfidência e alguns dos poemas mais musicais da língua portuguesa.',
  capa('autor', 'lua', 'Autora', '1901 – 1964'), [('"Romanceiro da Inconfidência" (1953), de Cecília Meireles', 'C4OSa2ub-6k')],
  ['cecilia-meireles', 'modernismo', 'literatura-brasileira', 'poesia', 'autoras'], [MN], ano=1901, chamada='A poesia que canta.', pop=66,
  ficha_=ficha('Cecília une história e poesia no Romanceiro e escreveu muito para crianças e jovens.',
    ['Musicalidade', 'Efemeridade', 'Espiritualidade', 'Romance histórico em versos'], ['Romanceiro da Inconfidência', 'Viagem', 'Ou isto ou aquilo'],
    ['Conhecer a obra de Cecília', 'Relacionar o Romanceiro à Inconfidência Mineira', 'Analisar a musicalidade'],
    ['Por que contar a Inconfidência em versos?', 'O que é "Ou isto ou aquilo"?', 'A liberdade "ainda que tardia" chegou?'],
    'Leia o "Romance XXIV ou da bandeira da Inconfidência" e discuta a palavra liberdade.'))

A('julia-lopes-de-almeida', 'videoaula', 'Júlia Lopes de Almeida',
  'Uma das escritoras mais lidas do Brasil no início do século XX, ajudou a idealizar a Academia Brasileira de Letras e foi deixada de fora dela por ser mulher. Contos de Ânsia eterna.',
  capa('autor', 'flor', 'Autora', '1862 – 1934', COBRE), [('"As rosas", de Ânsia eterna', 'QW-06Fb8aTw'), ('"O futuro presidente", de Ânsia eterna', 'NzDhbAEHHGM')],
  ['julia-lopes-de-almeida', 'pre-modernismo', 'literatura-brasileira', 'autoras', 'prosa'], [MN], ano=1862, chamada='A escritora esquecida pela Academia.', pop=56,
  ficha_=ficha('Recupera uma autora apagada da história e entrou em listas recentes de vestibular.',
    ['Conto', 'Condição feminina', 'Crítica social', 'Apagamento das autoras'], ['Ânsia eterna', 'A falência', 'Memórias de Marta'],
    ['Conhecer Júlia Lopes de Almeida', 'Analisar contos de Ânsia eterna', 'Discutir o apagamento das mulheres na literatura'],
    ['Por que Júlia ficou de fora da Academia?', 'Quantas autoras você estudou na escola?', 'O que os contos dizem sobre a vida das mulheres da época?'],
    'Leia o conto "A caolha" e discuta a relação entre mãe e filho.'))

A('fernando-pessoa', 'videoaula', 'Fernando Pessoa',
  'Um poeta que era muitos: Alberto Caeiro, Ricardo Reis, Álvaro de Campos e ele mesmo. Uma aula sobre Mensagem, o único livro em português que publicou em vida.',
  capa('autor', 'caravela', 'Autor', '1888 – 1935', PRATA), [('Literatura Fundamental 50: Mensagem, de Fernando Pessoa, com Paola Poma', 'kxEjhpzQz7s')],
  ['fernando-pessoa', 'literatura-portuguesa', 'poesia', 'enem'], [U], ano=1888, chamada='Navegar é preciso.', pop=70,
  ficha_=ficha('Pessoa fascina os alunos com os heterônimos e conversa com Os Lusíadas.',
    ['Heterônimos', 'Fingimento poético', 'Sebastianismo', 'Modernismo português'], ['Mensagem', 'Poemas de Alberto Caeiro', 'Odes de Ricardo Reis', 'Tabacaria'],
    ['Conhecer os heterônimos', 'Analisar poemas de Mensagem', 'Relacionar Mensagem e Os Lusíadas'],
    ['O poeta é um fingidor?', 'É possível ser várias pessoas ao mesmo tempo?', 'O que Portugal buscava em Mensagem?'],
    'Leia "Autopsicografia" e "Mar português" e compare os dois tons.'))

A('jose-de-alencar', 'videoaula', 'José de Alencar',
  'O romancista que quis escrever o Brasil inteiro: o indígena, a cidade, o sertão e a história. Duas aulas sobre seus romances urbanos.',
  capa('autor', 'flor', 'Autor', '1829 – 1877'), [('"A viuvinha" (1857), de José de Alencar', '4Tfgpxwcj6A'), ('"Cinco minutos" (1856), de José de Alencar', 'd8WQFwRRYiA'), ('Romantismo no Brasil: prosa', 'HoaCn9VnY2w')],
  ['jose-de-alencar', 'romantismo', 'literatura-brasileira', 'prosa'], [MN, N], ano=1829, chamada='Escrever o Brasil.', pop=60,
  ficha_=ficha('Alencar é o grande nome da prosa romântica e permite discutir a construção da identidade nacional.',
    ['Romance indianista', 'Romance urbano', 'Romance regionalista', 'Idealização', 'Nacionalismo'], ['Iracema', 'O Guarani', 'Senhora', 'Lucíola', 'A viuvinha'],
    ['Conhecer o projeto literário de Alencar', 'Diferenciar os tipos de romance', 'Analisar a idealização romântica'],
    ['Por que Alencar quis escrever sobre todas as regiões?', 'Iracema é uma personagem ou um símbolo?', 'O romance urbano critica a sociedade?'],
    'Leia o início de Iracema e destaque as comparações com a natureza.'))

# ======================= OBRAS DO VESTIBULAR =======================
O = lambda *a, **k: add(*a[:2], 'obra', *a[2:], **k)
O('dom-casmurro', 'videoaula', 'Dom Casmurro',
  'Bentinho, já velho, tenta "atar as duas pontas da vida" e conta sua história com Capitu. Mas dá para confiar em quem narra? O romance mais discutido da literatura brasileira.',
  capa('obra', 'olho', 'Machado de Assis', '1899'), [('"Dom Casmurro" (1900), de Machado de Assis: videoaula', '5cGtrVxbIvc')],
  ['machado-de-assis', 'realismo', 'literatura-brasileira', 'prosa', 'vestibular', 'enem'], [MN], ano=1899, chamada='Capitu traiu?', pop=97,
  ficha_=ficha('Ensina a desconfiar do narrador e a ler nas entrelinhas, habilidade central nas provas.',
    ['Narrador em primeira pessoa', 'Ciúme', 'Olhos de ressaca', 'Memória', 'Ambiguidade'], ['Bentinho', 'Capitu', 'Escobar', 'José Dias'],
    ['Analisar o narrador não confiável', 'Discutir a ambiguidade do romance', 'Relacionar o ciúme à estrutura do livro'],
    ['Capitu traiu Bentinho?', 'Por que só ouvimos a versão de Bentinho?', 'O que são "olhos de cigana oblíqua e dissimulada"?'],
    'Leia o capítulo "Olhos de ressaca" e discuta como Bentinho descreve Capitu.',
    [('Júri de Capitu', 'Organize um júri simulado: acusação, defesa e jurados, usando só trechos do livro como prova.')]))

O('memorias-postumas', 'videoaula', 'Memórias Póstumas de Brás Cubas',
  'Um defunto autor conta a própria vida com ironia e sem pudor. O romance que inaugurou o Realismo no Brasil e virou a literatura brasileira de cabeça para baixo.',
  capa('obra', 'pena', 'Machado de Assis', '1881'), [('"Memórias póstumas de Brás Cubas" (1881), de Machado de Assis', '1ECclj4j8Ms')],
  ['machado-de-assis', 'realismo', 'literatura-brasileira', 'prosa', 'vestibular', 'enem'], [MN], ano=1881, chamada='Ao verme que primeiro roeu as frias carnes.', pop=93,
  ficha_=ficha('Mostra a ironia de Machado contra a elite e a estrutura inovadora do romance.',
    ['Defunto autor', 'Ironia', 'Metalinguagem', 'Crítica à elite', 'Capítulos curtos', 'Pessimismo'], ['Brás Cubas', 'Virgília', 'Quincas Borba', 'Eugênia', 'Prudêncio'],
    ['Analisar o narrador defunto', 'Reconhecer a crítica à elite escravocrata', 'Identificar a metalinguagem'],
    ['Por que o narrador está morto?', 'O que a cena de Prudêncio revela sobre a escravidão?', 'O que significa "não tive filhos, não transmiti a nenhuma criatura o legado da nossa miséria"?'],
    'Leia o capítulo "O vergalho", em que Prudêncio, já livre, bate em um escravizado.'))

O('vidas-secas', 'videoaula', 'Vidas Secas',
  'Fabiano, Sinhá Vitória, os meninos e a cachorra Baleia fogem da seca pelo sertão. Um romance em capítulos que quase se leem sozinhos, sobre fome, silêncio e dignidade.',
  capa('obra', 'sertao', 'Graciliano Ramos', '1938', COBRE), [('"Vidas secas" (1938), de Graciliano Ramos: videoaula', 'iDLUv-IHEk8')],
  ['graciliano-ramos', 'modernismo', 'literatura-brasileira', 'prosa', 'vestibular', 'enem'], [MN], ano=1938, chamada='A seca que cala.', pop=92,
  ficha_=ficha('Une literatura e questão social e é uma das obras mais cobradas no Enem.',
    ['Romance desmontável', 'Seca', 'Animalização', 'Opressão', 'Linguagem e poder', 'Ciclo'], ['Fabiano', 'Sinhá Vitória', 'Baleia', 'Soldado amarelo'],
    ['Analisar a estrutura em capítulos', 'Discutir a falta de linguagem como forma de opressão', 'Relacionar a obra ao contexto da seca'],
    ['Por que Fabiano tem dificuldade de falar?', 'Baleia é mais humana que os humanos?', 'O final é de esperança ou de repetição?'],
    'Leia o capítulo "Baleia" em voz alta com a turma.',
    [('Capítulo perdido', 'Os alunos escrevem um capítulo novo do ponto de vista de um dos meninos.')]))

O('triste-fim-de-policarpo-quaresma', 'videoaula', 'Triste Fim de Policarpo Quaresma',
  'O major Quaresma ama tanto o Brasil que propõe o tupi como língua oficial, tenta salvar a agricultura e defende o governo de Floriano. O patriotismo ingênuo diante de um país cruel.',
  capa('obra', 'cidade', 'Lima Barreto', '1915'), [('"Triste fim de Policarpo Quaresma" (1915), de Lima Barreto: videoaula', 'hh8-PfGpTTA')],
  ['lima-barreto', 'pre-modernismo', 'literatura-brasileira', 'prosa', 'vestibular', 'enem'], [MN], ano=1915, chamada='O patriota que o Brasil não quis.', pop=79,
  ficha_=ficha('Discute nacionalismo, poder e crítica social com humor e tragédia.',
    ['Nacionalismo ingênuo', 'Crítica à República', 'Ironia', 'Loucura', 'Subúrbio'], ['Policarpo Quaresma', 'Olga', 'Ricardo Coração dos Outros', 'Floriano Peixoto'],
    ['Analisar as três partes do romance', 'Discutir o nacionalismo de Policarpo', 'Relacionar a obra à Revolta da Armada'],
    ['Amar o país pode ser perigoso?', 'Por que o fim de Policarpo é "triste"?', 'Quem são os Policarpos de hoje?'],
    'Leia o requerimento ao Congresso pedindo o tupi como língua oficial.'))

O('capitaes-da-areia', 'videoaula', 'Capitães da Areia',
  'Pedro Bala, Professor, Sem-Pernas, Volta Seca e Dora: meninos abandonados que vivem num trapiche de Salvador. Um romance sobre infância, injustiça e liberdade.',
  capa('obra', 'caravela', 'Jorge Amado', '1937'), [('"Capitães da areia" (1937), de Jorge Amado', 'q_yLZmXOOjs')],
  ['jorge-amado', 'modernismo', 'literatura-brasileira', 'prosa', 'vestibular'], [MN], ano=1937, chamada='Os meninos do trapiche.', pop=83,
  ficha_=ficha('Os alunos se identificam com os personagens e o livro abre debate sobre infância e direitos.',
    ['Infância abandonada', 'Denúncia social', 'Coletivo', 'Liberdade', 'Religiosidade popular'], ['Pedro Bala', 'Professor', 'Sem-Pernas', 'Dora', 'Volta Seca'],
    ['Analisar a denúncia social do romance', 'Discutir o destino de cada personagem', 'Relacionar a obra ao contexto de 1937'],
    ['Os Capitães da Areia são vítimas ou culpados?', 'Por que o livro foi queimado em praça pública em 1937?', 'O que mudou para as crianças de rua desde então?'],
    'Leia o capítulo do carrossel e discuta a infância que os meninos não tiveram.'))

O('auto-da-barca-do-inferno', 'videoaula', 'Auto da Barca do Inferno',
  'Num cais, o Diabo e o Anjo recebem as almas: fidalgo, onzeneiro, frade, sapateiro, alcoviteira. Quem vai para o inferno? O teatro de Gil Vicente que ri dos poderosos.',
  capa('obra', 'mascara', 'Gil Vicente', '1517', COBRE),
  [('"Auto da barca do inferno" (1517), de Gil Vicente: videoaula', 'Yg8P9y14EDk'), ('Auto da Barca do Inferno: análise (parte 1)', 'bPLRdHTs2_I'), ('Auto da Barca do Inferno: análise (parte 2)', 'var6khRpGAA')],
  ['gil-vicente', 'humanismo', 'literatura-portuguesa', 'teatro', 'vestibular'], [MN, AA], ano=1517, chamada='Embarca, que é tarde!', pop=81,
  ficha_=ficha('É curto, engraçado e perfeito para encenar em sala.',
    ['Auto', 'Alegoria', 'Personagens-tipo', 'Crítica social', 'Moral cristã'], ['Diabo', 'Anjo', 'Fidalgo', 'Onzeneiro', 'Parvo', 'Frade'],
    ['Identificar a crítica a cada personagem', 'Reconhecer a alegoria', 'Encenar uma cena'],
    ['Por que o Parvo vai para o céu?', 'O que cada personagem leva para a barca?', 'Quem seria julgado hoje?'],
    'Leia a cena do Onzeneiro e discuta o que ele representa.',
    [('Barca de hoje', 'Em grupos, os alunos escrevem e encenam a chegada de um personagem atual à barca.')]))

O('auto-da-compadecida', 'videoaula', 'Auto da Compadecida',
  'João Grilo e Chicó enganam padre, bispo e patrão no sertão da Paraíba, até o julgamento final diante da Compadecida. A peça de Ariano Suassuna que une Gil Vicente e o cordel.',
  capa('obra', 'mascara', 'Ariano Suassuna', '1955'), [('"Auto da Compadecida" (1955), de Ariano Suassuna', 'Fea295nM0o0')],
  ['ariano-suassuna', 'modernismo', 'literatura-brasileira', 'teatro', 'vestibular'], [MN], ano=1955, chamada='Não sei, só sei que foi assim.', pop=87,
  ficha_=ficha('É popular, engraçado e dialoga com o Auto da Barca, o que permite comparar épocas.',
    ['Teatro popular', 'Cordel', 'Crítica à Igreja e aos poderosos', 'Esperteza', 'Julgamento final'], ['João Grilo', 'Chicó', 'Padre João', 'A Compadecida', 'Manuel'],
    ['Reconhecer a influência do cordel e do auto medieval', 'Analisar a crítica social', 'Comparar com o Auto da Barca do Inferno'],
    ['João Grilo é herói ou malandro?', 'O que a peça diz sobre os pobres e os ricos?', 'Por que a Compadecida intercede por João?'],
    'Leia a cena do enterro da cachorra e discuta como a peça critica a Igreja.'))

O('a-hora-da-estrela', 'videoaula', 'A Hora da Estrela',
  'Rodrigo S.M. tenta contar a história de Macabéa, nordestina pobre no Rio de Janeiro que "não sabia que era infeliz". O último livro publicado em vida por Clarice Lispector.',
  capa('obra', 'estrela', 'Clarice Lispector', '1977'), [('A hora da estrela', 'gt3nX23qmNI'), ('"A hora da estrela", de Clarice Lispector: análise', 'vLWb2tLJjRo')],
  ['clarice-lispector', 'modernismo', 'literatura-brasileira', 'prosa', 'vestibular', 'enem', 'autoras'], [BE], ano=1977, chamada='Ela não sabia que era infeliz.', pop=95,
  ficha_=ficha('Discute migração, invisibilidade social e o próprio ato de escrever.',
    ['Metalinguagem', 'Narrador-personagem', 'Migração nordestina', 'Invisibilidade', 'Epifania'], ['Macabéa', 'Rodrigo S.M.', 'Olímpico de Jesus', 'Glória', 'Madama Carlota'],
    ['Analisar o narrador Rodrigo S.M.', 'Discutir a invisibilidade de Macabéa', 'Reconhecer a metalinguagem'],
    ['Por que Clarice cria um narrador homem?', 'Macabéa é feliz?', 'Quem são as Macabéas de hoje?'],
    'Leia o diálogo entre Macabéa e Olímpico sobre a Rádio Relógio.'))

O('grande-sertao-veredas', 'videoaula', 'Grande Sertão: Veredas',
  'Riobaldo, ex-jagunço, conta a um ouvinte sua travessia pelo sertão, o pacto com o diabo e o amor por Diadorim. A obra-prima de Guimarães Rosa, comentada por Willi Bolle.',
  capa('obra', 'sertao', 'Guimarães Rosa', '1956'), [('Literatura Fundamental 42: Grande sertão: veredas, com Willi Bolle', 'Jcfpbm7owCo')],
  ['guimaraes-rosa', 'modernismo', 'literatura-brasileira', 'prosa', 'vestibular'], [U], ano=1956, chamada='Viver é muito perigoso.', pop=77,
  ficha_=ficha('Um livro gigante que pode ser apresentado por trechos e perguntas, sem medo.',
    ['Travessia', 'Pacto com o diabo', 'Bem e mal', 'Oralidade', 'Neologismos', 'Amor proibido'], ['Riobaldo', 'Diadorim', 'Zé Bebelo', 'Hermógenes', 'Joca Ramiro'],
    ['Conhecer a estrutura do romance', 'Analisar a linguagem de Rosa', 'Discutir os grandes temas da obra'],
    ['O diabo existe?', 'Por que Riobaldo conta a história a um ouvinte que nunca fala?', 'O que é a travessia?'],
    'Leia a abertura "Nonada. Tiros que o senhor ouviu foram de briga de homem não" e discuta a oralidade.'))

O('mensagem', 'videoaula', 'Mensagem',
  'Os 44 poemas em que Fernando Pessoa reconta a história de Portugal, dos heróis à espera de D. Sebastião. O único livro em português publicado pelo poeta em vida.',
  capa('obra', 'caravela', 'Fernando Pessoa', '1934', PRATA), [('Literatura Fundamental 50: Mensagem, de Fernando Pessoa, com Paola Poma', 'kxEjhpzQz7s')],
  ['fernando-pessoa', 'literatura-portuguesa', 'poesia', 'vestibular'], [U], ano=1934, chamada='Tudo vale a pena se a alma não é pequena.', pop=69,
  ficha_=ficha('Permite comparar a épica de Camões com a visão moderna e mítica de Pessoa.',
    ['Sebastianismo', 'Mito', 'Quinto Império', 'Épica fragmentária', 'Simbolismo'], ['D. Sebastião', 'Infante D. Henrique', 'Ulisses', 'O Mostrengo'],
    ['Conhecer a estrutura de Mensagem', 'Analisar "Mar português"', 'Comparar com Os Lusíadas'],
    ['Valeu a pena?', 'O que é o sebastianismo?', 'Por que transformar a história em mito?'],
    'Leia "Mar português" e "O mostrengo" e discuta o medo e a coragem.'))

O('quarto-de-despejo', 'documentario', 'Quarto de Despejo',
  'O diário de Carolina Maria de Jesus na favela do Canindé, entre 1955 e 1960: a fome, os filhos, o lixo, a política e a escrita como forma de sobreviver.',
  capa('obra', 'raiz', 'Carolina Maria de Jesus', '1960'),
  [('"Quarto de despejo: diário de uma favelada" (1960): videoaula', 'WYbcq__ObU4'), ('Carolina de Jesus é o tema do Caminhos da Reportagem', '4UdObZw8Jjw')],
  ['carolina-maria-de-jesus', 'contemporanea', 'literatura-brasileira', 'prosa', 'vestibular', 'enem', 'vozes-negras', 'autoras'], [MN, TVB], ano=1960, chamada='A fome tem cor.', pop=90,
  ficha_=ficha('É uma das obras mais importantes para discutir desigualdade e está nas listas de vestibulares recentes.',
    ['Diário', 'Fome', 'Favela', 'Literatura de testemunho', 'Racismo', 'Maternidade'], ['Carolina', 'Vera Eunice', 'João José', 'José Carlos'],
    ['Ler trechos do diário', 'Discutir a desigualdade retratada', 'Reconhecer o valor literário do testemunho'],
    ['Por que a favela é o "quarto de despejo" da cidade?', 'O que muda quando quem escreve vive o que conta?', 'A fome ainda existe no Brasil?'],
    'Leia o trecho sobre a "cor da fome" e discuta a metáfora.'))

O('romanceiro-da-inconfidencia', 'videoaula', 'Romanceiro da Inconfidência',
  'Em 85 romances em versos, Cecília Meireles reconta a Inconfidência Mineira, de Tiradentes às vozes anônimas de Vila Rica.',
  capa('obra', 'louro', 'Cecília Meireles', '1953', COBRE), [('"Romanceiro da Inconfidência" (1953), de Cecília Meireles', 'C4OSa2ub-6k')],
  ['cecilia-meireles', 'modernismo', 'literatura-brasileira', 'poesia', 'vestibular', 'autoras'], [MN], ano=1953, chamada='Liberdade, ainda que tarde.', pop=63,
  ficha_=ficha('Une história e poesia e mostra o lado humano da Inconfidência.',
    ['Romance em versos', 'Memória histórica', 'Liberdade', 'Musicalidade', 'Vozes anônimas'], ['Tiradentes', 'Tomás Antônio Gonzaga', 'Marília', 'Chica da Silva'],
    ['Relacionar o Romanceiro à história', 'Analisar a musicalidade', 'Discutir a ideia de liberdade'],
    ['Por que contar a Inconfidência em versos?', 'Quem são os heróis do Romanceiro?', 'O que a palavra liberdade significa no livro?'],
    'Leia o "Romance XXIV ou da bandeira da Inconfidência".'))

O('campo-geral', 'videoaula', 'Campo Geral',
  'Miguilim, menino míope do sertão do Mutum, descobre o mundo, a família e a perda. A novela mais delicada de Guimarães Rosa.',
  capa('obra', 'olho', 'Guimarães Rosa', '1964'), [('"Campo geral" (1964), de Guimarães Rosa', 'tHZ3SI5LIao')],
  ['guimaraes-rosa', 'modernismo', 'literatura-brasileira', 'prosa', 'vestibular'], [MN], ano=1964, chamada='O mundo pelos olhos de Miguilim.', pop=67,
  ficha_=ficha('Uma porta de entrada para Guimarães Rosa, mais curta e muito emocionante.',
    ['Infância', 'Olhar', 'Sertão', 'Perda', 'Linguagem poética'], ['Miguilim', 'Dito', 'Mãe', 'Pai', 'Doutor'],
    ['Analisar o ponto de vista infantil', 'Discutir o simbolismo dos óculos', 'Ler a linguagem de Rosa'],
    ['O que muda quando Miguilim põe os óculos?', 'O Mutum é bonito?', 'Como a infância aparece na literatura?'],
    'Leia a cena final em que Miguilim experimenta os óculos do doutor.'))

O('as-meninas', 'videoaula', 'As Meninas',
  'Lorena, Lia e Ana Clara vivem num pensionato de freiras em São Paulo, durante a ditadura. Três vozes, três destinos e um país em silêncio.',
  capa('obra', 'flor', 'Lygia Fagundes Telles', '1973'), [('"As meninas" (1973), de Lygia Fagundes Telles', '68xmwnwlt-o')],
  ['lygia-fagundes-telles', 'contemporanea', 'literatura-brasileira', 'prosa', 'vestibular', 'autoras'], [MN], ano=1973, chamada='Três meninas e um país calado.', pop=65,
  ficha_=ficha('Permite discutir ditadura, juventude e foco narrativo múltiplo.',
    ['Foco narrativo múltiplo', 'Fluxo de consciência', 'Ditadura', 'Juventude', 'Condição feminina'], ['Lorena', 'Lia', 'Ana Clara'],
    ['Analisar as três vozes', 'Relacionar o romance à ditadura', 'Reconhecer o fluxo de consciência'],
    ['Como cada menina reage ao mundo?', 'Por que o livro passou pela censura?', 'O que as três têm em comum?'],
    'Leia o trecho do relato de tortura e discuta como ele aparece no romance.'))

O('inocencia', 'videoaula', 'Inocência',
  'No sertão de Mato Grosso, o falso médico Cirino se apaixona por Inocência, prometida pelo pai a outro homem. O romance regionalista romântico de Visconde de Taunay.',
  capa('obra', 'flor', 'Visconde de Taunay', '1872', COBRE), [('"Inocência" (1872), de Visconde de Taunay', '46SMxCghR3w')],
  ['romantismo', 'literatura-brasileira', 'prosa', 'vestibular'], [MN], ano=1872, chamada='Amor no sertão.', pop=48,
  ficha_=ficha('Mostra o regionalismo romântico e o poder patriarcal.',
    ['Regionalismo romântico', 'Patriarcalismo', 'Amor impossível', 'Descrição da paisagem'], ['Inocência', 'Cirino', 'Pereira', 'Manecão', 'Meyer'],
    ['Reconhecer o regionalismo romântico', 'Discutir o casamento arranjado', 'Analisar a paisagem do sertão'],
    ['Inocência tinha escolha?', 'Como o sertão é descrito?', 'O que o naturalista Meyer representa?'],
    'Leia a descrição do sertão no primeiro capítulo.'))

O('a-moreninha', 'videoaula', 'A Moreninha',
  'Augusto aposta que não vai se apaixonar durante um fim de semana numa ilha e encontra Carolina. O primeiro grande sucesso do romance brasileiro.',
  capa('obra', 'flor', 'Joaquim Manuel de Macedo', '1844'), [('"A moreninha" (1844), de Joaquim Manuel de Macedo', 'U7bEDfYEMyY')],
  ['romantismo', 'literatura-brasileira', 'prosa', 'vestibular'], [MN], ano=1844, chamada='Uma aposta e um amor.', pop=57,
  ficha_=ficha('Mostra o romance urbano romântico e os costumes da elite carioca.',
    ['Romance urbano', 'Idealização', 'Folhetim', 'Costumes da elite'], ['Augusto', 'Carolina', 'Filipe', 'D. Ana'],
    ['Reconhecer o romance romântico urbano', 'Discutir a idealização amorosa', 'Analisar os costumes da época'],
    ['O amor é uma aposta?', 'Como a mulher aparece no romance?', 'O que o livro mostra da elite carioca?'],
    'Leia o capítulo da lenda da ilha e discuta seu papel na trama.'))

O('angustia', 'videoaula', 'Angústia',
  'Luís da Silva, funcionário público humilhado, narra sua obsessão por Marina e o ódio por Julião Tavares. O mergulho psicológico mais sombrio de Graciliano Ramos.',
  capa('obra', 'cidade', 'Graciliano Ramos', '1936'), [('"Angústia" (1936), de Graciliano Ramos', 'ewNvd8ZfOa8')],
  ['graciliano-ramos', 'modernismo', 'literatura-brasileira', 'prosa', 'vestibular'], [MN], ano=1936, chamada='Uma mente em ruína.', pop=54,
  ficha_=ficha('Mostra o lado psicológico da geração de 30.',
    ['Romance psicológico', 'Fluxo de consciência', 'Ressentimento', 'Classe social'], ['Luís da Silva', 'Marina', 'Julião Tavares'],
    ['Analisar o narrador perturbado', 'Discutir classe social e ressentimento', 'Comparar com Vidas secas'],
    ['O que leva Luís à angústia?', 'O narrador é confiável?', 'Como a cidade aparece no romance?'],
    'Leia as primeiras páginas e discuta o estado mental do narrador.'))

O('boca-do-inferno', 'videoaula', 'Boca do Inferno',
  'Salvador, 1683: um assassinato mergulha a cidade em intrigas, e no meio delas estão Gregório de Matos e o Padre Antônio Vieira. O romance histórico de Ana Miranda.',
  capa('obra', 'barroco', 'Ana Miranda', '1989'), [('"Boca do Inferno" (1989), de Ana Miranda', 'DG7m5R1Lr6A'), ('Barroco no Brasil', '1FN2jCxgnt0')],
  ['barroco', 'contemporanea', 'literatura-brasileira', 'prosa', 'vestibular', 'autoras'], [MN, N], ano=1989, chamada='O Barroco vira romance.', pop=55,
  ficha_=ficha('Une Barroco e literatura contemporânea num romance de suspense.',
    ['Romance histórico', 'Barroco', 'Intriga política', 'Sátira'], ['Gregório de Matos', 'Padre Antônio Vieira', 'Antônio de Souza de Menezes'],
    ['Relacionar o romance ao Barroco', 'Discutir romance histórico', 'Conhecer Gregório de Matos'],
    ['Por que Gregório era chamado de Boca do Inferno?', 'Romance histórico é história ou ficção?', 'A Salvador de 1683 lembra o Brasil de hoje?'],
    'Leia um poema satírico de Gregório de Matos citado no romance.'))

O('sermao-da-sexagesima', 'videoaula', 'Sermão da Sexagésima',
  'Na Capela Real de Lisboa, em 1655, o Padre Antônio Vieira pergunta por que a palavra de Deus não dá fruto. Uma aula de argumentação barroca.',
  capa('obra', 'barroco', 'Padre Antônio Vieira', '1655', COBRE), [('"Sermão da Sexagésima", do Padre Antônio Vieira: análise', 'egh2tDx-JMw')],
  ['barroco', 'literatura-portuguesa', 'literatura-brasileira', 'vestibular'], [MN], ano=1655, chamada='Semear a palavra.', pop=52,
  ficha_=ficha('Ótimo para ensinar argumentação e conceptismo, útil também para a redação.',
    ['Conceptismo', 'Argumentação', 'Metalinguagem', 'Alegoria do semeador'], ['Padre Antônio Vieira'],
    ['Analisar a estrutura argumentativa do sermão', 'Reconhecer o conceptismo', 'Relacionar com a redação dissertativa'],
    ['Por que a palavra não dá fruto, segundo Vieira?', 'Um sermão pode ensinar a argumentar?', 'Quem são os "pregadores" de hoje?'],
    'Leia o trecho sobre o semeador e o pregador e identifique os argumentos.'))

O('contos-gauchescos', 'videoaula', 'Contos Gauchescos',
  'Blau Nunes, velho vaqueano, conta histórias do pampa gaúcho com a fala da região. Simões Lopes Neto e o regionalismo do Sul.',
  capa('obra', 'sol', 'Simões Lopes Neto', '1912', COBRE), [('"Duelo de farrapos", de Contos gauchescos', 'vzcXk-eNEpg')],
  ['pre-modernismo', 'literatura-brasileira', 'prosa', 'vestibular'], [MN], ano=1912, chamada='Histórias do pampa.', pop=46,
  ficha_=ficha('Mostra o regionalismo do Sul e a força da oralidade.',
    ['Regionalismo', 'Narrador oral', 'Pampa', 'Linguagem regional'], ['Blau Nunes'],
    ['Reconhecer o regionalismo sulista', 'Analisar o narrador oral', 'Comparar com o regionalismo nordestino'],
    ['Como a fala do narrador aparece no texto?', 'O que é ser gaúcho nos contos?', 'Regionalismo é coisa do passado?'],
    'Leia "O negro Bonifácio" ou "Trezentas onças" e marque as palavras regionais.'))

# ======================= LITERATURA UNIVERSAL (Univesp) =======================
def UNI(slug, titulo, autor, ano, vid, nome, sinopse, motif, pop=50):
    add(slug, 'videoaula', 'universal', titulo, sinopse, capa('universal', motif, autor, str(ano) if ano > 0 else 'Antiguidade', PRATA if pop % 2 else OURO),
        [(f'Literatura Fundamental: {titulo}, com {nome}', vid)], ['literatura-universal', 'classicos'], [U], ano=ano, pop=pop)
UNI('1984', '1984', 'George Orwell', 1949, 'VL-sjRG4aC0', 'Mayumi Ilari', 'O Grande Irmão vigia tudo, a história é reescrita e a linguagem é reduzida para impedir o pensamento. A distopia que se tornou vocabulário do mundo.', 'olho', 75)
UNI('o-processo', 'O Processo', 'Franz Kafka', 1925, 'mVCYpeaff_4', 'Celeste H. M. Ribeiro de Sousa', 'Josef K. é preso sem saber por quê e enfrenta uma justiça que não se explica. O romance que deu nome ao "kafkiano".', 'cidade', 64)
UNI('o-estrangeiro', 'O Estrangeiro', 'Albert Camus', 1942, 'WWKrFF-54i0', 'Cláudia Amigo Pino', 'Meursault não chora no enterro da mãe e mata um homem numa praia da Argélia. Um romance sobre o absurdo e a indiferença.', 'sol', 62)
UNI('as-flores-do-mal', 'As Flores do Mal', 'Charles Baudelaire', 1857, 'nM-z2vcjFWY', 'Álvaro Faleiros', 'A poesia que encontrou beleza na cidade, no tédio e no mal. Baudelaire inventa a lírica moderna e influencia o Simbolismo.', 'flor', 58)
UNI('guerra-e-paz', 'Guerra e Paz', 'Liev Tolstói', 1869, 'iIbM0FobowE', 'Aurora Bernardini', 'Famílias russas atravessam as guerras napoleônicas. Um dos maiores romances já escritos, sobre história, destino e amor.', 'louro', 57)
UNI('pedro-paramo', 'Pedro Páramo', 'Juan Rulfo', 1955, '_J4YPNxQN_U', 'Laura Hossiasson', 'Juan Preciado vai a Comala procurar o pai e encontra uma cidade de mortos que ainda falam. A obra que abriu caminho para o realismo mágico.', 'lua', 55)
UNI('o-apanhador-no-campo-de-centeio', 'O Apanhador no Campo de Centeio', 'J. D. Salinger', 1951, 'xNP5pBs9tGU', 'Maria Elisa Cevasco', 'Holden Caulfield foge da escola e vaga por Nova York. O romance que deu voz à adolescência.', 'cidade', 61)
UNI('teogonia', 'Teogonia', 'Hesíodo', -700, 'tHlJrpJxh5s', 'JAA Torrano', 'O poema grego que conta o nascimento do mundo e dos deuses, do Caos a Zeus. Base para entender mito e literatura.', 'sol', 53)
UNI('o-som-e-a-furia', 'O Som e a Fúria', 'William Faulkner', 1929, 'mSUjdRgOhnE', 'Munira Mutran', 'A decadência da família Compson contada por vozes diferentes, inclusive a de Benjy. Um marco do fluxo de consciência.', 'olho', 49)
UNI('um-bonde-chamado-desejo', 'Um Bonde Chamado Desejo', 'Tennessee Williams', 1947, 'X8lWpluLR-4', 'Maria Silvia Betti', 'Blanche DuBois chega à casa da irmã em Nova Orleans e se choca com Stanley Kowalski. Teatro sobre ilusão e violência.', 'mascara', 51)
UNI('contos-de-andersen', 'Contos de Andersen', 'Hans Christian Andersen', 1835, 'sTDF0YtWRO4', 'Karin Volobuef', 'A pequena sereia, O patinho feio, A roupa nova do imperador: os contos que atravessaram gerações.', 'estrela', 60)
UNI('tristram-shandy', 'A Vida e as Opiniões do Cavalheiro Tristram Shandy', 'Laurence Sterne', 1759, 'BMqrz2rLrkY', 'professores da Univesp', 'Um narrador que nunca consegue contar a própria vida em ordem. O livro que inspirou Machado de Assis em Memórias póstumas.', 'pena', 59)
UNI('cancoes-da-inocencia', 'Canções da Inocência e da Experiência', 'William Blake', 1789, 'X1NmE7zt0qw', 'José Garcez', 'Poemas em dois estados da alma: a inocência da infância e a experiência do mundo. A força visionária de Blake.', 'flor', 47)

# ======================= TRILHAS =======================
def TR(slug, titulo, chamada, sinopse, motif, eps, temas, fontes, pop):
    add(slug, 'serie', 'trilha', titulo, sinopse, capa('trilha', motif, f'Trilha · {len(eps)} episódios'), [(f'Episódio {k + 1}: {t}', i) for k, (t, i) in enumerate(eps)], temas + ['trilhas'], fontes, chamada=chamada, pop=pop, generos=['Trilha de conteúdo'])
TR('trilha-escolas-literarias', 'Escolas Literárias do Zero', 'Do Trovadorismo à literatura de hoje, em ordem.',
   'Uma temporada inteira sobre as escolas literárias, na ordem em que aconteceram. Ideal para o 1º ao 3º ano e para revisar antes do Enem.', 'livro',
   [('Linha do tempo das escolas literárias', 'WGZFBePibF0'), ('Trovadorismo', 'N8aCwmWgVyA'), ('Humanismo', 'TaiiIil8-Ow'), ('Quinhentismo', 'WULOzFYZ30g'), ('Classicismo', 'yUx7vExUi4k'),
    ('Barroco no Brasil', '1FN2jCxgnt0'), ('Arcadismo no Brasil', 'leb7oRjtsO8'), ('Romantismo: poesia', 'M7okFxuX8fM'), ('Romantismo: prosa', 'HoaCn9VnY2w'), ('Realismo', 'iCXp_ic4p_E'),
    ('Naturalismo', '0ca0bBqnxE4'), ('Parnasianismo', 'JKmrUc1PhuE'), ('Simbolismo', 'rVjVUTXHocQ'), ('Pré-Modernismo', 'UBxq1C4jVLE'), ('Modernismo: 1ª geração', 'WmOICqpg4Rg'),
    ('Modernismo: 2ª geração (prosa)', 'YlqUollEjyo'), ('Modernismo: 3ª geração (prosa)', 'fUqkhFQvYNE'), ('Literatura contemporânea', 'dWmGwQCl32s')],
   ['enem', 'literatura-brasileira'], [N, BE], 99)
TR('trilha-machado-de-assis', 'Machado de Assis', 'O bruxo do Cosme Velho em oito episódios.',
   'A vida, o Realismo, os dois romances mais cobrados e quatro contos para ler em sala.', 'pena',
   [('Machado de Assis', 'Q5dtkkUun2I'), ('Realismo no Brasil', 'iCXp_ic4p_E'), ('Memórias póstumas de Brás Cubas', '1ECclj4j8Ms'), ('Dom Casmurro', '5cGtrVxbIvc'),
    ('Missa do galo', 'MJUGbmIOy5g'), ('Mariana', 'NyzXAU5VHT0'), ('Verba testamentária', 'AFCwwaVQtng'), ('Fernando e Fernanda', 'WsOtiGjUX68')],
   ['machado-de-assis', 'realismo', 'vestibular'], [BE, N, MN], 96)
TR('trilha-modernismo', 'Modernismo Brasileiro', 'De 1922 a Guimarães Rosa.',
   'As três gerações modernistas, com as obras que mais caem: Vidas secas, A hora da estrela e Grande sertão: veredas.', 'estrela',
   [('Pré-Modernismo', 'UBxq1C4jVLE'), ('Modernismo: 1ª geração', 'WmOICqpg4Rg'), ('Manuel Bandeira: poemas', '0jGwgfB2wXc'), ('Modernismo: 2ª geração (poesia)', 'PyojY1qM9pU'),
    ('Modernismo: 2ª geração (prosa)', 'YlqUollEjyo'), ('Vidas secas', 'iDLUv-IHEk8'), ('Modernismo: 3ª geração (poesia)', 'bQiS0HlnuX4'), ('Modernismo: 3ª geração (prosa)', 'fUqkhFQvYNE'),
    ('A hora da estrela', 'gt3nX23qmNI'), ('Grande sertão: veredas', 'Jcfpbm7owCo')],
   ['modernismo', 'enem'], [N, MN, BE, U], 95)
TR('trilha-vozes-negras', 'Vozes Negras na Literatura', 'De Cruz e Sousa a Conceição Evaristo.',
   'Autores negros que mudaram a literatura brasileira, para trabalhar a Lei 10.639 com obras que estão nas provas.', 'raiz',
   [('Cruz e Sousa', '_lpDA9i-q9E'), ('Machado de Assis', 'Q5dtkkUun2I'), ('Lima Barreto', 'O7tA6_gtoQ0'), ('Triste fim de Policarpo Quaresma', 'hh8-PfGpTTA'),
    ('Carolina de Jesus no Caminhos da Reportagem', '4UdObZw8Jjw'), ('Quarto de despejo', 'WYbcq__ObU4'), ('Conceição Evaristo no Roda Viva', 'PppP5_TQjQE')],
   ['vozes-negras', 'enem'], [BE, MN, TVB, RV], 94)
TR('trilha-elas-escrevem', 'Elas Escrevem', 'Autoras que a escola demorou a ler.',
   'De Júlia Lopes de Almeida a Conceição Evaristo: a literatura brasileira escrita por mulheres.', 'flor',
   [('Júlia Lopes de Almeida: "As rosas"', 'QW-06Fb8aTw'), ('Cecília Meireles: Romanceiro da Inconfidência', 'C4OSa2ub-6k'), ('Clarice Lispector', '267TNFtoxHc'), ('A hora da estrela', 'gt3nX23qmNI'),
    ('Lygia Fagundes Telles no Roda Viva', '1pLcCM5ztN8'), ('As meninas', '68xmwnwlt-o'), ('Carolina de Jesus no Caminhos da Reportagem', '4UdObZw8Jjw'), ('Conceição Evaristo no Roda Viva', 'PppP5_TQjQE')],
   ['autoras'], [MN, U, BE, RV, TVB], 92)
TR('trilha-literatura-portuguesa', 'Literatura Portuguesa', 'Das cantigas a Fernando Pessoa.',
   'A literatura de Portugal em dez episódios, para o vestibular e para entender as raízes da nossa.', 'caravela',
   [('Trovadorismo', 'N8aCwmWgVyA'), ('Humanismo', 'TaiiIil8-Ow'), ('Auto da barca do inferno', 'Yg8P9y14EDk'), ('Classicismo', 'yUx7vExUi4k'), ('Barroco em Portugal', 'zGVONzNXGSo'),
    ('Arcadismo em Portugal', 'Yadx1nAvgyo'), ('Romantismo em Portugal', 'MUvd5BJiGI4'), ('Naturalismo em Portugal', 'FAzWo39rMYY'), ('Parnasianismo em Portugal', 'iqP66FxK0h4'), ('Mensagem, de Fernando Pessoa', 'kxEjhpzQz7s')],
   ['literatura-portuguesa'], [N, MN, U], 85)
TR('trilha-poesia-brasileira', 'Poesia Brasileira', 'Cinco séculos em verso.',
   'Do Barroco à geração de 45, os poetas e os poemas que mais aparecem em sala e nas provas.', 'lua',
   [('Barroco no Brasil', '1FN2jCxgnt0'), ('Arcadismo no Brasil', 'leb7oRjtsO8'), ('Romantismo: poesia', 'M7okFxuX8fM'), ('Parnasianismo', 'JKmrUc1PhuE'), ('Simbolismo', 'rVjVUTXHocQ'),
    ('Manuel Bandeira', '0jGwgfB2wXc'), ('Modernismo: 2ª geração (poesia)', 'PyojY1qM9pU'), ('Romanceiro da Inconfidência', 'C4OSa2ub-6k'), ('Modernismo: 3ª geração (poesia)', 'bQiS0HlnuX4')],
   ['poesia'], [N, BE, MN], 84)
TR('trilha-literatura-universal', 'Clássicos do Mundo', 'Grandes livros comentados por professores universitários.',
   'Oito episódios da série Literatura Fundamental, da Univesp, sobre clássicos que todo leitor deveria conhecer.', 'sol',
   [('1984', 'VL-sjRG4aC0'), ('O processo', 'mVCYpeaff_4'), ('O estrangeiro', 'WWKrFF-54i0'), ('As flores do mal', 'nM-z2vcjFWY'),
    ('Guerra e paz', 'iIbM0FobowE'), ('Pedro Páramo', '_J4YPNxQN_U'), ('O apanhador no campo de centeio', 'xNP5pBs9tGU'), ('Tristram Shandy', 'BMqrz2rLrkY')],
   ['literatura-universal', 'classicos'], [U], 80)

add('palavras-ancestrais', 'documentario', 'documentario', 'Palavras Ancestrais',
    'Uma reportagem sobre a literatura indígena brasileira: escritores, narrativas orais e a palavra como forma de resistência e memória.',
    capa('documentario', 'raiz', 'Documentário', 'literatura indígena'), [('Caminhos da Reportagem: Palavras ancestrais, reflexões sobre literatura indígena', 'uXaKHzroJXs')],
    ['contemporanea', 'literatura-brasileira', 'enem'], [TVB], ano=None, chamada='A palavra que vem de antes.', pop=78, generos=['Reportagem'],
    ficha_=ficha('Apresenta a literatura indígena, presente na BNCC e cada vez mais cobrada.',
      ['Oralidade', 'Ancestralidade', 'Literatura indígena', 'Resistência', 'Território'], ['Daniel Munduruku', 'Ailton Krenak', 'Eliane Potiguara', 'Olívio Jekupé'],
      ['Conhecer autores indígenas', 'Valorizar a oralidade', 'Discutir representação e autoria'],
      ['Qual a diferença entre falar sobre indígenas e indígenas falarem?', 'A palavra dita também é literatura?', 'Que autores indígenas você conhece?'],
      'Leia um trecho de Daniel Munduruku ou de Ailton Krenak e compare com o indígena idealizado de Iracema.'))


# ======================= IMAGENS (Wikimedia Commons) =======================
# Nome exato do arquivo no Commons. O site usa o endereço Special:FilePath, que
# sempre aponta para o arquivo certo. Se uma imagem sair do ar, a capa desenhada aparece.
from urllib.parse import quote
IMG = {
    # escolas
    'linha-do-tempo-das-escolas': 'Laurentius de Voltolina 001.jpg',
    'trovadorismo': 'Les Très Riches Heures du duc de Berry juin.jpg',
    'humanismo': 'Gil Vicente na Corte de D. Manuel I (Roque Gameiro, Quadros da História de Portugal, 1917).png',
    'quinhentismo': 'Meirelles-primeiramissa2.jpg',
    'classicismo': 'Camões por Fernão Gomes.jpg',
    'barroco': 'Rembrandt - The Philosopher in Meditation (cleaned).jpg',
    'arcadismo': 'Nicolas Poussin - Et in Arcadia ego (deuxième version).jpg',
    'romantismo': 'Iracema.jpg',
    'realismo-naturalismo': 'Modesto Brocos - A Redenção de Cam (cropped).jpg',
    'parnasianismo': 'Sandro Botticelli 046.jpg',
    'simbolismo': 'Arnold Böcklin - Die Toteninsel III (Alte Nationalgalerie, Berlin).jpg',
    'pre-modernismo': 'Canudos rebels.jpg',
    'modernismo-1922': 'Modernistas 1922.jpg',
    'geracao-de-30': 'A Seca no Sertão Nordestino.jpg',
    'geracao-de-45': 'Paul Klee ~ Angelus Novus ~ 1920.jpg',
    'literatura-contemporanea': 'Contradição de Dois Mundos.jpg',
    # autores
    'machado-de-assis': 'Machado de Assis aos 57 anos.jpg',
    'clarice-lispector': 'Clarice Lispector, 1968.jpg',
    'guimaraes-rosa': 'Guimarães Rosa, anos 1960.jpg',
    'graciliano-ramos': 'Amaral Gurgel - Graciliano Ramos - 1949.jpg',
    'lima-barreto': 'Retrato de Lima Barreto, da ficha de internação no Hospício Nacional de Alienados.jpg',
    'carolina-maria-de-jesus': 'Carolina Maria de Jesus, 1960 (cropped).png',
    'conceicao-evaristo': 'Conceição Evaristo, September 2024.jpg',
    'lygia-fagundes-telles': 'Lygia Fagundes Telles - MinC (7) headshot.jpg',
    'cruz-e-sousa': 'Cruz e Sousa.jpg',
    'olavo-bilac': 'Olavo Bilac.jpg',
    'manuel-bandeira': 'Manuel Bandeira no Centro - Rio de Janeiro - 20220921152915.jpg',
    'cecilia-meireles': 'Cecília-Meireles.jpg',
    'julia-lopes-de-almeida': 'Almeida Júnior - Moça com Livro.jpg',
    'fernando-pessoa': 'Pessoa chapeu.jpg',
    'jose-de-alencar': 'José de Alencar.jpg',
    # obras
    'dom-casmurro': 'DomCasmurroMachadodeAssis.jpg',
    'memorias-postumas': 'Machado de Assis by Marc Ferrez - Original.jpg',
    'vidas-secas': 'CAATINGA SERTÃO.JPG',
    'triste-fim-de-policarpo-quaresma': 'Bonde virado (Revolta da Vacina).jpg',
    'capitaes-da-areia': 'Jorge Amado, gtfy.00010.jpg',
    'auto-da-barca-do-inferno': 'Gil Vicente.jpg',
    'auto-da-compadecida': 'Ariano Suassuna.jpg',
    'a-hora-da-estrela': 'Clarice Lispector (cropped).jpg',
    'grande-sertao-veredas': 'Joaoguimaraesrosa1.jpg',
    'mensagem': 'Fernando Pessoa.jpg',
    'quarto-de-despejo': 'Carolina Maria de Jesus assinando seu livro Quarto de Despejo em 1960.jpg',
    'romanceiro-da-inconfidencia': 'Ouro Preto MG Brasil - Casario colonial - panoramio.jpg',
    'campo-geral': 'Museu Casa Guimarães Rosa - panoramio.jpg',
    'as-meninas': 'Lygia Fagundes Telles em 1945.jpg',
    'inocencia': 'Alfredo Taunay.JPG',
    'a-moreninha': 'Joaquim manuel de macedo 1866.jpg',
    'angustia': 'Edvard Munch - Melancholy (1894).jpg',
    'boca-do-inferno': 'Gregório de Matos 1775.jpg',
    'sermao-da-sexagesima': 'Padre António Vieira.jpg',
    'contos-gauchescos': 'João Simões Lopes Neto.jpg',
    # literatura universal
    '1984': 'George Orwell press photo.jpg',
    'o-processo': 'Franz Kafka, 1923.jpg',
    'o-estrangeiro': 'Albert Camus, gagnant de prix Nobel, portrait en buste, posé au bureau, faisant face à gauche, cigarette de tabagisme.jpg',
    'as-flores-do-mal': 'Étienne Carjat, Portrait of Charles Baudelaire, circa 1862.jpg',
    'guerra-e-paz': 'L.N.Tolstoy Prokudin-Gorsky.jpg',
    'pedro-paramo': 'Rulfo por Lyon.jpg',
    'o-apanhador-no-campo-de-centeio': 'J. D. Salinger (Catcher in the Rye portrait).jpg',
    'teogonia': 'Hesiod and the Muses by Gustave Moreau.jpg',
    'o-som-e-a-furia': 'Carl Van Vechten - William Faulkner.jpg',
    'um-bonde-chamado-desejo': 'Tennessee Williams NYWTS.jpg',
    'contos-de-andersen': 'HCA by Thora Hallager 1869.jpg',
    'tristram-shandy': 'Laurence Sterne, alias Tristram Shandy- "And When Death Himself Knocked at My Door" MET DP835344.jpg',
    'cancoes-da-inocencia': 'William Blake by Thomas Phillips.jpg',
    # trilhas e documentários
    'trilha-escolas-literarias': 'Almeida Júnior - Reading - Google Art Project.jpg',
    'trilha-machado-de-assis': 'Machado de Assis 1904.jpg',
    'trilha-modernismo': 'Mario de andrade 1928.png',
    'trilha-vozes-negras': 'Estátua Zumbi dos Palmares - 1.jpg',
    'trilha-elas-escrevem': 'Leitura by José Ferraz de Almeida Júnior 1892.jpg',
    'trilha-literatura-portuguesa': 'Os Lusíadas.jpg',
    'trilha-poesia-brasileira': 'Alberto Henschel - Castro Alves.jpg',
    'trilha-literatura-universal': 'Leo Tolstoi v kabinetie.05.1908.ws.jpg',
    'palavras-ancestrais': 'Líderes indígenas.jpg',
}
def arquivo(nome, largura):
    return 'https://commons.wikimedia.org/wiki/Special:FilePath/' + quote(nome.replace(' ', '_')) + f'?width={largura}'
for t in T:
    n = IMG.get(t['slug'])
    if not n: continue
    t['capa'] = arquivo(n, 500)
    t['banner'] = arquivo(n, 1280)
    t['credito'] = 'https://commons.wikimedia.org/wiki/File:' + quote(n.replace(' ', '_'))
assert set(IMG) <= {t['slug'] for t in T}, set(IMG) - {t['slug'] for t in T}
print('com imagem:', sum(1 for t in T if t.get('capa')), 'de', len(T))

# ======================= DESTAQUES =======================
for k, s in enumerate(['trilha-escolas-literarias', 'dom-casmurro', 'carolina-maria-de-jesus', 'modernismo-1922', 'a-hora-da-estrela']):
    t = next(x for x in T if x['slug'] == s); t['destaque'] = True; t['ordemDestaque'] = k + 1

# ======================= CATEGORIAS =======================
C = []
for s, n in [('introducao', 'Introdução à literatura'), ('trovadorismo', 'Trovadorismo'), ('humanismo', 'Humanismo'), ('quinhentismo', 'Quinhentismo'), ('classicismo', 'Classicismo'),
             ('barroco', 'Barroco'), ('arcadismo', 'Arcadismo'), ('romantismo', 'Romantismo'), ('realismo', 'Realismo e Naturalismo'), ('parnasianismo', 'Parnasianismo'),
             ('simbolismo', 'Simbolismo'), ('pre-modernismo', 'Pré-Modernismo'), ('modernismo', 'Modernismo'), ('contemporanea', 'Literatura contemporânea')]:
    C.append({'slug': s, 'nome': n, 'tipo': 'escola'})
for s, n in [('machado-de-assis', 'Machado de Assis'), ('clarice-lispector', 'Clarice Lispector'), ('guimaraes-rosa', 'Guimarães Rosa'), ('graciliano-ramos', 'Graciliano Ramos'),
             ('lima-barreto', 'Lima Barreto'), ('carolina-maria-de-jesus', 'Carolina Maria de Jesus'), ('conceicao-evaristo', 'Conceição Evaristo'), ('lygia-fagundes-telles', 'Lygia Fagundes Telles'),
             ('cruz-e-sousa', 'Cruz e Sousa'), ('olavo-bilac', 'Olavo Bilac'), ('manuel-bandeira', 'Manuel Bandeira'), ('cecilia-meireles', 'Cecília Meireles'), ('julia-lopes-de-almeida', 'Júlia Lopes de Almeida'),
             ('fernando-pessoa', 'Fernando Pessoa'), ('jose-de-alencar', 'José de Alencar'), ('gil-vicente', 'Gil Vicente'), ('camoes', 'Luís de Camões'), ('mario-de-andrade', 'Mário de Andrade'),
             ('jorge-amado', 'Jorge Amado'), ('ariano-suassuna', 'Ariano Suassuna')]:
    C.append({'slug': s, 'nome': n, 'tipo': 'autor'})
for s, n in [('vestibular', 'Obras do vestibular'), ('enem', 'Caem no Enem'), ('poesia', 'Poesia'), ('prosa', 'Prosa'), ('teatro', 'Teatro'), ('vozes-negras', 'Vozes negras'),
             ('autoras', 'Autoras'), ('literatura-portuguesa', 'Literatura portuguesa'), ('literatura-brasileira', 'Literatura brasileira'), ('literatura-universal', 'Literatura universal'),
             ('classicos', 'Clássicos'), ('trilhas', 'Trilhas')]:
    C.append({'slug': s, 'nome': n, 'tipo': 'colecao'})

usadas = {c['slug'] for c in C}
for t in T:
    for x in t['temas']: assert x in usadas, (t['slug'], x)
assert len({t['slug'] for t in T}) == len(T)
ids = sorted({v['url'][-11:] for t in T for v in t['videos']})
dest = os.path.join(os.path.dirname(__file__), '..', 'src', 'data', 'catalogo.json')
json.dump({'titulos': T, 'categorias': C}, open(dest, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(os.path.join(os.path.dirname(__file__), 'videos.txt'), 'w').write('\n'.join(ids) + '\n')
from collections import Counter
print(len(T), 'títulos', Counter(t['disciplinas'][0] for t in T), len(ids), 'vídeos únicos')
