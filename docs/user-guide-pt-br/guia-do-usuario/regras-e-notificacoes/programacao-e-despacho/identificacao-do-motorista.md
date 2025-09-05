# Identificação do motorista

## Visão geral

A regra "Identificação do motorista" foi criada para ajudar os gerentes de frota a monitorar e controlar o uso do veículo por meio da identificação precisa dos motoristas. Essa regra garante que somente motoristas autorizados possam operar veículos, rastreia qual motorista está ao volante e registra a duração e as condições de cada sessão de direção. Ela aumenta a eficiência operacional, melhora a responsabilidade e apoia a conformidade com os protocolos de segurança.

A regra opera usando os recursos integrados do dispositivo para verificar a identidade do motorista diretamente na fonte. As informações autorizadas do motorista são armazenadas na memória interna do dispositivo. Quando um motorista usa um iButton, uma chave RFID ou o reconhecimento facial por meio de uma câmera inteligente para se autenticar, o dispositivo verifica sua identidade no local. A plataforma então registra esses eventos de identificação, gerando alertas em tempo real, relatórios detalhados e notificações, conforme necessário.

**Casos de uso de aplicativos:**

- **Veículos compartilhados:** Rastreie e gerencie vários motoristas usando o mesmo veículo.
- **Segurança:** Restrinja a operação do veículo apenas ao pessoal autorizado, com alertas em tempo real para tentativas não autorizadas.
- **Conformidade:** Garantir que a operação do veículo esteja em conformidade com as políticas e os regulamentos da empresa.
- **Eficiência:** Reduza os erros e agilize o processo de identificação do motorista, especialmente em ambientes de alta pressão, com o reconhecimento baseado em câmera.

## Configurações de regras

Não são necessárias outras configurações específicas do Rule.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Identificação do motorista" tem um cronômetro de reinicialização de 5 segundos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 5 segundos. Se ocorrer um evento enquanto a regra estiver no período de reinicialização, a plataforma omitirá o alerta, garantindo que as notificações e os relatórios permaneçam claros e gerenciáveis.
- **Vários dispositivos:** Os usuários podem aplicar essa regra a vários rastreadores, desde que eles suportem "Identificação do motorista" por meio de eventos de RFID, iButton ou câmera. Isso permite monitorar eventos de identificação do motorista em vários veículos ou dispositivos, garantindo uma cobertura abrangente.
- **Processamento de eventos independente de GPS:** A plataforma processará e exibirá eventos de identificação do motorista mesmo que o pacote de dados não tenha coordenadas de GPS válidas. Esses eventos são registrados independentemente de ocorrerem dentro de uma delimitação geográfica definida. Nesse caso, as configurações de geofence interna/externa são ignoradas para garantir que nenhum evento crítico seja perdido.

## Veja também

- [**Regra de troca de motorista**](mudanca-de-motorista.md) - A regra se concentra no registro de quando um motorista diferente assume o controle do veículo, com a plataforma comparando os dados do motorista atual e anterior para detectar alterações e gerar relatórios após o fato.