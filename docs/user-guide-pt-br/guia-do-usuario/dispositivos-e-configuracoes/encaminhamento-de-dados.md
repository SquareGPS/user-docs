# Encaminhamento de dados

O **Encaminhamento de dados** O widget na Navixy permite que você transmita dados de rastreamento GPS e telemática da Navixy para outros servidores e aplicativos de terceiros usando API e serviços da Web.

## O que é encaminhamento de dados?

O encaminhamento de dados (ou retransmissão de dados) é um recurso que permite o envio de dados de rastreamento GPS e telemática da Navixy para outros servidores ou aplicativos de terceiros em tempo real. Os tipos de dados que podem ser encaminhados incluem:

- Dados do veículo
- Localização GPS
- Dados de dispositivos IoT

O encaminhamento de dados pode ser feito off-line ou quase instantaneamente à medida que os dados são transmitidos.

### Principais objetivos do encaminhamento de dados

1. **Conformidade com as regulamentações governamentais:** Em alguns países, as autoridades exigem que os veículos transmitam dados (como localização e velocidade) usando protocolos específicos para cumprir as leis locais.
2. **Integrações empresariais:** As grandes empresas, principalmente em setores como varejo ou logística, geralmente exigem que seus fornecedores enviem dados de GPS e telemática para seus sistemas a fim de cumprir obrigações contratuais, como garantir entregas pontuais ou manter condições específicas (como temperatura) para a carga.
3. **Consolidação de dados:** A integração de vários componentes em sistemas de software complexos geralmente requer a normalização de dados, especialmente quando esses componentes são fornecidos por vários fornecedores independentes.

### Como funciona o encaminhamento de dados

Os dados coletados do veículo são enviados em um formato de protocolo especificado para um endereço e uma porta determinados pelo usuário. A Navixy oferece vários protocolos de encaminhamento de dados que podem ser selecionados com base em suas necessidades específicas na interface do usuário.

## Gerenciamento do encaminhamento de dados

Você pode gerenciar o encaminhamento de dados por meio do widget correspondente na seção "Devices and settings" (Dispositivos e configurações).

Nesse widget, você pode:

- Vincular um ou mais retranslatadores a um dispositivo.
- Especifique a ID usada ao enviar dados (por padrão, é usada a mesma ID do próprio dispositivo).
- Desvincular retranslatadores do dispositivo.
- Crie novos retradutores e edite os existentes clicando no botão "Protocols" (Protocolos).

### Gerenciamento de retradutores

Ao gerenciar um retranslator, você pode configurar os seguintes parâmetros:

- **Nome:** Uma etiqueta conveniente para facilitar a identificação.
- **Protocolo de transferência de dados:** Escolha entre os protocolos compatíveis.
- **Endereço e porta do servidor de destino:** Especifique para onde os dados devem ser enviados.
- **Login e senha:** Para autorização no servidor receptor (se necessário).
- **Atividade de retradução:** Ative ou desative o retranslator conforme necessário.

Você pode criar vários retradutores se o seu plano de assinatura permitir. Os perfis de retradução podem ser editados, excluídos ou suspensos.

### Protocolos

Aqui estão alguns exemplos de protocolos disponíveis para várias finalidades:

#### Protocolos de conformidade com regulamentos governamentais

| Protocolo | Descrição |
| --- | --- |
| **Maquinário amarelo** (🇨🇴) | Protocolo baseado em SOAP obrigatório para máquinas amarelas, informando aos servidores da polícia. |
| **Olympstroy** (🇷🇺) | Protocolo baseado em SOAP usado durante a preparação para os Jogos Olímpicos de 2014. |
| **OSINERGMIN** (🇵🇪) | Protocolo para envio de informações telemáticas ao governo peruano para unidades de monitoramento em setores como mineração e gás. |
| **RNIS** (🇷🇺) | Usado no sistema de informações e navegação regional de Moscou para controle de movimento de veículos. |

#### Conformidade empresarial

| Protocolo | Descrição |
| --- | --- |
| **Altotrack Chep México** | Encaminha as posições dos veículos da plataforma Chep para o HUB do Altotrack. |
| **ArmCargo** | Envia dados aos serviços de Asset Risk Management para avaliação de riscos. |
| **Carga on-line** | Encaminha dados para o serviço CargoOnline. |
| [**ILSP**](encaminhamento-de-dados/ilsp.md) | Permite que o software da ILSP compartilhe dados de veículos em redes no México. |
| **Localizar-t** | Encaminha dados para o projeto de logística da Localizar-t, o Forza. |
| **Soluções ReC** | Envia dados para os servidores da ReC Servicios Consultores. |
| [**Recurso confiável**](encaminhamento-de-dados/recurso-confiavel.md) | Usado para encaminhamento de dados com o software da Recurso Confiable em vários setores no México e em outros países. |
| **Pulsos SafetyNet** | Encaminha alarmes SOS para um servidor SafetyNet CAD para assistência de emergência. |
| [**SimpliRoute**](encaminhamento-de-dados/simpliroute.md) | Protocolo para transmissão de dados de rastreamento de veículos para o SimpliRoute. |
| **TraceReports** | Envia dados para o sistema TraceReports. |
| [**Unigis**](encaminhamento-de-dados/unigis.md) | Permite o compartilhamento de dados com a plataforma TMS da Unigis, frequentemente usada por departamentos de logística. |
| **Wirtrack** | Encaminha dados para os serviços da Wirsolut. |

#### Consolidação de dados

| Protocolo | Descrição |
| --- | --- |
| **Controle AVL** | Envia dados aos servidores de controle AVL para gerenciamento e estatísticas de segurança. |
| **Granito3** | Encaminha dados para os servidores de navegação da Santel. |
| **Startrack** | Protocolo baseado em SOAP para envio de dados ao sistema de logística da Startrack. |
| **Lacak.io** | Protocolo de encaminhamento de dados para o Lacak.io. |
| [**Serviço Web Navixy**](encaminhamento-de-dados/navixy-ws.md) | Protocolo baseado em SOAP para transmissão de dados da frota para sistemas de terceiros. |
| **SA-RM** | Protocolo geral de encaminhamento de dados. |
| **Transnavegação** | Encaminha dados para os servidores da Transnavigation. |
| [**Wialon IPS**](encaminhamento-de-dados/wialon-ips.md) | Protocolo público da Gurtam para retransmissão de dados do rastreador GPS e GLONASS. |
| **Wisetrack** | Encaminha dados para os servidores do Wisetrack. |

Essas opções oferecem uma estrutura robusta para o compartilhamento de dados, ajudando-o a atender aos requisitos regulamentares, integrar-se aos sistemas corporativos e consolidar dados para uma análise abrangente.