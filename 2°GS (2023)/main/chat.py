import telebot
import folium
from geopy.geocoders import Nominatim
import requests
import webbrowser

##### INICIALIZANDO
API = "6820946733:AAH3w-rMU3EodSlzTfmq2HgcDcfla8FqR7c"
bot = telebot.TeleBot(API)
conversa_estado = {}


##### GERAR MAPA
def obter_coordenadas(endereco):
    geolocator = Nominatim(user_agent="hospital_locator")

    try:
        location = geolocator.geocode(endereco, timeout=10)
        if location:
            return (location.latitude, location.longitude)
        else:
            print("Coordenadas não encontradas para o endereço:", endereco)
            bot.send_message("Coordenadas não encontradas para o endereço:", endereco)
            return None
    except Exception as e:
        print("Erro ao obter coordenadas:", str(e))
        return None

def obter_mapa(coordenadas, hospitais):
    mapa = folium.Map(location=coordenadas, zoom_start=13)

    folium.Marker(
        location=coordenadas,
        popup='Sua localização',
        icon=folium.Icon(color='blue')
    ).add_to(mapa)

    for hospital in hospitais:
        folium.Marker(
            location=[hospital['geometry']['location']['lat'], hospital['geometry']['location']['lng']],
            popup=hospital['name'],
            icon=folium.Icon(color='red')
        ).add_to(mapa)

    return mapa

def salvar_mapa(mapa, file_path='mapa_hospitais.html'):
    mapa.save(file_path)

def obter_hospitais_proximos(api_key, coordenadas, raio=5000, tipo='hospital'):
    endpoint = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': f'{coordenadas[0]},{coordenadas[1]}',
        'radius': raio,
        'type': tipo,
        'key': api_key
    }

    try:
        response = requests.get(endpoint, params=params, timeout=10)
        response.raise_for_status()
        hospitais = response.json().get('results', [])
        return hospitais
    except requests.exceptions.RequestException as e:
        print("Erro ao obter hospitais próximos:", str(e))
        return []

def gerar_mapa_hospitais(endereco_usuario):
    coordenadas_usuario = obter_coordenadas(endereco_usuario)

    if coordenadas_usuario:
        api_key = 'AIzaSyCKBpEQOuC01QuSyC_jX_MUzbuygWwwEic'
        hospitais_proximos = obter_hospitais_proximos(api_key, coordenadas_usuario)

        mapa = obter_mapa(coordenadas_usuario, hospitais_proximos)
        salvar_mapa(mapa)

        # Abre automaticamente a página HTML no navegador
        webbrowser.open('mapa_hospitais.html', new=2)

        print("O mapa foi gerado em HTML.")
    else:
        print("Não foi possível obter coordenadas para o endereço fornecido.")


##### DIAGNÓSTICO POR ÁREA
@bot.message_handler(commands=["ver_mais_cardiacas"])
def ver_mais_cardiacas(msg):
    mensagem = """
---- Doenças Cardíacas ----

Infarto do Miocárdio:
Sintomas comuns: Dor no peito, que pode irradiar para o braço esquerdo, pescoço, mandíbula; falta de ar, sudorese, náuseas.
    
Angina:
Sintomas comuns: Dor ou desconforto no peito, sensação de aperto, queimação ou peso; pode se manifestar durante o esforço físico ou estresse.
    
Insuficiência Cardíaca:
Sintomas comuns: Fadiga, falta de ar, inchaço nas pernas e tornozelos, ganho de peso inexplicado, tosse persistente.
    
Diagnóstico:
1 - Eletrocardiograma (ECG): Registra a atividade elétrica do coração.
    
2 - Exames de sangue: Avaliam enzimas cardíacas.
    
3 - Teste de esforço: Monitora a resposta do coração ao esforço físico.
    
4 - Ecocardiograma: Usa ultrassom para avaliar a estrutura e função cardíacas.
    
Tratamento:
1 - Medicamentos como anti-hipertensivos e estatinas.
    
2 - Intervenções cirúrgicas como angioplastia e cirurgia de bypass.
    
3 - Mudanças no estilo de vida, incluindo dieta saudável, exercícios regulares e cessação do tabagismo.
    
Hábitos Saudáveis:
1 - Exercícios regulares.
2 - Dieta balanceada.
3 - Controle do peso.
4 - Evitar o tabagismo.
5 - Limitar o consumo de álcool.
"""
    bot.send_message(msg.chat.id, mensagem)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["ver_mais_derma"])
def ver_mais_derma(msg):
    mensagem = """
---- Doenças Dermatológicas ----

Dermatite:
Sintomas comuns: Coceira, vermelhidão, descamação, irritação da pele.

Psoríase:
Sintomas comuns: Manchas vermelhas e escamosas na pele, comum nos cotovelos, joelhos e couro cabeludo.

Urticária:
Sintomas comuns: Placas elevadas e avermelhadas na pele (urticárias), coceira intensa.

Diagnóstico:
1 - Exame clínico.
2 - Biópsia da pele.
3 - Testes alérgicos.

Tratamento:
1 - Medicamentos tópicos como cremes e pomadas.

2 - Medicamentos sistêmicos como antibióticos e corticosteroides.

3 - Terapia de luz.

4 - Mudanças na dieta.

Hábitos Saudáveis:
1 - Manter a pele limpa, hidratada e protegida do sol.
2 - Evitar alérgenos conhecidos.
3 - Adotar uma dieta balanceada.
"""
    bot.send_message(msg.chat.id, mensagem)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["ver_mais_hema"])
def ver_mais_hema(msg):
    mensagem = """
---- Doenças Dermatológicas ----

Dermatite:
Sintomas comuns: Coceira, vermelhidão, descamação, irritação da pele.

Psoríase:
Sintomas comuns: Manchas vermelhas e escamosas na pele, comum nos cotovelos, joelhos e couro cabeludo.

Urticária:
Sintomas comuns: Placas elevadas e avermelhadas na pele (urticárias), coceira intensa.

Diagnóstico:
1 - Exame clínico.
2 - Biópsia da pele.
3 - Testes alérgicos.

Tratamento:
1 - Medicamentos tópicos como cremes e pomadas.
2 - Medicamentos sistêmicos como antibióticos e corticosteroides.
3 - Terapia de luz.
4 - Mudanças na dieta.

Hábitos Saudáveis:
1 - Manter a pele limpa, hidratada e protegida do sol.
2 - Evitar alérgenos conhecidos.
3 - Adotar uma dieta balanceada.
4 - Doenças Hematológicas (Anemia):

Anemia Ferropriva:
Sintomas comuns: Fadiga, palidez, fraqueza, falta de ar.

Anemia Perniciosa:
Sintomas comuns: Fraqueza, palidez, formigamento nas mãos e nos pés.

Anemia Falciforme:
Sintomas comuns: Dor intensa, icterícia, fadiga.

Diagnóstico:
1 - Exame de sangue completo.
2 - Dosagem de ferritina.
3 - Hemograma.

Tratamento:
1 - Suplementos de ferro.
2 - Transfusões de sangue.
3 - Tratamento da causa subjacente, como correção de deficiências nutricionais.

Hábitos Saudáveis:
1 - Consumir uma dieta rica em ferro, vitamina B12 e ácido fólico.
2 - Manter uma hidratação adequada.
3 - Evitar o consumo excessivo de chá e café.
"""
    bot.send_message(msg.chat.id, mensagem)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["ver_mais_pressao"])
def ver_mais_pressao(msg):
    mensagem = """
---- Distúrbios de Pressão ----

Hipertensão Arterial:
Sintomas comuns: Dor de cabeça, tontura, visão turva, fadiga.

Hipotensão:
Sintomas comuns: Tontura, fraqueza, desmaios.

Diagnóstico:
1 - Medição regular da pressão arterial.
2 - Monitoramento ambulatorial da pressão arterial (MAPA).
3 - Exames de sangue.

Tratamento:
1 - Medicamentos anti-hipertensivos.
2 - Mudanças no estilo de vida, como dieta com baixo teor de sódio e exercícios regulares.
3 - Gestão do estresse.

Hábitos Saudáveis:
1 - Manter um peso saudável.
2 - Praticar atividades físicas regularmente.
3 - Reduzir o consumo de sal.
4 - Moderar o consumo de álcool.
5 - Evitar o tabagismo.
"""
    bot.send_message(msg.chat.id, mensagem)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["ver_mais_respiratoria"])
def ver_mais_respiratoria(msg):
    mensagem = """
---- Doenças Respiratórias:

Asma:
Sintomas comuns: Falta de ar, chiado no peito, tosse.

Doença Pulmonar Obstrutiva Crônica (DPOC):
Sintomas comuns: Tosse crônica, falta de ar, produção excessiva de muco.

Pneumonia:
Sintomas comuns: Febre, tosse com muco, dificuldade para respirar.

Diagnóstico:
1 - Testes de função pulmonar.
2 - Radiografias torácicas.
3 -Exames de sangue.

Tratamento:
1 - Broncodilatadores.
2 - Corticosteroides.
3 - Antibióticos, se necessário.
4 - Oxigenoterapia.

Hábitos Saudáveis:
1 - Evitar a exposição a poluentes do ar.
2 - Parar de fumar.
3 - Manter um ambiente livre de alérgenos.
4 - Praticar exercícios respiratórios.
"""
    bot.send_message(msg.chat.id, mensagem)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass


##### FUNÇÕES DE DIAGNÓSTICO
@bot.message_handler(commands=["cardiacas"])
def cardiacas(msg):
    mensagem = """
Doenças Cardíacas:
    
As doenças cardíacas incluem condições como infarto do miocárdio, angina e insuficiência cardíaca. O diagnóstico envolve exames como eletrocardiograma, testes de sangue e ecocardiograma. 
    
O tratamento pode incluir medicamentos,intervenções cirúrgicas e mudanças no estilo de vida, como uma dieta saudável e exercícios regulares. Adotar hábitos saudáveis, como evitar o tabagismo e moderar o consumo de álcool, é crucial para a prevenção.
    
Espero ter ajudado! Se você estiver sentindo algum desses sintomas não exite em visitar um média ou acionar a ambulância através do 192."""

    btn = """Caso sinta que está com algum problema dessa área, clique em /ver_mais_cardiacas para mais informações."""
    bot.send_message(msg.chat.id, mensagem)
    bot.send_message(msg.chat.id, btn)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["dermatologicas"])
def dermatologicas(msg):
    mensagem = """
Doenças Dermatológicas:
    
Doenças dermatológicas, como dermatite e psoríase, demandam diagnóstico através de exame clínico e, em alguns casos, biópsia da pele.
     
O tratamento inclui medicamentos tópicos, sistêmicos e terapias de luz, além de mudanças na dieta. 
Manter a pele limpa, hidratada e protegida do sol, juntamente com a identificação e evitação de alérgenos, são hábitos saudáveis essenciais.
    
Espero ter ajudado! Se você estiver sentindo algum desses sintomas não exite em visitar um média ou acionar a ambulância através do 192."""

    btn = """Caso sinta que está com algum problema dessa área, clique em /ver_mais_derma para mais informações."""
    bot.send_message(msg.chat.id, mensagem)
    bot.send_message(msg.chat.id, btn)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["hematologicas"])
def hematologicas(msg):
    mensagem = """
Doenças Hematológicas (Anemia):
    
Anemias, como a ferropriva e perniciosa, requerem diagnóstico por meio de exames de sangue, incluindo hemograma e dosagem de ferritina.
    
O tratamento envolve suplementos de ferro, transfusões de sangue e abordagem da causa subjacente. Adotar uma dieta rica em nutrientes, como ferro, vitamina B12 e ácido fólico, e manter uma boa hidratação são hábitos saudáveis fundamentais.
    
Espero ter ajudado! Se você estiver sentindo algum desses sintomas não exite em visitar um média ou acionar a ambulância através do 192."""

    btn = """Caso sinta que está com algum problema dessa área, clique em /ver_mais_hema para mais informações."""
    bot.send_message(msg.chat.id, mensagem)
    bot.send_message(msg.chat.id, btn)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["pressao"])
def pressao(msg):
    mensagem = """
Distúrbios de Pressão:
    
Distúrbios de pressão, como hipertensão arterial, exigem diagnóstico regular através da medição da pressão arterial e outros exames. 
    
O tratamento envolve medicamentos e mudanças no estilo de vida, como dieta com baixo teor de sódio e prática regular de exercícios.
    
Hábitos saudáveis incluem manter um peso adequado, praticar atividades físicas, reduzir o consumo de sal e evitar o tabagismo.
    
Espero ter ajudado! Se você estiver sentindo algum desses sintomas não exite em visitar um média ou acionar a ambulância através do 192.
"""
    btn = """Caso sinta que está com algum problema dessa área, clique em /ver_mais_pressao para mais informações."""
    bot.send_message(msg.chat.id, mensagem)
    bot.send_message(msg.chat.id, btn)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["respiratorias"])
def respiratorias(msg):
    mensagem = """
Doenças Respiratórias:
    
Doenças respiratórias, como asma e DPOC, são diagnosticadas por meio de testes de função pulmonar e exames de imagem. 
    
O tratamento inclui broncodilatadores, corticosteroides e, se necessário, antibióticos. 
Evitar a exposição a poluentes do ar, parar de fumar e manter um ambiente livre de alérgenos são hábitos saudáveis essenciais para prevenir e controlar doenças respiratórias.
    
Espero ter ajudado! Se você estiver sentindo algum desses sintomas não exite em visitar um média ou acionar a ambulância através do 192.
"""
    btn = """Caso sinta que está com algum problema dessa área, clique em /ver_mais_respiratoria para mais informações."""
    texto = "/voltar"

    bot.send_message(msg.chat.id, mensagem)
    bot.send_message(msg.chat.id, btn)
    bot.reply_to(msg, texto)
    pass


##### FUNÇÕES DE INÍCIO
@bot.message_handler(commands=["opcao1"])
def opcao1(msg):
    selec = """
Ótimo, vamos começar!
Qual dos conjuntos de sintomas abaixo você está sentindo?
    
/cardiacas - Dor no peito, falta de ar, fadiga, palpitações, tonturas.
    
/dermatologicas - Coceira persistente, erupções cutâneas, inchaço na pele, vermelhidão, sensação de queimação.
    
/hematologicas - Fadiga extrema, palidez na pele, fraqueza, falta de concentração, tonturas.
    
/pressao - Dor de cabeça, visão embaçada, zumbido no ouvido, tonturas, sangramento nasal.
    
/respiratorias - Tosse persistente, falta de ar, chiado no peito, aperto no peito, respiração rápida.
    
Evite escrever as mensagens, não vou conseguir entende-las😞
"""
    bot.reply_to(msg, selec)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["opcao2"])
def opcao2(msg):
    chat_id = msg.chat.id

    # Define o estado para aguardar o endereço do usuário
    conversa_estado[chat_id] = "aguardando_endereco"

    mensagem = "Digite seu endereço ou localização:"
    ex = "Por exemplo: Rua exemplo, Cidade exemplo/Estado exemplo"
    bot.reply_to(msg, mensagem)
    bot.reply_to(msg, ex)

@bot.message_handler(commands=["opcao3"])
def opcao3(msg):
    doencas = """
Doenças mais recorrentes no Brasil:
Olá! Estou aqui para fornecer informações sobre as doenças de pele mais comuns no Brasil. É importante lembrar que, embora eu possa oferecer   informações úteis, a consulta a um profissional de saúde é sempre recomendada para diagnóstico e tratamento adequados.
    
Acne:
A acne é uma condição inflamatória da pele que afeta pessoas de todas as idades. Manifesta-se quando os folículos pilosos ficam obstruídos por óleo e células mortas da pele. Áreas comuns incluem rosto, pescoço, ombros, peito e parte superior das costas. Tratamentos incluem produtos tópicos e, em casos mais graves, medicamentos prescritos.
    
Herpes Labial:
Uma infecção viral que resulta em bolhas dolorosas nos lábios, boca ou gengivas. Altamente contagioso, pode ser transmitido por contato com saliva ou líquido das bolhas.
Embora incurável, pode ser gerenciado com medicamentos antivirais.
    
Dermatite de Contato:
Uma reação alérgica ou irritante desencadeada pelo contato com uma substância específica.
Sintomas incluem coceira, vermelhidão, inchaço e bolhas. 
O tratamento envolve medicamentos tópicos e evitar a exposição à substância causadora.
    
Psoríase:
Doença autoimune que causa manchas vermelhas e escamosas na pele, afetando várias partes do corpo.
Não é contagiosa, mas pode ser desconfortável e impactar a qualidade de vida. Tratamentos variam de medicamentos tópicos a terapias orais e injetáveis.
    
Vitiligo:
Condição autoimune que leva à perda de pigmentação da pele, resultando em manchas brancas.
Não é contagioso, mas pode impactar a autoestima.
Tratamento inclui medicamentos tópicos, orais ou injetáveis.
    
Outras Doenças de Pele Comuns:
Micoses superficiais, transtornos de pigmentação, dermatite de contato alérgica e irritante, estrias, cicatrizes e fibroses cutâneas são também observadas no Brasil. 
Cada condição requer abordagens específicas de tratamento, podendo variar de cremes a procedimentos mais especializados.
    
Doenças Recorrentes no Brasil:

Doenças Crônicas não Transmissíveis (DCNTs):
De acordo com o Ministério da Saúde, as DCNTs são prevalentes no Brasil, incluindo doenças cardiovasculares, cânceres, diabetes e doenças respiratórias crônicas.
Entre as cardiovasculares, destacam-se a doença coronariana, cerebrovascular, arterial periférica, cardíaca reumática, cardiopatia congênita, trombose venosa profunda e embolia pulmonar.
    
Câncer:
O câncer é uma preocupação significativa, sendo o de pele não-melanoma o mais comum no Brasil. 
A detecção precoce e hábitos saudáveis são essenciais para reduzir os riscos.
    
Doenças Respiratórias:
A asma é um desafio respiratório frequente no país. 
A gestão adequada, incluindo a identificação de gatilhos e o uso de medicamentos, é vital para melhor qualidade de vida.
    
Doenças de Pele:
A acne é a condição cutânea mais comum, afetando principalmente adolescentes. 
Além disso, micoses superficiais, transtornos de pigmentação, dermatite de contato alérgica e irritante, estrias, cicatrizes e fibroses cutâneas são comuns. 
A psoríase, que atinge cerca de 2% da população, também requer atenção especializada.
    
Lembre-se sempre de procurar a orientação de um dermatologista para diagnóstico preciso e tratamento adequado! 😊"""
    bot.send_message(msg.chat.id, doencas)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["opcao4"])
def opcao4(msg):
    habitos = """  
Alguns hábitos saudáveis! 😊
Manter hábitos saudáveis é essencial para uma vida plena e cheia de energia. 
Aqui estão algumas dicas para incorporar bons hábitos em sua rotina diária:
    
Alimentação Balanceada: Consuma uma variedade de alimentos, incluindo frutas, vegetais, proteínas magras e grãos integrais. Isso fornece os nutrientes necessários para o bom funcionamento do seu corpo.
    
Atividade Física Regular: Mexa-se! Encontre uma atividade que você goste, seja caminhar, correr, nadar ou dançar. 
A atividade física regular ajuda a manter o peso saudável e melhora a saúde cardiovascular.
    
Hidratação Adequada: Beba água suficiente ao longo do dia. 
A hidratação é crucial para a função celular e ajuda na digestão, além de manter a pele saudável.
    
Bom Sono: Priorize um sono de qualidade. Estabeleça uma rotina de sono regular, evite dispositivos eletrônicos antes de dormir e crie um ambiente propício para o descanso.
    
Gestão do Estresse: Encontre maneiras saudáveis de lidar com o estresse, como meditação, yoga ou simplesmente tirar um tempo para relaxar. O estresse crônico pode afetar negativamente a saúde mental e física.

Evite Tabaco e Álcool em Excesso: O tabaco e o consumo excessivo de álcool têm impactos significativos na saúde. Tente reduzir ou eliminar esses hábitos para promover um estilo de vida mais saudável.
    
Check-ups Regulares: Não se esqueça das consultas médicas de rotina. Exames preventivos podem identificar problemas de saúde antes que se tornem sérios.
    
Lembre-se, pequenas mudanças podem fazer uma grande diferença. Estamos aqui para apoiar seus esforços em direção a uma vida mais saudável. 🌱💪"""
    bot.send_message(msg.chat.id, habitos)
    texto = "/voltar"
    bot.reply_to(msg, texto)
    pass

@bot.message_handler(commands=["opcao5"])
def opcao5(msg):
    bot.send_message(msg.chat.id, "Isso é ótimo, tenha um bom dia! Até mais!")
    pass


#### FUNÇÃO PARA VOLTAR
@bot.message_handler(commands=["voltar"])
def voltar(msg):
    texto = """
Clique na opção desejada abaixo
/opcao1 - Diagnóstico Rápido
/opcao2 - Chamar Ambulância
/opcao3 - Doencas mais recorrentes
/opcao4 - Bons hábitos de saúde
/opcao5 - Estou bem, obrigado(a)!
Evite escrever as mensagens, não vou conseguir entende-las😞"""
    bot.reply_to(msg, texto)


#### FUNÇÕES PARA O FUNCIONAMENTO DA OPÇÃO 2
@bot.message_handler(func=lambda message: conversa_estado.get(message.chat.id) == "aguardando_endereco")
def handle_endereco(message):
    chat_id = message.chat.id
    endereco_usuario = message.text

    # Processar o endereço
    gerar_mapa_hospitais(endereco_usuario)

    # Reiniciar o estado da conversa
    del conversa_estado[chat_id]

    # Responder o usuário
    bot.reply_to(message, "Encontrei seu endereço!")
    bot.send_message(chat_id, f"Buscando hospitais na região próxima a {endereco_usuario}")
    bot.send_message(chat_id, "Deseja que e contate o serviço ambulatório mais próximo?")
    texto = """/sim | /nao"""
    bot.send_message(chat_id, texto)
    pass

@bot.message_handler(commands=["sim"])
def sim(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Estou contatando o serviço ambulatório mais próximo!")
    texto = "/voltar"
    bot.send_message(chat_id, texto)
    pass

@bot.message_handler(commands=["nao"])
def nao(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Tudo bem, estarei aqui se precisar!")
    texto = "/voltar"
    bot.send_message(chat_id, texto)
    pass





#### INICIA O PROGRAMA
@bot.message_handler(commands=["start"])
def start(msg):
    texto = """
Clique na opção desejada abaixo
/opcao1 - Diagnóstico Rápido
/opcao2 - Chamar Ambulância
/opcao3 - Doencas mais recorrentes
/opcao4 - Bons hábitos de saúde
/opcao5 - Estou bem, obrigado(a)!
Evite escrever as mensagens, não vou conseguir entende-las😞"""
    bot.reply_to(msg, texto)

bot.polling()