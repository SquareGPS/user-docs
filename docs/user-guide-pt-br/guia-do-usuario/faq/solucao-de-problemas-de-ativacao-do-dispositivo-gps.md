# Solução de problemas de ativação do dispositivo GPS

A ativação de dispositivos de rastreamento GPS na plataforma Navixy é geralmente simples graças a [ativação automática do dispositivo](../inicio-rapido/ativar-o-dispositivo-gps.md). No entanto, se você encontrar problemas, este guia o ajudará a solucionar problemas comuns de ativação de dispositivos.

### **As configurações de fuso horário do dispositivo são diferentes de UTC+0h**

Certifique-se de que os dispositivos de rastreamento GPS estejam configurados para UTC+0h para evitar a má interpretação dos dados pelo servidor Navixy. Reconfigure todos os dispositivos configurados manualmente ou conectados anteriormente para UTC+0h antes da ativação na Navixy.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**Questão:**  
Quando o software do servidor Navixy recebe dados de um dispositivo de rastreamento GPS, os dados vêm com um registro de data e hora. O servidor processa esses dados com base nas preferências de fuso horário do usuário, garantindo detalhes precisos da trilha e relatórios em diferentes fusos horários. No entanto, o servidor espera que todos os dados do dispositivo estejam em UTC+0h. Dispositivos configurados manualmente ou dispositivos conectados anteriormente a outra plataforma podem ter um fuso horário diferente, fazendo com que a Navixy interprete incorretamente os registros de data e hora, podendo marcar os dados como desatualizados ou defeituosos.

**Solução:**  
Para o processamento e exibição precisos dos dados, todos os dispositivos de rastreamento GPS devem ser configurados para UTC+0h. Se o dispositivo não estiver configurado para UTC+0h, o servidor da Navixy poderá interpretar os dados incorretamente, afetando a confiabilidade dos detalhes da trilha e dos relatórios.

**Recomendações para solução de problemas:**

1. Certifique-se de que o dispositivo esteja configurado para UTC+0h antes de ativá-lo na Navixy.
2. Evite definir o fuso horário local no dispositivo.

### O dispositivo está desligado ou não tem conexão GSM

Verifique se o dispositivo está ligado e conectado à rede GSM. Isso pode ser feito verificando o status de energia do dispositivo e verificando se ele está registrado na rede GSM. Se possível, envie um SMS de teste para confirmar que o dispositivo está recebendo mensagens corretamente.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**Questão:**

Quando o servidor Navixy tenta se comunicar com um dispositivo de rastreamento GPS, o dispositivo deve estar ligado e conectado à rede GSM. Se o dispositivo estiver desligado ou não tiver uma conexão GSM, os comandos de ativação não poderão ser entregues, fazendo com que o dispositivo pareça estar off-line ou sem resposta.

**Solução:**

Para garantir a comunicação adequada entre o servidor Navixy e o dispositivo de rastreamento GPS, verifique se o dispositivo está ligado e tem uma conexão GSM estável. Isso permite que o servidor receba e processe os dados corretamente.

**Recomendações para solução de problemas:**

- Se você tiver acesso físico ao dispositivo, verifique os indicadores LED para confirmar se ele está ligado e conectado à rede GSM.
- Envie um SMS para o dispositivo com confirmação de entrega para verificar o registro GSM. Se a entrega do SMS falhar, o dispositivo não está registrado na rede GSM. Talvez seja necessário enviar um SMS para o dispositivo por meio do portal do SIM para verificar.

### O saldo do cartão SIM é baixo ou não há serviço de Internet

Verifique se o cartão SIM tem saldo suficiente e se o serviço de Internet está ativado para que o dispositivo se conecte à plataforma. Verifique o saldo do cartão SIM e verifique se ele tem fundos suficientes para suportar o uso de dados da Internet. Além disso, confirme se o plano de dados do cartão SIM inclui tráfego de Internet adequado para manter uma conexão estável com a plataforma.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**Questão:**  
Durante o processo de ativação do dispositivo, um dispositivo de rastreamento tenta se conectar à plataforma Navixy e transmitir seus dados de localização pela Internet. Se o cartão SIM do dispositivo não tiver saldo suficiente ou tiver esgotado os limites de tráfego da Internet, o dispositivo não poderá se conectar à plataforma. Isso resulta em uma falha no envio de dados de localização e outras informações essenciais, tornando o dispositivo de rastreamento não funcional.

**Solução:**  
Para garantir conectividade e transmissão de dados ininterruptas, verifique se o cartão SIM usado no dispositivo de rastreamento tem saldo e tráfego GPRS adequados. Monitore e recarregue regularmente o saldo do cartão SIM para evitar problemas de conectividade.

**Recomendações para solução de problemas:**

- Verifique o saldo do cartão SIM para garantir que ele tenha fundos suficientes para suportar o acesso à Internet. Verifique se o plano do cartão SIM inclui dados de Internet suficientes para atender às necessidades de comunicação do dispositivo.
- Certifique-se de que as configurações de APN estejam configuradas corretamente em seu dispositivo. Obtenha as configurações corretas de APN do seu provedor de rede celular, que normalmente incluem o nome do APN, o nome de usuário e a senha. Geralmente, eles podem ser encontrados no site do provedor ou entrando em contato com o suporte ao cliente.
- Se os problemas de conectividade persistirem, entre em contato com o provedor do cartão SIM para confirmar se não há problemas relacionados à rede que afetem o tráfego da Internet.

### Número de telefone ou IMEI inserido incorretamente

Verifique o IMEI e o número de telefone inseridos durante a ativação para garantir a precisão. Verifique novamente cada dígito do IMEI e do número de telefone em relação à documentação ou etiqueta do dispositivo para garantir que não haja erros. Corrija todas as discrepâncias para evitar problemas de ativação e garantir uma comunicação bem-sucedida com a plataforma.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**Questão:**

Ao ativar um dispositivo na plataforma Navixy, um IMEI ou número de telefone incorreto pode causar falha na ativação. Esse erro geralmente ocorre devido a um erro de digitação ou à inserção incorreta dos detalhes do dispositivo, o que leva a uma comunicação malsucedida entre o dispositivo e o servidor.

**Solução:**

Para garantir que a ativação seja bem-sucedida, verifique novamente o IMEI e o número de telefone inseridos para o dispositivo. Confirme se todos os dígitos estão corretos e correspondem às informações do dispositivo.

**Recomendações para solução de problemas:**

- Verifique o IMEI e o número do telefone verificando novamente a documentação ou a etiqueta do dispositivo.
- Se a ativação falhar, exclua o dispositivo e repita a ativação, reinserindo cuidadosamente o IMEI e o número do telefone para corrigir possíveis erros.

### A configuração é protegida por senha ou número mestre

Se o dispositivo tiver configurações personalizadas, como senhas ou números de telefone mestre, isso pode impedir a configuração automática pela Navixy, levando a falhas de ativação. Remova todas as senhas personalizadas ou números mestres antes de tentar a ativação automática.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**Questão:**  
Durante a ativação do dispositivo, a plataforma Navixy envia comandos SMS de configuração para o dispositivo a partir do número de telefone de serviço. Se o dispositivo tiver sido previamente configurado para receber comandos de configuração de um número mestre dedicado ou se uma senha personalizada tiver sido definida, esses comandos poderão falhar, levando a uma ativação malsucedida.

**Solução:**  
Para permitir a ativação automática, remova todas as senhas personalizadas ou números mestres do dispositivo. Como alternativa, configure manualmente o dispositivo usando os comandos de ativação apropriados.

**Recomendações para solução de problemas:**

- Remova todas as senhas personalizadas ou números mestres do dispositivo antes de tentar a ativação automática.
- Se a ativação automática falhar, [configurar manualmente](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) o dispositivo usando os comandos de ativação fornecidos.

### Dispositivo não suportado ou modificação de dispositivo

Certifique-se de que seu dispositivo esteja listado entre aqueles [suportado pela Navixy](https://navixy.com/devices/). Se você não tiver certeza do fabricante e/ou do modelo, consulte o fornecedor do dispositivo. Também é recomendável atualizar o firmware do dispositivo para a versão mais recente.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**Questão:**  
Ao ativar um dispositivo de rastreamento GPS na plataforma Navixy, é importante que o modelo do dispositivo seja identificado e indicado corretamente durante a ativação. Se o dispositivo não for identificado corretamente, os dados enviados pelo dispositivo podem não ser analisados corretamente ou podem ser mal interpretados. Além disso, a versão do firmware para o mesmo modelo pode estar desatualizada ou ser uma versão personalizada, causando problemas de compatibilidade.

**Solução:**  
Para resolver esses problemas, verifique se seu dispositivo está na lista de dispositivos compatíveis e se ele tem a versão mais recente do firmware. Se o seu dispositivo não estiver na lista de modelos compatíveis ou tiver uma versão de firmware personalizada, entre em contato com seu provedor de serviços para obter suporte.

**Recomendações para solução de problemas:**

- Consulte nossa lista de dispositivos compatíveis.
- Atualize o firmware do dispositivo para a versão mais recente.
- Se o dispositivo não for compatível ou usar uma versão de firmware personalizada, entre em contato com a equipe de suporte técnico do seu [provedor de serviços.](../inicio-rapido/provedor-de-servicos.md)

### Teltonika e Ruptela lideram o problema de espaço com ativação automática

Garanta a configuração adequada dos dispositivos Teltonika e Ruptela para evitar problemas com espaços à esquerda nos comandos SMS. Configure os dispositivos [manualmente](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) ou verifique com seu provedor de serviços a possibilidade de usar outro gateway de SMS otimizado para comunicação M2M.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Click here to expand...

**Questão:**  
Durante a ativação automática dos dispositivos Teltonika e Ruptela, os usuários podem encontrar problemas devido à remoção dos espaços iniciais por alguns gateways de SMS. Esses dispositivos esperam um usuário e uma senha antes do comando, como `<login> <password> command`. Quando o login e a senha não são definidos (como recomendado), isso resulta em espaços duplos à esquerda `command`. Alguns gateways de SMS, não otimizados para comunicação M2M, cortam esses espaços, fazendo com que os comandos não sejam reconhecidos pelos dispositivos.

**Solução:**  
Para resolver esse problema, entre em contato com o provedor de serviços para substituir o gateway de SMS ou configure manualmente esses dispositivos por meio do software de configuração Teltonika ou Ruptela usando o IP do servidor Navixy e os detalhes da porta.

**Recomendações para solução de problemas:**

- [Configurar manualmente os dispositivos](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) usando o software de configuração.
- Entre em contato com o seu provedor de serviços para usar um gateway de SMS otimizado para comunicação M2M que preserva os espaços principais.

### O cartão SIM não tem número de telefone

[Processo de ativação automática do dispositivo](../inicio-rapido/ativar-o-dispositivo-gps.md) requer a inserção do número de telefone de um cartão SIM, mas os cartões SIM para comunicação M2M podem não ter um. Nesse caso, [configurar manualmente o dispositivo](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) e insira o IMEI do dispositivo (ou qualquer conjunto arbitrário de dígitos) como o número do telefone na caixa de diálogo de ativação. Como alternativa, entre em contato com o provedor de serviços para solicitar a integração com a plataforma MVNO para habilitar a comunicação usando ICCID.

![](https://squaregps.atlassian.net/wiki/images/icons/grey_arrow_down.png)

Leia mais

**Questão:**

Ao usar cartões SIM M2M de provedores MVNO, eles geralmente não têm números de telefone associados. Em vez disso, esses cartões SIM são identificados por meio de outros identificadores, mais comumente o ICCID. Como resultado, os comandos de configuração não podem ser enviados por meio de um gateway SMS comum, como acontece com os cartões SIM normais. Isso leva a desafios na ativação e na comunicação do dispositivo.

**Solução:**

Para resolver esse problema, você tem duas opções: [configurar manualmente o dispositivo](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) e coloque o IMEI do dispositivo (ou qualquer conjunto arbitrário de dígitos) como o número do telefone na caixa de diálogo de ativação, ou entre em contato com o seu [provedor de serviços](../inicio-rapido/provedor-de-servicos.md) para solicitar a integração com a plataforma MVNO, permitindo a comunicação bidirecional por SMS usando ICCID em vez de um número de telefone.

**Recomendações para solução de problemas:**

- [Configurar manualmente o dispositivo](https://squaregps.atlassian.net/wiki/spaces/USERDOCSOLD/pages/2909016770/Manual+device+activation) e insira o IMEI do dispositivo como o número do telefone na caixa de diálogo de ativação.
- [Entre em contato com o provedor do servidor](../inicio-rapido/provedor-de-servicos.md) para solicitar a integração com a plataforma MVNO para permitir a comunicação usando ICCID.

## Veja também

- [Guia de ativação do dispositivo MQTT](https://squaregps.atlassian.net/wiki/spaces/SC/pages/2732589133/Activate+Your+MQTT+Device+on+Navixy)