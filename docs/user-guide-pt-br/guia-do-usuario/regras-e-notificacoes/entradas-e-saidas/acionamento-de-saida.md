# Acionamento de saída

## Visão geral

Os dispositivos GPS para veículos geralmente vêm equipados com saídas configuráveis que permitem aos usuários controlar várias funções do veículo, como imobilização do motor, ativação de alarme e muito mais. Essas saídas podem ser gerenciadas diretamente do painel de controle em sua plataforma de telemática. Ao configurar uma regra para alterações no estado da saída, você pode receber notificações por meio da interface do usuário, aplicativo móvel, SMS ou e-mail sempre que houver uma modificação no status da saída.

Esse recurso garante que você permaneça informado sobre qualquer alteração no equipamento conectado ao seu dispositivo GPS. Seja para ativar ou desativar funções específicas, essa regra oferece uma maneira confiável de monitorar e gerenciar o status das saídas do seu veículo.

Por exemplo, no gerenciamento de frotas, essa regra é particularmente útil para monitorar o status de um bloco de motor ou de um sistema de corte de combustível. Se um dispositivo GPS estiver configurado para controlar essas saídas, a regra poderá gerar alertas sempre que o bloco do motor for ativado ou desativado. Isso permite que os gerentes de frota garantam que as medidas de segurança estejam sendo aplicadas adequadamente e que o uso não autorizado do veículo seja evitado.

## Configurações de regras

#### Saída

Especifique a saída de hardware que deseja monitorar selecionando o número de saída apropriado. Consulte a documentação do fabricante do rastreador para determinar qual saída controla qual funcionalidade.

## Detalhes da operação do sistema

- **Alerta de evento independente de GPS:** Se a plataforma detectar um evento de alteração de saída (como uma mudança de 1 para 0 ou vice-versa) de um pacote de dados do rastreador sem coordenadas válidas, ela ainda contará o evento como válido e o exibirá. Isso se aplica independentemente de o evento ter ocorrido dentro ou fora de uma geocerca, pois a lógica de geocerca dentro/fora é ignorada para garantir que eventos potencialmente importantes não sejam esquecidos.
- **Alertas seletivos:** Se quiser receber alertas apenas para alterações específicas de saída, como de "OFF para ON" e não de "ON para OFF", você pode fazer isso limpando o texto de notificação para o estado de saída indesejado nas configurações.
- **Reiniciar o cronômetro:** O alerta "Outputs Triggering" tem um cronômetro de reinicialização de 10 segundos, o que significa que ele não será acionado com mais frequência do que uma vez a cada 10 segundos. Se outro evento ocorrer durante o período de reinicialização, ele será omitido da plataforma, inclusive nos relatórios.
- **Vários dispositivos:** Você pode atribuir vários rastreadores a essa regra, com cada rastreador utilizando o mesmo número de saída especificado nas configurações da regra. Por exemplo, se você selecionar a saída nº 2, a regra o notificará sempre que qualquer um dos rastreadores selecionados informar uma alteração na saída nº 2.