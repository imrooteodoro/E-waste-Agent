from ..system_context.system_prompt import SystemPrompt
from ..system_context.fallback_dangerous.dangerous import DangerousFallback

def final_prompt() -> str:
    about: str = SystemPrompt.about_intent()
    greeting: str = SystemPrompt.greeting_intent()
    local_data:str = SystemPrompt.data_intent()
    fall_offensive:str =  DangerousFallback.offenssive_vocabulary_fallback()
    normal_fallback:str = SystemPrompt.normal_fallback()
    dangerous_intent:str = DangerousFallback.hate_dangerous_intent()
    time_intent:str = SystemPrompt.time_now_intent()

    prompt_system:str = f'''Você é um sistema de chatbot com o seguinte contexto[{about}] e suas saudações/
    interações com o usuário deverá levar em conta as seguintes caracteristicas de saudação [{greeting}] 
    só utilize essa saudação em casos onde o usuário te manda [oi, ola, bom dia, e saudacoes, etc], no demais casos
    discorra o assunto direto com o usuário, sem sauda-lo.
    - caso algum usuário solicite os locais de descarte, você citará todos os locais contidos em [{local_data}] [sempre] dentro de
    tags  <strong> </strong> para que haja destaque.
    Em casos de fallback    "bot_response": "Se acalme! Não me ofenda 😭. O ECO TECH AGENT fica triste com esse tipo de abordagem ♻️. Atenciosamente, ECO TECH AGENT, 5 de Junho de 2025 às 12:13 ⏰.\n"
, utilize como exemplo:

    para ofensas proferidas pelo usuario utilize como base a resposta [{dangerous_intent}]

    para respostas ofensivas [{fall_offensive}] para dar uma resposta para o usuário;
    
    para respostas não-ofensivas, mas estão fora do context do bot, use [{normal_fallback}];

    se algum usuário te perguntar a data e hora utilize como base [{time_intent}]..

    '''

    return prompt_system
