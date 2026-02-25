# Veículos

Os veículos na Navixy são essenciais para rastrear e gerenciar sua frota. Eles permitem que você monitore vários aspectos, como localização, consumo de combustível, cronogramas de manutenção e desempenho geral da frota, permitindo operações eficientes e melhores tomadas de decisão.

## Guia Veículos

A guia "Vehicles" (Veículos) apresenta uma visão geral detalhada de todos os veículos de sua frota. As informações são organizadas em formato de tabela, complementadas por um menu visual no lado direito da tela. Aqui, você pode adicionar ou editar facilmente os detalhes do veículo, associá-los a depósitos específicos e vinculá-los a rastreadores que foram ativados na plataforma.

### Adição de um novo veículo

Para adicionar um novo veículo, basta pressionar o botão **+** botão. Você também tem a opção de carregar uma imagem do veículo para facilitar a identificação.

- **Guia principal:** Insira informações essenciais sobre o veículo, incluindo etiquetas e quaisquer notas relevantes.
- **Guia de especificações:** Forneça especificações detalhadas, como as dimensões do veículo, o tamanho da distância entre eixos, o número de rodas, a velocidade permitida, a disponibilidade do reboque e o ano de fabricação.
- **Registro de combustível:** Registre informações relacionadas ao combustível, incluindo tipo de combustível, capacidade do tanque e taxa de consumo por 100 km (ou milhas). Esses dados são cruciais para gerar relatórios precisos de consumo de combustível.
- **Guia de seguros:** Insira os detalhes do seguro do veículo, incluindo o número da apólice e a data de validade.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Consumo de combustível no perfil do veículo e sua função nos relatórios de combustível

Na Navixy, a configuração do **Consumo de combustível** no perfil do veículo é uma etapa essencial para rastrear e informar o uso de combustível em sua frota com base na quilometragem percorrida, sem depender de dados OBDII ou de sensores de combustível especializados.

Esse parâmetro é normalmente definido em termos de litros por 100 quilômetros (L/100 km) ou milhas por galão (MPG), dependendo da sua preferência regional.

#### Como o consumo de combustível é usado nos relatórios de combustível

1. **Estimativa do uso de combustível:**
  - O valor de consumo de combustível inserido no perfil do veículo serve como uma linha de base para estimar o uso de combustível de um veículo em uma determinada distância. Por exemplo, se um veículo estiver definido para consumir 10 L/100 km, o sistema estimará que ele usa 10 litros de combustível a cada 100 quilômetros percorridos.
2. **Cálculo dos custos esperados de combustível:**
  - A Navixy usa a taxa de consumo de combustível definida junto com a quilometragem registrada para calcular os custos de combustível esperados. Ao inserir o preço por litro ou galão nas configurações, o sistema pode gerar relatórios que estimam quanto você deve gastar com combustível, o que ajuda no orçamento e no planejamento financeiro.
3. **Comparação com dados reais de combustível:**
  - Quando combinada com dados de sensores de nível de combustível, a Navixy pode comparar o consumo de combustível estimado com o uso real de combustível. Essa comparação ajuda a identificar discrepâncias, como roubo de combustível, ineficiências no comportamento do motorista ou problemas com o motor do veículo que podem levar a um consumo de combustível maior do que o esperado.

### Importação de veículos

Se você tiver uma frota grande e precisar criar perfis para vários veículos, é mais eficiente importar todas as informações de uma só vez usando um único arquivo, em vez de criar perfis de veículos um a um. Os dados devem estar nos formatos de arquivo XLS, XLSX ou CSV.

Para importar perfis de veículos:

1. Abra o aplicativo "Fleet management" (Gerenciamento de frota), clique em "Add vehicle" (Adicionar veículo) e selecione "Import from Excel file" (Importar do arquivo Excel).
2. Na janela de importação, você encontrará um arquivo de exemplo do Excel que pode ser usado como modelo.
3. Certifique-se de que as colunas em seu arquivo correspondam aos campos corretos no sistema de rastreamento, inserindo os campos de cabeçalho apropriados. Isso pode ser feito antes da importação ou durante o processo.
4. No arquivo carregado, você precisará especificar informações importantes, como
  - Nome
  - Placa de identificação
  - TipoDepois de preencher o formulário, salve o arquivo em seu computador.

Para carregar o arquivo no sistema:

1. Clique no botão "Select" (Selecionar), localize seu arquivo e clique em "Next" (Avançar).
2. Você será solicitado a revisar os campos do cabeçalho. Se tudo estiver correto, clique em "Next" novamente.
3. Se algum campo estiver incorreto, o sistema solicitará que você o corrija. Se algum campo obrigatório estiver vazio, essa informação não será importada.
4. Quando as informações estiverem corretas, a importação será concluída com êxito e os novos perfis de veículos aparecerão no aplicativo "Fleet management" (Gerenciamento de frota).