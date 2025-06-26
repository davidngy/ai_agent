# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info
from functions.get_file_content import  get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    # print("TESTING\n")
    # print('"""""""""""""\n')
    # print(get_files_info("calculator", "."))
    # print('"""""""""""""\n')
    # print(get_files_info("calculator", "pkg"))
    # print('"""""""""""""\n')
    # print(get_files_info("calculator", "/bin"))
    # print('"""""""""""""\n')
    # print(get_files_info("calculator", "../")) 
    # print('"""""""""""""\n')
    # print(get_file_content("calculator", "main.py"), "\n",
    # get_file_content("calculator", "pkg/calculator.py"),"\n",
    # get_file_content("calculator", "/bin/cat"))
    # print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    # print("\n")
    # print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    # print("\n")
    # print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
    # print("\n")
    # print(write_file("calculator", "/pkg/temp", "this should not be allowed"))
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "main.py"))
    print(run_python_file("calculator", "tests.py"))
    print(run_python_file("calculator", "../main.py"))
    print(run_python_file("calculator", "nonexistent.py"))
if __name__ == "__main__":
    test()
