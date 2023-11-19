# Global Solutions Mecatrônica

Neste repositório pretendo guardar todas as Global Solutions durante a faculdade


# 1° GS - 2023 

<p>No primeiro semestre de 2023, como solução da Global Solutions no curso de Engenharia Mecatrônica, desenvolvemos um sistema hidropônico autossuficiente e modular. Este sistema contava com um controle preciso das medições, incluindo temperatura, umidade, fluxo de água, quantidade de nutrientes e nível de luminosidade. Além disso, implementamos um sistema de poka-yoke preventivo, no qual, caso o usuário adicionasse, em excesso, os nutrientes, colocando as plantas em risco, a comporta de acesso ao tanque de água, na qual circularia pelo sistema e regaria as plantas, não se abriria.</p>

<p>Todas essas variáveis foram cuidadosamente planejadas visando a otimização do cultivo hidropônico, com foco inicial na produção de alface, a hortaliça mais consumida pelos brasileiros. Para a placa micro controladora, utilizamos o arduino, enquanto na construção do protótipo empregamos PVC rígido para a base e o tanque de água, garantindo suporte ao peso, e PVC comum para as demais partes da hidropônica.</p>
<p>O nosso protótipo proporcionou uma forma de agricultura caseira inteiramente sustentável, com um desperdício mínimo de água e um planejamento inteligente do espaço. Isso possibilitou que as alfaces atingissem um diâmetro de até 60 cm, otimizando o aproveitamento do espaço disponível.</p>

<p>O nosso foco era disponibilizar o produto para residências com restrições de espaço, onde residiam pessoas com o desejo de adotar um estilo de vida saudável. Nesse sentido, desenvolvemos também um sistema modular, o qual permitia que os possuidores do produto o expandissem, caso houvesse espaço disponível na vertical. Esse sistema consistia na adição de módulos adicionais, que poderiam ser facilmente encaixados ao módulo já existente anexado à base, proporcionando uma solução simples, rápida e prática.</p>
<br>
<strong><p>Integrantes</p></strong>
<ul>
<li>Gabriel Tadashi Sawaguchi Cavanha</li>
<li>Giulia de Barbon Henritzi</li>
<li>Leonardo Martins Cunha</li>
</ul>
<br>
<strong>Design do Circuito da Hidropônica</strong>
<p>Circuito da hidropônica, na qual apresentamos à banca da Global Solutions, concebido para demonstração por meio da plataforma Tinkercad. Empregamos duas placas Arduino com a finalidade de exemplificar o protocolo de comunicação UART. Além disso, adotamos o protocolo I2C para simplificar a interconexão das duas placas com os displays LCD. A programação foi realizada exclusivamente em linguagem C++.</p>

![sadasdfas](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/e4d779ad-7d84-491b-b2e6-2765e7754059)
<br>

## Desesenhos da Hidropônica


## Links dos projetos 

**Circuito feito no Tinkercad**
[Tinkercad](https://www.tinkercad.com/things/deKLxw0SsRG-global-solutions-2023-hidroponica)
<br>
<br>

# 2° GS - 2023

<p> Pensando nas dificuldades de monitoramento e na falta de acesso á saude de qualidade por grande parte da população, iniciamos o desenvolvimento de uma pulseira que atua como assistente de saúde pessoal, empregando visão computacional para detectar feridas e um sistema de monitoramento completo do usuário para acompanhar parâmetros vitais, como batimentos cardíacos e temperatura corporal e pressão. Nosso sistema integra comandos de voz e respostas por voz, proporcionando uma interface mais humana, amigável e empática para o usuário.
Além disso, implementamos um sistema de alerta, que é ativado quando os parâmetros monitorados se encontram fora da faixa normal. A pressão arterial, que também é monitorada, é ajustável pelo usuário para atender tanto pacientes hipertensos quanto hipotensos. Ambos os alertas seriam emitidos por voz pela pulseira e, por meio do Node-Red, AWS e Telegram, o usuário receberia as notificações também no celular. <br> </p>
<p> O sistema também inclui um ChatBot, projetado para esclarecer dúvidas sobre doenças de pele ou ferimentos visíveis, indicando a gravidade dos mesmos. Ele analisa os sintomas com base nas respostas pré-definidas do usuário e fornece informações sobre as possíveis causas, aconselhando se é necessário ou não chamar uma ambulância. Adicionalmente, o ChatBot fornece dados importantes, como números de telefone de emergência e ambulatórios próximos, através da geração de um mapa utilizando a API do Google Maps. </p>
A detecção de feridas por meio da visão computacional oferece uma ferramenta valiosa para a identificação precoce de potenciais problemas de saúde, permitindo a intervenção rápida e eficaz. Além disso, o sistema de monitoramento contínuo possibilita uma avaliação holística da saúde do usuário, evitando futuras complicações.
O sistema de alerta, acionado quando parâmetros críticos estão fora da faixa normal, é crucial para fornecer alertas precoces e permitir uma resposta imediata diante de situações de emergência. A inclusão do ChatBot, dedicado a esclarecer dúvidas sobre saúde da pele e fornecer orientações sobre a gravidade dos sintomas, hábitos saudáveis e formas de prevenção; acrescenta uma camada adicional de suporte, capacitando os usuários a tomar decisões informadas sobre a necessidade de assistência médica.
<p>Em um cenário em que a saúde preventiva e o monitoramento contínuo se tornam cada vez mais essenciais, a proposta do projeto oferece uma solução abrangente na telemedicina. Ao integrar tecnologias avançadas de detecção, monitoramento e interação; a pulseira não apenas proporciona cuidados personalizados, mas também fortalece a capacidade dos indivíduos de gerenciar ativamente sua saúde, contribuindo para uma abordagem mais proativa e eficiente no cuidado pessoal. </p>

<p>Abaixo estão as imagens dos nossos dashboards na plataforma Blynk, onde o usuário pode monitorar em tempo real os dados do corpo obtidos pela pulseira:</p>
<br>

![dashboard_1](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/922e47f4-7114-4015-89ac-3d53754fea3d)
![dashboard_2](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/6c9bd4af-254f-4cca-82af-b54fdc025fb4)
<br>
<p>Abaixo está o circuito elétrico para fins de demonstração da pulseira:</p>
<p>Especificações do Hardware:</p>
<ul>
<li>
  <p>Botão Verde: Alternar entre os modos 1, 2, 3 e 4 do código</p>
    <p>
      Modo 1: Relógio (segundo o protocolo NTP) <br>
      Modo 2: Simula a ativação da camêra para identificar ferimentos <br>
      Modo 3: Exibe a temperatura corporal do usuário <br>
      Modo 4: Exibe os batimentos cardiácos do usuário <br>
    </p>
</li>
<li><p>Botão Preto: Delisgar/Ligar</p></li>
<li><p>Buzzer: Função para simular o alarme</p></li>
<li><p>Display OLED: Simular a tela da pulseira</p></li>
</ul>
<br>

![simulação pulseira](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/c326f49d-a3df-457e-aa09-4303f5862465)

<br>
<p>Abaixo está o processo de treinamento do modelo de demonstração utilizando o Teachable Machine da Google:</p>
<br>

![Treinando a AI](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/fbaff1bb-2e91-4579-9cad-f5a9f8bf9c6e)

## Link das partes do projeto 

**Dashboard – Blynk:**
[Blynk.Console](https://blynk.cloud/dashboard/124086/global/filter/838741/organization/124086/devices/480543/dashboard)

**BOT para diagnóstico facilitado:**
[Pipper (telegram.org)](https://web.telegram.org/a/#6820946733)

**BOT para monitoramento de batimentos e temperatura:**
[Monitoramento Swift (telegram.org)](https://web.telegram.org/a/#6977331128)

**Código para simular batimentos cardíacos e temperatura corporal:**
[Opp2 - Wokwi ESP32, STM32, Arduino Simulator](https://wokwi.com/projects/381115733791622145)
<br>
<br>

# 1° GS - 2024 
