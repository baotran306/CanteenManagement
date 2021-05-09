
const checkRegex = (mySDT, myCMND) => {
    var sdt = /^[0-9]{10,11}$/
    var cmnd = /^[0-9]{9,10}$/
    if (!mySDT.match(sdt)) {
        alert("Số điện thoại phải có 10 chữ số")
        return
    }
    if (!myCMND.match(cmnd)) {
        alert("CMND phải có 9-10 chữ số")
        return
    }
}
const checkBirthday = (date) => {
    if (date == '') {
        alert('Bạn chưa chọn ngày sinh')
        return
    }
    var newDate = new Date(date)
    var dateNow = new Date()
    if (!(newDate.getFullYear() < dateNow.getFullYear() - 16)) {
        alert("Bạn cần đủ 16 tuổi để đăng ký")
        return
    }
}

const checkPass = (myPass) => {
    var pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}$/
    if (!myPass.match(pass)) {
        alert("Mật khẩu phải nhập từ 8-16 ký tự có ít nhất 1 chữ viết hoa và không sử dụng ký tự đặc biệt")
        return
    }
}

const checkUser = (myUser) => {
    var user = /^[a-zA-Z0-9]+$/
    if (!myUser.match(user)) {
        alert("Tên đăng nhập phải không dùng khoảng trắng và ký tự đặc biệt")
        return
    }
}



function addNewStaff() {
    document.getElementById("form-resgiter").onsubmit = (e) => {
        e.preventDefault();
        var user = document.getElementById("IDUSER")
        var phone = document.getElementById("Phone")
        var name = document.getElementById("Name")
        var role = document.getElementById("Role")
        var CMND = document.getElementById("CMND")
        var address = document.getElementById("Address")
        var dob = document.getElementById("Birthday")
        var gender = document.getElementById("Gender")
        var password = document.getElementById("Password")
        var repeatPassword = document.getElementById("RepeatPassword")
        var check = true;
        if (user.value == '') {
            user.focus()
            check = false
            user.placeholder = "Bạn chưa nhập tên đăng nhập"
        }
        if (phone.value == '') {
            phone.focus()
            check = false
            phone.placeholder = "Bạn chưa nhập SĐT"
        }
        if (name.value == '') {
            name.focus()
            check = false
            name.placeholder = "Bạn chưa nhập họ và tên"
        }
        if (role.value == '') {
            role.focus()
            check = false
            role.placeholder = "Bạn chưa nhập vai trò"
        }
        if (CMND.value == '') {
            CMND.focus()
            check = false
            CMND.placeholder = "Bạn chưa nhập CMND"
        }
        if (address.value == '') {
            address.focus()
            check = false
            address.placeholder = "Bạn chưa nhập địa chỉ"
        }
        if (password.value == '') {
            password.focus()
            check = false
            password.placeholder = "Bạn chưa nhập password"
        }
        if (repeatPassword.value == '') {
            repeatPassword.focus()
            repeatPassword.placeholder = "Bạn chưa nhập lại passWord"
            check = false
        }
        if (repeatPassword.value !== password.value) {
            repeatPassword.focus()
            alert("Mật khẩu nhập lại không trùng khớp")
            check = false
        }
        checkUser(user.value)
        checkRegex(phone.value, CMND.value)
        checkBirthday(dob.value)
        checkPass(password.value)
        if (check) {
            var data = {
                user: user.value,
                password: password.value,
                name: name.value,
                phone: phone.value,
                id_card: CMND.value,
                role_name: role.options[role.selectedIndex].value,
                address: address.value,
                gender: gender.options[gender.selectedIndex].value,
                dob: dob.value
            }
            fetch("http://127.0.0.1:5000/admin/register", {
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
                    if (newdata.result === false)
                        alert(newdata.error)
                    if (newdata.result === true) {
                        alert(newdata.error)
                        window.location.href = 'registerStaff.html'
                    }
                })
        }
    }
}

const addNewCustomer = function () {
    document.getElementById("form-resgiter").onsubmit = (e) => {
        e.preventDefault();
        var user = document.getElementById("IDUSER")
        var phone = document.getElementById("SDT")
        var name = document.getElementById("fullname")
        var CMND = document.getElementById("CMND")
        var address = document.getElementById("address")
        var dob = document.getElementById("Birthday")
        var gender = document.getElementById("Gender")
        var password = document.getElementById("password")
        var repeatPassword = document.getElementById("password_confirmation")
        var check = true;
        if (user.value == '') {
            user.focus()
            check = false
            user.placeholder = "Bạn chưa nhập tên đăng nhập"
        }
        if (phone.value == '') {
            phone.focus()
            check = false
            phone.placeholder = "Bạn chưa nhập SĐT"
        }
        if (name.value == '') {
            name.focus()
            check = false
            name.placeholder = "Bạn chưa nhập họ và tên"
        }

        if (CMND.value == '') {
            CMND.focus()
            check = false
            CMND.placeholder = "Bạn chưa nhập CMND"
        }
        if (address.value == '') {
            address.focus()
            check = false
            address.placeholder = "Bạn chưa nhập địa chỉ"
        }
        if (password.value == '') {
            password.focus()
            check = false
            password.placeholder = "Bạn chưa nhập password"
        }
        if (repeatPassword.value == '') {
            repeatPassword.focus()
            repeatPassword.placeholder = "Bạn chưa nhập lại passWord"
            check = false
        }
        if (repeatPassword.value !== password.value) {
            repeatPassword.focus()
            alert("Mật khẩu nhập lại không trùng khớp")
            check = false
        }
        checkUser(user.value)
        checkRegex(phone.value, CMND.value)
        checkBirthday(dob.value)
        checkPass(password.value)
        if (check) {
            var data = {
                user: user.value,
                password: password.value,
                name: name.value,
                phone: phone.value,
                id_card: CMND.value,
                address: address.value,
                gender: gender.options[gender.selectedIndex].value,
                dob: dob.value
            }
            fetch("http://127.0.0.1:5000/customer/register", {
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
                    if (newdata.result === false)
                        alert(newdata.error)
                    if (newdata.result === true) {
                        alert(newdata.error)
                        window.location.href = 'loginCustom.html'
                    }
                })
        }
    }
}

const addNewFood = function () {
    var foodName = document.getElementById('foodName')
    var price = document.getElementById('price')
    var description = document.getElementById('description')
    var inputIMG = document.getElementById('myInputImg')
    if (foodName.value == '') {
        foodName.focus()
        foodName.placeholder = "Bạn chưa nhập tên món ăn"
    }
    if (price.value == '') {
        price.focus()
        price.placeholder = 'Bạn chưa nhập giá tiền'
    }
    if (description.value == '') {
        description.focus()
        description.placeholder = 'Hãy nhập 1 số mô tả cho khách hàng cùng biết'
    }
    try {
        var pic = inputIMG.files[0].name
    } catch (error) {
        inputIMG.focus()
        alert("Hãy chọn ảnh")
        return
    }
    var data = {
        name: foodName.value,
        price: price.value,
        describe: description.value,
        image: pic
    }
    fetch('http://127.0.0.1:5000/admin/food', {
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
            alert(newdata.error)
        })
}
