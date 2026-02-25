# Direção distraída

## Visão geral

O recurso de direção distraída é um componente dos sistemas avançados de telemática, projetado para detectar e alertar os usuários quando os motoristas se envolvem em atividades de distração, como fumar ou usar um telefone celular.

Esse recurso dependente do dispositivo depende da configuração do hardware, normalmente câmeras de painel ou dispositivos GPS com câmeras, para identificar e relatar distrações. A plataforma processa esses eventos em tempo real e envia notificações, permitindo ações corretivas imediatas para aumentar a segurança nas estradas e promover um comportamento responsável ao dirigir.

Essa regra é dependente do dispositivo, o que significa que ela depende da configuração do hardware (normalmente câmeras de painel ou dispositivos GPS com recursos de câmera) para detectar e relatar eventos de distração. A plataforma processa esses eventos e envia notificações ao usuário de acordo.

## Configurações de regras

Como essa regra é baseada na configuração do hardware, é necessário um mínimo de configuração na própria plataforma. A chave é garantir que os dispositivos selecionados estejam configurados para detectar e relatar eventos de distração do motorista.

Para configurações comuns, consulte [Regras e notificações](../../regras-e-notificacoes.md).

## Detalhes da operação do sistema

- **Reiniciar o cronômetro:** O alerta "Distração ao volante" é gerenciado por um cronômetro de reinicialização de 10 segundos, garantindo que os alertas não sejam gerados com mais frequência do que uma vez a cada 10 segundos. Se um evento de distração ocorrer durante o período de reinicialização, ele será omitido da plataforma e dos relatórios.
- **Vários dispositivos:** Os usuários podem configurar essa regra em vários rastreadores, desde que eles suportem eventos de "Distração ao volante" e tenham esse recurso integrado à plataforma. Isso permite um monitoramento abrangente em vários veículos ou dispositivos, garantindo uma supervisão consistente do comportamento do motorista.
- **Alerta de evento independente de GPS:** A plataforma registrará e exibirá eventos de "Direção distraída" mesmo que o pacote de dados não tenha coordenadas de GPS válidas. As configurações de geocerca interna/externa são ignoradas nesses casos, pois o sistema prioriza a exibição de eventos potencialmente críticos para garantir que nenhuma informação importante seja perdida.