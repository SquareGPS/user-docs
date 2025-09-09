# Fadiga ao dirigir

## Visão geral

A regra de direção por fadiga é um recurso essencial da plataforma de telemática, projetado para aumentar a segurança nas estradas, detectando e alertando as equipes de despacho quando forem identificados sinais de fadiga do motorista. Utilizando câmeras de rastreamento avançadas, o sistema monitora continuamente os motoristas em busca de indicadores de sonolência ou fadiga, que são os principais contribuintes para os acidentes rodoviários.

Quando a fadiga é detectada, um alerta imediato é enviado à central, permitindo uma intervenção imediata, como a organização de intervalos para descanso ou o fornecimento do suporte necessário. A implementação dessa regra não só ajuda a evitar acidentes e a reduzir perdas operacionais, mas também prioriza o bem-estar do motorista e promove práticas de direção seguras.

## Configurações de regras

Como essa regra depende do hardware, a configuração é mínima na própria plataforma. O principal requisito é garantir que os rastreadores selecionados estejam equipados para suportar e detectar eventos de Fadiga ao volante.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Condução com fadiga" é controlado por um cronômetro de reinicialização de 5 segundos, garantindo que os alertas não sejam acionados com mais frequência do que uma vez a cada 5 segundos. Se um evento de fadiga for detectado durante esse período de reinicialização, ele será omitido da plataforma e dos relatórios.

- **Vários dispositivos:** Essa regra permite a seleção de vários dispositivos para monitoramento. Os dispositivos selecionados devem ser compatíveis com eventos de Fadiga do Motorista e ter esse recurso integrado à plataforma. Isso permite um monitoramento abrangente em vários veículos ou dispositivos, garantindo que a fadiga do motorista seja monitorada e gerenciada de forma consistente.

- **Alerta de evento independente de GPS:** A plataforma registrará e exibirá eventos de Fadiga ao volante mesmo que o pacote de dados não tenha coordenadas de GPS válidas. Nesses casos, as configurações de geocerca interna/externa são ignoradas, pois o sistema prioriza a exibição de eventos críticos, garantindo que nenhuma informação crucial seja ignorada.