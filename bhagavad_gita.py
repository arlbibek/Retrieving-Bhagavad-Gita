# Bhagvat Geeet from web scrping

'''Addtional Info
verse_sa                :   Sanskrit Version Transliteration version"
verse_literal_en        :   Exact meaning of the transliterated
verse_words_meaning_en  :   Exact meaning of the transliterated words.
verse_en                :   English translation
verse_cmnt_en           :   Commentary
verse_audio_sa          :   Audio version.
'''
import time
try:
    from bs4 import BeautifulSoup
    import requests
    print('Requirements satsfied!')
except Exception:
    print('Requirements unsatsfied!')
    print("Installing 'beautifulsoup4' & 'requests' module.")
    try:
        from subprocess import Popen
        # Runing install_requirements.bat to install 'beautifulsoup4' & 'requests'
        p = Popen("install_requirements.bat")
        stdout, stderr = p.communicate()
        print("'beautifulsoup4' & 'requests' has been instlled run the program again")
    except Exception:
        print("Do:\n\tpip install -r requirements.txt")
        input("Press Enter to exit..")
        exit()

filename = 'the_Bhagvhat_Gita.txt'
f = open(filename, 'w')
f.write("Bhagavad Gita, The Song of God\n")
f.write("******************************\n")
f.close
'''creating an empty text file'''

# setting default option, chapter and verse numbers
chap_no = 1
verse_no = 1
selected_options = 1

# used needs
user_needs = {}
user_needs['verse_sa'] = ["Sanskrit Version", 'y']
user_needs['verse_literal_en'] = ["Transliteration version", 'y']
user_needs['verse_words_meaning_en'] = [
    "Exact meaning of the transliterated words", 'y']
user_needs['verse_en'] = ["English translation", 'y']
user_needs['verse_cmnt_en'] = ["Commentary", 'y']
user_needs['verse_audio_sa'] = ["Audio version", 'y']

'''Checking if the host is up'''
print('Checking if the host is online.\nPlease wait..')
try:
    response_status = requests.get("https://www.holy-bhagavad-gita.org/")
    print('The host is UP!')
except Exception:
    print("Couldn't reach the HOST")
    exit()


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def sample_text():
    '''Sample printing'''
    sample_txt = {}
    sample_txt['1'] = ["Sanskrit version",
                       "धृतराष्ट्र उवाच | धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः | मामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय ||1|| "]
    sample_txt['2'] = ["Transliteration version",
                       "dhṛitarāśhtra uvācha dharma-kṣhetre kuru-kṣhetre samavetā yuyutsavaḥ māmakāḥ pāṇḍavāśhchaiva kimakurvata sañjaya"]
    sample_txt['3'] = ["Exact meaning of the transliterated words",
                       "dhṛitarāśhtraḥ uvācha—Dhritarashtra said; dharma-kṣhetre—the land of dharma; kuru-kṣhetre—at Kurukshetra; samavetāḥ—having gathered; yuyutsavaḥ—desiring to fight; māmakāḥ—my sons; pāṇḍavāḥ—the sons of Pandu; cha—and; eva—certainly; kim—what; akurvata—did they do; sañjaya—Sanjay "]
    sample_txt['4'] = ["English translation",
                       "Dhritarashtra said: O Sanjay, after gathering on the holy field of Kurukshetra, and desiring to fight, what did my sons and the sons of Pandu do? "]
    sample_txt['5'] = ["Commentary", "The two armies had gathered on the battlefield of Kurukshetra, well prepared to fight a war that was inevitable. Still, in this verse, King Dhritarashtra asked Sanjay, what his sons and his brother Pandu’s sons were doing on the battlefield? It was apparent that they would fight, then why did he ask such a question?..."]
    sample_txt['6'] = ["Audio version", "Not Avaliable"]

    for key, values in sample_txt.items():
        print(values[0])
        print('---')
        print(values[1] + '\n')
        time.sleep(0.5)


def spd(x):
    if x == '!SPD':
        print('Emergency Exit!!')
        exit()


def get_user_needs(un):
    for key, values in un.items():
        while True:
            user_input = input('Do you want "' + values[0] + '"?(y/n)[default = y]: ')
            spd(user_input)
            if user_input == 'y' or user_input == 'Y' or user_input == '':
                un[key][1] = 'y'
                break
            elif user_input == 'n' or user_input == 'N':
                un[key][1] = 'n'
                break
            else:
                print("Wrong input.Pless enter 'y' for 'yes' and 'n' for 'no'")
                continue

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def get_verse_title(article, chap_no, verse_no):
    '''Title: Chapter number and Verse number'''
    try:
        verse_title = article.h1.text
        return verse_title
    except Exception:
        verse_title = "HEADING NOT FOUND for chapter " + \
            str(chap_no) + " verse " + str(verse_no) + "."
        return verse_title


def get_verse_sa(article, chap_no, verse_no):
    '''Retrieving Sanskrit version of the verse'''
    try:
        verse_sa = article.find(
            'div', id="originalVerse").text.strip()
        return verse_sa
    except Exception:
        verse_sa = "SANSKRIT VERSION NOT FOUND for chapter " + \
            str(chap_no) + " verse " + str(verse_no) + "."
        return verse_sa


def get_verse_literal_en(article, chap_no, verse_no):
    '''Retrieving transliteration version of the verse'''
    try:
        verse_literal_en = article.find('div', id="transliteration").text
        # print(verse_literal_en)
        return verse_literal_en
    except Exception:
        verse_literal_en = "SANSKRIT VERSION NOT FOUND for chapter " + \
            str(chap_no) + " verse " + str(verse_no) + "."
        return verse_literal_en


def get_verse_words_meaning_en(article, chap_no, verse_no):
    '''Retrieving meaning of the transliteration version of the words in english'''
    try:
        verse_words_meaning_en = article.find('div', id="wordMeanings").text.replace(
            '; ', '\n').replace('—', ' — ').strip()
        # print(verse_words_meaning_en)
        return verse_words_meaning_en
    except Exception:
        verse_words_meaning_en = "WORDS MEANING NOT FOUND for chapter " + \
            str(chap_no) + " verse " + str(verse_no) + "."
        return verse_words_meaning_en


def get_bg(article):
    # this removes BG. 1.1 from eng translation.
    try:
        bg = article.find('div', id="translation").span.text
    except Exception:
        bg = ""
    return bg


def get_verse_en(article, chap_no, verse_no):
    '''Retrieving english tranlsation of the verse'''
    bg = get_bg(article)    # removing BG 0.0 from text
    try:
        verse_en = article.find(
            'div', id="translation").text.strip().replace(bg, '').lstrip()
        # print(verse_en)
        return verse_en
    except Exception:
        verse_en = "ENGLISH VERSION NOT FOUND for chapter " + \
            str(chap_no) + " verse " + str(verse_no) + "."
        return verse_en


def get_verse_cmnt_en(article, chap_no, verse_no):
    '''Retrieving commentary on the verse'''
    try:
        verse_cmnt_en = article.find('div', id="commentary").text.rstrip()
        # print(verse_cmnt_en)
        return verse_cmnt_en
    except Exception:
        verse_cmnt_en = "COMMENTARY NOT FOUND for chapter " + \
            str(chap_no) + " verse " + str(verse_no) + "."
        return verse_cmnt_en


def get_verse_audio_sa():
    '''Retrieving sanskrit audio versoin of the verse'''
    try:
        # SOME TASK
        # SOME TASK
        # SOME TASK
        verse_audio_sa = "Sorry audio vesion of the verse is not avaliable at the movement."
        return verse_audio_sa
    except Exception:
        verse_audio_sa = "AUDIo VERSION NOT FOUND for chapter " + \
            str(chap_no) + " verse " + str(verse_no) + "."

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def get_selected_option():
    '''prividing options to user to retrive Everyting or Specific Chapter or a Specific Verse'''
    menu_options = {}
    menu_options['1'] = "Retrive: Everything [Total: 700 Verse]"
    menu_options['2'] = "Retrive: All verse from a Chapter [Total: 18 Chapters]."
    menu_options['3'] = "Retrive: Specific Verse from a Specific Chapter."

    chapter_verse_info = {'1': "47", '2': "72", '3': "43", '4': "42", '5': "29",
                          '6': "47", '7': "30", '8': "28", '9': "34", '10': "42",
                          '11': "55", '12': "20", '13': "35", '14': "27", '15': "20",
                          '16': "24", '17': "28", '18': "78"}

    while True:
        time.sleep(0.2)
        print("\nYou can do following things: \n")
        for entry in sorted(menu_options.keys()):
            time.sleep(0.2)
            print('\t', entry + '.', menu_options[entry])

        try:
            selected_options = input("\nChoose and option: ")
            spd(selected_options)
            selected_options = int(selected_options)
        except Exception:
            print("\nPlease choose (1,2 or 3).\n")
            continue

        if selected_options == 1:
            # 1: Everything(all 701 Verse)
            print('\nOption', selected_options, ':', menu_options[str(selected_options)])
            return selected_options, 1, 1
            break

        elif selected_options == 2:
            # 2: Specific Chapter
            print('\nOption', selected_options, ':', menu_options[str(selected_options)])
            while True:
                try:
                    selected_chapter = input("\nWhich chapter?(1-18): ")
                    spd(selected_chapter)
                    selected_chapter = int(selected_chapter)
                except Exception:
                    print("\n(2a)**Invalid Input.**\n")
                    continue
                if selected_chapter >= 1 and selected_chapter <= 18:
                    return selected_options, selected_chapter, 1
                    break
                else:
                    print("\nPlease choose an interger in range (1 - 18).\n")
                    continue
            break

        elif selected_options == 3:
            # 2: Specific verse (specific verse from specific verse)
            print('\nOption', selected_options, ':', menu_options[str(selected_options)])
            while True:
                try:
                    selected_chapter = input(
                        "\nSpecific Verse form which chapter?(1-18): ")
                    spd(selected_chapter)
                    selected_chapter = int(selected_chapter)
                except Exception:
                    print("\n(3a)**Invalid Input.**\n")
                    continue

                if selected_chapter >= 1 and selected_chapter <= 18:
                    no_of_verse = chapter_verse_info[str(selected_chapter)]
                    print('\nChapter ', selected_chapter,
                          'has', no_of_verse, ' verse.')
                    while True:
                        try:
                            selected_verse = input(
                                "\nChoose a verse no?(1 - " + no_of_verse + "): ")
                            spd(selected_verse)
                            selected_verse = int(selected_verse)
                        except Exception:
                            print("\n(3b)**Invalid Input.**\n")
                            continue
                        if selected_verse >= 1 and selected_verse <= int(no_of_verse):
                            return selected_options, selected_chapter, selected_verse
                            break
                        else:
                            print(
                                "\nPlease choose an interger in range (1 - " + no_of_verse + "): ")
                            continue
                    break
                else:
                    print("\nPlease choose an interger in range (1 - 18).\n")
                    continue
            break
        else:
            print("\nPlease choose (1,2 or 3).\n")
            continue

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


selected_options, selected_chapter, selected_verse = get_selected_option()

if selected_options == 2:
    chap_no = selected_chapter
if selected_options == 3:
    chap_no = selected_chapter
    verse_no = selected_verse

print()
get_user_needs(user_needs)
print()
for key, values in user_needs.items():
    print('Retrieving Status for ' + values[0] + ': ' + values[1])
print()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

'''This is where the actual things happen'''
url_list = []
while True:
    url = "https://www.holy-bhagavad-gita.org/chapter/" + \
        str(chap_no) + "/verse/" + str(verse_no)
    print('Retrieving: ', url)
    response_status = requests.get(url).status_code
    print('Response Status: ', response_status)
    if response_status == 200:
        webpage = requests.get(url).text
        soup = BeautifulSoup(webpage, 'lxml')
        article = soup.find('article')

        # Writing the results in to a file.
        f = open(filename, 'a', encoding="utf-8")
        if get_bg(article) not in url_list:
            url_list.append(get_bg(article))

            # Calling functions and writing into the text file

            f.write('\n')
            verse_title = get_verse_title(article, chap_no, verse_no)
            f.write('-------------------------------\n')
            f.write(verse_title + '\n')

            f.write('\n')
            if user_needs['verse_sa'][1] == 'y':
                verse_sa = get_verse_sa(article, chap_no, verse_no)
                f.write(verse_sa)
                f.write('\n')
            if user_needs['verse_literal_en'][1] == 'y':
                verse_literal_en = get_verse_literal_en(
                    article, chap_no, verse_no)
                f.write(verse_literal_en)
                f.write('\n')
            if user_needs['verse_words_meaning_en'][1] == 'y':
                verse_words_meaning_en = get_verse_words_meaning_en(
                    article, chap_no, verse_no)
                f.write(verse_words_meaning_en)
                f.write('\n')
            if user_needs['verse_en'][1] == 'y':
                verse_en = get_verse_en(article, chap_no, verse_no)
                f.write(verse_en)
                f.write('\n')
            if user_needs['verse_cmnt_en'][1] == 'y':
                verse_cmnt_en = get_verse_cmnt_en(article, chap_no, verse_no)
                f.write(verse_cmnt_en)
                f.write('\n')
            f.close

            if selected_options == 3:
                print("Done!!\nVerse", selected_verse, "from chapter",
                      selected_chapter, "retrieved and saved into '" + filename + "' file.")
                print('Bye!!')
                exit()
        # Increasing the verse number by plus 1
        verse_no += 1  # increasing verse no to go to next verse
        print("Sucess!")
        # break
    elif response_status == 404:
        if selected_options == 2:
            print("Done!!\nAll verse from chapter",
                  selected_chapter, "retrieved and saved into '" + filename + "' file.")
            print('Bye!!')
            exit()
        print("Retrieving from next Chapter!")
        chap_no += 1
        verse_no = 1
    if chap_no > 18:
        print("Done!!\nALL 701 Verse of The Bhagvat Gita retrieved and saved into '" +
              filename + "' file.")
        print('Bye!!')
        exit()
