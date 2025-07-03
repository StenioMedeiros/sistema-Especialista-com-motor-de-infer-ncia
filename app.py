# app.py
import streamlit as st
from inference_engine import InferenceEngine
import google.generativeai as genai
import os
from dotenv import load_dotenv # <-- Importe esta linha

st.set_page_config(layout="wide")

# =========================================================================
# Área para configurar sua chave de API do Gemini
#
# Opção 1 (Recomendado): Usar variável de ambiente via .env
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY") # Obtém a chave da variável de ambiente

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("Erro: A variável de ambiente GOOGLE_API_KEY não está configurada no arquivo .env ou no ambiente.")
    # Você pode querer sair ou desabilitar funcionalidades da IA aqui
    # st.stop() # Interrompe a execução do app se a chave não estiver configurada

# =========================================================================

# Inicializa o modelo Gemini Pro FORA da função para evitar recarregamento
# Apenas inicializa se a chave da API foi configurada com sucesso
gemini_model = None
if GOOGLE_API_KEY:
    try:
        gemini_model = genai.GenerativeModel('gemini-2.5-pro')
    except Exception as e:
        st.error(f"Erro ao inicializar o modelo Gemini: {e}. Verifique se sua chave de API está correta e a conexão.")
        gemini_model = None # Garante que seja None em caso de falha

def get_keywords_from_gemini(text_description):
    """
    Esta função irá interagir com a API do Google Gemini para extrair palavras-chave.
    """
    if not text_description.strip():
        return []

    if gemini_model is None:
        st.warning("Modelo Gemini não disponível. Não foi possível extrair palavras-chave com a IA. Verifique a configuração da chave de API.")
        return []

    try:
        prompt = f"""
        Analise o seguinte texto em português e extraia as palavras-chave mais relevantes que descrevam o tipo de conduta, a intensidade e qualquer aspecto relacionado a comportamento, assédio, discriminação, ou a ausência deles. Foque em termos que ajudem a classificar a gravidade ou aceitabilidade da ação.
        Liste as palavras-chave separadas por vírgulas.

        Texto: "{text_description}"

        Palavras-chave:
        """
        response = gemini_model.generate_content(prompt)
        raw_keywords_string = response.text.strip()

        keywords = [k.strip().lower() for k in raw_keywords_string.split(',') if k.strip()]
        return keywords

    except Exception as e:
        st.error(f"Erro ao extrair palavras-chave com a API Gemini: {e}. Isso pode ocorrer por problemas de conexão, limites de uso ou conteúdo inadequado. Tente novamente ou ajuste a descrição.")
        return []

def main():
    st.title("**Sistema Especialista para Avaliação de Gravidade de Condutas UFAPE** ")
    st.write("Este sistema avalia a gravidade de condutas no ambiente universitário, com foco em assédio e discriminação, baseado na Matriz de Avaliação da Gravidade de Condutas da UFAPE.")

    st.header("Informações da Conduta")

    descricao_conduta = st.text_area("Descreva a conduta:", height=150, help="Descreva detalhadamente o comportamento ou fala a ser avaliado. Inclua palavras-chave que possam indicar o nível de ofensa.")

    grok_extracted_keywords = [] # Mantido para compatibilidade com 'rules.py'
    if descricao_conduta:
        with st.spinner("Analisando descrição com IA..."):
            grok_extracted_keywords = get_keywords_from_gemini(descricao_conduta)
        if grok_extracted_keywords:
            st.info(f"**Palavras-chave detectadas pela IA:** {', '.join(grok_extracted_keywords)}")
        else:
            st.info("Nenhuma palavra-chave relevante detectada pela IA para a descrição fornecida.")


    st.subheader("**Fatores Adicionais para Avaliação** ")

    st.markdown("---")
    st.markdown("**Fator 1: Contexto em que ocorreu a conduta** ")
    contexto_formal_informal = st.radio(
        "A conduta ocorreu em um ambiente formal ou informal?",
        ('Formal', 'Informal', 'Não se aplica'),
        index=2
    )
    contexto_publico_privado = st.radio(
        "A conduta foi um ato público ou privado?",
        ('Público', 'Privado', 'Não se aplica'),
        index=2
    )
    st.markdown("---")

    st.markdown("**Fator 2: Histórico dos envolvidos**")
    historico_envolvidos = st.radio(
        "Existe histórico de condutas inapropriadas envolvendo a mesma pessoa?",
        ('Primário', 'Reincidente', 'Frequente', 'Não se aplica'),
        index=3,
        help="Primário: Sem histórico anterior. Reincidente: Histórico de condutas similares. Frequente: Múltiplas reincidências que indicam um padrão comportamental."
    )
    st.markdown("---")

    st.markdown("**Fator 3: Frequência das Condutas** ")
    frequencia_conduta = st.radio(
        "Qual a frequência da conduta?",
        ('Isolado', 'Ocasional', 'Repetitivo e/ou Insistente', 'Não se aplica'),
        index=3,
        help="Isolado: Incidente único. Ocasional: Ocorre esporadicamente, mais de uma vez. Repetitivo e/ou Insistente: Acontece frequentemente."
    )
    st.markdown("---")

    st.markdown("**Fator 4: Impacto na Vítima**")
    impacto_vitima = st.radio(
        "Qual o impacto percebido na vítima?",
        ('Impacto não-significativo', 'Impacto negativo considerável', 'Impacto Negativo Intenso', 'Não se aplica'),
        index=3,
        help="Não-significativo: Não teve maiores repercussões. Negativo considerável: Consequências de curto prazo e não muito graves. Negativo Intenso: Consequências de médio e longo prazo, sofrimento físico, emocional ou psicológico."
    )
    st.markdown("---")

    st.markdown("**Fator 5: Sinais Não-Verbais**")
    sinais_nao_verbais = st.radio(
        "Houve sinais não-verbais que intensificaram a conduta?",
        ('Neutro', 'Agravado', 'Não se aplica'),
        index=2,
        help="Neutro: Sem sinais significativos. Agravado: Sinais não-verbais que intensificam a negatividade da conduta."
    )
    st.markdown("---")

    st.markdown("**Fator 6: Intenção Percebida** ")
    intencao_percebida = st.radio(
        "Qual a intenção percebida da conduta?",
        ('Acidental', 'Negligente', 'Intencional', 'Não se aplica'),
        index=3,
        help="Acidental: Sem intenção clara de causar dano. Negligente: Falta de consideração pelas consequências. Intencional: Evidente objetivo de causar dano ou desconforto. "
    )
    st.markdown("---")

    st.markdown("**Fator 7: Relação Hierárquica**")
    relacao_hierarquica = st.radio(
        "Qual a relação hierárquica entre os envolvidos?",
        ('Mesmo nível hierárquico ou nível hierárquico não relevante', 'Superior - subordinado direto', 'Superior - subordinado indireto', 'Não se aplica'),
        index=3,
        help="Superior - subordinado direto: Agressor é superior direto da vítima. Superior - subordinado indireto: Agressor tem posição superior, mas não é o superior direto."
    )
    st.markdown("---")


    if st.button("Avaliar Conduta"):
        engine = InferenceEngine()

        conduta_data = {
            'descricao': descricao_conduta,
            'grok_keywords': grok_extracted_keywords # Passa as palavras-chave do Gemini
        }

        if contexto_formal_informal != 'Não se aplica':
            conduta_data['contexto_formal_informal'] = contexto_formal_informal
        if contexto_publico_privado != 'Não se aplica':
            conduta_data['contexto_publico_privado'] = contexto_publico_privado
        if historico_envolvidos != 'Não se aplica':
            conduta_data['historico_envolvidos'] = historico_envolvidos
        if frequencia_conduta != 'Não se aplica':
            conduta_data['frequencia_conduta'] = frequencia_conduta
        if impacto_vitima != 'Não se aplica':
            conduta_data['impacto_vitima'] = impacto_vitima
        if sinais_nao_verbais != 'Não se aplica':
            conduta_data['sinais_nao_verbais'] = sinais_nao_verbais
        if intencao_percebida != 'Não se aplica':
            conduta_data['intencao_percebida'] = intencao_percebida
        if relacao_hierarquica != 'Não se aplica':
            conduta_data['relacao_hierarquica'] = relacao_hierarquica

        for key, value in conduta_data.items():
            engine.add_fact(key, value)

        final_facts, explanations, applied_rules = engine.run()

        st.subheader("Resultado da Avaliação:")
        nivel_final = final_facts.get('nivel_gravidade')

        if nivel_final is not None:
            st.markdown(f"**Nível de Gravidade da Conduta: NÍVEL {nivel_final}**")
        else:
            st.warning("Não foi possível determinar o nível de gravidade da conduta com as informações fornecidas.")

        st.subheader("Explicações Detalhadas:")
        if explanations:
            for exp in explanations:
                st.info(exp)
        else:
            st.info("Nenhuma explicação detalhada gerada para esta conduta.")

        st.subheader("Regras Aplicadas:")
        if applied_rules:
            for rule_name in applied_rules:
                st.code(rule_name)
        else:
            st.info("Nenhuma regra foi aplicada para esta conduta.")

        st.markdown("""
            ---
            **Observação Importante:** Este sistema é uma ferramenta de apoio baseada na Matriz de Avaliação da Gravidade de Condutas da UFAPE.
            Ele oferece uma classificação inicial e explicações fundamentadas nas regras definidas.
            Para casos reais, a avaliação final e as ações cabíveis devem sempre ser conduzidas por profissionais especializados e seguir os procedimentos oficiais da instituição.
            A UFAPE busca garantir ambientes seguros e inclusivos, construídos por meio de escolhas e atitudes diárias.
        """)

if __name__ == '__main__':
    main()