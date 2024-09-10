import telebot

def sendMessage(message_telegram,numero):
    API_TOKEN = '7520118227:AAH8HtGJBo2KubqGSRNpMDGSXCUVTNi4mNE'
    bot = telebot.TeleBot(API_TOKEN)
    CHAT_ID = '5534428149'
    numbers_of_file = read_numbers_from_file("data\\output.txt")
    if not check_number_in_list(int(numero), numbers_of_file):
        with open("data\\output.txt", 'a') as f:
            f.write(f"{numero}\n")
        bot.send_message(CHAT_ID, message_telegram)

def read_numbers_from_file(file_path):
    numbers = []
    with open(file_path, 'r') as f:
        for line in f:
            # Suppression des espaces et sauts de ligne, puis conversion en entier
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                # Si la ligne n'est pas un nombre valide, on l'ignore
                continue
    return numbers

def check_number_in_list(number, numbers_list):
    return number in numbers_list


