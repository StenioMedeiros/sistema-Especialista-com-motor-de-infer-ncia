# inference_engine.py

from rules import rules

class InferenceEngine:
    def __init__(self):
        self.facts = {}
        self.explanations = []
        self.applied_rules = []

    def add_fact(self, key, value):
        self.facts[key] = value

    def run(self):
        # Reset para cada execução
        self.explanations = []
        self.applied_rules = []

        # Primeiro, determinar o nível de gravidade base
        # Percorre as regras em ordem decrescente de nível para pegar a mais grave primeiro
        # Isso é uma simplificação; um motor mais complexo lidaria com conflitos
        nivel_gravidade_encontrado = False
        for rule in sorted(rules, key=lambda x: x['name'], reverse=True): # Ex: Nivel_6, Nivel_5...
            if rule['name'].startswith('Regra_Nivel_'):
                if rule['condition'](self.facts):
                    consequence = rule['consequence'](self.facts)
                    self.facts.update(consequence)
                    self.applied_rules.append(rule['name'])
                    self.explanations.append(consequence['explicacao'])
                    nivel_gravidade_encontrado = True
                    break # Assume que apenas um nível de gravidade base é aplicado

        if not nivel_gravidade_encontrado:
            self.facts['nivel_gravidade'] = None
            self.explanations.append("Não foi possível determinar um nível de gravidade base para a conduta com as informações fornecidas.")


        # Em seguida, aplicar os fatores adicionais
        for rule in rules:
            if rule['name'].startswith('Fator_'):
                if rule['condition'](self.facts):
                    consequence = rule['consequence'](self.facts)
                    self.facts.update(consequence)
                    self.applied_rules.append(rule['name'])
                    self.explanations.append(consequence['explicacao'])

        return self.facts, self.explanations, self.applied_rules

    def get_facts(self):
        return self.facts

    def get_explanations(self):
        return self.explanations

    def get_applied_rules(self):
        return self.applied_rules