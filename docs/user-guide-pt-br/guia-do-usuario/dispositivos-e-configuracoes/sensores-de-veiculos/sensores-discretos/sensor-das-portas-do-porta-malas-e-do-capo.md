# Sensor das portas, do porta-malas e do capô

# Estado das portas, do porta-malas e do capô

Não é necessária nenhuma configuração especial. Entretanto, vários fatores precisam ser considerados.

Em primeiro lugar, nem todos os modelos de carro transmitem essas informações por meio do barramento CAN. Infelizmente, só é possível descobrir isso por experiência própria ou solicitando documentação detalhada ao fabricante.

Em segundo lugar, devido a algumas peculiaridades do protocolo de transferência de dados do dispositivo, não será possível rastrear o status das portas, etc., até que o sistema receba o status "Open" (Aberto) pelo menos uma vez. Para a operação correta, recomendamos que você deixe o porta-malas, o capô e todas as portas abertas por vários minutos com o motor ligado.