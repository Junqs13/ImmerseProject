# Código para populate_quiz.py
from django.core.management.base import BaseCommand
from core.models import Video, Question, Choice

class Command(BaseCommand):
    help = 'Popula o banco de dados com um questionário expandido de 5 perguntas por vídeo.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE('Iniciando o cadastro do questionário expandido...'))
        
        quiz_data = {
            'Do schools kill creativity?': [
                {'question_text': 'What does Sir Ken Robinson argue about creativity in schools?', 'choices': [{'choice_text': 'It is as important as literacy', 'is_correct': True}, {'choice_text': 'Schools enhance it naturally', 'is_correct': False}, {'choice_text': 'It is not a real subject', 'is_correct': False}]},
                {'question_text': 'What subject did the girl Gillian Lynne eventually excel in?', 'choices': [{'choice_text': 'Mathematics', 'is_correct': False}, {'choice_text': 'Dance', 'is_correct': True}, {'choice_text': 'History', 'is_correct': False}]},
                {'question_text': 'What is a common consequence of being wrong in our education system?', 'choices': [{'choice_text': 'It is encouraged', 'is_correct': False}, {'choice_text': 'It is ignored', 'is_correct': False}, {'choice_text': 'It is stigmatized', 'is_correct': True}]},
                {'question_text': 'Which subjects are at the top of the hierarchy in every education system?', 'choices': [{'choice_text': 'Arts and Music', 'is_correct': False}, {'choice_text': 'Mathematics and Languages', 'is_correct': True}, {'choice_text': 'Physical Education', 'is_correct': False}]},
                {'question_text': 'What does Ken Robinson believe about intelligence?', 'choices': [{'choice_text': 'It is diverse, dynamic, and distinct', 'is_correct': True}, {'choice_text': 'It is defined by a single IQ score', 'is_correct': False}, {'choice_text': 'It is fixed from birth', 'is_correct': False}]}
            ],
            'What makes a good life? Lessons from the longest study on happiness': [
                {'question_text': 'What is the main message from the 75-year study?', 'choices': [{'choice_text': 'Good relationships keep us happier and healthier', 'is_correct': True}, {'choice_text': 'Fame and wealth are the key to happiness', 'is_correct': False}, {'choice_text': 'Working hard is the most important thing', 'is_correct': False}]},
                {'question_text': 'A survey of millennials showed their main life goal was what?', 'choices': [{'choice_text': 'To travel the world', 'is_correct': False}, {'choice_text': 'To get rich or famous', 'is_correct': True}, {'choice_text': 'To help others', 'is_correct': False}]},
                {'question_text': 'According to the speaker, what "kills"?', 'choices': [{'choice_text': 'Conflict', 'is_correct': False}, {'choice_text': 'High cholesterol', 'is_correct': False}, {'choice_text': 'Loneliness', 'is_correct': True}]},
                {'question_text': 'What protects our bodies and brains as we age?', 'choices': [{'choice_text': 'A healthy diet', 'is_correct': False}, {'choice_text': 'Good relationships', 'is_correct': True}, {'choice_text': 'Regular exercise', 'is_correct': False}]},
                {'question_text': 'The study tracked the lives of how many men?', 'choices': [{'choice_text': '1000', 'is_correct': False}, {'choice_text': '724', 'is_correct': True}, {'choice_text': '50', 'is_correct': False}]}
            ],
            'A Simple Guide to Cooking Pasta | SORTEDfood': [
                {'question_text': 'What do they recommend adding to the pasta water?', 'choices': [{'choice_text': 'A generous amount of salt', 'is_correct': True}, {'choice_text': 'Olive oil', 'is_correct': False}, {'choice_text': 'Sugar', 'is_correct': False}]},
                {'question_text': 'What does "al dente" literally mean?', 'choices': [{'choice_text': 'To the sauce', 'is_correct': False}, {'choice_text': 'To the tooth', 'is_correct': True}, {'choice_text': 'Very soft', 'is_correct': False}]},
                {'question_text': 'Should you rinse your pasta with cold water after cooking?', 'choices': [{'choice_text': 'Yes, always', 'is_correct': False}, {'choice_text': 'No, it removes the starch', 'is_correct': True}, {'choice_text': 'Only for spaghetti', 'is_correct': False}]},
                {'question_text': 'What is the purpose of the starchy pasta water?', 'choices': [{'choice_text': 'To drink', 'is_correct': False}, {'choice_text': 'To help the sauce stick to the pasta', 'is_correct': True}, {'choice_text': 'To clean the pan', 'is_correct': False}]},
                {'question_text': 'When should you add the pasta to the water?', 'choices': [{'choice_text': 'When the water is boiling rapidly', 'is_correct': True}, {'choice_text': 'As soon as you put the pan on the stove', 'is_correct': False}, {'choice_text': 'When the water is lukewarm', 'is_correct': False}]}
            ],
            'The Egg - A Short Story': [
                {'question_text': 'In the story, what is the main character\'s relationship to every other human?', 'choices': [{'choice_text': 'They are all different incarnations of himself', 'is_correct': True}, {'choice_text': 'They are all his ancestors', 'is_correct': False}, {'choice_text': 'He has no relationship to them', 'is_correct': False}]},
                {'question_text': 'What is the entire universe, according to the story?', 'choices': [{'choice_text': 'A simulation', 'is_correct': False}, {'choice_text': 'An egg for the main character to grow in', 'is_correct': True}, {'choice_text': 'A random accident', 'is_correct': False}]},
                {'question_text': 'Who is the "God" character talking to?', 'choices': [{'choice_text': 'An angel', 'is_correct': False}, {'choice_text': 'A man who died in a car crash', 'is_correct': True}, {'choice_text': 'A philosopher', 'is_correct': False}]},
                {'question_text': 'The character has lived the lives of famous people, including whom?', 'choices': [{'choice_text': 'Abraham Lincoln', 'is_correct': True}, {'choice_text': 'Albert Einstein', 'is_correct': False}, {'choice_text': 'Cleopatra', 'is_correct': False}]},
                {'question_text': 'What is the ultimate purpose of the character\'s existence?', 'choices': [{'choice_text': 'To be reborn as a god himself', 'is_correct': True}, {'choice_text': 'To pay for his sins', 'is_correct': False}, {'choice_text': 'To experience everything once', 'is_correct': False}]}
            ],
            'How to sound smart in your TEDx Talk': [
                {'question_text': 'What is the main joke of the presentation?', 'choices': [{'choice_text': 'He is saying absolutely nothing of substance', 'is_correct': True}, {'choice_text': 'He is presenting a real scientific breakthrough', 'is_correct': False}, {'choice_text': 'He forgot his lines', 'is_correct': False}]},
                {'question_text': 'What does the speaker do with his hands to look smart?', 'choices': [{'choice_text': 'Puts them in his pockets', 'is_correct': False}, {'choice_text': 'Adjusts his glasses frequently', 'is_correct': True}, {'choice_text': 'Claps them together', 'is_correct': False}]},
                {'question_text': 'What mathematical term does he use to sound intelligent?', 'choices': [{'choice_text': 'A numerical anecdote', 'is_correct': True}, {'choice_text': 'The pythagorean theorem', 'is_correct': False}, {'choice_text': 'A quadratic equation', 'is_correct': False}]},
                {'question_text': 'The speaker says "This is a picture of a ..." what?', 'choices': [{'choice_text': 'Graph', 'is_correct': True}, {'choice_text': 'Cat', 'is_correct': False}, {'choice_text': 'House', 'is_correct': False}]},
                {'question_text': 'What is the speaker\'s concluding statement?', 'choices': [{'choice_text': '"Thank you."', 'is_correct': True}, {'choice_text': '"Any questions?"', 'is_correct': False}, {'choice_text': '"This is the future."', 'is_correct': False}]}
            ],
            'The Lord of the Rings - Official Trailer': [
                {'question_text': 'Who is the main protagonist who must destroy the Ring?', 'choices': [{'choice_text': 'Frodo Baggins', 'is_correct': True}, {'choice_text': 'Gandalf', 'is_correct': False}, {'choice_text': 'Aragorn', 'is_correct': False}]},
                {'question_text': 'What is the name of the evil lord who created the One Ring?', 'choices': [{'choice_text': 'Saruman', 'is_correct': False}, {'choice_text': 'Sauron', 'is_correct': True}, {'choice_text': 'Gollum', 'is_correct': False}]},
                {'question_text': 'How many rings were given to the Elven-kings?', 'choices': [{'choice_text': 'Seven', 'is_correct': False}, {'choice_text': 'Three', 'is_correct': True}, {'choice_text': 'Nine', 'is_correct': False}]},
                {'question_text': 'What is the name of the fellowship formed to destroy the ring?', 'choices': [{'choice_text': 'The Fellowship of the Ring', 'is_correct': True}, {'choice_text': 'The Council of Elrond', 'is_correct': False}, {'choice_text': 'The Riders of Rohan', 'is_correct': False}]},
                {'question_text': 'Where must the One Ring be destroyed?', 'choices': [{'choice_text': 'In the fires of Mount Doom', 'is_correct': True}, {'choice_text': 'In the mines of Moria', 'is_correct': False}, {'choice_text': 'In the city of Minas Tirith', 'is_correct': False}]}
            ],
            'What would happen if you didn’t sleep?': [
                {'question_text': 'Which part of the body is significantly affected by lack of sleep?', 'choices': [{'choice_text': 'The brain', 'is_correct': True}, {'choice_text': 'The hair', 'is_correct': False}, {'choice_text': 'The nails', 'is_correct': False}]},
                {'question_text': 'What is one of the functions of sleep mentioned in the video?', 'choices': [{'choice_text': 'Digesting food', 'is_correct': False}, {'choice_text': 'Allowing the brain to clear out toxins', 'is_correct': True}, {'choice_text': 'Growing taller', 'is_correct': False}]},
                {'question_text': 'A lack of sleep can lead to what kind of problems?', 'choices': [{'choice_text': 'Hormonal imbalance and slower reactions', 'is_correct': True}, {'choice_text': 'Improved memory', 'is_correct': False}, {'choice_text': 'Stronger immune system', 'is_correct': False}]},
                {'question_text': 'The world record for staying awake is how many days?', 'choices': [{'choice_text': '5', 'is_correct': False}, {'choice_text': '11', 'is_correct': True}, {'choice_text': '20', 'is_correct': False}]},
                {'question_text': 'What are "microsleeps"?', 'choices': [{'choice_text': 'Brief periods of sleep lasting a few seconds', 'is_correct': True}, {'choice_text': 'A type of meditation', 'is_correct': False}, {'choice_text': 'A short nap', 'is_correct': False}]}
            ],
            'Learn English with The Fresh Prince of Bel-Air': [
                {'question_text': 'What city did Will Smith\'s character originally come from?', 'choices': [{'choice_text': 'West Philadelphia', 'is_correct': True}, {'choice_text': 'Los Angeles', 'is_correct': False}, {'choice_text': 'New York', 'is_correct': False}]},
                {'question_text': 'What is the name of the family butler?', 'choices': [{'choice_text': 'Alfred', 'is_correct': False}, {'choice_text': 'Geoffrey', 'is_correct': True}, {'choice_text': 'James', 'is_correct': False}]},
                {'question_text': 'Who is Will\'s nerdy and preppy cousin?', 'choices': [{'choice_text': 'Jazz', 'is_correct': False}, {'choice_text': 'Carlton', 'is_correct': True}, {'choice_text': 'Uncle Phil', 'is_correct': False}]},
                {'question_text': 'What does the phrase "Yo, holmes, smell ya later" mean?', 'choices': [{'choice_text': 'A friendly greeting', 'is_correct': False}, {'choice_text': 'A casual way of saying goodbye', 'is_correct': True}, {'choice_text': 'An insult', 'is_correct': False}]},
                {'question_text': 'Where does the Banks family live?', 'choices': [{'choice_text': 'Compton', 'is_correct': False}, {'choice_text': 'Bel-Air', 'is_correct': True}, {'choice_text': 'Beverly Hills', 'is_correct': False}]}
            ],
            'How to Tie a Tie (Mirrored / Slowly) - The Windsor Knot': [
                {'question_text': 'The video is mirrored. What does this help with?', 'choices': [{'choice_text': 'It helps you follow the steps as if looking in a mirror', 'is_correct': True}, {'choice_text': 'It makes the video look better', 'is_correct': False}, {'choice_text': 'It is a mistake in the recording', 'is_correct': False}]},
                {'question_text': 'What is the first step shown in the video?', 'choices': [{'choice_text': 'Crossing the wide end over the narrow end', 'is_correct': True}, {'choice_text': 'Making a knot', 'is_correct': False}, {'choice_text': 'Putting the tie around the neck', 'is_correct': False}]},
                {'question_text': 'The Windsor Knot is described as a what kind of knot?', 'choices': [{'choice_text': 'A small and simple knot', 'is_correct': False}, {'choice_text': 'A wide, triangular, and symmetrical knot', 'is_correct': True}, {'choice_text': 'An informal knot', 'is_correct': False}]},
                {'question_text': 'Where does the wide end of the tie go in the final step?', 'choices': [{'choice_text': 'Through the loop in the front', 'is_correct': True}, {'choice_text': 'Around the back of the neck', 'is_correct': False}, {'choice_text': 'Under the collar', 'is_correct': False}]},
                {'question_text': 'What part of the tie should the tip of the wide end touch when finished?', 'choices': [{'choice_text': 'The top of the belt buckle', 'is_correct': True}, {'choice_text': 'The chest', 'is_correct': False}, {'choice_text': 'The shoes', 'is_correct': False}]}
            ],
            'What is writer\'s block?': [
                {'question_text': 'Writer\'s block is often a problem related to what?', 'choices': [{'choice_text': 'Perfectionism and fear of judgment', 'is_correct': True}, {'choice_text': 'A lack of pens', 'is_correct': False}, {'choice_text': 'Not having a good computer', 'is_correct': False}]},
                {'question_text': 'The video mentions that writer\'s block is NOT a what?', 'choices': [{'choice_text': 'A real problem', 'is_correct': False}, {'choice_text': 'A medical condition', 'is_correct': True}, {'choice_text': 'A common issue', 'is_correct': False}]},
                {'question_text': 'What is one of the suggested solutions to overcome writer\'s block?', 'choices': [{'choice_text': 'To stop writing for a long time', 'is_correct': False}, {'choice_text': 'To set a small, manageable goal, like writing one sentence', 'is_correct': True}, {'choice_text': 'To buy a new keyboard', 'is_correct': False}]},
                {'question_text': 'What famous author is mentioned as having suffered from writer\'s block?', 'choices': [{'choice_text': 'J.K. Rowling', 'is_correct': False}, {'choice_text': 'Herman Melville', 'is_correct': True}, {'choice_text': 'Stephen King', 'is_correct': False}]},
                {'question_text': 'The video argues that inspiration is more a product of what?', 'choices': [{'choice_text': 'Hard work', 'is_correct': True}, {'choice_text': 'Sudden genius', 'is_correct': False}, {'choice_text': 'Good luck', 'is_correct': False}]}
            ],
        }

        for video_title, questions_list in quiz_data.items():
            try:
                video = Video.objects.get(title=video_title)
                for question_data in questions_list:
                    # Usamos 'defaults' para evitar criar perguntas duplicadas se o script for rodado de novo
                    question, created = Question.objects.get_or_create(
                        video=video,
                        question_text=question_data['question_text']
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'  Pergunta para "{video.title}" criada.'))
                        for choice_data in question_data['choices']:
                            Choice.objects.create(
                                question=question,
                                choice_text=choice_data['choice_text'],
                                is_correct=choice_data['is_correct']
                            )
                    else:
                        self.stdout.write(self.style.WARNING(f'  Pergunta para "{video.title}" já existia. Pulando.'))

            except Video.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Vídeo "{video_title}" não encontrado. Pulando.'))
        
        self.stdout.write(self.style.SUCCESS('Cadastro do questionário expandido finalizado!'))