def triage(data):
    triage_output = []
    for user in data:
        print('\n')
        print(user['login'] + ':  ' + user['bio'])
        decide(user, triage_output)
    return triage_output


def decide(user, triage_output):
    decide = input('is this a librarian? [Y/n]: ')
    if decide == 'n':
        pass
    elif (decide == '' or decide == 'y'):
        triage_output.append(user)
    else:
        print('error')
        decide()
