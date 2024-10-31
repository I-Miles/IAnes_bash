import unittest
from Main import carregar_conteudo, obter_parametros_usuario, recomenda_investimento, analise_melhor_json


class TestRecomendacaoInvestimento(unittest.TestCase):

    def test_recomenda_investimento_tecnologia(self):
        # Carrega os conteúdos JSON reais da pasta de dados
        conteudos_json = carregar_conteudo('C:/Users/CTDEV23/PycharmProjects/IAnes/DADOS')

        # Define os inputs do usuário para um projeto de TI
        inputs_usuario = {
            'tema': '1',  # Tecnologia da Informação
            'vertente': '1',  # Desenvolvimento de Software
            'num_colaboradores': '10',
            'responsavel': 'João Silva',
            'empresa': 'Empresa X',
            'projeto': 'Projeto Y',
            'orcamento': '100000',
            'extensao': 'Nacional',
            'tempo': '12',
            'lucro': '50000',
            'cnpj': '12345678901234',
            'publico_alvo': 'Público Z',
            'itens_financiaveis': 'Sim'
        }

        # Faz a recomendação de investimento com os inputs reais
        melhor_opcao, melhor_score, melhor_conteudo = recomenda_investimento(conteudos_json, inputs_usuario)

        # Verifica se foi identificada uma melhor opção
        self.assertIsNotNone(melhor_opcao, "Nenhuma opção de investimento recomendada.")
        self.assertGreater(melhor_score, 0, "O score da melhor opção deveria ser maior que zero.")

        # Analisa os índices do melhor JSON e seleciona o de melhor score
        melhor_index, melhor_index_score, melhor_url = analise_melhor_json(melhor_conteudo, inputs_usuario)

        # Verificações finais para garantir que o índice e URL do melhor JSON foram encontrados
        self.assertIsNotNone(melhor_index, "Nenhum índice encontrado no melhor JSON.")
        self.assertGreater(melhor_index_score, 0, "O score do melhor índice deveria ser maior que zero.")
        self.assertIsNotNone(melhor_url, "URL do melhor índice não encontrada.")

        print(f"\nMelhor opção: {melhor_opcao} com score {melhor_score:.2f}.")
        print(f"Melhor índice: {melhor_index} com score {melhor_index_score:.2f}.")
        print(f"URL do melhor índice: {melhor_url}")


if __name__ == "__main__":
    unittest.main()
