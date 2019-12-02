

function my_js_func() {
    console.log('my js function...');
    let username_info = 'doubleZ';
    let password_info = '1234';
    let data = {
        username: username_info,
        password: password_info
    };

    console.log('调用my_python_function');

    eel.my_python_func(data);       //使用json传递数据
}