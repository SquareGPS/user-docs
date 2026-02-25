# Inatividade de movimento

## Visão geral

O alerta "Movement Inactivity" (Inatividade de movimento), também conhecido como alerta "No Movement" (Sem movimento), foi projetado para aumentar a segurança e a proteção. Ele dispara um alerta quando nenhum movimento é detectado por um período prolongado, contando com dispositivos GPS equipados com acelerômetros e os recursos de firmware necessários.

Essa regra é especialmente útil em três áreas principais:

1. **Ativos móveis**: Aplicado a equipamentos como máquinas de construção e reboques, o alerta "Movement inactivity" (Inatividade de movimento) ajuda a monitorar paradas não autorizadas ou ociosidade prolongada, garantindo que os ativos estejam em uso conforme pretendido e evitando possíveis roubos ou uso indevido.
2. **Monitoramento de carga**: Para cargas em trânsito, esse alerta pode ser crucial para detectar quando as mercadorias foram deixadas sem supervisão ou estão em risco, permitindo a intervenção oportuna para proteger remessas valiosas.
3. **Segurança pessoal**: Para indivíduos que usam rastreadores GPS pessoais, como idosos ou trabalhadores solitários, o alerta "Movement inactivity" (Inatividade de movimento) oferece uma camada adicional de proteção ao sinalizar uma possível emergência quando o dispositivo detecta uma falta incomum de movimento, solicitando uma resposta para garantir o bem-estar do indivíduo.

## Configurações de regras

Como a "Inatividade de movimento" é um evento detectado pelo dispositivo, não há configuração específica nas Regras e notificações. Em vez disso, use o widget Device Settings (Configurações do dispositivo) para configurar remotamente o limite de velocidade no dispositivo.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro.** O alerta "Movement inactivity" (Inatividade de movimento) tem um cronômetro de reinicialização de 1 minuto, o que significa que o alerta não será acionado com mais frequência do que uma vez a cada minuto. Se ocorrer um evento enquanto a regra estiver aguardando a reinicialização, a plataforma omitirá o evento, inclusive nos relatórios.
- **Alerta de evento independente de GPS.** O sistema pode gerar um alerta de "Inatividade de movimento" mesmo que os dados de GPS não estejam disponíveis. Se forem detectadas coordenadas de GPS inválidas, a plataforma ainda registrará e exibirá o evento, independentemente de ele ter ocorrido dentro ou fora das cercas geográficas designadas. A lógica das configurações de geocerca interna/externa é ignorada nesses casos para garantir que eventos críticos não sejam perdidos.