# Relatório sobre todos os eventos

O **Relatório sobre todos os eventos** na Navixy é uma ferramenta abrangente que fornece uma visão geral detalhada de cada evento registrado pela plataforma. Ela abrange uma ampla gama de tipos de eventos, categorizados em eventos gerais, eventos baseados em localização, eventos de hardware e notificações de serviço.

Esse relatório é particularmente valioso quando há necessidade de monitorar a atividade do dispositivo durante um período específico, analisar padrões de eventos e documentar incidentes específicos.

## Visão geral do relatório

O relatório de todos os eventos inclui os seguintes recursos:

- **Registro de eventos:** Exibe quando e onde cada evento ocorreu, juntamente com as informações do driver associado, caso um driver tenha sido atribuído ao dispositivo no momento.
- **Gráfico de distribuição de eventos:** Representação visual de como os eventos foram distribuídos no período de tempo selecionado.
- **Resumo agregado:** Resume o número total de eventos registrados para cada tipo durante o período do relatório.

Para garantir que os eventos sejam registrados corretamente, é necessário criar as regras apropriadas para os seus dispositivos. Esse relatório também inclui uma coluna de driver, indicando qual driver foi atribuído ao dispositivo quando cada evento foi registrado.

## Parâmetros do relatório

Além dos parâmetros de relatório padrão, o relatório sobre todos os eventos inclui:

- **Agrupar por tipo de evento:** Organiza os eventos em tabelas com base em seu tipo. Se não for selecionado, os eventos serão exibidos na ordem em que foram registrados pelo dispositivo.
- **Seleção do tipo de evento:** Permite que você filtre o relatório por tipos de eventos específicos, divididos em quatro grupos. Um recurso de pesquisa rápida ajuda a encontrar os eventos de que você precisa.

## Compreensão dos tipos de eventos

Os eventos deste relatório se enquadram em três categorias principais:

1. **Eventos de hardware:** Eles são processados pelo dispositivo usando seus algoritmos e configurações internos antes de serem enviados à plataforma.
2. **Eventos de software:** Registrados com base nos dados processados pela plataforma.
3. **Sempre realizando eventos:** Eventos acionados continuamente que não correspondem a regras específicas.

Veja a seguir um detalhamento dos tipos de eventos comuns e suas regras associadas:

- **Eventos gerais:**
  - **Geocerca interna/externa criada automaticamente:** Acionada pela regra "movimento não autorizado (por coordenadas)".
  - **Controle de cruzeiro ligado/desligado:** Associado à regra "controle de cruzeiro ligado/desligado".
  - **Rastreador anexado:** Relacionado à regra de "desvinculação do rastreador do objeto".
  - **Aviso de colisão frontal:** Vinculado à regra dos "sistemas avançados de assistência ao motorista (ADAS)".
  - **Sinal de GPS perdido/recuperado:** Vinculado à regra "sinal de GPS perdido/recuperado".
  - **Condução severa:** Acionado pela regra de "direção severa".
  - **Início/fim do estacionamento:** Relacionado à regra "detecção de estado de estacionamento".
- **Eventos baseados em localização:**
  - **Entrada/saída de geofence:** Registra quando um veículo entra ou sai de uma cerca geográfica predefinida.
  - **Visitas a pontos de interesse:** Rastreia visitas a pontos de interesse (POIs).
- **Eventos de hardware:**
  - **Ativação da ignição:** Registra quando a ignição é ligada ou desligada.
  - **Bloqueio de GSM/GPS:** Indica tentativas de interferência nos sinais GSM ou GPS.
- **Notificações de serviço:**
  - **Bateria fraca:** Alerta quando o nível da bateria do dispositivo cai abaixo de um determinado limite.
  - **Luz de verificação do motor (MIL) acesa:** Registra quando a luz de verificação do motor do veículo é ativada.

## Visualização de dados

### Tabela de eventos

O **tabela de eventos** fornece uma lista detalhada de todos os eventos, incluindo:

- **Tempo:** A hora exata em que o evento ocorreu.
- **Nome do evento:** O nome do evento que foi acionado.
- **Endereço:** O local onde o evento foi realizado.
- **Funcionário:** O funcionário atribuído ao dispositivo quando o evento foi recebido.

### Gráfico de distribuição de eventos

O **gráfico de distribuição de eventos** representa visualmente a frequência e a distribuição de eventos durante o período de tempo selecionado. Isso pode ajudar a identificar padrões ou picos incomuns de atividade.

### Número de eventos por tipo

Esta seção do relatório registra o total de ocorrências de cada tipo de evento durante o período do relatório. Se um tipo específico de evento não tiver ocorrido, ele será marcado com um traço.