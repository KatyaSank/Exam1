class MyTestCase:
    @staticmethod
    def check_i18n():
        """Check, that first html tag consist "i18n"""
        with open(r'C:\Users\Admin\Desktop\Python\Exam\Exam1\app\view1\view1.html', 'r') as file1:
            data = file1.readlines()
            for num, x in enumerate(data):
                if '<p' in x:
                    if '<p i18n' in x:
                        pass
                    else:
                        print('File - view1. Error in p tag in line - ', str(num + 1))
                if '<button' in x:
                    if '<button i18n' in x:
                        pass
                    else:
                        print('File - view1. Error in button tag in line - ', str(num + 1))
                if '<h2' in x:
                    if '<h2 i18n' in x:
                        pass
                    else:
                        print('File - view1. Error in h2 tag in line - ', str(num + 1))
                if '<h' in x:
                    if '<h2' in x:
                        pass
                    else:
                        if '<h i18n' in x:
                            pass
                        else:
                            print('File - view1. Error in h tag in line - ', str(num + 1))

            with open(r'C:\Users\Admin\Desktop\Python\Exam\Exam1\app\view2\view2.html', 'r') as file2:
                data = file2.readlines()
                for num, x in enumerate(data):
                    if '<p' in x:
                        if '<p i18n' in x:
                            pass
                        else:
                            print('File - view2. Error in p tag in line - ', str(num + 1))
                    if '<button' in x:
                        if '<button i18n' in x:
                            pass
                        else:
                            print('File - view2. Error in button tag in line - ', str(num + 1))
                    if '<h2' in x:
                        if '<h2 i18n' in x:
                            pass
                        else:
                            print('File - view2. Error in h2 tag in line - ', str(num + 1))
                    if '<h' in x:
                        if '<h2' in x:
                            pass
                        else:
                            if '<h i18n' in x:
                                pass
                            else:
                                print('File - view1. Error in h tag in line - ', str(num + 1))

            with open(r'C:\Users\Admin\Desktop\Python\Exam\Exam1\app\view3\view3.html', 'r') as file3:
                data = file3.readlines()
                for num, x in enumerate(data):
                    if '<p' in x:
                        if '<p i18n' in x:
                            pass
                        else:
                            print('File - view3. Error in p tag in line - ', str(num + 1))
                    if '<button' in x:
                        if '<button i18n' in x:
                            pass
                        else:
                            print('File - view3. Error in button tag in line - ', str(num + 1))
                    if '<h2' in x:
                        if '<h2 i18n' in x:
                            pass
                        else:
                            print('File - view3. Error in h2 tag in line - ', str(num + 1))
                    if '<h' in x:
                        if '<h2' in x:
                            pass
                        else:
                            if '<h i18n' in x:
                                pass
                            else:
                                print('File - view3. Error in h tag in line - ', str(num + 1))


MyTestCase.check_i18n()
