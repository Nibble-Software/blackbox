from blackbox.evaluation.temp_files import delete_temp_file, create_temp_file


def test_cpp_workflow():
    body = """
    #include<iostream>
    
    using namespace std;
    
    int main(){
        cout<<"Hello World!"<<endl;
        return 0;
    }
    """

    filename = create_temp_file(body, "c++")

    assert filename is not None

    print(filename)

    delete_temp_file(filename)


def test_python_workflow():
    body = """print("Hello World!")"""

    filename = create_temp_file(body, "python")

    print(filename)

    assert filename is not None

    delete_temp_file(filename)
