from django.core.management.base import BaseCommand
from core.models import Category, Video, Question, Choice, Testimonial
from django.core.exceptions import ValidationError  # Importar isto

class Command(BaseCommand):
    help = 'Cria e atualiza todo o conteúdo base do site: Categorias, Vídeos, Quizzes e Avaliações, sem sobrescrever URLs existentes.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando o setup completo do conteúdo base...'))

        # --- DADOS DAS CATEGORIAS ---
        categories_list = [
            'Conversação', 'Gramática', 'Cultura', 'Negócios (Business)', 'Nível Iniciante',
            'Nível Intermediário', 'Nível Avançado', 'Psicologia', 'Tecnologia',
            'Neurociência', 'Comunicação', 'Astronomia', 'História', 'Biologia',
            'Economia', 'Design', 'Filosofia', 'Ciência'
        ]
        for category_name in categories_list:
            Category.objects.get_or_create(name=category_name)
        self.stdout.write(self.style.SUCCESS('--- Categorias criadas/verificadas.'))

        # --- DADOS COMPLETOS DOS VÍDEOS E QUIZZES (Mínimo 3, Máximo 5 perguntas) ---
        content_data = [
           
            {'category': 'Psicologia', 'video_title': 'Do schools kill creativity?', 'video_desc': 'Sir Ken Robinson faz um caso divertido e profundo para a criação de um sistema educacional que nutre a criatividade.', 'video_url': 'https://www.youtube.com/watch?v=iG9CE55wbtY', 'questions': [
                {'text': 'What does Sir Ken Robinson argue about creativity in schools?', 'explanation': 'Ele argumenta que a criatividade é tão fundamental para a educação quanto a alfabetização e deveria ser tratada com a mesma importância.', 'choices': [{'text': 'It is as important as literacy', 'correct': True}, {'text': 'Schools enhance it naturally', 'correct': False}]},
                {'text': 'What subject did the girl Gillian Lynne eventually excel in?', 'explanation': 'O médico sabiamente identificou que Gillian não estava doente, mas era uma dançarina, destacando a existência de diversos tipos de inteligência.', 'choices': [{'text': 'Dance', 'correct': True}, {'text': 'Mathematics', 'correct': False}]},
                {'text': 'What is a common consequence of being wrong in our education system?', 'explanation': 'Na maioria dos sistemas educacionais, cometer um erro é visto como o pior resultado possível, o que desencoraja os alunos a serem criativos.', 'choices': [{'text': 'It is stigmatized', 'correct': True}, {'text': 'It is encouraged', 'correct': False}]},
                {'text': 'Which subjects are at the top of the hierarchy in every education system?', 'explanation': 'Ele ressalta que as matérias úteis para o trabalho industrial (como matemática e línguas) estão no topo, refletindo um modelo ultrapassado de educação.', 'choices': [{'text': 'Mathematics and Languages', 'correct': True}, {'text': 'Arts and Music', 'correct': False}]},
                {'text': 'What does Ken Robinson believe about intelligence?', 'explanation': 'Ele acredita que a inteligência é multifacetada e se manifesta de várias formas, não apenas academicamente.', 'choices': [{'text': 'It is diverse, dynamic, and distinct', 'correct': True}, {'text': 'It is defined by a single IQ score', 'correct': False}]},
            ]},
            {'category': 'Psicologia', 'video_title': 'What makes a good life? Lessons from the longest study on happiness', 'video_desc': 'Robert Waldinger compartilha os resultados de um estudo de 75 anos sobre a felicidade.', 'video_url': 'https://www.youtube.com/watch?v=8KkKuTCFvzI', 'questions': [
                {'text': 'What is the main message from the 75-year study?', 'explanation': 'O estudo de Harvard concluiu que bons relacionamentos nos mantêm mais felizes e saudáveis.', 'choices': [{'text': 'Good relationships keep us happier and healthier', 'correct': True}, {'text': 'Fame and wealth are the key to happiness', 'correct': False}]},
                {'text': 'A survey of millennials showed their main life goal was what?', 'explanation': 'A pesquisa reflete uma ênfase cultural moderna na validação externa (fama) e no sucesso material (riqueza).', 'choices': [{'text': 'To get rich or famous', 'correct': True}, {'text': 'To travel the world', 'correct': False}]},
                {'text': 'According to the speaker, what "kills"?', 'explanation': 'O estudo descobriu que as pessoas socialmente mais isoladas são menos felizes e vivem vidas mais curtas.', 'choices': [{'text': 'Loneliness', 'correct': True}, {'text': 'Conflict', 'correct': False}]},
                {'text': 'What protects our bodies and brains as we age?', 'explanation': 'Pessoas que sentem que podem contar com seus parceiros têm memórias que permanecem mais nítidas por mais tempo.', 'choices': [{'text': 'Good relationships', 'correct': True}, {'text': 'A healthy diet', 'correct': False}]},
            ]},
            {'category': 'Cultura', 'video_title': 'A Simple Guide to Cooking Pasta | SORTEDfood', 'video_desc': 'Um guia básico e divertido sobre como cozinhar macarrão.', 'video_url': 'https://youtu.be/slLGniM_mJA?si=Z6V8xxkeEqXMuVEH', 'questions': [
                {'text': 'What do they recommend adding to the pasta water?', 'explanation': 'Salgar a água serve para temperar a massa de dentro para fora durante o cozimento.', 'choices': [{'text': 'A generous amount of salt', 'correct': True}, {'text': 'Olive oil', 'correct': False}]},
                {'text': 'What does "al dente" literally mean?', 'explanation': 'É um termo italiano que significa "ao dente", descrevendo a massa que está cozida, mas ainda firme.', 'choices': [{'text': 'To the tooth', 'correct': True}, {'text': 'To the sauce', 'correct': False}]},
                {'text': 'Why do they say *not* to add oil to the pasta water?', 'explanation': 'O óleo na água impede que o molho grude (clings) na massa mais tarde.', 'choices': [{'text': 'It prevents the sauce from clinging to the pasta', 'correct': True}, {'text': 'It makes the pasta cook too quickly', 'correct': False}]},
            ]},
            {'category': 'Filosofia', 'video_title': 'The Egg - A Short Story', 'video_desc': 'Uma animação do Kurzgesagt baseada em um conto de Andy Weir sobre o sentido da vida.', 'video_url': 'https://www.youtube.com/watch?v=h6fcK_fRYaI', 'questions': [
                {'text': 'In the story, what is the main character\'s relationship to every other human?', 'explanation': 'A ideia central do conto é que todas as almas humanas são, na verdade, a mesma alma vivendo todas as vidas possíveis.', 'choices': [{'text': 'They are all different incarnations of himself', 'correct': True}, {'text': 'They are all his ancestors', 'correct': False}]},
                {'text': 'What is the ultimate purpose of the character\'s existence?', 'explanation': 'O objetivo final é que, após viver todas as vidas, a consciência do protagonista terá amadurecido o suficiente para nascer como um ser de nível divino.', 'choices': [{'text': 'To be reborn as a god himself', 'correct': True}, {'text': 'To pay for his sins', 'correct': False}]},
                {'text': 'How does the character (God) describe the universe?', 'explanation': 'Ele descreve o universo inteiro como um "ovo" para a consciência do protagonista amadurecer.', 'choices': [{'text': 'As an "egg" for the protagonist', 'correct': True}, {'text': 'As an endless simulation', 'correct': False}]},
            ]},
            
            {'category': 'Comunicação', 'video_title': 'How to sound smart in your TEDx Talk', 'video_desc': 'Will Stephen mostra de forma cômica como a forma de falar pode soar mais importante que o conteúdo.', 'video_url': 'https://www.youtube.com/watch?v=8S0FDjFBj8o', 'questions': [
                {'text': 'What is the speaker\'s main point in this talk?', 'explanation': 'O palestrante está satirizando o fato de que o estilo de apresentação (confiança, pausas, gestos) pode fazer alguém parecer inteligente, mesmo sem dizer nada de substância.', 'choices': [{'text': 'That presentation style matters more than content', 'correct': True}, {'text': 'That you must use complex vocabulary', 'correct': False}]},
                {'text': 'What does the speaker use to fill time?', 'explanation': 'Ele usa pausas dramáticas, gestos com as mãos e óculos para parecer ponderado, sem realmente ter um argumento.', 'choices': [{'text': 'Dramatic pauses and hand gestures', 'correct': True}, {'text': 'Detailed charts and graphs', 'correct': False}]},
                {'text': 'What does the speaker say about "nothing"?', 'explanation': 'Ele repete a palavra "nada" (nothing) várias vezes de forma séria, provando que a entonação pode fazer qualquer palavra soar profunda.', 'choices': [{'text': 'He repeats it to make it sound profound', 'correct': True}, {'text': 'He defines it using science', 'correct': False}]},
            ]},
            {'category': 'Cultura', 'video_title': 'The Lord of the Rings - Official Trailer', 'video_desc': 'Um trailer de filme com narração épica e diálogos curtos.', 'video_url': 'https://www.youtube.com/watch?v=x8UAUAuKNcU', 'questions': [
                {'text': 'What is the "One Ring"?', 'explanation': 'O narrador e Gandalf explicam que é o anel mestre ("one ring to rule them all") que o Lorde das Trevas, Sauron, criou.', 'choices': [{'text': 'The master ring created by the Dark Lord', 'correct': True}, {'text': 'A gift for the Elves', 'correct': False}]},
                {'text': 'Who is tasked with destroying the Ring?', 'explanation': 'Gandalf diz a Frodo que o anel "foi escolhido para você" (was chosen for you) e que ele deve ser destruído.', 'choices': [{'text': 'Frodo Baggins', 'correct': True}, {'text': 'Gandalf', 'correct': False}]},
                {'text': 'Where must the Ring be taken to be destroyed?', 'explanation': 'Elrond afirma no conselho que o anel deve ser levado "nas profundezas de Mordor" e destruído no fogo onde foi forjado.', 'choices': [{'text': 'To Mordor', 'correct': True}, {'text': 'To the Shire', 'correct': False}]},
                {'text': 'What is the name of the fellowship (group)?', 'explanation': 'Ao final do conselho, Elrond declara: "You shall be the Fellowship of the Ring." (Vocês serão a Sociedade do Anel).', 'choices': [{'text': 'The Fellowship of the Ring', 'correct': True}, {'text': 'The Ringbearers', 'correct': False}]},
            ]},
            {'category': 'Ciência', 'video_title': 'What would happen if you didn’t sleep?', 'video_desc': 'Claudia Aguirre, da TED-Ed, detalha os efeitos da privação de sono no corpo e cérebro.', 'video_url': 'https://youtu.be/dqONk48l5vY?si=NhbcuidiNB_7E4SR', 'questions': [
                {'text': 'What is "microsleep"?', 'explanation': 'Microsleeps são episódios incontroláveis de sono que duram alguns segundos, o que é muito perigoso se você estiver dirigindo.', 'choices': [{'text': 'Uncontrollable brief episodes of sleep', 'correct': True}, {'text': 'A very light and relaxing sleep', 'correct': False}]},
                {'text': 'Which part of the brain is most affected by lack of sleep?', 'explanation': 'A falta de sono afeta o córtex pré-frontal, que é responsável pela tomada de decisões, julgamento e resolução de problemas.', 'choices': [{'text': 'The prefrontal cortex (decision-making)', 'correct': True}, {'text': 'The cerebellum (balance)', 'correct': False}]},
                {'text': 'What chemical builds up in the brain the longer we are awake?', 'explanation': 'A adenosina se acumula durante o dia e promove a sonolência. A cafeína funciona bloqueando os receptores de adenosina.', 'choices': [{'text': 'Adenosine', 'correct': True}, {'text': 'Melatonin', 'correct': False}]},
            ]},
            {'category': 'Conversação', 'video_title': 'Learn English with The Fresh Prince of Bel-Air', 'video_desc': 'Uma análise de cenas do seriado para aprender inglês coloquial, gírias e humor.', 'video_url': 'https://youtu.be/rAMvLi4wGhI?si=_7_kGQmMDYNWCUHP', 'questions': [
                {'text': 'What does the slang "phat" mean in this 90s context?', 'explanation': '"P.H.A.T." era uma gíria dos anos 90 que significava "Pretty, Hot, And Tempting", ou simplesmente "muito legal" ou "excelente".', 'choices': [{'text': 'Cool, awesome, or excellent', 'correct': True}, {'text': 'Overweight', 'correct': False}]},
                {'text': 'Where was Will "chillin\' out, maxin\', relaxin\' all cool"?', 'explanation': 'Esta é da famosa música tema. Ele estava relaxando ("chillin\' out") no parquinho ("on the playground").', 'choices': [{'text': 'On the playground', 'correct': True}, {'text': 'In his room in Bel-Air', 'correct': False}]},
                {'text': 'What does "knock it off" mean?', 'explanation': 'É uma expressão muito comum que significa "pare com isso!" (stop it!) ou "deixe disso!".', 'choices': [{'text': 'Stop it!', 'correct': True}, {'text': 'To hit something', 'correct': False}]},
            ]},
            {'category': 'Cultura', 'video_title': 'How to Tie a Tie (Mirrored / Slowly) - The Windsor Knot', 'video_desc': 'Um tutorial prático e lento sobre como dar um nó em uma gravata.', 'video_url': 'https://www.youtube.com/watch?v=xAg7z6u4NE8', 'questions': [
                {'text': 'Why is this video "mirrored"?', 'explanation': 'O vídeo é espelhado para que o espectador possa copiar os movimentos como se estivesse olhando em um espelho, facilitando o aprendizado.', 'choices': [{'text': 'To make it easy to follow, like looking in a mirror', 'correct': True}, {'text': 'Because of a camera error', 'correct': False}]},
                {'text': 'What is the defining characteristic of a "Windsor Knot"?', 'explanation': 'O nó Windsor (ou "full Windsor") é conhecido por ser um nó grande, largo e perfeitamente triangular.', 'choices': [{'text': 'It is wide and triangular', 'correct': True}, {'text': 'It is very thin and simple', 'correct': False}]},
                {'text': 'At the start, which end of the tie should be much longer?', 'explanation': 'Para ter comprimento suficiente para todas as voltas do nó Windsor, a extremidade larga (wide end) deve ficar muito mais longa que a extremidade fina.', 'choices': [{'text': 'The wide end', 'correct': True}, {'text': 'The narrow end', 'correct': False}]},
            ]},
            {'category': 'Psicologia', 'video_title': 'What is writer\'s block?', 'video_desc': 'Um vídeo da Vox que explora o bloqueio criativo.', 'video_url': 'https://youtu.be/rcKtcXbjwD4?si=N8eB3ZjMI4hF-MDy', 'questions': [
                {'text': 'What is "writer\'s block"?', 'explanation': 'É a condição de não conseguir produzir novos trabalhos ou de sentir a criatividade "travada", o que é muito comum entre escritores.', 'choices': [{'text': 'An inability to produce new creative work', 'correct': True}, {'text': 'A physical injury to the hand', 'correct': False}]},
                {'text': 'The video suggests that "writer\'s block" is often caused by what?', 'explanation': 'Muitas vezes, é causado por fatores psicológicos, como ansiedade, perfeccionismo ou o medo de que o trabalho não seja bom o suficiente.', 'choices': [{'text': 'Anxiety or fear of failure', 'correct': True}, {'text': 'A lack of good ideas', 'correct': False}]},
                {'text': 'What is one strategy mentioned to overcome it?', 'explanation': 'Uma estratégia comum é o "freewriting" (escrita livre), onde você força a si mesmo a escrever qualquer coisa, sem julgamento, apenas para fazer a criatividade fluir.', 'choices': [{'text': 'Freewriting (writing without stopping or judging)', 'correct': True}, {'text': 'Waiting for inspiration to come', 'correct': False}]},
            ]},
            
           
            {'category': 'Psicologia', 'video_title': 'The surprising habits of original thinkers | Adam Grant', 'video_desc': 'Adam Grant explora os hábitos de pessoas criativas e originais.', 'video_url': 'https://www.youtube.com/watch?v=fxbCHn6gE3U', 'questions': [
                {'text': 'What concept does Adam Grant introduce as the opposite of "déjà vu"?', 'explanation': '"Vuja de" é quando você olha para algo que já viu muitas vezes e, de repente, vê com uma nova perspectiva.', 'choices': [{'text': 'Vuja de', 'correct': True}, {'text': 'Jamais vu', 'correct': False}]},
                {'text': 'According to the talk, what do "originals" do frequently?', 'explanation': 'Pessoas criativas costumam procrastinar moderadamente, o que dá tempo para suas ideias incubarem.', 'choices': [{'text': 'Procrastinate', 'correct': True}, {'text': 'Wake up early', 'correct': False}]},
                {'text': 'What is the relationship between procrastination and creativity?', 'explanation': 'A procrastinação moderada pode, na verdade, impulsionar a criatividade, permitindo que as ideias "incubem" e se desenvolvam.', 'choices': [{'text': 'Moderate procrastination can boost creativity', 'correct': True}, {'text': 'All procrastination kills creativity', 'correct': False}]},
            ]},
            {'category': 'Tecnologia', 'video_title': 'How a handful of tech companies control billions of minds every day | Tristan Harris', 'video_desc': 'O ex-designer ético do Google expõe como a tecnologia é projetada para sequestrar nossa atenção.', 'video_url': 'https://youtu.be/C74amJRp730?si=nxA4B4SdAotcnsSk', 'questions': [
                {'text': 'What does Tristan Harris compare the notification sounds on our phones to?', 'explanation': 'Ele compara os sons e vibrações a uma máquina caça-níqueis (slot machine), que usa recompensas variáveis para manter os usuários viciados.', 'choices': [{'text': 'A slot machine', 'correct': True}, {'text': 'A doorbell', 'correct': False}]},
                {'text': 'What is the "race to the bottom of the brain stem"?', 'explanation': 'Descreve como as empresas de tecnologia competem para sequestrar nossos instintos mais básicos e vulnerabilidades de atenção.', 'choices': [{'text': 'A race to hook users by appealing to their primal instincts', 'correct': True}, {'text': 'A neurological study', 'correct': False}]},
                {'text': 'What is Tristan Harris\'s main concern?', 'explanation': 'Ele teme que a "corrida pela atenção" das empresas de tecnologia possa não estar alinhada com o que é melhor para nós como seres humanos.', 'choices': [{'text': 'That technology\'s goals are misaligned with human well-being', 'correct': True}, {'text': 'That smartphones are too expensive', 'correct': False}]},
            ]},
            {'category': 'Neurociência', 'video_title': 'Your brain on video games | Daphne Bavelier', 'video_desc': 'Uma neurocientista explora como os videogames afetam o cérebro, melhorando a visão e a atenção.', 'video_url': 'https://youtu.be/FktsFcooIG8?si=xbIlk8r5VjUkoIO_', 'questions': [
                {'text': 'What is one of the benefits of playing action video games mentioned in the talk?', 'explanation': 'A pesquisa de Daphne Bavelier mostra que jogadores de ação têm uma visão melhor em termos de distinguir tons de cinza (sensibilidade ao contraste).', 'choices': [{'text': 'Better eyesight (contrast sensitivity)', 'correct': True}, {'text': 'Improved social skills', 'correct': False}]},
                {'text': 'How does the brain of an action gamer handle attention?', 'explanation': 'O cérebro deles aprende a alocar melhor os recursos de atenção, permitindo-lhes rastrear vários objetos e alternar tarefas com mais eficiência.', 'choices': [{'text': 'It learns to better control and deploy attention', 'correct': True}, {'text': 'It becomes less focused', 'correct': False}]},
                {'text': 'Does the speaker suggest all video games are beneficial?', 'explanation': 'Não. Ela é específica ao dizer que os benefícios cognitivos, como melhoria da visão, foram encontrados principalmente em jogos de ação.', 'choices': [{'text': 'No, she specifies "action" video games', 'correct': True}, {'text': 'Yes, all games make you smarter', 'correct': False}]},
            ]},
            {'category': 'Comunicação', 'video_title': 'How to speak so that people want to listen | Julian Treasure', 'video_desc': 'O especialista em som Julian Treasure demonstra como usar a voz para se comunicar de forma poderosa.', 'video_url': 'https://www.youtube.com/watch?v=eIho2S0ZahI', 'questions': [
                {'text': 'What does the acronym HAIL stand for?', 'explanation': 'HAIL representa os quatro pilares da fala poderosa: Honesty (honestidade), Authenticity (autenticidade), Integrity (integridade) e Love (amor).', 'choices': [{'text': 'Honesty, Authenticity, Integrity, Love', 'correct': True}, {'text': 'Hearing, Attention, Interest, Listening', 'correct': False}]},
                {'text': 'Which vocal tool relates to the "vertical plane of sound"?', 'explanation': 'Ele se refere ao "pitch" (tom), explicando que vozes mais graves são associadas a poder e autoridade.', 'choices': [{'text': 'Pitch (tom)', 'correct': True}, {'text': 'Pace (ritmo)', 'correct': False}]},
                {'text': 'What is one of the "7 deadly sins of speaking" he mentions?', 'explanation': 'Ele lista vários, incluindo "Gossip" (fofoca), "Judging" (julgar) e "Negativity" (negatividade).', 'choices': [{'text': 'Gossip', 'correct': True}, {'text': 'Silence', 'correct': False}]},
            ]},
            {'category': 'Astronomia', 'video_title': 'What if we detonated a nuke in the Marianas Trench?', 'video_desc': 'Uma exploração fascinante do Kurzgesagt sobre o que aconteceria se uma bomba nuclear fosse detonada no ponto mais profundo do oceano.', 'video_url': 'https://youtu.be/A7eb1DHZ9GQ?si=Q5wpAeYPoAVCqWof', 'questions': [
                {'text': 'Would a nuke in the Marianas Trench cause a mega-tsunami?', 'explanation': 'Não. A imensa pressão da água conteria a maior parte da explosão, criando uma bolha de vapor que colapsaria rapidamente.', 'choices': [{'text': 'No, the water pressure would contain the blast', 'correct': True}, {'text': 'Yes, it would destroy coastal cities', 'correct': False}]},
                {'text': 'What would be the most significant long-term consequence?', 'explanation': 'A principal consequência seria a contaminação radioativa da área, que seria dispersa lentamente pelas correntes oceânicas profundas.', 'choices': [{'text': 'Radioactive contamination of the deep ocean', 'correct': True}, {'text': 'A new volcano would form', 'correct': False}]},
                {'text': 'What is the main takeaway about the ocean\'s power?', 'explanation': 'A escala e a pressão do oceano profundo são tão imensas que podem conter (em grande parte) até mesmo uma explosão nuclear.', 'choices': [{'text': 'The deep ocean\'s pressure is immense', 'correct': True}, {'text': 'The ocean is fragile and would boil', 'correct': False}]},
            ]},
            {'category': 'História', 'video_title': 'The rise and fall of the Inca Empire - Gordon McEwan', 'video_desc': 'Uma animação da TED-Ed que resume a ascensão e a queda de um dos maiores impérios da América pré-colombiana.', 'video_url': 'https://www.youtube.com/watch?v=UO5ktwPXsyM', 'questions': [
                {'text': 'What was the capital of the Inca Empire?', 'explanation': 'Cusco, localizada no atual Peru, era o centro político e religioso do vasto Império Inca.', 'choices': [{'text': 'Cusco', 'correct': True}, {'text': 'Machu Picchu', 'correct': False}]},
                {'text': 'What was the "mita" system?', 'explanation': 'A "mita" era uma forma de tributo em trabalho. Os cidadãos eram obrigados a trabalhar para o estado em projetos como construção de estradas.', 'choices': [{'text': 'A form of labor tax', 'correct': True}, {'text': 'The Incan writing system', 'correct': False}]},
                {'text': 'What was a major factor in the fall of the Inca Empire?', 'explanation': 'A chegada dos conquistadores espanhóis, liderados por Francisco Pizarro, e as doenças que trouxeram (como a varíola) devastaram o império.', 'choices': [{'text': 'Spanish conquest and disease', 'correct': True}, {'text': 'A massive earthquake', 'correct': False}]},
            ]},
            {'category': 'Biologia', 'video_title': 'How do cancer cells behave differently from healthy ones? - George Zaidan', 'video_desc': 'A TED-Ed explica a principal diferença entre células normais e cancerígenas: a perda do controle sobre a divisão celular.', 'video_url': 'https://youtu.be/BmFEoCFDi-w?si=xcRuiEEFtnxG6U1S', 'questions': [
                {'text': 'What is the main characteristic of cancer cells?', 'explanation': 'Células cancerígenas ignoram os sinais que dizem para parar de se dividir, resultando em um crescimento descontrolado que forma tumores.', 'choices': [{'text': 'They have uncontrolled cell division', 'correct': True}, {'text': 'They are smaller than normal cells', 'correct': False}]},
                {'text': 'What is "metastasis"?', 'explanation': 'Metástase é o processo pelo qual as células cancerígenas se separam do tumor original e viajam para outras partes do corpo para formar novos tumores.', 'choices': [{'text': 'The spread of cancer to new areas', 'correct': True}, {'text': 'The initial formation of a tumor', 'correct': False}]},
                {'text': 'What is "angiogenesis"?', 'explanation': 'É o processo de criação de novos vasos sanguíneos, que as células cancerígenas induzem para obter os nutrientes de que precisam para crescer.', 'choices': [{'text': 'The creation of new blood vessels', 'correct': True}, {'text': 'The shrinking of a tumor', 'correct': False}]},
            ]},
            {'category': 'Cultura', 'video_title': 'Why does the Leaning Tower of Pisa lean? - Alex Gendler', 'video_desc': 'Descubra a história e a engenharia por trás de um dos erros de construção mais famosos do mundo.', 'video_url': 'https://youtu.be/HFqf6aKdOC0?si=6q7-2_rdsa5qHah5', 'questions': [
                {'text': 'Why did the tower start to lean?', 'explanation': 'A torre foi construída sobre um solo instável de argila e areia, e a fundação era muito rasa para suportar seu peso.', 'choices': [{'text': 'Due to a poor and unstable foundation', 'correct': True}, {'text': 'It was designed that way', 'correct': False}]},
                {'text': 'How long did the construction of the tower take?', 'explanation': 'A construção demorou quase 200 anos (199 anos), ocorrendo em três fases, o que permitiu que o solo se assentasse.', 'choices': [{'text': 'Nearly 200 years', 'correct': True}, {'text': 'Exactly 10 years', 'correct': False}]},
                {'text': 'How did engineers eventually help stabilize the tower?', 'explanation': 'Eles removeram cuidadosamente o solo do lado norte (o lado não inclinado) para permitir que a torre se "endireitasse" ligeiramente e parasse de tombar.', 'choices': [{'text': 'By removing soil from under the north side', 'correct': True}, {'text': 'By pushing it back with large cables', 'correct': False}]},
            ]},
            {'category': 'Economia', 'video_title': 'What gives a dollar bill its value? - Doug Levinson', 'video_desc': 'Uma explicação simples sobre o que é "fiat money" (moeda fiduciária) e por que o dinheiro que usamos tem valor.', 'video_url': 'https://youtu.be/XNu5ppFZbHo?si=Qmz8Z0mSNXkD1ji2', 'questions': [
                {'text': 'What is "fiat money"?', 'explanation': '"Fiat" vem do latim "faça-se". É uma moeda que tem valor porque o governo assim o declara, e não por ser lastreada em um bem físico como o ouro.', 'choices': [{'text': 'Money that has value by government order', 'correct': True}, {'text': 'Money backed by gold', 'correct': False}]},
                {'text': 'What does it mean that the dollar is "not backed by gold"?', 'explanation': 'Significa que o seu valor não está ligado a uma mercadoria física; você não pode trocar um dólar por uma quantidade fixa de ouro.', 'choices': [{'text': 'Its value isn\'t tied to a physical commodity', 'correct': True}, {'text': 'It is worthless', 'correct': False}]},
                {'text': 'What gives "fiat money" its value, if not gold?', 'explanation': 'O seu valor vem da confiança pública e do facto de o governo o declarar como moeda legal (e aceitá-lo para pagamento de impostos).', 'choices': [{'text': 'Government decree and public trust', 'correct': True}, {'text': 'The amount of paper it is printed on', 'correct': False}]},
            ]},
            {'category': 'Design', 'video_title': 'The first secret of great design | Tony Fadell', 'video_desc': 'O designer do iPod e co-criador do iPhone, Tony Fadell, fala sobre a importância de notar e resolver os pequenos problemas do dia a dia.', 'video_url': 'https://www.youtube.com/watch?v=9uOMectkCCs', 'questions': [
                {'text': 'What is the first step to solving a problem, according to Tony Fadell?', 'explanation': 'O primeiro passo é notar o problema. Ele argumenta que nos acostumamos com os pequenos problemas do cotidiano (habituação) e paramos de vê-los.', 'choices': [{'text': 'Noticing the problem', 'correct': True}, {'text': 'Brainstorming solutions', 'correct': False}]},
                {'text': 'What is "habituation"?', 'explanation': 'É o processo em que o nosso cérebro se habitua a problemas quotidianos e deixa de os notar, o que impede a inovação.', 'choices': [{'text': 'Getting used to everyday problems', 'correct': True}, {'text': 'A type of good design', 'correct': False}]},
                {'text': 'What does Tony Fadell encourage designers to do?', 'explanation': 'Ele incentiva os designers (e todos) a "pensar mais jovem" e a ver os problemas quotidianos com um olhar novo, em vez de os aceitar.', 'choices': [{'text': 'To "think younger" and see problems fresh', 'correct': True}, {'text': 'To copy successful products', 'correct': False}]},
            ]},
        ]
        
        for data in content_data:
            category, _ = Category.objects.get_or_create(name=data['category'])
            
            try:
                video_obj = Video.objects.filter(title=data['video_title']).first()

                if not video_obj:
                    video = Video(
                        title=data['video_title'],
                        description=data['video_desc'],
                        video_url=data['video_url'],
                        category=category
                    )
                    video.save() 
                    self.stdout.write(self.style.SUCCESS(f'Vídeo "{video.title}" verificado e criado.'))
                else:
                    video = video_obj
                    self.stdout.write(self.style.WARNING(f'Vídeo "{video.title}" já existe. Verificando/adicionando quiz...'))

                if data.get('questions'):
                    for q_data in data['questions']:
                        question, q_created = Question.objects.update_or_create(
                            video=video,
                            question_text=q_data['text'],
                            defaults={'explanation': q_data.get('explanation', '')}
                        )
                        
                        if q_created and q_data.get('choices'):
                            for c_data in q_data['choices']:
                                Choice.objects.create(question=question, choice_text=c_data['text'], is_correct=c_data['correct'])
            
            except ValidationError as e:
                self.stdout.write(self.style.ERROR(f'--- VÍDEO IGNORADO --- "{data["video_title"]}". Motivo: {e}'))
        
        self.stdout.write(self.style.SUCCESS('Processamento de vídeos e quizzes concluído.'))

        # --- DADOS DAS AVALIAÇÕES ---
        self.stdout.write(self.style.NOTICE('Limpando e recriando avaliações...'))
        Testimonial.objects.all().delete()
        testimonials_list = [
            {'author_name': 'Carlos Silva', 'testimonial_text': 'Plataforma incrível! A imersão com vídeos realmente funciona.', 'rating': 5},
            {'author_name': 'Juliana Pereira', 'testimonial_text': 'Meu "listening" melhorou muito em poucas semanas.', 'rating': 5},
            {'author_name': 'Fernando Costa', 'testimonial_text': 'Adorei a seleção de vídeos. Temas atuais e relevantes que me mantêm engajado.', 'rating': 4},
            {'author_name': 'Beatriz Almeida', 'testimonial_text': 'A funcionalidade de salvar o progresso e ver meu perfil é muito motivadora. Recomendo!', 'rating': 5},
            {'author_name': 'Lucas Martins', 'testimonial_text': 'Finalmente uma ferramenta que foca em entender o inglês do dia a dia.', 'rating': 5},
            {'author_name': 'Gabriela Souza', 'testimonial_text': 'O site é rápido, bonito e funciona perfeitamente no celular.', 'rating': 5},
            {'author_name': 'Rafael Oliveira', 'testimonial_text': 'Gostei muito das categorias. Consigo focar nos vídeos de "Business English".', 'rating': 4},
            {'author_name': 'Mariana Lima', 'testimonial_text': 'Simples, direto ao ponto e eficaz. É o que eu precisava.', 'rating': 5},
            {'author_name': 'Thiago Santos', 'testimonial_text': 'O modo escuro é um toque de classe! Mostra o cuidado com os detalhes.', 'rating': 5},
            {'author_name': 'Ana Clara Rocha', 'testimonial_text': 'A melhor parte é aprender com conteúdo real, não com diálogos fabricados.', 'rating': 5},
        ]
        for item in testimonials_list:
            Testimonial.objects.create(**item)
        self.stdout.write(self.style.SUCCESS(f'{len(testimonials_list)} avaliações foram criadas.'))

        self.stdout.write(self.style.SUCCESS('Setup completo do conteúdo base finalizado!'))