class Utils:
    # Classe auxiliar, apenas guarda alguns valores que são utilizados na main
    def __init__(self):
        self.acumula_delta_t = 0
        self.angulo = 0.0
        self.n_frames = 0
        self.tempo = 5
        self.tempo_da_animacao = 0
        self.tempo_total = 0
        self.animando = False
        self.desenha = False