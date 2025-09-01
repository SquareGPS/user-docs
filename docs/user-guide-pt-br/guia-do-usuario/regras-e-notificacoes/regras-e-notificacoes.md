# Regras e notificações

Usando **Regras e notificações** Na Navixy, você pode detectar vários eventos e ser notificado sobre eles. Esses recursos ajudam os usuários a monitorar e gerenciar a frota, os ativos e os funcionários de campo com mais eficiência. Os eventos podem variar de simples violações de cercas geográficas a cenários complexos, como alertas antifurto ou prevenção de roubo de combustível. Veja os [exemplos](#) para obter mais detalhes.

## Tipos de eventos detectados

A Navixy oferece um conjunto abrangente de eventos estruturados em várias categorias para ajudá-lo a monitorar e gerenciar sua frota, ativos e funcionários de campo de forma eficiente. Abaixo estão as categorias dos eventos:

- [**Potência do dispositivo**](./regras-e-notificacoes/potencia-do-dispositivo.md) \- Monitore o status de energia do dispositivo, incluindo a bateria e as conexões externas
- [**Conexão do dispositivo**](./regras-e-notificacoes/conexao-do-dispositivo.md) \- Rastreie a conectividade do dispositivo com a rede ou plataforma celular
- [**Posicionamento do dispositivo**](./regras-e-notificacoes/posicionamento-do-dispositivo.md) \- Monitorar informações de GPS
- [**Segurança**](./regras-e-notificacoes/seguranca.md) \- Eventos relacionados à segurança e adulteração de veículos
- [**Segurança**](./regras-e-notificacoes/safety.md) \- Eventos relacionados à segurança do motorista
- [**Monitoramento de movimento**](./regras-e-notificacoes/monitoramento-de-movimento.md) \- Rastrear o movimento, a velocidade e a rota do veículo
- [**Programação e despacho**](./regras-e-notificacoes/programacao-e-despacho.md) \- Gerenciar a programação de veículos e pessoal
- [**Eficiência do veículo**](./regras-e-notificacoes/eficiencia-do-veiculo.md) \- Monitorar o consumo e a eficiência do combustível
- [**Entradas e saídas**](./regras-e-notificacoes/entradas-e-saidas.md) \- Rastrear o status dos sensores e equipamentos conectados

### Onde os eventos são computados

Nos sistemas de IoT, os eventos podem ser detectados no lado do dispositivo ou no lado do servidor:

- **Eventos detectados no dispositivo**: Acionados pelos sensores ou entradas do dispositivo de rastreamento GPS instalado no veículo ou no ativo. Esses eventos ocorrem devido a ações ou condições físicas, como pressionar um botão de emergência, detectar uma batida de carro ou registrar um comportamento severo ao dirigir. Os eventos específicos detectados dependem dos recursos do dispositivo que está sendo usado.
- **Eventos detectados no lado do servidor**: Gerado pela análise de dados recebidos do dispositivo em relação a regras e condições predefinidas pelo usuário. Esses eventos são identificados por meio da lógica do servidor, como a detecção de violações de geofence, desvios de rota, alertas de manutenção programada ou alterações incomuns no nível de combustível. O servidor processa os dados e dispara alertas com base nos critérios configurados.

## Gerenciar regras

As regras na Navixy são condições predefinidas que acionam eventos quando atendidas. Para configurar, editar ou excluir regras que você deseja monitorar e sobre as quais deseja ser notificado, selecione **Alertas** no menu principal.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

Para acessar a configuração das regras de notificação na Navixy, vá para o menu à esquerda e escolha **Alertas**. Isso abrirá o painel Notification (Notificação). Clique em **Definir regras**e a interface de regras de alerta será exibida.

![image-20240805-214736.png](./attachments/image-20240805-214736.png)

Na interface de regras de alerta, você pode:

- **Exibir regras existentes**: A interface exibirá uma lista de todas as regras de alerta existentes.
- **Selecionar ou criar novas regras**: Você pode selecionar regras existentes para editar ou criar novas regras clicando no botão "+".
- **Configurações de regras**: Para cada regra, você pode definir as seguintes configurações:
  - **Nome e tipo**: Defina o nome e a descrição da regra.
  - **Configurações**: Defina as condições e os parâmetros específicos para a regra.
  - **Notificações**: Configure como e para quem as notificações serão enviadas.
  - **Cronograma**: Defina a programação para quando a regra estará ativa.

### Vincular regras a objetos

Uma regra pode ser vinculada a um ou vários objetos, como veículos individuais ou grupos de veículos, dependendo do alerta. Essa flexibilidade permite que você aplique a mesma regra em vários ativos, garantindo monitoramento e notificações consistentes.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Etapas para vincular uma regra a objetos

1. **Abra as configurações da regra**: Navegue até a seção **Alertas** no menu principal e selecione a regra que deseja configurar.
2. **Selecionar objetos**: No **Configurações de regras** você verá uma lista de objetos disponíveis no lado esquerdo. Esses objetos podem ser veículos individuais ou grupos de veículos organizados por departamentos.
3. **Selecionar objetos**: Marque as caixas ao lado dos objetos ou grupos aos quais você deseja vincular a regra. Por exemplo, você pode selecionar veículos individuais, como "Oliver (Chevrolet)" e "Marisol (Nissan)", ou grupos inteiros, como "Departamento de vendas".

### Nome e tipo

No **Nome e tipo** da caixa de diálogo, é possível especificar os seguintes detalhes para a regra de notificação:

- **Tipo de regra**: Selecione um dos vários tipos de eventos que podem ser monitorados com a plataforma.
- **Rótulo da regra**: Forneça um nome para a regra a fim de identificá-la facilmente. Exemplo: "O veículo está fora do depósito ABC".
- **Descrição da regra**: Adicione uma breve descrição da regra para explicar sua finalidade ou quaisquer detalhes adicionais. Exemplo: "Essa regra aciona um alerta quando um veículo sai da área designada do depósito ABC, ajudando a monitorar movimentos não autorizados."

O uso do rótulo e da descrição o ajuda a organizar e gerenciar muitas regras de forma eficaz.

### Notificações

Você pode receber notificações por meio de vários canais para garantir que seja prontamente informado sobre eventos importantes. Esses canais incluem:

- **Notificações por SMS**: Alertas imediatos enviados para o telefone celular do usuário.
- **Notificações por e-mail**: Notificações detalhadas enviadas ao endereço de e-mail do usuário.
- **Notificações push**: Alertas instantâneos por meio do aplicativo móvel X-GPS.
- **Notificações no aplicativo**: Alertas exibidos na interface web da Navixy.

O texto da notificação aqui ajudará a identificar especificamente qual alerta foi acionado. A mensagem de notificação aqui será a que aparece quando acionada.

### Cronograma

No **Cronograma** é possível definir quando as regras de notificação estão ativas ou inativas. Isso permite um controle preciso sobre quando os alertas devem ser acionados, com base nas suas necessidades operacionais específicas.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Configuração da programação

Veja como você pode configurar a programação:

- **Modelo**: Selecione um modelo de programação predefinido, se disponível, para aplicar rapidamente padrões de programação comuns, como fins de semana, dias da semana e todos os dias.
- **Períodos ativos**: Os blocos azuis representam os horários em que a regra está ativa e acionará as notificações. Você pode definir esses blocos para horas específicas do dia e dias da semana.
- **Períodos inativos**: Os blocos cinza indicam os horários em que a regra está inativa e não acionará notificações. Isso ajuda a evitar alertas desnecessários em horários não operacionais.

Para personalizar a programação, basta clicar nos blocos de tempo desejados para alternar entre os estados ativo e inativo. Essa flexibilidade garante que você receba notificações somente durante os horários relevantes, reduzindo as chances de fadiga de alertas e aumentando a eficácia dos seus esforços de monitoramento.

![image-20240805-221914.png](./attachments/image-20240805-221914.png)

## Exibir o histórico de notificações

O histórico de notificações pode ser visualizado em diferentes plataformas, permitindo que os usuários revisem eventos e alertas anteriores.

- **Aplicativo da Web**: Acesse o histórico de notificações por meio da seção 'Events' na interface web da Navixy. Filtre por data, tipo de evento e outros critérios.
- **Aplicativo móvel**: Veja as notificações recentes e o histórico no aplicativo móvel da Navixy.
- **Relatórios**: Gerar relatórios detalhados sobre eventos e notificações anteriores para análise e manutenção de registros.

## Suspender e retomar regras

Os usuários podem suspender temporariamente as regras e retomá-las conforme necessário. Esse recurso é útil durante períodos em que as ações das regras não são necessárias, como durante a manutenção ou inatividade sazonal.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Como suspender uma regra existente

1. **Navegue até os alertas**: Vá para a seção **Alertas** no menu principal.
2. **Selecione a regra**: Localize a regra que você deseja suspender na lista de regras de alerta.
3. **Suspender a regra**: Clique no ícone de pausa ao lado do nome da regra para suspendê-la.

Para retomar a regra, basta clicar no ícone de reprodução na regra. Isso reativará as ações da regra.

## Exemplos

Aqui estão alguns exemplos de como as notificações de eventos podem ser utilizadas em vários cenários:

### Alertas de geofence

Os alertas de geofence são um recurso poderoso da Navixy que ajuda os usuários a monitorar os movimentos de seus veículos e ativos dentro de limites geográficos predefinidos, conhecidos como geofences. Essa funcionalidade é essencial para garantir a eficiência operacional, a segurança e a conformidade com as políticas organizacionais.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**O QUE É UMA GEOFENCE?**

Uma geofence é um perímetro virtual definido em um mapa em torno de uma área geográfica específica. Essa área pode ter qualquer forma e tamanho, como um raio circular em torno de um ponto ou um polígono mais complexo que delimita uma região específica.

**COMO FUNCIONAM OS ALERTAS DE GEOFENCE**

Quando um veículo ou ativo equipado com um dispositivo de rastreamento GPS ultrapassa o limite de uma geocerca, um evento é acionado. O sistema registra esse evento e envia notificações ao usuário de acordo com as configurações predefinidas.

**CONFIGURAÇÃO DE ALERTAS DE GEOFENCE**

1. **Definir a área de geofence**:
  - **Geofence circular**: Defina um raio em torno de um ponto central, como um depósito ou escritório.
  - **Geofence poligonal**: Desenhe uma forma complexa no mapa para cobrir áreas como canteiros de obras, zonas de entrega ou bairros da cidade.
  - **Geofence da rota:** Crie uma cerca geográfica estreita e alongada que siga uma rota ou caminho específico, como uma rodovia, ferrovia ou oleoduto, para monitorar o movimento ao longo dessa rota e detectar desvios.
2. **Configurar condições de alerta**:
  - **Alertas de entrada**: Notificar quando um veículo ou ativo entrar na cerca geográfica.
  - **Alertas de saída**: Notificar quando um veículo ou ativo sair da cerca geográfica.
3. **Definir preferências de notificação**:
  - Escolha os canais pelos quais as notificações serão enviadas, como SMS, e-mail, notificações push ou alertas no aplicativo.
  - Personalize o conteúdo da mensagem para incluir detalhes relevantes, como ID do veículo, local, horário do evento e muito mais.

**USOS PRÁTICOS DOS ALERTAS DE GEOFENCE**

- **Gerenciamento de frotas**: Garantir que os veículos cumpram as rotas predefinidas e detectar viagens não autorizadas ou desvios das rotas atribuídas.
- **Segurança de ativos**: Monitore a localização de ativos valiosos e receba alertas imediatos se eles forem movidos para fora de uma área segura.
- **Gerenciamento de funcionários**: Rastrear os funcionários de campo e garantir que estejam dentro das zonas de trabalho designadas durante seus turnos.
- **Eficiência operacional**: Otimize a logística monitorando os horários de entrada e saída em locais importantes, como depósitos e pontos de entrega.

**CENÁRIO DE EXEMPLO**

Uma empresa de entregas configura uma cerca geográfica em torno de seu armazém principal. Quando um caminhão de entrega entra nessa cerca geográfica, um alerta de entrada é acionado, notificando o gerente do depósito por meio de notificação por push. Isso permite que o gerente se prepare para descarregar o caminhão. Se o caminhão sair da cerca geográfica, um alerta de saída é enviado à equipe de segurança, indicando possível uso não autorizado ou roubo.

Com o uso de alertas de geofence, as organizações podem aprimorar seu controle operacional, melhorar a segurança e garantir a conformidade com normas internas e externas.

### Alertas antifurto para carros

Os alertas antifurto de veículos são um recurso crucial da Navixy, projetado para aumentar a segurança dos veículos por meio da detecção de movimentos não autorizados ou adulteração. Essa funcionalidade proporciona tranquilidade aos proprietários de veículos e gerentes de frotas, garantindo a tomada de medidas imediatas em caso de atividades suspeitas.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**COMO FUNCIONAM OS ALERTAS ANTIFURTO DE AUTOMÓVEIS**

Os alertas antifurto de automóveis são acionados quando condições específicas indicativas de uso não autorizado ou adulteração são atendidas. Essas condições podem ser personalizadas com base nos requisitos do usuário e nas necessidades de segurança do veículo.

**CONFIGURAÇÃO DE ALERTAS ANTIFURTO DO CARRO**

1. **Definir critérios de movimentação não autorizada**:
  - **Detecção de ignição**: Monitore o status da ignição do veículo para detectar se o veículo está ligado.
  - **Detecção de movimento**: Use o rastreamento por GPS para identificar quando um veículo sai inesperadamente do local onde está estacionado.
  - **Restrições baseadas no tempo**: Defina alertas para o movimento de veículos fora do horário de expediente ou fora dos horários de funcionamento designados.
2. **Detecção de adulteração**:
  - **Sensores de portas e janelas**: Instale sensores para detectar se as portas ou janelas são abertas à força ou sem a devida autorização.
  - **Desconexão da bateria**: Defina alertas para os casos em que a bateria do veículo for desconectada, que é um método comum usado por ladrões para desativar os sistemas de rastreamento.
  - **Interferência no sinal de GPS**: Monitore se há interferência ou bloqueio no sinal de GPS, indicando possível adulteração.
3. **Configurar notificações de alerta**:
  - **Notificações instantâneas**: Configure SMS, e-mail, notificações push ou alertas no aplicativo para serem enviados imediatamente quando uma atividade não autorizada for detectada.
  - **Alertar os destinatários**: Designe indivíduos ou equipes específicas (por exemplo, pessoal de segurança, gerentes de frota) para receber esses alertas.
  - **Personalização do conteúdo do alerta**: Inclua detalhes essenciais na notificação, como a localização atual do veículo, a hora do evento e o tipo de atividade não autorizada detectada.

**USOS PRÁTICOS DOS ALERTAS ANTIFURTO PARA CARROS**

- **Segurança de veículos particulares**: Os proprietários de veículos particulares podem usar alertas antifurto para proteger seus carros contra roubo ou uso não autorizado, especialmente em áreas de alto risco.
- **Gerenciamento de frotas**: Os gerentes de frota podem garantir a segurança de seus veículos, evitando o uso não autorizado por funcionários ou o roubo em estacionamentos e depósitos.
- **Serviços de aluguel**: As empresas de aluguel de carros podem monitorar seus veículos para detectar e responder a movimentos não autorizados ou adulterações, protegendo seus ativos.
- **Logística e entrega**: As empresas envolvidas em logística e entrega podem proteger seus veículos e os bens valiosos que transportam contra roubo ou acesso não autorizado.

**CENÁRIO DE EXEMPLO**

Uma empresa de logística criou alertas específicos de segurança para seus caminhões de entrega. Certa noite, após o horário comercial, o sistema detecta que a ignição de um dos caminhões foi ligada. Um alerta instantâneo é enviado ao gerente de frota por meio de notificação por push, SMS e e-mail, indicando uma ignição não autorizada.

Simultaneamente, o rastreamento por GPS mostra que o caminhão está se afastando do local de estacionamento designado. O gerente de frota entra em contato imediatamente com as autoridades locais e fornece a localização do caminhão em tempo real. Graças ao alerta oportuno, as autoridades interceptam o veículo, evitando o roubo e protegendo os ativos da empresa.

Ao utilizar alertas antifurto para carros, as organizações podem aumentar significativamente a segurança de seus veículos, reagir rapidamente a possíveis furtos e minimizar o risco de perda de ativos.

### Alertas de controle de temperatura

Os alertas de controle de temperatura são um recurso útil da Navixy projetado para garantir que cargas sensíveis sejam transportadas em condições ideais. Essa funcionalidade é crucial para setores como o farmacêutico, o de alimentos e bebidas e outros setores em que a manutenção de uma faixa de temperatura específica é essencial para preservar a qualidade e a segurança dos produtos.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**COMO FUNCIONAM OS ALERTAS DE CONTROLE DE TEMPERATURA**

Os alertas de controle de temperatura monitoram a temperatura da carga em tempo real usando sensores instalados no veículo de transporte. Quando a temperatura excede ou cai abaixo dos limites predefinidos, um alerta é acionado. Isso permite que sejam tomadas medidas imediatas para corrigir a situação e evitar danos à carga.

**CONFIGURAÇÃO DOS ALERTAS DE CONTROLE DE TEMPERATURA**

1. **Instalar sensores de temperatura**:
  - **Posicionamento do sensor**: Coloque sensores de temperatura em locais estratégicos na área de carga para garantir um monitoramento preciso e abrangente.
  - **Calibração do sensor**: Certifique-se de que os sensores estejam calibrados corretamente para fornecer leituras de temperatura precisas.
2. **Definir limites de temperatura**:
  - **Limites superior e inferior**: Defina os limites máximo e mínimo de temperatura com base nos requisitos da carga específica.
  - **Faixas de temperatura**: Definir faixas de temperatura aceitáveis para atender a diferentes tipos de carga que podem ter requisitos variados.
3. **Configurar condições de alerta**:
  - **Monitoramento em tempo real**: Monitore continuamente a temperatura e acione alertas se ela se desviar dos limites definidos.
  - **Alertas baseados em duração**: Defina alertas para serem acionados se a temperatura permanecer fora da faixa aceitável por uma duração especificada, indicando um problema persistente.
  - **Múltiplos limites**: Defina vários limites para diferentes níveis de alertas (por exemplo, aviso, crítico) com base na gravidade do desvio de temperatura.
4. **Definir preferências de notificação**:
  - **Canais de notificação**: Escolha os canais pelos quais os alertas serão enviados, como SMS, e-mail, notificações por push ou alertas no aplicativo.
  - **Alertar os destinatários**: Especifique os indivíduos ou as equipes responsáveis por responder aos alertas de temperatura (por exemplo, controle de qualidade, gerentes de logística).
  - **Personalização do conteúdo do alerta**: Inclua detalhes essenciais nas notificações, como o rótulo do objeto, a temperatura atual, o local, a hora do alerta e as ações recomendadas.

**USOS PRÁTICOS DOS ALERTAS DE CONTROLE DE TEMPERATURA**

- **Indústria farmacêutica**: Assegurar que vacinas, medicamentos e outros produtos farmacêuticos sensíveis à temperatura sejam transportados dentro da faixa de temperatura necessária para manter sua eficácia e segurança.
- **Setor de alimentos e bebidas**: Evite a deterioração e garanta a segurança dos alimentos mantendo a temperatura correta de produtos perecíveis, como laticínios, carnes e produtos agrícolas, durante o transporte.
- **Indústria química**: Proteja produtos químicos sensíveis à temperatura contra degradação ou reações perigosas, monitorando e controlando as condições de transporte.
- **Logística da cadeia de frio**: Otimize o processo da cadeia de frio, garantindo que todos os elos da cadeia de suprimentos mantenham as condições de temperatura necessárias, desde a produção até a entrega.

**CENÁRIO DE EXEMPLO**

Uma empresa farmacêutica usa os alertas de controle de temperatura da Navixy para monitorar o transporte de vacinas. Essas vacinas devem ser mantidas entre 2°C e 8°C para permanecerem eficazes. A empresa instala sensores de temperatura em seus caminhões refrigerados e define os limites superior e inferior de temperatura de acordo.

Durante uma entrega, um dos caminhões encontra um defeito em sua unidade de refrigeração, fazendo com que a temperatura suba acima do limite de 8°C. O sistema aciona imediatamente um alerta, enviando notificações para a equipe de controle de qualidade por SMS, e-mail e notificações push.

A notificação inclui detalhes como a temperatura atual (10°C), a localização do caminhão e a hora do alerta. A equipe de controle de qualidade entra em contato com o motorista e o instrui a tomar medidas corretivas, como parar na instalação mais próxima com serviços de reparo de refrigeração.

Além disso, a equipe providencia um veículo alternativo para continuar a entrega, garantindo que as vacinas permaneçam dentro da faixa de temperatura segura. A resposta rápida evita a possível deterioração das vacinas, poupando a empresa de perdas financeiras significativas e mantendo a integridade de seus produtos.

Ao usar alertas de controle de temperatura, as organizações podem garantir o transporte seguro e eficaz de cargas sensíveis, minimizar o risco de deterioração ou danos e cumprir as normas do setor.

### Alertas de prevenção de roubo de combustível

Os alertas de prevenção de roubo de combustível são um recurso essencial da Navixy projetado para proteger os veículos contra o desvio não autorizado de combustível e para garantir o uso eficiente do combustível. Essa funcionalidade ajuda os gerentes de frota e os proprietários de veículos a monitorar os níveis de combustível em tempo real e a receber alertas imediatos quando são detectadas quedas suspeitas nos níveis de combustível, permitindo uma intervenção rápida e a redução de perdas.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Alertas de prevenção de roubo de combustível

**COMO FUNCIONAM OS ALERTAS DE PREVENÇÃO DE ROUBO DE COMBUSTÍVEL**

Os alertas de prevenção de roubo de combustível são acionados quando o nível de combustível no tanque de um veículo cai inesperadamente, indicando possível roubo ou uso não autorizado. O sistema usa dados de sensores de nível de combustível instalados no veículo para monitorar e analisar os níveis de combustível continuamente.

**CONFIGURAÇÃO DE ALERTAS DE PREVENÇÃO DE ROUBO DE COMBUSTÍVEL**

1. **Instalar sensores de nível de combustível**:
  - **Posicionamento do sensor**: Instale sensores no tanque de combustível para fornecer leituras precisas do nível de combustível.
  - **Calibração do sensor**: Certifique-se de que os sensores estejam calibrados corretamente para refletir os níveis precisos de combustível, levando em conta o formato e o tamanho do tanque.
2. **Definir condições de alerta**:
  - **Quedas inesperadas**: Defina condições para detectar quedas significativas nos níveis de combustível que ocorrem fora dos padrões normais de uso, como quando o veículo está estacionado ou não está em uso.
  - **Limites de limiar**: Estabeleça limites específicos para quedas de combustível (por exemplo, mais de 10 litros em um curto período) para acionar alertas.
  - **Alertas baseados em tempo**: Configure os alertas para serem mais sensíveis durante os horários em que o veículo não deve estar em uso, como após o expediente ou durante os finais de semana.
3. **Configurar definições de notificação**:
  - **Canais de notificação**: Escolha os canais para receber alertas, como SMS, e-mail, notificações por push ou alertas no aplicativo.
  - **Alertar os destinatários**: Designe indivíduos ou equipes (por exemplo, gerentes de frota, pessoal de segurança) responsáveis por responder aos alertas de roubo de combustível.
  - **Personalização de alertas**: Inclua informações detalhadas nos alertas, como a identificação do veículo, a localização atual, a hora da queda de combustível e a quantidade de combustível perdida.

**USOS PRÁTICOS DOS ALERTAS DE PREVENÇÃO DE ROUBO DE COMBUSTÍVEL**

- **Gerenciamento de frotas**: Proteja os veículos da frota contra roubo de combustível, reduzindo os custos operacionais e garantindo registros precisos do uso de combustível.
- **Equipamento estacionário:** Proteja equipamentos estacionários, como geradores elétricos a diesel, contra o desvio não autorizado de combustível, garantindo uma operação consistente e evitando perdas dispendiosas de combustível.

**CENÁRIO DE EXEMPLO**

Uma empresa de logística utiliza os alertas de prevenção de roubo de combustível da Navixy para monitorar seus caminhões de entrega. Eles instalaram sensores de nível de combustível em todos os seus veículos e configuraram o sistema para detectar quedas inesperadas nos níveis de combustível, especialmente em horários não operacionais.

Certa noite, depois que todas as entregas foram concluídas e os caminhões estão estacionados no depósito da empresa, o sistema detecta uma queda repentina de 15 litros no nível de combustível de um dos caminhões. Essa queda inesperada aciona um alerta imediato, enviando notificações ao gerente de frota por SMS, e-mail e notificações push.

O alerta inclui a identificação do caminhão, sua localização dentro do depósito, o horário da queda de combustível e a quantidade de combustível perdida. O gerente de frota entra em contato rapidamente com a equipe de segurança no local para investigar a situação. A equipe de segurança encontra evidências de adulteração do tanque de combustível e consegue prender o suspeito, evitando mais roubos de combustível.

Com o uso de alertas de prevenção de roubo de combustível, a empresa de logística pode monitorar e proteger efetivamente seus ativos de combustível, reduzindo as perdas por roubo e garantindo um gerenciamento eficiente do combustível. Essa abordagem proativa não apenas economiza custos, mas também ajuda a manter a integridade de suas operações.

## Regras criadas automaticamente

Quando você [ativar](../guia-do-usuario/inicio-rapido/ativar-o-dispositivo-gps.md) Quando o usuário cria um novo dispositivo na plataforma Navixy, o sistema cria automaticamente algumas regras com base nos recursos do dispositivo, como a regra "Pressionando o botão SOS" para um rastreador GPS pessoal com um botão de emergência. Essa automação economiza seu tempo ao configurar os recursos essenciais de monitoramento desde o início, garantindo que seu dispositivo esteja pronto para uso imediato.

Essas regras pré-configuradas são totalmente personalizáveis - você pode facilmente adicionar notificações, ajustar as configurações ou suspender qualquer regra se ela não for necessária. Essa abordagem simplificada aumenta a segurança e a experiência do usuário, permitindo que você se concentre no que é mais importante, sem o incômodo da configuração manual.

## Personalização das notificações no navegador

Você pode personalizar as notificações de eventos no navegador clicando no ícone de engrenagem na lista de eventos. Para acessar e personalizar as configurações de notificação, clique em "Alerts" (Alertas) no menu à esquerda para abrir Notifications (Notificações) e, em seguida, clique no ícone de engrenagem.

![image-20240814-041437.png](./attachments/image-20240814-041437.png)

- **Notificações do navegador:** Ative essa opção para receber alertas de eventos diretamente na central de notificações do seu sistema operacional (por exemplo, a Central de Ações do Windows). Seu navegador solicitará que você permita essas notificações.
- **Exibir notificações:** Os novos eventos serão exibidos como notificações pop-up no canto superior direito da página da plataforma de monitoramento.
- **Notificação de áudio:** Cada novo evento acionará um alerta sonoro no navegador.
- **Volume:** Ajuste o volume das notificações sonoras em seu navegador de acordo com sua preferência.