import os
import consultant_work_downloader


def main():
    print_header()
    folder = get_or_create_download_directory()
    print()
    work_count = get_integer('How much work do you want? (Enter number of images to download; default is 8) ')
    print()
    download_work(folder, work_count)
    # display folder


def print_header():
    print('-----------------------------------')
    print('    CONSULTANT WORK DOWNLOADER')
    print('-----------------------------------')
    print()


def get_integer(question):
    ask = input(question)
    try:
        work_count = int(ask)
        return work_count
    except ValueError:
        if ask == 'exit':
            print('Exiting...')
            exit()
        elif not ask:
            return 8
        else:
            print('Please enter an integer.')
            return get_integer(question)


def get_or_create_download_directory():
    dirname = input('In what folder would you like your work delivered? ')
    base_folder = os.path.dirname(__file__)
    full_path = os.path.join(base_folder, dirname)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new folder at {}'.format(full_path))
        os.mkdir(full_path)
        print('The new "{}" folder has been created in the same directory this file is in.'.format(dirname))
    else:
        print('The "{}" folder has been found in the directory this file is in.'.format(dirname))

    return full_path


def download_work(folder, count=8):
    print('Contacting consultingrandomworkgenerator.com to download work...')
    for i in range(1, count+1):
        name = 'Consultant_babble_{}'.format(i)
        print('Downloading work request', name)
        consultant_work_downloader.get_work(folder, name)
    print('Done.')


if __name__ == '__main__':
    main()
