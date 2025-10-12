from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def test1():
    print('Result for current directory: ')
    print(get_files_info("calculator", "."))

    print('Result for \'pkg\' directory: ')
    print(get_files_info("calculator", "pkg"))

    print("Result for '/bin' directory")
    print(get_files_info("calculator", '/bin'))

    print("Result for '../' directory")
    print(get_files_info('calculator', '../'))


def test2():
    #print(get_file_contents('calculator', 'lorem.txt'))

    print(get_file_content("calculator", "main.py"))

    print(get_file_content("calculator", "pkg/calculator.py"))
    
    print(get_file_content("calculator", "/bin/cat"))

    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == '__main__':
    test2()
