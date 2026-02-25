# Relatório de sensores de medição

O **Relatório de sensores de medição** O Navixy foi projetado para fornecer dados detalhados de sensores de medição configurados ou sensores virtuais com um método de cálculo de valor de origem em um período selecionado.

Esse relatório permite que os usuários visualizem informações gráficas e estatísticas dos sensores de seus dispositivos, auxiliando no monitoramento e na tomada de decisões eficazes.

## Requisitos para gerar o relatório

Para gerar com sucesso o **Relatório de sensores de medição**As seguintes condições devem ser atendidas:

- **Compatibilidade de dispositivos:** Certifique-se de que o dispositivo seja compatível com a leitura de sensor necessária na plataforma. Você pode verificar isso consultando a lista de entradas compatíveis com o modelo específico.
- **Transmissão de dados ativa:** O dispositivo e seus sensores devem estar configurados corretamente e transmitindo dados ativamente.
- **Sensores virtuais:** [Sensores virtuais](../../dispositivos-e-configuracoes/sensores-de-veiculos/sensores-virtuais.md) deve ter um método de cálculo de valor de origem e fornecer valores numéricos à plataforma.
- **Configuração do sensor:** Os sensores de medição devem ser configurados corretamente na plataforma.

## Parâmetros do relatório

O relatório usa vários parâmetros para adaptar o resultado às suas necessidades:

- **Detalhes do intervalo de tempo:** Exibe as leituras recebidas em incrementos de 5, 30 minutos, 1, 3 ou 6 horas na tabela de detalhes de dados.
- **Eixo X no gráfico:** Escolha se deseja exibir as informações por tempo ou quilometragem.
- **Dados suaves:** Aplique suavização ao gráfico para filtrar os valores de pico e calcular a média dos dados quando houver uma variação significativa.
- **Mostrar endereço:** Exibe o endereço recebido pela plataforma junto com os dados do sensor. O endereço mostrado corresponde à primeira leitura no segmento de detalhes.
- **Use o filtro inteligente:** Excluir dados de viagens curtas, definidas como viagens com menos de 300 metros e com menos de 4 pontos de dados enviados pelo dispositivo.

Para cada dispositivo, você deve selecionar o sensor para o qual deseja gerar o relatório. Somente os dispositivos com [medição](../../dispositivos-e-configuracoes/sensores-de-veiculos/measurement-sensors.md) ou [virtual](../../dispositivos-e-configuracoes/sensores-de-veiculos/sensores-virtuais.md) sensores estarão disponíveis na lista. Se você selecionar um sensor virtual de um tipo errado, o relatório indicará "Este não é um sensor de medição".

## Visualizações

### Gráfico com as leituras do sensor

O gráfico no relatório exibe leituras de medições ou de sensores virtuais em formato gráfico, ajudando-o a visualizar as tendências de dados ao longo do tempo ou da distância.

- **Passar o mouse sobre os pontos:** Ao passar o mouse sobre um ponto no gráfico, é possível visualizar a hora exata em que ele foi registrado e o valor do sensor. Se o eixo X estiver definido como quilometragem, você também verá a distância em que a leitura foi feita.

### Tabela com dados estatísticos

O relatório inclui uma tabela de dados estatísticos que fornece resumos diários das leituras do sensor.

**Colunas na tabela de dados estatísticos:**

- **Data:** A data específica para os dados registrados.
- **Mínimo (unidades de medida):** O valor mais baixo registrado pelo sensor nessa data.
- **Máximo (unidades de medida):** O valor mais alto registrado pelo sensor nessa data.
- **Valor médio (unidades de medida):** A média de todas as leituras do sensor para essa data.

Observação: As unidades de medida variam de acordo com as configurações do sensor.

### Tabela de detalhamento de dados

O **tabela de detalhamento de dados** apresenta as leituras do sensor em intervalos de tempo especificados, como a cada 30 minutos, a partir de um horário definido. Ele fornece uma visão detalhada dos dados do sensor, ajudando a identificar tendências ou problemas durante períodos específicos.

- **Interpretação da tabela:** Se aparecer "No data" (Sem dados), significa que nenhuma leitura foi recebida durante esse período. Isso pode ser devido ao fato de o dispositivo não estar transmitindo dados, ter sido desligado ou o sensor ter sido desconectado.