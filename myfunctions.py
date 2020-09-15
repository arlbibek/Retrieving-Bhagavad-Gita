"""All the function used in: Retrieving Bhagvat Gita from web-scraping"""
import time

# START: Dynamic functions #
# Functions than can be used in other programs as well (with few modifications of course).


def pause():
    """Similar to pause on power shell"""
    input('\nPress [Return] to continue..')


def drawline(length, line='-'):
    """An horizontal line of 'of' with length of 'length'"""
    return ''.join([line[:1]] * (length))


def clear_screen():
    """Clear console screen"""
    import platform as pf
    from os import system as sys
    try:
        if pf.system().startswith('Windows'): sys('cls')  # on windows
        else: sys('clear')  # on Linux / os x
        print('I just cleared your screen!')
    except Exception: pass


def get_filename():
    """Returns filename with extension (.txt or .md)"""
    print(
        'What do you want to name your output file?[Default = Bhagavad Gita.md]')
    while True:
        try:
            filename = input(
                'Enter filename: ')
            if len(filename) < 1: filename = 'Bhagavad Gita.md'
            if filename.endswith('.txt') or filename.endswith('.md'):
                print(f'Your file will be named {filename}')
                return filename
            print("Enter file extension (.txt or .md) as well.")
            print(
                "  .txt for Text file\n  .md  for Markdown file*")
        except KeyboardInterrupt: exit('Abort!')
        except EOFError: continue


def display_menu(option_dict):
    """Display dict.items (key, values) in beautiful fashion."""
    max_len = max([len(v) for v in option_dict.values()]) + 4
    line = drawline(max_len + 8, '_')
    clear_screen()
    print("\n    The Holy Bhagavad Gita")
    print(f'{line}\n')
    for key, value in option_dict.items():
        if key == 7:
            value += '\t    [CTRL + C] will terminate the process'
        print(f'    [{key}] {value}')
        if key in [2, 5]:
            print(f'    {drawline(max_len)}')

    print(f'{line}')


# END: Dynamic functions

# START: Static functions #
# Functions designed specifically for the program 'main.py'

def display_sample():
    '''Prints sample text to the console'''
    sample = dict()
    sample['Sanskrit Version'] = "धृतराष्ट्र उवाच | धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः | मामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय ||1||"
    sample["Transliteration version"] = "dhṛitarāśhtra uvācha dharma-kṣhetre kuru-kṣhetre samavetā yuyutsavaḥ māmakāḥ pāṇḍavāśhchaiva kimakurvata sañjaya"
    sample["Exact meaning of the transliterated words"] = "dhṛitarāśhtraḥ uvācha—Dhritarashtra said; dharma-kṣhetre—the land of dharma; kuru-kṣhetre—at Kurukshetra; samavetāḥ—having gathered; yuyutsavaḥ—desiring to fight; māmakāḥ—my sons; pāṇḍavāḥ—the sons of Pandu; cha—and; eva—certainly; kim—what; akurvata—did they do; sañjaya—Sanjay"
    sample["English translation"] = "Dhritarashtra said: O Sanjay, after gathering on the holy field of Kurukshetra, and desiring to fight, what did my sons and the sons of Pandu do?"
    sample["Commentary"] = "Commentary", "The two armies had gathered on the battlefield of Kurukshetra, well prepared to fight a war that was inevitable. Still, in this verse, King Dhritarashtra asked Sanjay, what his sons and his brother Pandu’s sons were doing on the battlefield? It was apparent that they would fight, then why did he ask such a question?"
    sample["Audio version"] = "Not Available"

    print('\nContents of the Chapter 1, Verse 1')
    for k, v in sample.items():
        time.sleep(0.25)
        print(f'{k}:\n{v}\n')


def include_extra():
    '''Returns True if users want to write additional content to the output file; False otherwise.'''
    print("""
Do your want to write the following to the output file as well?
    - Transliteration: Transliteration of the Original Verse
    - Words Meaning: Exact meaning of the transliterated words
    - Commentary: Extensive explanation of the verse.
    * Original Verse and it's English translation is included by default.
""")
    while True:
        try:
            include = input('Enter here (y/n)[Return = No]: ').title()
            if include in ['Y', 'Yes']:
                print(f'[OK] will write Everything.\n')
                return True
            elif len(include) < 1 or include in ['N', 'No']:
                print(
                    f"[OK] will write Original verse and it's English translation only.\n")
                return False
            print("Enter 'y' for 'Yes' or 'n' for 'no'")
        except KeyboardInterrupt: exit('Abort!')


def getC_title(html, chap_num):
    """Extract Chapter Title such as:  'Chapter 1 : Arjun Viṣhād Yog'"""
    try: return html.find('a', href=f"/chapter/{chap_num}").text
    except Exception: return f"CHAPTER TITLE NOT FOUND."


def getV_title(html):
    """Extract Verse Title such as: 'Chapter 1 Verse 3'"""
    try: return html.h1.text.strip("Bhagavad Gita:").strip()
    except Exception: return "VERSE TITLE NOT FOUND."


def get_originalVerse(html):
    """Extract Sanskrit version of the verse"""
    try: return html.find(
        'div', id="originalVerse").text.strip()
    except Exception: return "SANSKRIT VERSION NOT FOUND."


def get_transliteration(html):
    """Extract transliteration version of the verse"""
    try:
        return html.find('div', id="transliteration").text.strip()
    except Exception:
        return "TRANSLITERATION VERSION NOT FOUND."


def get_wordMeanings_en(html):
    """Extract Meaning of the transliteration version of the words in English"""
    try:
        return html.find('div', id="wordMeanings").text.replace(
            '; ', '\n> - ').replace('—', ' — ').strip()
    except Exception: return "WORDS MEANING NOT FOUND"


def get_translation_en(html):
    """Extracting English translation of the verse"""
    def get_bg(html):
        # Extract BG.___ from English translation.
        try: return html.find('div', id="translation").span.text
        except Exception: return ""
    try:
        return html.find(
            'div', id="translation").text.strip().replace(get_bg(html), '').lstrip()
    except Exception:
        return "ENGLISH VERSION NOT FOUND."


def get_commentary_en(html):
    """Retrieving commentary on the verse"""
    try:
        return html.find('div', id="commentary").text.strip()
    except Exception: return "COMMENTARY NOT FOUND."


def get_audio_sa():
    """Extract and download Audio (in Sanskrit) of the verse."""
    print("Audio version of the verse is NOT DOWNLOADABLE at the movement.")
    # SOME TASK
    # SOME TASK


def get_option(info, options):
    """Returns (Selected Options, Chapter Number and Verse Number)"""
    # Note: This function calls an sub function called get_retrieving_info() itself
    msg = ""
    while True:
        print(f'{msg}')
        display_menu(options)
        keys = [i for i in options.keys()]
        try:
            user_input = int(input(
                f'\nChoose and Enter an option {keys}: '))
            if user_input not in keys:
                msg = f'Error: {user_input} not in {keys}'
                continue
            time.sleep(0.5)
            result = f'[{user_input}] : {options[user_input]}'
            len_r = len(result) + 1
            print(drawline(len_r))
            print(result)

            # Option: Exit
            if user_input == 7:
                time.sleep(0.7)
                exit('Exiting..')

            # Read Me
            elif user_input == 1:
                print('Not Available at the movement.')
                pause()

            # Option: Print Sample
            elif user_input == 2:
                display_sample()
                pause()

            # Option: Retrieve
            elif user_input in [3, 4, 5]:
                return get_retrieving_info(user_input, info)
                break
            elif user_input == 6:
                return randChapterVerse(user_input, info)
        except KeyboardInterrupt: exit('Abort!')
        except EOFError:
            msg = "Enter 'CTRL + C' to exit."
            continue
        except ValueError:
            msg = "Error: Enter and valid integer value."
            continue


def get_retrieving_info(option, info):
    """Returns '(Selected Options, Chapter Number and Verse Number)' based on user inputs"""
    # Note: This function is a part of get_option()

    # Option: Retrieve: Everything
    if option == 3:
        return option, 1, 1

    # Option: Retrieve: All Verses from a Chapter & Specific Verse from a Specific Chapter
    elif option in [4, 5]:

        print(
            f'\nThe Bhagavad Gita has {len(info.keys())} chapters.')
        while True:
            chap = [chap for chap in info.keys()]
            chap_range = f'{chap[0]} - {chap[-1]}'
            try:
                chap_opt = int(
                    input(f'Choose and enter a chapter number [{chap_range}]\n: '))
                if chap_opt not in chap:
                    print(f"Enter value in range({chap_range})")
                    continue
                print(f'\nChapter {chap_opt} it is.')
                # For: All Verses from a Chapter
                if option == 4:
                    print(
                        f'Will retrieve {info[chap_opt]} verses from chapter {chap_opt}')
                    return option, chap_opt, 1

                # For: Specific Verse from a Specific Chapter
                print(
                    f'\nChapter {chap_opt} has {info[chap_opt]} verses.')
                while True:
                    try:
                        total_verse = info[chap_opt]
                        verse_range = f'1 - {total_verse}'
                        verse_opt = int(
                            input(f'Choose and enter a verse number [{verse_range}]\n: '))
                        if verse_opt not in range(1, total_verse + 1):
                            print(f"Enter value in range {verse_range}")
                            continue
                        return option, chap_opt, verse_opt
                    except KeyboardInterrupt: exit('Abort!')
                    except EOFError:
                        print("Enter 'CTRL + C' to exit.")
                        continue
                    except ValueError:
                        print('Error: Please enter a valid integer value.')
                        continue
            except KeyboardInterrupt: exit('Abort!')
            except EOFError:
                print("Enter 'CTRL + C' to exit.")
                continue
            except ValueError:
                print('Error: Please enter a valid integer value.')
                continue


# END: Static functions #

# if __name__ == "__main__":
#     print("Run 'main.py'")

# # The End


def randChapterVerse(opt, info):
    '''Returns Random Chapter number, Verse number'''
    import random
    '''random quote'''
    chapter = [k for k in info.keys()]
    randChapter = random.randrange(1, len(chapter) + 1)
    randVerse = random.randrange(1, info[randChapter] + 1)
    return opt, randChapter, randVerse
