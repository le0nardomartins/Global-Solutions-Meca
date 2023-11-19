# Global Solutions Mecatrônica

Neste repositório pretendo guardar todas as Global Solutions durante a faculdade


# 1° GS - 2023 


# 2° GS - 2023

<p> Pensando nas dificuldades de monitoramento e na falta de acesso á saude de qualidade por grande parte da população, iniciamos o desenvolvimento de uma pulseira que atua como assistente de saúde pessoal, empregando visão computacional para detectar feridas e um sistema de monitoramento completo do usuário para acompanhar parâmetros vitais, como batimentos cardíacos e temperatura corporal e pressão. Nosso sistema integra comandos de voz e respostas por voz, proporcionando uma interface mais humana, amigável e empática para o usuário.
Além disso, implementamos um sistema de alerta, que é ativado quando os parâmetros monitorados se encontram fora da faixa normal. A pressão arterial, que também é monitorada, é ajustável pelo usuário para atender tanto pacientes hipertensos quanto hipotensos. Ambos os alertas seriam emitidos por voz pela pulseira e, por meio do Node-Red, AWS e Telegram, o usuário receberia as notificações também no celular. <br> </p>
<p> O sistema também inclui um ChatBot, projetado para esclarecer dúvidas sobre doenças de pele ou ferimentos visíveis, indicando a gravidade dos mesmos. Ele analisa os sintomas com base nas respostas pré-definidas do usuário e fornece informações sobre as possíveis causas, aconselhando se é necessário ou não chamar uma ambulância. Adicionalmente, o ChatBot fornece dados importantes, como números de telefone de emergência e ambulatórios próximos, através da geração de um mapa utilizando a API do Google Maps. </p>
A detecção de feridas por meio da visão computacional oferece uma ferramenta valiosa para a identificação precoce de potenciais problemas de saúde, permitindo a intervenção rápida e eficaz. Além disso, o sistema de monitoramento contínuo possibilita uma avaliação holística da saúde do usuário, evitando futuras complicações.
O sistema de alerta, acionado quando parâmetros críticos estão fora da faixa normal, é crucial para fornecer alertas precoces e permitir uma resposta imediata diante de situações de emergência. A inclusão do ChatBot, dedicado a esclarecer dúvidas sobre saúde da pele e fornecer orientações sobre a gravidade dos sintomas, hábitos saudáveis e formas de prevenção; acrescenta uma camada adicional de suporte, capacitando os usuários a tomar decisões informadas sobre a necessidade de assistência médica.
<p>Em um cenário em que a saúde preventiva e o monitoramento contínuo se tornam cada vez mais essenciais, a proposta do projeto oferece uma solução abrangente na telemedicina. Ao integrar tecnologias avançadas de detecção, monitoramento e interação; a pulseira não apenas proporciona cuidados personalizados, mas também fortalece a capacidade dos indivíduos de gerenciar ativamente sua saúde, contribuindo para uma abordagem mais proativa e eficiente no cuidado pessoal. </p>

Abaixo estão as imagens dos nossos dashboards na plataforma Blynk, onde o usuário pode monitorar em tempo real os dados do corpo obtidos pela pulseira:
<br>
![dashboard_1](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/922e47f4-7114-4015-89ac-3d53754fea3d)
![dashboard_2](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/6c9bd4af-254f-4cca-82af-b54fdc025fb4)
<br>
Abaixo está o circuito elétrico para fins de demonstração da pulseira:
<br>
![simulação pulseira](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/c326f49d-a3df-457e-aa09-4303f5862465)
<br>
Abaixo está o processo de treinamento do modelo de demonstração utilizando o Teachable Machine da Google:
<br>
![Treinando a AI](https://github.com/le0nardomartins/Global-Solutions-Meca/assets/98195508/fbaff1bb-2e91-4579-9cad-f5a9f8bf9c6e)
