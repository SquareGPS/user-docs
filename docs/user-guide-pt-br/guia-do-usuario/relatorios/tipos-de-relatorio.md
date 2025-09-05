# Tipos de relatório

A Navixy fornece um conjunto abrangente de relatórios que lhe permite monitorar vários aspectos das operações da sua frota. Esses relatórios são organizados em categorias, facilitando a localização e a geração dos dados de que você precisa. Veja abaixo uma visão geral das categorias de relatórios disponíveis e os relatórios específicos que elas contêm.

## Relatórios de atividades

Os relatórios de atividades fornecem informações detalhadas sobre os movimentos e paradas de seus veículos, permitindo monitorar os históricos de viagens e identificar padrões de uso dos veículos.

- **Viagens**  
Esse relatório oferece um histórico detalhado das viagens, incluindo a duração, o tempo de viagem, a duração das paradas e a velocidade. Ele também fornece uma visão geral do consumo de combustível para veículos sem sensores de combustível.
- **Paradas**  
O relatório de paradas detalha as paradas e os estacionamentos, incluindo local, duração e tempo ocioso (tempo gasto com o motor ligado enquanto estacionado).
- **Viagens e paradas por turnos**  
Um relatório combinado que permite visualizar dados de viagens e paradas segmentados por turnos, ajudando a analisar o uso do veículo durante intervalos de tempo específicos.

## Relatórios de pontos de referência

Os relatórios de pontos de referência o ajudam a rastrear visitas a áreas geográficas predefinidas, como cercas geográficas e pontos de interesse (POIs).

- **Visitas de Geofence**  
Rastreia o número de visitas a áreas cercadas geograficamente em um período específico, fornecendo detalhes sobre entradas, saídas e a duração das estadias.
- **Visitas a POIs**  
Semelhante ao relatório de geofence, ele rastreia as visitas a pontos de interesse, detalhando a data e a hora de cada visita.

## Relatórios de segurança e proteção

Esses relatórios concentram-se em eventos e alertas relacionados à segurança gerados pelo sistema, ajudando-o a garantir a segurança de seus veículos e motoristas.

- **Segurança do carro**  
Fornece detalhes sobre alarmes de carros, evacuações, acidentes e outros eventos de segurança.
- **Botão de emergência (SOS)**  
Captura eventos acionados pelo botão SOS em dispositivos GPS equipados com um botão de pânico.
- **Detecção de quedas**  
Rastreia eventos de queda detectados por dispositivos com sensores de queda, comumente usados em rastreadores pessoais.
- **Desprendimento do rastreador**  
Relata casos em que um dispositivo de rastreamento foi removido de seu objeto atribuído, geralmente usado para rastreamento de carga.
- **Relatório geral de segurança**  
Um relatório abrangente que agrega todos os eventos de segurança e proteção.

## Relatórios de uso de veículos

Os relatórios de uso de transporte permitem monitorar como seus veículos e seus recursos estão sendo utilizados, incluindo o consumo de combustível e o uso do motor.

- **Horas do motor**  
Exibe informações detalhadas sobre as horas do motor, tanto em movimento quanto em marcha lenta, juntamente com diagramas de atividade e histogramas. Leia mais:
  - [Relatório de horas do motor](detalhes-especificos-do-relatorio/relatorio-de-horas-do-motor.md)
- **Volume de combustível**  
Fornece dados sobre o consumo de combustível, enchimentos e drenos, juntamente com os volumes de combustível inicial e final. Leia mais:
  - [Relatório de consumo de combustível](detalhes-especificos-do-relatorio/relatorio-de-volume-de-combustivel.md)
  - [Gerenciamento de combustível na Navixy](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2380890113/Fuel+control+in+Navixy)
- **Medidor de vazão**  
Concentra-se nos dados de consumo de combustível coletados dos medidores de vazão, sem mostrar os níveis de combustível em momentos específicos.
- **Sensores de veículos**  
Exibe dados recebidos dos sensores do veículo via CAN-bus ou OBDII, incluindo quilometragem, RPM, velocidade e temperatura do líquido de arrefecimento. Leia mais:
  - [Relatório de leituras CAN / OBDII do veículo](https://squaregps.atlassian.net/wiki/spaces/UDOCPT/pages/3025243479/Tipos+de+relat+rio)

## Geração de relatórios de qualidade

Esses relatórios são essenciais para monitorar o comportamento do motorista, principalmente em relação ao excesso de velocidade e a outras ações potencialmente perigosas.

- **Violação de velocidade**  
Detalha as instâncias em que o veículo excedeu o limite de velocidade, incluindo data, local e velocidade real. Veja também:
  - [Condução severa em regras e notificações](../regras-e-notificacoes/safety/direcao-severa.md)
  - [Condução ecológica no gerenciamento de frotas](../gerenciamento-de-frotas/conducao-ecologica.md)

### Relatórios de status do dispositivo

Os relatórios de status do dispositivo fornecem informações sobre o status operacional dos seus dispositivos de rastreamento, ajudando-o a garantir um monitoramento ininterrupto.

- **Ativação e desativação do dispositivo**  
Rastreia as instâncias em que o dispositivo GPS foi ligado ou desligado manualmente. Veja também:
  - [Dispositivo ligado/desligado em Regras e notificações](../regras-e-notificacoes/potencia-do-dispositivo/dispositivo-ligadodesligado.md)
- **Perda de conexão GSM**  
Relata períodos em que o dispositivo GPS perdeu a conexão GSM, indicando uma falta de comunicação com o servidor de monitoramento. Veja também:
  - [Perda de conexão do dispositivo em Regras e notificações](../regras-e-notificacoes/conexao-do-dispositivo/perda-de-conexao-do-dispositivo.md)

## Relatórios de dispositivos conectados

Esses relatórios se concentram nos sensores e equipamentos conectados aos seus dispositivos de rastreamento, fornecendo dados operacionais detalhados.

- **Sensores de medição**  
Fornece um histórico detalhado das leituras dos sensores, como temperatura, níveis de combustível e tensão.
- **Tempo de trabalho do equipamento**  
Rastreia a atividade e o tempo ocioso do equipamento conectado ao dispositivo de rastreamento por meio de entradas digitais. Leia mais:
  - [Relatório de horas de trabalho do equipamento](detalhes-especificos-do-relatorio/relatorio-de-tempo-de-trabalho-do-equipamento.md)

## Relatórios de negócios

Os relatórios comerciais são projetados para ajudá-lo a monitorar as tarefas operacionais e o desempenho da sua força de trabalho de campo.

- **Relatório de tarefas**  
Resume o status das tarefas atribuídas aos funcionários, ajudando-o a acompanhar seu progresso e conclusão.
- **Valores do formulário de tarefas**  
Exibe dados de formulários enviados por funcionários ao completarem tarefas por meio do aplicativo X-GPS Tracker.
- **Relatório de status de trabalho**  
Registra as alterações nos status de trabalho, sejam elas feitas por funcionários ou operadores.
- **Check-ins**  
Lista todos os check-ins feitos por funcionários no mapa usando o aplicativo X-GPS Tracker.
- **Troca de turno do motorista**  
Rastreia as mudanças de motorista, ajudando-o a monitorar qual motorista estava operando um veículo em determinado momento.
- **Viagens por estado**  
Um relatório de viagem especializado que agrupa os dados por região ou país.

## Outros relatórios

Esses relatórios abrangem uma variedade de eventos e atividades adicionais, oferecendo amplas percepções sobre as operações de sua frota.

- **Todos os eventos**  
Um relatório abrangente que agrega todos os tipos de eventos suportados pela plataforma, agrupados por categoria de evento.
- **Entrada/saída de geofence**  
Rastreia eventos de entrada e saída de áreas cercadas geograficamente, fornecendo dados detalhados sobre o movimento de entrada e saída dessas regiões.
- **Relatório de localizações por SMS**  
Lista as solicitações de localização enviadas por SMS quando o dispositivo GPS não tem conexão com a Internet.
- **Relatório de pontos**  
Mostra o movimento do dispositivo ao longo do tempo por pontos, incluindo coordenadas e links para mapas.