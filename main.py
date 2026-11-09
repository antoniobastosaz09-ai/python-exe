def tuplas2():
    turmas_por_periodo = {
        (2026, 1): ["logica de programação", "Estrutura de dados"],

        (2026, 2): ["Fundamentos de python", "aplicação web", "Banco de dados", 
        "Desenvolvimento web", "redes de computadores", "segurança de informação"],

        (2027, 1): ["Inteligencia artificial", "Prompt", "fake news"],
    }
    periodo = (2027, 1)
    print(turmas_por_periodo[periodo]);

tuplas2()