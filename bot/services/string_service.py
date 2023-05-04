from bot.services.language_service import get_word

def question_caption_string(question, lang):
    text = "{index}.\n{question}".format(
        index = question.index,
        question = question.text_uz if lang == 'uz' else question.text_ru
    )
    return text