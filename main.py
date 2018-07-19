import csv
import re

import pymorphy2
import string

from click._unicodefun import click
from nltk import MWETokenizer


def tokenize_text(text):
    tokenizer = MWETokenizer()

    punctuation = string.punctuation
    text = re.sub(rf'[{punctuation}]', '', text)

    return tokenizer.tokenize(text.split())


def get_pos(parse):
    parts_of_speech = {
        "NOUN": "существительное",
        "ADJF": "прилагательное(полное)",
        "ADJS": "прилагательное(краткое)",
        "COMP": "компаратив",
        "VERB": "глагол(личная форма)",
        "INFN": "глагол(инфинитив)",
        "PRTF": "причастие(полное)",
        "PRTS": "причастие(краткое)",
        "GRND": "деепричастие",
        "NUMR": "числительное",
        "ADVB": "наречие",
        "NPRO": "местоимение - существительное",
        "PRED": "предикатив",
        "PREP": "предлог",
        "CONJ": "союз",
        "PRCL": "частица",
        "INTJ": "междометие"
    }

    return parts_of_speech[parse.tag.POS]


def get_number(number):
    if number == "sing":
        return "единственное"
    elif number == "plur":
        return "множественное"


def get_case(case):
    if case is None:
        return None
    cases = {"nomn": "именительный",
             "gent": "родительный",
             "datv": "дательный",
             "accs": "винительный",
             "ablt": "творительный",
             "loct": "предложный",
             "voct": "звательный",
             "gen2": "второй родительный(частичный)",
             "acc2": "второй винительный",
             "loc2": "второй предложный(местный)"
             }

    return cases[case]


def get_gender(gender):
    if gender == "masc":
        return "мужской"
    elif gender == "femn":
        return "женский"
    elif gender is None:
        return ""


def get_header():
    header = {'word': "Слово", 'POS': "Часть речи", 'number': "Число", 'case': "Падеж",
              'gender': "Пол"}

    return header


def save_to_csv(data):
    csv_file_name = "data.csv"
    header = get_header()

    with open(csv_file_name, "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([v for k, v in header.items()])

    with open(csv_file_name, "a", encoding='utf-8', newline='') as file:
        dict_writer = csv.DictWriter(file, header, delimiter=';')
        dict_writer.writerows(data)


def analyze_text(text):
    words = tokenize_text(text)
    morph = pymorphy2.MorphAnalyzer()

    text_data = []
    for word in words:
        info = {}
        parse = morph.parse(word)[0]
        info['word'] = word
        info['POS'] = get_pos(parse)
        info['number'] = get_number(parse.tag.number)
        info['case'] = get_case(parse.tag.case)
        info['gender'] = get_gender(parse.tag.gender)

        # print(info)
        # print(parse, end='\n\n')

        text_data.append(info)

    save_to_csv(text_data)


@click.command()
@click.option("-f", "--filename", help="Source file with text")
def main(filename):
    with open(filename, encoding='utf-8') as file:
        analyze_text(file.read())


if __name__ == "__main__":
    main()
