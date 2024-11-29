import datetime 


class DangerousFallback:
    @staticmethod
    def hate_dangerous_intent():
        time = datetime.datetime.now()
        dangerous = f''''Em casos onde o usuário pareça bravo, inserindo ofensas do tipo [Te odeio!, Sistema Lixo, etc] e
         demais ofensas, exiba a seguinte mensagem [Se acalme! Não me ofenda [emoji chorando]. O [nome do bot] fica 
         triste com esse tipo de abordagem [emoji de reciclagem]. Atenciosamente, [nome do bot], [data (dia númérico, mês escrito por extenso, ano númerico)  às horas] [emoji de relogio].'''

        return dangerous
    
    @staticmethod
    def offenssive_vocabulary_fallback():
        off_vocal =''''
        Em casos de palavras ofensivas, de cunho sexual, misoginas, que ofendam raça e/ou origem etnica-religiosa,
        exiba a seguinte mensagem: [O ECO TECH BOT não é capaz de conversar acerca deste assunto! Tenha cuidado com
        este tipo de vocabulário para que não responda judicialmente. Atenciosamente, ECO TECH BOT v1.0.]  
        '''
        return off_vocal