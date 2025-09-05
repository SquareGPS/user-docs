# Relatório de viagem

O **Relatório de viagem** A Navixy fornece uma análise abrangente do histórico de viagens do seu veículo, oferecendo informações sobre a distância percorrida, o tempo de viagem, a duração das paradas, as velocidades e o consumo de combustível.

Esse relatório é inestimável para os gerentes de frota que precisam monitorar o uso do veículo, calcular os custos operacionais e avaliar a eficiência da condução. Abaixo está um guia detalhado sobre como o Relatório de Viagens funciona, os parâmetros envolvidos e como interpretar os dados de forma eficaz.

![image-20240815-010251.png](attachments/image-20240815-010251.png)

## Visão geral

O relatório de viagem detalha cada viagem feita por seus veículos, incluindo horários de início e término, distâncias, velocidades e consumo de combustível. O relatório também oferece um resumo de todas as viagens durante o período selecionado, permitindo uma visão geral fácil do desempenho do veículo.

## Como o relatório pode ser útil

O Relatório de Viagem fornece informações valiosas que podem ser usadas de várias maneiras:

- **Análise operacional:** Ao analisar os padrões de uso do veículo, você pode avaliar as frequências, distâncias e durações das viagens. Esses dados são essenciais para calcular a depreciação e prever o uso futuro do veículo.
- **Gerenciamento de custos:** O relatório pode ajudar a identificar viagens inesperadas ou não autorizadas que podem resultar em aumento de despesas. Ele também fornece informações detalhadas sobre o consumo de combustível, permitindo que você avalie os custos com base em diferentes rotas e cargas.
- **Desempenho do motorista:** O relatório destaca o tempo que os motoristas passam em rotas específicas, suas velocidades média e máxima e quanto tempo os veículos permanecem ociosos após as viagens.
- **Avaliação da eficiência:** Você pode avaliar o uso de combustível para diferentes tipos de viagens, como viagens com muita carga e viagens leves ou sem carga, para otimizar o gasto de combustível.

## Parâmetros do relatório

O Relatório de viagem oferece vários parâmetros configuráveis para adequar o relatório às suas necessidades:

- **Exibir resumo:** Alterna a visibilidade de uma página de resumo que fornece uma visão geral de todos os dispositivos.
- **Exibir apenas o resumo:** Gera uma planilha de resumo para todos os dispositivos selecionados sem informações detalhadas sobre a viagem. Requer que pelo menos dois dispositivos sejam selecionados.
- **Dividir por paradas:** Separa as viagens com base nos intervalos de estacionamento. Se não for selecionado, o relatório considerará o primeiro ponto registrado do dia como o início da viagem e o último ponto registrado como o fim da viagem.
- **Mostrar duração da parada:** Exibe a duração do tempo de estacionamento após cada viagem.
- **Mostrar coordenadas:** Inclui coordenadas de GPS para os pontos inicial e final de cada viagem, além de endereços.
- **Use o filtro inteligente:** Exclui viagens breves (menos de 300 metros, menos de quatro pontos de dados ou em um raio pequeno) do relatório.
- **Agrupar por motoristas:** Organiza viagens por [motoristas](../../gerenciamento-de-frotas/motoristas.md). Se um motorista não foi designado durante o período do relatório, as viagens serão atribuídas a um motorista não identificado.

### Colunas do relatório

O relatório organiza as informações nas seguintes colunas:

| Nome da coluna | Descrição |
| --- | --- |
| **Início do movimento** | Detalhes de quando e onde a viagem começou, incluindo a hora e o endereço. Se as coordenadas estiverem ocultas, somente a hora e o endereço serão exibidos. |
| **Fim do movimento** | Mostra quando e onde a viagem foi concluída. Se a viagem terminar em uma cerca geográfica ou em um ponto de interesse, seu nome será incluído. |
| **Duração total das viagens** | Indica a distância total da viagem, conforme medida pelo GPS. |
| **Tempo de viagem** | Mostra o tempo total da viagem. |
| **Velocidade média** | A velocidade média durante a viagem. |
| **Velocidade máxima** | A velocidade máxima atingida durante a viagem, conforme registrada pelo dispositivo. |
| **Combustível consumido por norma** | O consumo de combustível estimado para a viagem com base em taxas padrão requer dados de consumo de combustível do veículo por 100 km no [perfil do veículo](../../gerenciamento-de-frotas/veiculos.md). |
| **Custo da viagem por norma** | Exibe o custo do combustível com base na taxa de consumo padrão fornecida no [perfil do veículo](../../gerenciamento-de-frotas/veiculos.md). |
| **Consumo de combustível (sensor)** | Mostra o consumo real de combustível se um sensor de combustível estiver instalado e transmitindo dados para a plataforma. O sensor deve medir em litros ou galões. |
| **Tempo de estacionamento** | Lista a duração do estacionamento entre essa viagem e a próxima. |

**Exemplo:**

Uma linha no relatório pode indicar:

- **Horário e local de início:** 7 de fevereiro de 2024, às 00:00:06, 6750 Putnam Drive, Highland-on-the-Lake, Cidade de Evans, Condado de Erie, Nova York, EUA, 14047.
- **Horário e local de término:** 7 de fevereiro de 2024, às 00:57:46, 49 Steinfeldt Road, Town of Lancaster, Nova York, EUA, 14086.
- **Distância percorrida:** 42,89 quilômetros.
- **Tempo de viagem:** 57 minutos e 40 segundos.
- **Velocidade máxima:** 59 km/h.
- **Velocidade média:** 45 km/h.
- **Consumo de combustível:** 3,4 litros (com base nas tarifas padrão), com um custo de US$ 12,86.

### Bloco de resumo

O relatório também fornece um resumo de todas as viagens durante o período selecionado. Por exemplo:

- **Total de viagens:** 34
- **Distância total:** 1514,9 quilômetros
- **Tempo total de viagem:** 33 horas, 56 minutos e 45 segundos
- **Velocidade máxima:** 59 km/h
- **Velocidade média:** 45 km/h
- **Consumo de combustível estimado:** 121,2 litros, custando US$ 454,50
- **Leitura do odômetro no final do período:** 762052,8 km