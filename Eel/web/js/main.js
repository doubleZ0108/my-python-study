/* js向python发送数据 */
function my_js_func_send_data() {
    console.log('my js function...');
    let username_info = 'doubleZ';
    let password_info = '1234';
    let data = {
        username: username_info,
        password: password_info
    };

    console.log('调用my_python_function');

    eel.my_python_func_receive_data(data);       //使用json传递数据
}


/* js向python传数据并得到返回值 */
async function my_js_func_receive_data(){
    let origin_data = "111";

    let data = await my_js_func_receive_data_async(origin_data);
    console.log(data, data.username, data.password);
}

async function my_js_func_receive_data_async(origin_data){
    let data = eel.my_python_func_send_data(origin_data)();        //这里必须用两个括号
    return data;
}