# Direção severa

## Visão geral

A regra de "direção severa" foi criada para ajudar as empresas a monitorar e melhorar o comportamento ao volante, garantindo uma operação mais segura do veículo e reduzindo o risco de acidentes. Essa regra é particularmente valiosa para frotas, empresas de aluguel de carros e operações de logística, em que a qualidade da direção afeta diretamente os custos de manutenção do veículo, a segurança e a satisfação do cliente. Ao detectar e responder a incidentes de condução severa, as empresas podem gerenciar melhor seus veículos, reduzir o desgaste e manter um alto padrão de serviço.

Essa regra funciona utilizando o acelerômetro integrado dos dispositivos para monitorar aceleração repentina, frenagem brusca e curvas acentuadas. Quando o dispositivo GPS detecta qualquer um desses eventos, ele envia os dados para a plataforma, que gera alertas e registra os incidentes para análise. Para usar essa regra, certifique-se de que o recurso de detecção de direção severa esteja configurado corretamente no Configurações do dispositivo ou configurador de rastreador.

## Configurações de regras

Certifique-se de que o recurso de condução severa esteja configurado no Dispositivos e configurações no menu Harsh Driving, especificamente no widget Harsh Driving, ou por meio da ferramenta de configuração do dispositivo. Uma vez configurado, os usuários podem criar e gerenciar a regra a partir da plataforma.

Nenhuma outra configuração específica é necessária para essa regra. Para obter configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Harsh Driving" tem um cronômetro de reinicialização de 10 segundos, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada 10 segundos. Se ocorrer um evento durante o período de reinicialização, a plataforma suprimirá o alerta para manter as notificações e os relatórios precisos e gerenciáveis.
- **Vários dispositivos:** Os usuários podem aplicar essa regra a vários rastreadores, desde que eles ofereçam suporte à detecção de direção severa e tenham esse recurso integrado à plataforma. Isso permite que os usuários monitorem incidentes de condução severa em vários veículos ou dispositivos de forma eficiente.
- **Processamento de eventos independente de GPS:** A plataforma processa e exibe eventos de direção severa mesmo que o pacote de dados não tenha coordenadas de GPS válidas. Esses eventos são registrados independentemente de ocorrerem dentro ou fora de uma delimitação geográfica designada. As configurações de geofence interna/externa são ignoradas nesse caso para garantir que nenhum evento crítico seja perdido.