from bot.bot import *
from app.services.question_service import *

def to_the_get_answer(update, context):
    # get bot user
    bot_user = get_object_by_update(update)
    # get question index from bot user
    question_index = bot_user.next_question
    # check question
    if not check_question_availability_by_index(question_index):
        update_message_reply_text(update, get_word('you dont have not answered questions', update))
        # update_message_reply_text(update, get_word('question is not available', update))
        main_menu(update, context)
        return ConversationHandler.END
    # get question by index
    question = get_question_by_index(question_index)
    # set question obj to user_data
    context.user_data['question'] = question
    # get bot user language
    lang = bot_user.lang
    # generate text
    text = question_caption_string(question, lang)
    # get photo and video by language
    photo = question.photo_uz if lang == 'uz' else question.photo_ru
    video = question.video_uz if lang == 'uz' else question.video_ru
    # inline keyboard markup button
    markup = question_keyboard(update)
    # remove keyboards
    bot_send_and_delete_message(update, context, text, reply_keyboard_remove())
    # send message
    bot_send_chat_action(update, context)
    msg = send_newsletter(bot, update.message.chat.id, text, photo, video, reply_markup=markup)
    # set last msg
    set_last_msg_and_markup(context, msg, markup)
    return GET_ANSWER
    
@is_start
def get_answer_query(update, context):
    update = update.callback_query
    # get bot_user
    bot_user = get_object_by_update(update)
    if update.data == 'help':
        # get question obj from user_data
        question = context.user_data['question']
        text = question.help_uz if bot_user.lang == 'uz' else question.help_uz
        bot_answer_callback_query(update, context, text)

@is_start
def get_answer(update, context):
    # get bot user
    bot_user = get_object_by_update(update)
    # get user answer by message
    user_answer = update.message.text
    # get question from user data
    question = context.user_data['question']
    # get the real answer from question
    true_answer = question.answer_uz if bot_user.lang == 'uz' else question.answer_ru
    # compare two words and get similarity percent
    similarity_percent = words_similarity_percentage(true_answer, user_answer)
    if similarity_percent >= question.answer_similarity:
        # change next question index of bot user
        plus_object_next_question(update)
        # send message
        update_message_reply_text(update, get_word('true answer', update))
        return to_the_get_answer(update, context)
    else:
        update_message_reply_text(update, get_word('incorrect answer', update))
        return