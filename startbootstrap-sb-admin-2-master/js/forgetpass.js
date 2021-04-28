const getAgainPass = function () {
    document.getElementById("form-restpass").onsubmit = (e) => {
        e.preventDefault();
        var user = document.getElementById('UserName')
        var CMND = document.getElementById('CMND')
        var phone = document.getElementById('SDT')
        var password = document.getElementById('password')
        var repeat = document.getElementById('repeatpassword')
        var check = true
        if (user.value == '') {
            user.focus()
            check = false
            user.placeholder = 'Bạn chưa nhập tên đăng nhập'
        }
        if (CMND.value == '') {
            CMND.focus()
            check = false
            CMND.placeholder = 'Bạn chưa nhập CMND'
        }
        if (phone.value == '') {
            phone.focus()
            check = false
            phone.placeholder = 'Bạn chưa nhập SĐT'
        }
        if (password.value == '') {
            password.focus()
            check = false
            password.placeholder = 'Bạn chưa nhập mật khẩu'
        }
        if (repeat.value == '') {
            repeat.focus()
            check = false
            repeat.placeholder = 'Bạn chưa nhập lại mật khẩu'
        }
        if (password.value !== repeat.value) {
            repeat.focus()
            check = false
            alert("Nhập lại mật khẩu không trùng khớp")
        }
        if (check) {
            var data = {
                user: user.value,
                id_card: CMND.value,
                phone: phone.value,
                new_pass: password.value
            }
            fetch("http://127.0.0.1:5000/customer/reset_password", {
                method: 'POST',
                mode: 'cors',
                cache: 'no-cache',
                credentials: 'same-origin',
                headers: {
                    'Content-Type': 'application/json'
                },
                redirect: 'follow',
                referrerPolicy: 'no-referrer',
                body: JSON.stringify(data)
            })
                .then(res => res.json())
                .then(newdata => {
                    console.log(newdata)
                    if (newdata.result == true) {
                        alert(newdata.error)
                        window.location.href = 'loginCustom.html'
                    }
                    if (newdata.result == false) {
                        alert(newdata.error)
                    }

                })
        }
    }
}
