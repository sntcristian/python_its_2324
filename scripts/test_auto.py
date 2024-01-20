import unittest

class Auto:
    def __init__(self, marca, modello, velocita_max):
        self.marca = marca
        self.modello = modello
        self.velocita = 0
        self.velocita_max = velocita_max

    def accelera(self, incremento):
        self.velocita += incremento
        if self.velocita > self.velocita_max:
            self.velocita = self.velocita_max

# Classe di test per la classe Auto
class TestAuto(unittest.TestCase):

    def test_accelera_entro_limite(self):
        # Verifica che la velocità dell'auto aumenti correttamente entro il limite massimo
        auto = Auto("Toyota", "Corolla", 150)
        auto.accelera(50)
        self.assertEqual(auto.velocita, 50)

    def test_accelera_oltre_limite(self):
        # Verifica che la velocità dell'auto non superi mai il limite massimo
        auto = Auto("Honda", "Civic", 120)
        auto.accelera(150)
        self.assertEqual(auto.velocita, 120)

if __name__ == '__main__':
    unittest.main()