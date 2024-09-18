from blackbox.blackbox import blackbox


def test_success_on_hello_world_cpp():
    outputs = ["HELLO WORLD"]

    expected = {"status": "PASSED", "expected": outputs, "got": outputs}

    code = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }"""

    overview = blackbox("c++", code, None, outputs)

    assert expected == overview


def test_failed_on_hello_world_cpp():
    outputs = ["BYE WORLD"]

    expected = {"status": "FAILED", "expected": outputs, "got": ["HELLO WORLD"]}

    code = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }"""

    overview = blackbox("c++", code, None, outputs)

    assert expected == overview


def test_compilation_error_on_hello_world_cpp():
    outputs = ["HELLO WORLD"]

    expected = {"status": "COMPILATION_ERROR", "expected": outputs, "got": []}

    code = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD")
        return 0;
    }"""

    overview = blackbox("c++", code, None, outputs)

    assert expected == overview


def test_correct_sum_in_cpp():
    outputs = ["5", "7", "0"]

    inputs = ["3", "2 3", "6 1", "1 -1"]

    expected = {"status": "PASSED", "expected": outputs, "got": outputs}

    code = """
    #include <stdio.h>
    int main(){
        int a,b,num;
        
        scanf("%d",&num);
        
        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);
            
            printf("%d\\n",a+b);
            
        
        }
    
    }
    """

    overview = blackbox("c++", code, inputs, outputs)

    assert overview == expected


def test_incorrect_sum_in_cpp():
    outputs = ["5", "7", "0"]

    inputs = ["3", "2 3", "6 1", "1 -1"]

    expected = {"status": "FAILED", "expected": outputs, "got": ["-1", "5", "2"]}

    code = """
    #include <stdio.h>
    int main(){
        int a,b,num;

        scanf("%d",&num);

        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);

            printf("%d\\n",a-b);


        }

    }
    """

    overview = blackbox("c++", code, inputs, outputs)

    assert overview == expected


def test_compilation_error_sum_in_cpp():
    outputs = ["5", "7", "0"]

    inputs = ["3", "2 3", "6 1", "1 -1"]

    expected = {"status": "COMPILATION_ERROR", "expected": outputs, "got": []}

    code = """
    #include <stdio.h>
    int main(){
        int a,b,num;

        scanf("%d",&num)

        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);

            printf("%d\\n",a-b);


        }

    }
    """

    overview = blackbox("c++", code, inputs, outputs)

    assert overview == expected


def test_timeout_error_sum_in_cpp():
    outputs = ["5", "7", "0"]

    inputs = ["3", "2 3", "6 1", "1 -1"]

    expected = {"status": "TIMEOUT_ERROR", "expected": outputs, "got": []}

    code = """
    #include <stdio.h>
    int main(){
        int a,b,num;

        scanf("%d",&num);

        for(int i = 0; i < num ; i++){
            scanf("%d",&a);
            scanf("%d",&b);

            printf("%d\\n",a-b);


        }
        while(1);
        
        return 0;

    }
    """

    overview = blackbox("c++", code, inputs, outputs)

    assert overview == expected
