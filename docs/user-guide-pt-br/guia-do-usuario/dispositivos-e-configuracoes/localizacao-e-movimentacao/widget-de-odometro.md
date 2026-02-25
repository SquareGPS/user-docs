# Widget de odômetro

O **Widget de odômetro** permite monitorar a quilometragem de um veículo em tempo real. As leituras de quilometragem podem ser derivadas de dados recebidos por meio de um dispositivo de rastreamento GPS ou do barramento CAN. Além disso, a função de odômetro se integra com o [Manutenção da frota](../../gerenciamento-de-frotas/manutencao.md) permitindo que você agende serviços de manutenção para um veículo e receba lembretes em tempo hábil.

![image-20240815-181307.png](attachments/image-20240815-181307.png)

## Ativação do odômetro

Para ativar o odômetro:

1. Abra a seção "Devices and settings" (Dispositivos e configurações), selecione o objeto desejado e navegue até o widget Odometer (Odômetro).
2. Clique no botão "Add odometer" (Adicionar odômetro).
3. Escolha a fonte de dados apropriada. Fontes adicionais podem se tornar disponíveis após a criação de um sensor de medição de quilometragem.
4. Defina o valor inicial da milhagem.
5. Pressione "Salvar".

## Correção do odômetro

- **Fator de correção.** É possível definir um fator de correção para ajustar automaticamente as leituras do odômetro para cima ou para baixo. Digite um valor percentual no campo "Correction" (Correção). Um valor positivo aumentará as leituras do odômetro, enquanto um valor negativo as diminuirá com base no sensor de entrada.
- **Atualizando o valor.** Você também pode atualizar o valor do odômetro sempre que necessário. Os valores anteriores do odômetro podem ser visualizados gerando o "Relatório sobre todos os eventos" no aplicativo Relatórios.
- **Acesso rápido na visualização de objetos.** Para acesso rápido, o valor do odômetro pode ser acessado e configurado no widget dedicado do [Visualização detalhada do objeto](../../rastreamento-por-gps/lista-de-objetos/visualizacao-detalhada-do-objeto.md).

## Alteração das origens do odômetro

Os tipos de fontes de odômetro que podem ser usados dependem do modelo específico do dispositivo. Compreender e utilizar várias fontes pode aumentar a precisão do rastreamento da quilometragem do seu veículo.

Para adicionar fontes de odômetro adicionais:

1. **Crie um novo sensor de medição:** Dependendo dos recursos do seu dispositivo, você pode criar sensores como o CAN Mileage ou o hardware mileage. Esses sensores coletam dados diretamente dos sistemas do seu veículo, garantindo leituras precisas da quilometragem.
2. **Integração com o widget Odômetro:** Depois de criar o sensor, ele aparecerá como uma opção no widget Odômetro dentro da plataforma Navixy. Isso permite que você escolha a fonte mais apropriada para seus dados de quilometragem.

Ao aproveitar diferentes fontes de odômetro, você pode aumentar a confiabilidade do rastreamento de quilometragem, o que é especialmente útil para a programação de manutenção e relatórios precisos. Compreender os diferentes tipos de fontes e como integrá-las ao seu sistema é fundamental para otimizar a configuração da telemática.