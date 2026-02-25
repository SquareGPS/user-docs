# Avisos do ADAS

## Visão geral

Os Sistemas Avançados de Assistência ao Motorista (ADAS) são projetados para aumentar a segurança do motorista, fornecendo alertas e monitoramento em tempo real enquanto ele está na estrada. O ADAS utiliza algoritmos avançados e tecnologias de visão de máquina, alimentados por IA, para analisar dados de câmeras de vídeo e sensores lidar. Isso permite que o sistema detecte com precisão possíveis perigos e comportamentos de direção inseguros, garantindo uma abordagem proativa à segurança nas estradas, alinhada com os mais recentes avanços em telemática de veículos.

A plataforma Navixy registra e pode alertar os usuários sobre os seguintes eventos:

| **Evento** | **Descrição** |
| --- | --- |
| **Aviso de saída de pista (LDW)** | Alerta o motorista quando o veículo sai involuntariamente da faixa de rodagem, ajudando a evitar possíveis colisões devido à desatenção do motorista. |
| **Aviso de colisão frontal (FCW)** | Avisa o motorista sobre uma colisão iminente com um veículo ou objeto à frente, permitindo uma frenagem oportuna ou uma ação evasiva para evitar um acidente. |
| **Aviso de monitoramento de cabeceira (HMW)** | Monitora a distância até o veículo à frente e alerta o motorista se a distância de seguimento se tornar insegura, promovendo hábitos de direção mais seguros. |
| **Pedestre em zona de perigo (PDZ)** | Detecta quando um pedestre está próximo ao veículo, especialmente em pontos cegos, para evitar acidentes e aumentar a segurança nas estradas. |
| **Aviso de colisão de pedestres (PCW)** | Emite um aviso quando uma possível colisão com um pedestre é detectada, dando ao motorista tempo para reagir e evitar um incidente. |
| **Reconhecimento de sinais de trânsito (TSR)** | Identifica e alerta o motorista sobre sinais de trânsito importantes, como limites de velocidade ou sinais de parada, para garantir a conformidade com as normas rodoviárias. |

O monitoramento desses eventos ajuda a melhorar a conscientização do motorista, reduzir o risco de acidentes e garantir a adesão às normas de trânsito. Isso, por sua vez, apoia os esforços para melhorar o desempenho do motorista, reduzir a responsabilidade e evitar multas ou reparos dispendiosos no veículo.

## Configurações de regras

### Seleção de eventos

Como os eventos ADAS são processados no dispositivo de telemática de vídeo e não na nuvem, não são necessárias configurações adicionais. Basta selecionar os eventos que deseja monitorar para garantir um rastreamento abrangente do comportamento do motorista.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Não há cronômetro de reinicialização:** O alerta "ADAS" não tem um cronômetro de reinicialização, o que significa que um alerta será acionado sempre que um evento ADAS for detectado.
- **Vários dispositivos:** Os usuários podem selecionar vários rastreadores para receber notificações do ADAS. O único requisito é que os rastreadores escolhidos sejam compatíveis com os eventos do ADAS, e esse recurso deve ser integrado à plataforma. Isso permite o monitoramento eficiente dos comportamentos de direção em uma frota de veículos.
- **Alerta de evento independente de GPS:** A plataforma reconhecerá e exibirá eventos ADAS mesmo que o pacote de dados do rastreador não tenha coordenadas GPS válidas. Nesses casos, as configurações de geocerca interna/externa são ignoradas, garantindo que eventos críticos não sejam perdidos.