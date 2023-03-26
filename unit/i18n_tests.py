import os


def check_i18n():
    """Check, that first html tag consist "i18n"""

    path = "C:\\Users\\Admin\\Desktop\\Python\\Exam\\Exam1\\app"
    for (root, dirs, file) in os.walk(path):
        for f in file:
            if '.html' in f:
                fullpath = os.path.join(path, root, f)
                with open(fullpath, 'r') as file1:
                    data = file1.readlines()
                    for num, x in enumerate(data):
                        if '<p' in x:
                            if '<p i18n' in x:
                                pass
                            else:
                                print(f'Error in {f}(<p>), line - ', str(num + 1))
                        if '<button' in x:
                            if '<button i18n' in x:
                                pass
                            else:
                                print(f'Error in {f}(<button>), line - ', str(num + 1))
                        if '<h2' in x:
                            if '<h2 i18n' in x:
                                pass
                            else:
                                print(f'Error in {f}(<h2>), line - ', str(num + 1))
                        if '<h' in x:
                            if '<h2' in x:
                                pass
                            else:
                                if '<h i18n' in x:
                                    pass
                                else:
                                    print(f'Error in {f}(<h>), line - ', str(num + 1))


check_i18n()
