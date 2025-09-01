# Relatório de horas do motor

O **Horas do motor** na Navixy fornece informações detalhadas sobre a duração do funcionamento do motor do seu veículo, tanto em movimento quanto em períodos de inatividade. Esse relatório é essencial para os gerentes de frota que precisam monitorar o uso do motor, otimizar a eficiência operacional e planejar cronogramas de manutenção. Veja abaixo um guia completo sobre como esse relatório funciona, os parâmetros envolvidos e como interpretar os dados.

## Visão geral

O relatório de horas do motor foi projetado para mostrar o tempo total em que o motor do veículo ficou ligado, segmentado em períodos de movimento e de marcha lenta. Esse relatório inclui vários recursos visuais importantes, como um gráfico de atividade por período e um gráfico de barras de atividade diária, para ajudá-lo a entender e analisar rapidamente os dados.

## Como funciona

O relatório calcula as horas do motor com base nos pontos de dados recebidos pela plataforma Navixy. Para obter cálculos precisos, as seguintes configurações e condições devem ser atendidas:

1. **Configuração do sensor de ignição:**
  - O sensor de ignição deve estar corretamente conectado ao dispositivo e registrar com precisão o status da ignição. Pode ser um sensor de ignição discreto ou um sensor virtual baseado em ignição na plataforma.
2. **Duração da ignição:**
  - A ignição deve ficar ligada por pelo menos 60 segundos para que o tempo seja registrado no relatório.
3. **Detecção de estacionamento:**
  - A plataforma usa as configurações de detecção de estacionamento para diferenciar entre as horas do motor gastas em movimento e em marcha lenta. Por exemplo, se a velocidade de detecção de estacionamento estiver definida para menos de 3 km/h e o veículo permanecer nessa velocidade ou abaixo dela por mais de 5 minutos, esse tempo será registrado como ocioso, não em movimento.
4. **Frequência do ponto de dados:**
  - A frequência com que seu dispositivo envia pontos de dados afeta a precisão do relatório. Atrasos na transmissão de dados podem levar a imprecisões, principalmente se o estado da ignição mudar, mas não for imediatamente relatado.

### Exemplo de cálculo

| Ponto | Tempo | Estado da ignição | Horas do motor |
| --- | --- | --- | --- |
| 1   | 16:00:00 | Desligado | 0 minutos |
| 2   | 16:01:00 | Em  | 0 minutos (a ignição estava desligada no último ponto) |
| 3   | 16:01:32 | Em  | 0 minutos (menos de 60 segundos) |
| 4   | 16:05:32 | Desligado | 4 minutos e 32 segundos |

## Parâmetros do relatório

O relatório Engine Hours inclui vários parâmetros configuráveis que permitem personalizar o resultado para atender às suas necessidades específicas:

- **Mostrar detalhes:** Fornece informações detalhadas sobre o local e o horário específicos em que o motor estava ligado.
- **Exibir resumo:** Mostra uma visão geral de todos os dispositivos. Você pode ativar ou desativar esse recurso, dependendo da necessidade de uma página de resumo.
- **Exibir apenas o resumo:** Agrega dados de vários rastreadores em um único resumo. Essa opção requer pelo menos dois dispositivos.
- **Use o filtro inteligente:** Exclui viagens curtas do relatório. Uma viagem é considerada curta se percorrer menos de 300 metros e o dispositivo transmitir menos de quatro pontos de dados.

## Visualizações

![image-20240815-010415.png](attachments/image-20240815-010415.png)

### Diagrama geral de atividades

- Esse diagrama fornece uma visão abrangente do tempo total em que o motor esteve ligado durante o período selecionado. Ele faz distinção entre o tempo em que o motor esteve desligado, o tempo gasto em movimento e o tempo gasto em marcha lenta.

### Histograma de atividade diária

- O histograma divide as horas do motor em segmentos diários, mostrando os tempos de movimento e de inatividade. Passar o mouse sobre cada dia fornece uma visão mais detalhada da atividade do motor naquele dia.

### Tabela de horas do motor

- A tabela apresenta dados diários detalhados, incluindo:
  - **Data:** O dia específico para o qual os dados são calculados.
  - **Horas do motor:** Total de horas de motor para o dia.
  - **Em movimento:** Tempo gasto em movimento e sua porcentagem do total de horas do motor.
  - **Marcha lenta:** Tempo gasto em marcha lenta e sua porcentagem do total de horas do motor.
  - **Intervalo médio:** A duração média do funcionamento do motor após cada evento de ignição ligada.
  - **Quilometragem:** A distância percorrida enquanto o motor estava funcionando.
  - **Velocidade média:** A velocidade média do dia.
  - **Intervalos:** O número de intervalos durante os quais o motor esteve ligado durante o dia.

> [!INFO]
> Se você notar uma discrepância entre a quilometragem no relatório de viagem e o relatório de horas do motor, verifique duas coisas:
> 1. Certifique-se de que a configuração do filtro inteligente seja aplicada de forma consistente em todos os relatórios. Inconsistências em seu uso podem causar discrepâncias.
> 2. Verifique se a ignição foi detectada durante todos os movimentos do veículo, comparando os horários de início e término da viagem com os dados de horas do motor.

## Interpretação do relatório

Para usar efetivamente o relatório de horas do motor, considere o seguinte:

- **Discrepâncias:** Se você notar uma discrepância entre a quilometragem no relatório de viagem e as horas do motor, verifique se o filtro inteligente foi aplicado de forma consistente em todos os relatórios e se a ignição foi detectada corretamente durante o movimento.
- **Análise de dados:** O relatório permite que você analise o uso do motor pelos funcionários, avalie a eficiência do veículo, estime os cronogramas de substituição, calcule os custos de depreciação e reconfigure os custos de combustível e lubrificante com base no tempo ocioso.