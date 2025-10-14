from django.core.management.base import BaseCommand
from core.models import Question

class Command(BaseCommand):
    help = 'Adiciona textos explicativos para 70% das perguntas existentes no banco de dados.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando a adição de explicações para 70% do quiz...'))

        explanations_to_add = {
            # Vídeo: Do schools kill creativity? (4/5)
            'What does Sir Ken Robinson argue about creativity': 'Ele argumenta que a criatividade é tão fundamental para a educação quanto a alfabetização e deveria ser tratada com a mesma importância.',
            'What subject did the girl Gillian Lynne eventually excel in?': 'O médico sabiamente identificou que Gillian não estava doente, mas era uma dançarina, destacando a existência de diversos tipos de inteligência além da acadêmica.',
            'What is a common consequence of being wrong': 'Na maioria dos sistemas educacionais, cometer um erro é visto como o pior resultado possível, o que desencoraja os alunos a tentar coisas novas e a serem criativos.',
            'Which subjects are at the top of the hierarchy': 'Ele ressalta que as matérias úteis para o trabalho industrial (como matemática e línguas) estão no topo, enquanto as artes estão na base, refletindo um modelo ultrapassado de educação.',
            
            # Vídeo: What makes a good life? (4/5)
            'What is the main message from the 75-year study?': 'O estudo de Harvard concluiu que bons relacionamentos nos mantêm mais felizes e saudáveis. Não é sobre riqueza ou fama, mas sobre a qualidade de nossas conexões.',
            'A survey of millennials showed their main life goal': 'A pesquisa reflete uma ênfase cultural moderna na validação externa (fama) e no sucesso material (riqueza) como caminhos para a felicidade, o que o estudo contradiz.',
            'According to the speaker, what "kills"?': 'O estudo descobriu que as pessoas socialmente mais isoladas são menos felizes, sua saúde declina mais cedo na meia-idade e elas vivem vidas mais curtas.',
            'What protects our bodies and brains as we age?': 'Pessoas que sentem que podem contar com seus parceiros em momentos de necessidade têm memórias que permanecem mais nítidas por mais tempo.',

            # Vídeo: A Simple Guide to Cooking Pasta (4/5)
            'What do they recommend adding to the pasta water?': 'Salgar a água serve para temperar a massa de dentro para fora. Adicionar óleo, ao contrário da crença popular, pode impedir que o molho grude no macarrão.',
            'What does "al dente" literally mean?': 'É um termo italiano que significa "ao dente". Descreve a massa que está cozida, mas ainda firme e oferece uma leve resistência ao ser mordida.',
            'Should you rinse your pasta with cold water': 'Enxaguar a massa remove o amido da superfície, que é essencial para ajudar o molho a emulsificar e aderir ao macarrão.',
            'What is the purpose of the starchy pasta water?': 'Essa "água de ouro" é cheia de amido e sal. Adicionar um pouco dela ao seu molho ajuda a engrossá-lo e a ligá-lo perfeitamente à massa.',

            # Vídeo: The Egg - A Short Story (4/5)
            'In the story, what is the main character\'s relationship': 'A ideia central do conto é que todas as almas humanas são, na verdade, a mesma alma vivendo todas as vidas possíveis para poder amadurecer e se tornar um ser como Deus.',
            'What is the entire universe, according to the story?': 'No conto, o universo inteiro é descrito como um "ovo cósmico" para a consciência do protagonista, um lugar para ele crescer e amadurecer.',
            'The character has lived the lives of famous people': 'A entidade divina menciona que o protagonista já foi Abraão Lincoln, e também outras figuras como Hitler e seus milhões de vítimas.',
            'What is the ultimate purpose of the character\'s existence?': 'O objetivo final é que, após viver todas as vidas humanas, a consciência do protagonista terá amadurecido o suficiente para nascer como um ser de nível divino.',

            # Vídeo: How to sound smart in your TEDx Talk (3/5)
            'What is the main joke of the presentation?': 'O comediante Will Stephen usa gestos, óculos e uma entonação confiante para dar a impressão de que está dizendo algo profundo, quando na verdade não está dizendo nada.',
            'What does the speaker do with his hands': 'Ele menciona que palestrantes inteligentes frequentemente usam as mãos e ajustam os óculos para parecerem pensativos e reforçar sua autoridade no assunto.',
            'The speaker says "This is a picture of a ..."': 'Ele mostra um gráfico genérico de pizza e simplesmente o descreve como "um gráfico", uma tática para preencher o tempo e parecer que está apresentando dados.',
            
            # Vídeo: The Lord of the Rings - Official Trailer (3/5)
            'What is the name of the evil lord who created the One Ring?': 'Sauron, o Senhor Sombrio de Mordor, forjou o Um Anel em segredo para controlar todos os outros Anéis de Poder.',
            'How many rings were given to the Elven-kings?': 'A narração inicial do trailer explica a distribuição dos Anéis de Poder: três para os Elfos, sete para os Anões e nove para os Homens.',
            'Where must the One Ring be destroyed?': 'O Um Anel só pode ser destruído nos fogos da Montanha da Perdição (Mount Doom), o mesmo local onde foi forjado por Sauron.',

            # Vídeo: What would happen if you didn’t sleep? (3/5)
            'What is one of the functions of sleep': 'Durante o sono, o cérebro realiza uma "limpeza", removendo toxinas que se acumulam durante o dia, um processo vital para a saúde neurológica.',
            'A lack of sleep can lead to what kind of problems?': 'A privação de sono afeta negativamente a concentração, a memória, o humor e pode levar a desequilíbrios hormonais e um sistema imunológico enfraquecido.',
            'What are "microsleeps"?': 'São episódios de sono que duram apenas alguns segundos e podem ocorrer quando se está muito privado de sono, sendo extremamente perigosos em situações como dirigir.',

            # Vídeo: Learn English with The Fresh Prince of Bel-Air (3/5)
            'What is the name of the family butler?': 'Geoffrey é o mordomo britânico da família Banks, conhecido por seu sarcasmo e comentários espirituosos.',
            'Who is Will\'s nerdy and preppy cousin?': 'Carlton Banks é o primo de Will, famoso por seu estilo conservador, seu amor por Tom Jones e sua dança icônica.',
            'Where does the Banks family live?': 'A família se mudou da Filadélfia para o luxuoso bairro de Bel-Air, em Los Angeles, Califórnia, cenário principal da série.',

            # Vídeo: How to Tie a Tie (Mirrored / Slowly) (3/5)
            'The video is mirrored. What does this help with?': 'Ao espelhar o vídeo, o instrutor permite que o espectador imite seus movimentos diretamente, como se estivesse se olhando no espelho, facilitando o aprendizado.',
            'The Windsor Knot is described as a what kind of knot?': 'O nó Windsor é um nó clássico, preferido para ocasiões formais por ser largo, triangular e perfeitamente simétrico.',
            'What part of the tie should the tip of the wide end': 'A regra clássica de elegância dita que a ponta da gravata deve tocar levemente a parte superior da fivela do cinto.',
            
            # Vídeo: What is writer\'s block? (3/5)
            'Writer\'s block is often a problem related to what?': 'O bloqueio criativo frequentemente não é uma falta de ideias, mas sim o medo de que as ideias não sejam boas o suficiente, um sintoma do perfeccionismo.',
            'What famous author is mentioned as having suffered': 'O vídeo cita Herman Melville, autor de Moby Dick, que após o sucesso inicial, sofreu um longo período de bloqueio e obscuridade.',
            'The video argues that inspiration is more a product of what?': 'Ao contrário do mito do "raio de inspiração", o vídeo defende que a criatividade e a inspiração são, na maioria das vezes, o resultado de um trabalho consistente e disciplinado.',
        }
        
        updated_count = 0
        for partial_text, explanation_text in explanations_to_add.items():
            try:
                question_to_update = Question.objects.get(question_text__icontains=partial_text)
                if not question_to_update.explanation:
                    question_to_update.explanation = explanation_text
                    question_to_update.save()
                    self.stdout.write(self.style.SUCCESS(f'Explicação adicionada para a pergunta: "{partial_text}..."'))
                    updated_count += 1
                else:
                    self.stdout.write(self.style.WARNING(f'Pergunta "{partial_text}..." já tinha explicação. Pulando.'))
            except Question.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'Pergunta não encontrada para o texto: "{partial_text}..."'))
            except Question.MultipleObjectsReturned:
                self.stdout.write(self.style.ERROR(f'Múltiplas perguntas encontradas para: "{partial_text}...". Nenhuma foi atualizada.'))

        self.stdout.write(self.style.SUCCESS(f'Processo finalizado. {updated_count} novas explicações foram adicionadas.'))