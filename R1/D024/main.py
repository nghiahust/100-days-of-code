with open('./Input/Names/invited_names.txt') as input_names:
    invites_list = input_names.readlines()
with open('./Input/Letters/starting_letter.txt') as letter:
    letter_lines = letter.read()
    for name in invites_list:
        stripped_name = name.strip()
        content = letter_lines.replace('[name]', stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', mode='w') as written_letter:
            written_letter.write(content)