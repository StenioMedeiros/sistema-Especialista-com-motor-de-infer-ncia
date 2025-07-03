# rules.py

rules = []

# Regras para os Níveis de Gravidade
# NÍVEL 1: EM GERAL, NÃO OFENSIVO [cite: 65, 66]
rules.append({
    'name': 'Regra_Nivel_1',
    'condition': lambda conduta:
        "não ofensivo" in conduta['descricao'].lower() or \
        "socialmente aceitável" in conduta['descricao'].lower() or \
        "comentários neutros" in conduta['descricao'].lower() or \
        "elogios simples" in conduta['descricao'].lower() or \
        "discussões sobre assuntos neutros" in conduta['descricao'].lower() or \
        # NOVO: Adiciona a verificação das palavras-chave do Gemini
        any(keyword in ['não ofensivo', 'socialmente aceitável', 'neutro', 'elogio', 'discussão pacífica'] for keyword in conduta.get('grok_keywords', [])),
    'consequence': lambda conduta: {
        'nivel_gravidade': 1,
        'explicacao': "A conduta se enquadra no Nível 1 (Em Geral, Não Ofensivo) porque é considerada socialmente aceitável e cotidiana, sem implicar julgamentos ou avaliações baseadas em características pessoais ou culturais. Exemplos incluem comentários sobre corte de cabelo ou elogios por uma roupa nova."
    }
})

# NÍVEL 2: CONSTRANGEDOR E LEVEMENTE OFENSIVO [cite: 73, 74]
rules.append({
    'name': 'Regra_Nivel_2',
    'condition': lambda conduta:
        "constrangedor" in conduta['descricao'].lower() or \
        "levemente ofensivo" in conduta['descricao'].lower() or \
        "desconforto" in conduta['descricao'].lower() or \
        "embaraço" in conduta['descricao'].lower() or \
        "estereótipos sutis" in conduta['descricao'].lower() or \
        "desrespeitoso" in conduta['descricao'].lower() or \
        "insensível" in conduta['descricao'].lower() or \
        "perguntas sobre habilidades de trabalho baseadas em estereótipos de gênero" in conduta['descricao'].lower() or \
        "comentários sobre aptidão física ou aparência de pessoas de certos grupos étnicos" in conduta['descricao'].lower() or \
        # NOVO: Adiciona a verificação das palavras-chave do Gemini
        any(keyword in ['constrangedor', 'levemente ofensivo', 'desconforto', 'embaraço', 'estereótipos sutis', 'desrespeitoso', 'insensível'] for keyword in conduta.get('grok_keywords', [])),
    'consequence': lambda conduta: {
        'nivel_gravidade': 2,
        'explicacao': "A conduta se enquadra no Nível 2 (Constrangedor e Levemente Ofensivo) pois, embora não intencione prejudicar, cria desconforto ou embaraço, evocando estereótipos ou preconceitos sutis. Isso pode começar a erodir o sentimento de segurança. Exemplos incluem perguntas sobre habilidades de trabalho baseadas em estereótipos de gênero."
    }
})

# NÍVEL 3: OFENSIVO [cite: 81]
rules.append({
    'name': 'Regra_Nivel_3',
    'condition': lambda conduta:
        "ofensivo" in conduta['descricao'].lower() or \
        "falta de consideração pelas diferenças" in conduta['descricao'].lower() or \
        "reforçam negativamente estereótipos" in conduta['descricao'].lower() or \
        "preconceitos" in conduta['descricao'].lower() or \
        "reproduzem estruturas de privilégio" in conduta['descricao'].lower() or \
        "piadas sobre orientação sexual" in conduta['descricao'].lower() or \
        "apelidos pejorativos com marcas raciais ou de gênero" in conduta['descricao'].lower() or \
        "retirar oportunidades de trabalho por questões de gênero" in conduta['descricao'].lower() or \
        # NOVO: Adiciona a verificação das palavras-chave do Gemini
        any(keyword in ['ofensivo', 'preconceito', 'estereótipo', 'privilégio', 'piada', 'apelido pejorativo'] for keyword in conduta.get('grok_keywords', [])),
    'consequence': lambda conduta: {
        'nivel_gravidade': 3,
        'explicacao': "A conduta se enquadra no Nível 3 (Ofensivo) por manifestar falta de consideração pelas diferenças individuais, sociais e culturais, reforçando estereótipos ou preconceitos. Afeta significativamente o bem-estar emocional do indivíduo alvo. Exemplos incluem piadas sobre orientação sexual ou uso de apelidos pejorativos."
    }
})

# NÍVEL 4: BASTANTE OFENSIVO [cite: 85, 86]
rules.append({
    'name': 'Regra_Nivel_4',
    'condition': lambda conduta:
        "bastante ofensivo" in conduta['descricao'].lower() or \
        "explicitamente humilhantes" in conduta['descricao'].lower() or \
        "degradantes" in conduta['descricao'].lower() or \
        "intencionais" in conduta['descricao'].lower() or \
        "insultar" in conduta['descricao'].lower() or \
        "diminuir a pessoa" in conduta['descricao'].lower() or \
        "toques não solicitados" in conduta['descricao'].lower() or \
        "danos emocionais substanciais" in conduta['descricao'].lower() or \
        "insultos diretos" in conduta['descricao'].lower() or \
        "comentários depreciativos sobre capacidade intelectual" in conduta['descricao'].lower() or \
        "humilhação ou ridicularização maliciosa" in conduta['descricao'].lower() or \
        "imitação ofensiva do sotaque" in conduta['descricao'].lower() or \
        # NOVO: Adiciona a verificação das palavras-chave do Gemini
        any(keyword in ['humilhante', 'degradante', 'intencional', 'insulto', 'toque não solicitado', 'dano emocional', 'ridicularização', 'depreciativo'] for keyword in conduta.get('grok_keywords', [])),
    'consequence': lambda conduta: {
        'nivel_gravidade': 4,
        'explicacao': "A conduta se enquadra no Nível 4 (Bastante Ofensivo) por ser explicitamente humilhante ou degradante, frequentemente intencional. Inclui condutas fisicamente intrusivas como toques não solicitados, causando danos emocionais substanciais. Exemplos são insultos diretos ou humilhação maliciosa."
    }
})

# NÍVEL 5: AGRESSIVO E NÃO FISICAMENTE VIOLENTO [cite: 96, 97]
rules.append({
    'name': 'Regra_Nivel_5',
    'condition': lambda conduta:
        "agressivo e não fisicamente violento" in conduta['descricao'].lower() or \
        "ações persistentes ou degradantes baseadas em gênero, raça ou sexualidade" in conduta['descricao'].lower() or \
        "ambiente hostil e intimidador" in conduta['descricao'].lower() or \
        "avanços sexuais não solicitados" in conduta['descricao'].lower() or \
        "comentários racistas" in conduta['descricao'].lower() or \
        "compartilhamento ou armazenamento de material pornográfico no local de trabalho" in conduta['descricao'].lower() or \
        "sugestão de retaliação a não envolvimento sexual" in conduta['descricao'].lower() or \
        # NOVO: Adiciona a verificação das palavras-chave do Gemini
        any(keyword in ['agressivo', 'ambiente hostil', 'intimidador', 'assédio sexual', 'racista', 'material pornográfico', 'retaliação'] for keyword in conduta.get('grok_keywords', [])),
    'consequence': lambda conduta: {
        'nivel_gravidade': 5,
        'explicacao': "A conduta se enquadra no Nível 5 (Agressivo e Não Fisicamente Violento) por envolver ações persistentes ou degradantes baseadas em gênero, raça ou sexualidade, criando um ambiente hostil e intimidador. Exemplos incluem avanços sexuais não solicitados, comentários racistas ou compartilhamento de material pornográfico no local de trabalho."
    }
})

# NÍVEL 6: AGRESSIVO E FISICAMENTE VIOLENTO [cite: 103, 104]
rules.append({
    'name': 'Regra_Nivel_6',
    'condition': lambda conduta:
        "agressivo e fisicamente violento" in conduta['descricao'].lower() or \
        "agressões físicas" in conduta['descricao'].lower() or \
        "ameaças de violência grave" in conduta['descricao'].lower() or \
        "coerção que coloque em risco a segurança física" in conduta['descricao'].lower() or \
        "ameaça direta à integridade física ou psicológica" in conduta['descricao'].lower() or \
        "qualquer forma de coerção ou violência física" in conduta['descricao'].lower() or \
        # NOVO: Adiciona a verificação das palavras-chave do Gemini
        any(keyword in ['violência física', 'agressão física', 'ameaça grave', 'coerção física', 'risco segurança'] for keyword in conduta.get('grok_keywords', [])),
    'consequence': lambda conduta: {
        'nivel_gravidade': 6,
        'explicacao': "A conduta se enquadra no Nível 6 (Agressivo e Fisicamente Violento), representando a forma mais extrema de conduta inapropriada, envolvendo agressões físicas, ameaças de violência grave ou qualquer forma de coerção que coloque em risco a segurança física. Isso tem um impacto devastador sobre as vítimas."
    }
})

# Regras para Fatores Adicionais (Exemplo - Fator 1: Contexto) [cite: 131, 133]
rules.append({
    'name': 'Fator_Contexto_Formal_Publico',
    'condition': lambda conduta:
        conduta.get('contexto_formal_informal') == 'Formal' and \
        conduta.get('contexto_publico_privado') == 'Público',
    'consequence': lambda conduta: {
        'agravante_contexto': True,
        'explicacao': "O contexto da conduta (Formal/Público) é um agravante, pois condutas discriminatórias em contextos formais ou públicos podem ser consideradas mais graves devido ao seu amplo impacto potencial e ao exemplo negativo que representam. "
    }
})

rules.append({
    'name': 'Fator_Contexto_Conotacao_Sexual_Privado',
    'condition': lambda conduta:
        "conotação sexual" in conduta['descricao'].lower() or \
        any(keyword in ['conotação sexual', 'sexualmente sugestivo'] for keyword in conduta.get('grok_keywords', [])) and \
        conduta.get('contexto_publico_privado') == 'Privado',
    'consequence': lambda conduta: {
        'agravante_contexto': True,
        'explicacao': "O contexto da conduta (conotação sexual/Privado) é um agravante, pois comportamentos inapropriados de conotação sexual ocorridos em salas fechadas ou locais isolados devem ser avaliados com maior gravidade, aumentando a sensação de vulnerabilidade da possível vítima. "
    }
})

# Regras para Fator 2: Histórico dos Envolvidos [cite: 152, 153]
rules.append({
    'name': 'Fator_Historico_Reincidente',
    'condition': lambda conduta:
        conduta.get('historico_envolvidos') == 'Reincidente',
    'consequence': lambda conduta: {
        'agravante_historico': True,
        'explicacao': "O histórico do envolvido é um agravante porque há histórico de condutas similares ou relacionadas, o que pode aumentar a gravidade da avaliação e sugerir a necessidade de intervenções mais severas. "
    }
})

rules.append({
    'name': 'Fator_Historico_Frequente',
    'condition': lambda conduta:
        conduta.get('historico_envolvidos') == 'Frequente',
    'consequence': lambda conduta: {
        'agravante_historico': True,
        'explicacao': "O histórico do envolvido é um agravante porque há múltiplas reincidências que indicam um padrão comportamental, o que pode aumentar a gravidade da avaliação e sugerir a necessidade de intervenções mais severas. "
    }
})

# Regras para Fator 3: Frequência das Condutas [cite: 174, 175]
rules.append({
    'name': 'Fator_Frequencia_Ocasional',
    'condition': lambda conduta:
        conduta.get('frequencia_conduta') == 'Ocasional',
    'consequence': lambda conduta: {
        'agravante_frequencia': True,
        'explicacao': "A frequência da conduta é um agravante, pois ocorre esporadicamente, mas mais de uma vez. Condutas recorrentes devem ser tratadas com mais seriedade. "
    }
})

rules.append({
    'name': 'Fator_Frequencia_Repetitivo_Insistente',
    'condition': lambda conduta:
        conduta.get('frequencia_conduta') == 'Repetitivo e/ou Insistente',
    'consequence': lambda conduta: {
        'agravante_frequencia': True,
        'explicacao': "A frequência da conduta é um agravante, pois acontece frequentemente. Condutas recorrentes devem ser tratadas com mais seriedade, devido ao seu potencial de criar um ambiente de trabalho hostil continuado. "
    }
})

# Regras para Fator 4: Impacto na Vítima [cite: 197, 198]
rules.append({
    'name': 'Fator_Impacto_Negativo_Consideravel',
    'condition': lambda conduta:
        conduta.get('impacto_vitima') == 'Impacto negativo considerável',
    'consequence': lambda conduta: {
        'agravante_impacto': True,
        'explicacao': "O impacto na vítima é um agravante, pois gerou consequências de curto prazo e não muito graves para a vítima."
    }
})

rules.append({
    'name': 'Fator_Impacto_Negativo_Intenso',
    'condition': lambda conduta:
        conduta.get('impacto_vitima') == 'Impacto Negativo Intenso',
    'consequence': lambda conduta: {
        'agravante_impacto': True,
        'explicacao': "O impacto na vítima é um agravante, pois gerou consequências de médio e longo prazo, causando sofrimento físico, emocional ou psicológico, impactando sua saúde e bem-estar. "
    }
})

# Regras para Fator 5: Sinais Não-Verbais [cite: 211, 212]
rules.append({
    'name': 'Fator_Sinais_Agravado',
    'condition': lambda conduta:
        conduta.get('sinais_nao_verbais') == 'Agravado',
    'consequence': lambda conduta: {
        'agravante_sinais': True,
        'explicacao': "Os sinais não-verbais são um agravante, pois intensificam a negatividade da conduta, sugerindo ameaça ou desprezo."
    }
})

# Regras para Fator 6: Intenção Percebida [cite: 224, 225, 227]
rules.append({
    'name': 'Fator_Intencao_Negligente',
    'condition': lambda conduta:
        conduta.get('intencao_percebida') == 'Negligente',
    'consequence': lambda conduta: {
        'agravante_intencao': True,
        'explicacao': "A intenção percebida é um agravante, pois demonstra falta de consideração pelas consequências."
    }
})

rules.append({
    'name': 'Fator_Intencao_Intencional',
    'condition': lambda conduta:
        conduta.get('intencao_percebida') == 'Intencional',
    'consequence': lambda conduta: {
        'agravante_intencao': True,
        'explicacao': "A intenção percebida é um agravante, pois houve evidente objetivo de causar dano ou desconforto. Condutas intencionais podem ser julgadas mais severamente."
    }
})

# Regras para Fator 7: Relação Hierárquica [cite: 252, 253]
rules.append({
    'name': 'Fator_Hierarquia_Superior_Subordinado_Direto',
    'condition': lambda conduta:
        conduta.get('relacao_hierarquica') == 'Superior - subordinado direto',
    'consequence': lambda conduta: {
        'agravante_hierarquia': True,
        'explicacao': "A relação hierárquica é um agravante, pois o agressor é superior direto da vítima, caracterizando uma clara relação de subordinação. A dinâmica de poder pode intensificar o impacto da conduta, e a dificuldade da vítima para se defender é maior."
    }
})

rules.append({
    'name': 'Fator_Hierarquia_Superior_Subordinado_Indireto',
    'condition': lambda conduta:
        conduta.get('relacao_hierarquica') == 'Superior - subordinado indireto',
    'consequence': lambda conduta: {
        'agravante_hierarquia': True,
        'explicacao': "A relação hierárquica é um agravante, pois o agressor tem uma posição superior, mesmo que não seja o superior direto da vítima, ainda assim possui algum grau de influência hierárquica. A dinâmica de poder pode intensificar o impacto da conduta."
    }
})