from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

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

def test3():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

def test4():
    print(run_python_file("calculator", "main.py"))

    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print(run_python_file("calculator", "tests.py"))

    print(run_python_file("calculator", "../main.py"))

    print(run_python_file("calculator", "nonexistent.py"))

    print(run_python_file("calculator", "lorem.txt"))



    

if __name__ == '__main__':
    test4()
