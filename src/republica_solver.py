import itertools

class RepublicaSolver:
    PENALIDADE_CONSECUTIVO = 10000

    def __init__(self, moradores, semanas, comodos, dificuldade, qtd_vagas, indisponibilidade):
        self.moradores = moradores
        self.semanas = semanas
        self.comodos = comodos
        self.dificuldade = dificuldade
        self.qtd_vagas = qtd_vagas
        self.indisponibilidade = indisponibilidade
        
        self.melhor_custo = float('inf')
        self.melhor_solucao = None
        self.solucoes_encontradas = 0

    def resolver(self):
        # 1. Math Check Básico (Vagas vs Moradores na semana)
        total_vagas_semanal = sum(self.qtd_vagas.values())
        total_moradores = len(self.moradores)
        
        print(f"--- Verificação Inicial ---")
        print(f"Vagas por semana: {total_vagas_semanal}")
        print(f"Moradores totais: {total_moradores}")
        
        # 2. Math Check Avançado (Gargalo por Cômodo)
        # Verifica se tem gente suficiente para cobrir a demanda específica de um cômodo ao longo de todas as semanas
        num_semanas = len(self.semanas)
        for comodo, vagas in self.qtd_vagas.items():
            demanda_total_comodo = vagas * num_semanas
            if demanda_total_comodo > total_moradores:
                print(f"ERRO CRÍTICO: O cômodo '{comodo}' precisa de {demanda_total_comodo} pessoas diferentes ao todo, mas só existem {total_moradores}.")
                return None, 0

        if total_vagas_semanal > total_moradores:
            print("ERRO CRÍTICO: Falta gente para cobrir a semana!")
            return None, 0

        self._backtrack(0, 0, 0, set(), set(), set(), [])
        return self.melhor_solucao, self.melhor_custo

    def _backtrack(self, semana_idx, comodo_idx, custo_atual, alocados_na_semana, alocados_globalmente, alocados_semana_anterior, alocacao_atual):
        # PODA
        if custo_atual >= self.melhor_custo:
           return

        # SUCESSO
        if semana_idx == len(self.semanas):
            # if custo_atual < self.melhor_custo:
            self.melhor_custo = custo_atual
            self.melhor_solucao = list(alocacao_atual)
            self.solucoes_encontradas += 1
            print(f"Solução encontrada! Custo: {self.melhor_custo}")
            return

        # PREPARAÇÃO
        nome_semana = self.semanas[semana_idx]
        nome_comodo = self.comodos[comodo_idx]
        vagas_necessarias = self.qtd_vagas[nome_comodo]
        
        # FILTRAGEM DE CANDIDATOS
        candidatos = []
        for morador in self.moradores:
            # Já trabalhou nesta semana?
            if morador in alocados_na_semana:
                continue
            # Já fez este cômodo em qualquer semana anterior?
            if (morador, nome_comodo) in alocados_globalmente:
                continue
            candidatos.append(morador)

        # Se não tem gente suficiente para este cômodo, volta.
        if len(candidatos) < vagas_necessarias:
            return

        # BRANCHING (Testar combinações)
        # Usa itertools para pegar grupos do tamanho exato das vagas (ex: duplas para a cozinha)
        for equipe in itertools.combinations(candidatos, vagas_necessarias):
            
            custo_equipe = 0
            for m in equipe:
                custo_individual = (self.dificuldade[nome_comodo] * self.indisponibilidade[nome_semana][m])

            # Se o morador trabalhou na semana passada, multiplica o peso!
                if m in alocados_semana_anterior:
                     custo_individual *= self.PENALIDADE_CONSECUTIVO
                
                custo_equipe += custo_individual

            # Atualizar estados
            novos_alocados_semana = alocados_na_semana.copy()
            novos_alocados_semana.update(equipe)
            
            novos_alocados_global = alocados_globalmente.copy()
            for m in equipe:
                novos_alocados_global.add((m, nome_comodo))

            nova_alocacao = list(alocacao_atual)
            for m in equipe:
                nova_alocacao.append({'semana': nome_semana, 'comodo': nome_comodo, 'morador': m})

            # Avançar índices
            prox_comodo = comodo_idx + 1
            prox_semana = semana_idx
            prox_set_semana = novos_alocados_semana

            # Lógica para atualizar o set da semana anterior
            prox_alocados_anterior = alocados_semana_anterior # Por padrão mantém o mesmo (se estivermos na mesma semana)

            if prox_comodo == len(self.comodos):
                prox_comodo = 0
                prox_semana += 1

                # O set "anterior" da próxima semana será quem trabalhou na semana atual
                prox_alocados_anterior = novos_alocados_semana
                
                prox_set_semana = set() # Nova semana, reseta alocação semanal
            else:
                prox_set_semana = novos_alocados_semana # Continua na mesma semana

            self._backtrack(prox_semana, prox_comodo, custo_atual + custo_equipe, prox_set_semana, novos_alocados_global, prox_alocados_anterior, nova_alocacao)

# ==============================================================================
# DADOS QUE FUNCIONAM (6 Moradores para 3 Semanas)
# ==============================================================================
if __name__ == "__main__":
    # Adicionei "Carla" para termos 6 pessoas.
    # Cozinha (2 vagas) * 3 Semanas = 6 pessoas necessárias. Agora fecha a conta!
    moradores = ["Joao", "Maria", "Pedro", "Ana", "Lucas", "Carla", "Marcos", "Nicole", "Sophia"]
    
    semanas = ["Semana1", "Semana2", "Semana3", "Semana4"]
    comodos = ["Sala", "Cozinha", "Banheiro"]
    
    # Pesos
    dificuldade = {"Sala": 2, "Cozinha": 5, "Banheiro": 8}
    qtd_vagas = {"Sala": 1, "Cozinha": 2, "Banheiro": 1} # Total 4 vagas/semana
    
    # Indisponibilidade (Adicionei a coluna da Carla)
    indisponibilidade = {
        "Semana1": {"Joao": 1, "Maria": 10, "Pedro": 5, "Ana": 2, "Lucas": 1, "Carla": 3, "Marcos": 7,"Nicole": 1, "Sophia": 2},
        "Semana2": {"Joao": 5, "Maria": 2, "Pedro": 10, "Ana": 1, "Lucas": 5, "Carla": 8, "Marcos": 8,"Nicole": 6, "Sophia": 5},
        "Semana3": {"Joao": 10, "Maria": 5, "Pedro": 1, "Ana": 5, "Lucas": 2, "Carla": 1, "Marcos": 2,"Nicole": 3,"Sophia": 7},
        "Semana4": {"Joao": 7, "Maria": 3, "Pedro": 4, "Ana": 1, "Lucas": 4, "Carla": 1, "Marcos": 4,"Nicole": 10, "Sophia": 9}
    }

    solver = RepublicaSolver(moradores, semanas, comodos, dificuldade, qtd_vagas, indisponibilidade)
    solucao, custo = solver.resolver()

    print("\n" + "="*40)
    if solucao:
        print(f"MELHOR ESCALA ENCONTRADA (Custo: {custo})")
        print("="*40)
        
        semana_atual = ""
        for item in solucao:
            if item['semana'] != semana_atual:
                semana_atual = item['semana']
                print(f"\n--- {semana_atual} ---")
            
            print(f"{item['comodo']:<10}: {item['morador']}")
    else:
        print("Infeasible: Ajuste o número de moradores ou diminua as semanas.")