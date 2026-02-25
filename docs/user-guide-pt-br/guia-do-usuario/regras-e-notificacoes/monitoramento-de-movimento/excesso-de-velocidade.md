# Excesso de velocidade

## Visão geral

O objetivo da regra de detecção de excesso de velocidade é ajudar as empresas a aprimorar suas medidas gerais de segurança, monitorando e tratando os eventos de excesso de velocidade. Isso garante a conformidade com os limites de velocidade, promove um comportamento de direção responsável entre os funcionários e reduz o risco de acidentes. A plataforma oferece dois métodos de detecção de excesso de velocidade:

### Método I. Velocidade detectada pela plataforma

Esse método se baseia em dados de velocidade de rastreadores GPS para identificar o excesso de velocidade. A plataforma analisa os dados de velocidade dos pacotes de dados do GPS para verificar se o limite de velocidade especificado foi excedido. Embora esse método seja menos preciso do que o excesso de velocidade detectado pelo dispositivo, ele pode ser usado com qualquer rastreador GPS que informe a velocidade. É uma opção adequada para dispositivos que não podem detectar nativamente eventos de excesso de velocidade.

### Método II. Aceleração detectada por hardware

Esse método usa o hardware do rastreador GPS para detectar o excesso de velocidade. O próprio dispositivo calcula quando ocorre um evento de excesso de velocidade usando comandos remotos ou o software de configuração do dispositivo. Em seguida, a plataforma recebe notificações do dispositivo com base nesses cálculos. Esse método é altamente preciso e funciona com a maioria dos rastreadores modernos que podem enviar eventos de excesso de velocidade diretamente para a plataforma.

## Configurações de regras

#### Limite de velocidade, excesso de velocidade detectado pela plataforma

A configuração do limite de velocidade define o limite no qual a regra é acionada. Quando a plataforma recebe dados de velocidade do dispositivo, ela compara esse valor com o limite especificado. Se a velocidade exceder o limite, a plataforma gera um alerta de excesso de velocidade.

#### Limite de velocidade, excesso de velocidade detectado por hardware

Para eventos de excesso de velocidade detectados pelo dispositivo, não há configuração específica nas Regras e Notificações. Em vez disso, use o widget Device Settings (Configurações do dispositivo) para configurar remotamente o limite de velocidade no lado do dispositivo.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Requisitos de hardware e processamento de eventos**
  - **Excesso de velocidade detectado pela plataforma**: Essa regra pode ser aplicada à maioria dos rastreadores que enviam dados de velocidade em seus pacotes. A regra é processada na nuvem, onde a plataforma usa os dados de velocidade dos pacotes do dispositivo para determinar se o limite de velocidade foi excedido. O alerta tem um cronômetro de reinicialização de 15 minutos, o que significa que o alerta não será acionado mais do que uma vez a cada 15 minutos. Se ocorrer um evento enquanto a regra estiver aguardando a redefinição, a plataforma omitirá o evento, inclusive nos relatórios.
  - **Excesso de velocidade Detectado por hardware**: Essa regra só é aplicável a rastreadores que suportam o envio de eventos de velocidade baseados em hardware. O próprio dispositivo processa a regra, e a plataforma gera notificações com base nos cálculos feitos pelo hardware. O alerta tem um cronômetro de reinicialização de 1 minuto, o que significa que o alerta não será acionado mais de uma vez a cada minuto. Se ocorrer um evento enquanto a regra estiver aguardando a redefinição, a plataforma omitirá o evento, inclusive nos relatórios.

- **Vários rastreadores**: A regra permite a seleção de vários rastreadores em uma única regra, possibilitando o monitoramento abrangente de vários veículos ou dispositivos.
- **GPS à deriva**: O sistema pode gerar um alerta de excesso de velocidade mesmo que ocorra um desvio de GPS. Embora as coordenadas de GPS inválidas sejam filtradas, pequenos desvios de GPS ainda podem aparecer na trilha. No entanto, a plataforma oferece vários métodos para minimizar essas ocorrências, dependendo da funcionalidade do modelo do rastreador. Para obter informações detalhadas sobre como evitar desvios de GPS, consulte o manual do dispositivo. Isso garante uma detecção de eventos mais precisa e confiável, aumentando a eficácia geral do monitoramento.