# Widget de dados brutos

A ferramenta de exportação de dados brutos na Navixy permite que você baixe dados analisados e decodificados de qualquer rastreador GPS na plataforma em formato CSV. Esse recurso é essencial para diagnósticos de dispositivos, análise de dados e integração de dados com programas de IA/ML.

[![Raw data export tool](https://www.navixy.com/wp-content/uploads/2023/12/browser_a0qszuge3l.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_a0qszuge3l.png)

## Visão geral

Com a ferramenta de exportação de dados brutos, você pode:

- **Download de dados analisados** de qualquer rastreador GPS na plataforma.
- **Selecionar parâmetros específicos** para incluir em seu arquivo CSV, com uma função de pesquisa fácil de usar.
- **Acesso a dados históricos** sem a necessidade de ativar a economia de dados com antecedência.
- **Ajustar registros de data e hora** para o fuso horário de sua preferência, facilitando o gerenciamento de dados em diferentes regiões.

A saída dos dados brutos consiste em todas as informações decodificadas dos protocolos proprietários do modelo do dispositivo. Depois de decodificados, os dados são armazenados em um formato universal, incluindo detalhes importantes, como localização e leituras do sensor. Os dados são fornecidos em um formato de arquivo CSV para facilitar o acesso e a integração.

## Como usar a exportação de dados brutos

Comece indo para a seção "Devices and Settings" (Dispositivos e configurações) e localize o dispositivo. Em seguida, clique no botão "Export Data" (Exportar dados) no portlet "Raw Data" (Dados brutos).

[![Raw data export tool file configuration window](https://www.navixy.com/wp-content/uploads/2023/12/browser_ybwmnfdh8h.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_ybwmnfdh8h.png)

Isso abrirá a ferramenta "Raw data export" (Exportação de dados brutos). Escolha o intervalo de datas, o fuso horário e os parâmetros que devem ser incluídos em um arquivo csv.

Para evitar o fechamento acidental de janelas, a ferramenta "Raw Data Export" só pode ser fechada clicando-se no "X" no canto superior direito. Além disso, se você não tiver trocado de dispositivo ou atualizado a página, a ferramenta lembrará as configurações selecionadas anteriormente. Esse recurso facilita a revisão das configurações do rastreador GPS ou do sensor, o retorno e a continuação do trabalho.

### Seleção de um intervalo de datas

Você pode selecionar até os últimos 30 dias ou mais, dependendo do seu plano. As datas podem ser escolhidas clicando no calendário ou inserindo-as manualmente. Também é possível definir horários específicos. Aqui estão algumas opções de seleção rápida:

- Ontem
- Semana passada
- Últimos 30 dias

Clicar nessas opções definirá automaticamente o intervalo de datas apropriado.

Para simplificar o processo, um contador mostra quantos dias você selecionou. Se você tentar selecionar uma data com mais de 30 dias no passado, receberá uma mensagem e o botão de seleção será desativado.

### Escolha de um fuso horário

O fuso horário padrão é o fuso horário da conta do usuário, mas pode ser ajustado por:

- Escolher em uma lista de fusos horários disponíveis.
- Inserir o nome do fuso horário.
- Inserção do deslocamento do fuso horário (por exemplo, -8, +2).

### Seleção de parâmetros

Os parâmetros disponíveis variam de acordo com o modelo do dispositivo e incluem todos os parâmetros integrados à plataforma para cada modelo. Até 1.000 parâmetros podem ser selecionados por arquivo.

As opções para a seleção de parâmetros incluem:

- **Selecionar tudo**: Clique na caixa de seleção para selecionar todos os parâmetros.
- **Selecionar parâmetros específicos**: Use as caixas de seleção ao lado de cada parâmetro.
- **Pesquisa**: Localize parâmetros específicos digitando o nome ou parte do nome deles.

Para vários inputs do mesmo tipo, o sistema prioriza o input com o maior número de índice. Você pode especificar os índices a serem incluídos inserindo números separados por vírgulas ou definindo um intervalo usando um traço (por exemplo, "1-2, 4, 7").

É exibida uma contagem dos parâmetros selecionados, e cada parâmetro escolhido adicionará uma coluna ao arquivo CSV.

[![Raw data export tool file configuration window with chosen parameters](https://www.navixy.com/wp-content/uploads/2023/12/browser_imbnj05cft.png)

](https://www.navixy.com/wp-content/uploads/2023/12/browser_imbnj05cft.png)

## Como ler o arquivo de dados brutos

Depois de selecionar os parâmetros necessários, clique em "Download CSV" para fazer o download do arquivo.

- O arquivo pode ser aberto com qualquer editor de texto ou visualizador de tabelas que suporte o formato CSV. As colunas são separadas por vírgulas.
- O nome do arquivo inclui o ID do dispositivo, o rótulo do rastreador e o intervalo de data e hora especificado.
- Cada linha (a partir da segunda linha) representa uma mensagem enviada do dispositivo para a plataforma. A primeira linha contém a hora da mensagem no fuso horário escolhido, seguida pelos parâmetros selecionados.

[![Raw data file columns example](https://www.navixy.com/wp-content/uploads/2023/12/nvidia_share_xbgmryofhf.png)

](https://www.navixy.com/wp-content/uploads/2023/12/nvidia_share_xbgmryofhf.png)

Essa ferramenta é essencial para diagnósticos e análises, fornecendo insights detalhados sobre os dados de seu dispositivo.