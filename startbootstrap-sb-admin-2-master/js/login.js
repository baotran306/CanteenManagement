

function loginCustomer() {
    document.getElementById("form-1").onsubmit = (e) => {
        e.preventDefault();
        var user = document.getElementById('User').value
        var password = document.getElementById('password').value
        if (user == '') {
            alert("Chưa nhập tên đăng nhập")
            return
        }
        if (password == '') {
            alert("Bạn chưa nhập mật khẩu")
            return
        }
        var data = {
            user: user,
            password: password
        }
        
        fetch("http://127.0.0.1:5000/customer/login", {
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
                // console.log(newdata)
                if (newdata.result === false)
                    alert(newdata.error)
                if (newdata.result === true) {
                    sessionStorage.setItem('IdCustomer', newdata.id)
                    sessionStorage.setItem('NameCustomer', newdata.name)
                    sessionStorage.setItem('Vip', newdata.vip)
                    sessionStorage.setItem('UserCustomer',user)
                }
                // console.log(sessionStorage.getItem('Id'))
                if (sessionStorage.getItem('IdCustomer') != null) {
                    window.location.href = 'homepage.html'
                }
            })
    }
}



function loginStaff() {

    var user = document.getElementById('userName').value
    var password = document.getElementById('passWord').value
    if (user == '') {
        alert("Chưa nhập tên đăng nhập")
        return
    }
    if (password == '') {
        alert("Bạn chưa nhập mật khẩu")
        return
    }
    var data = {
        user: user,
        password: password
    }
    fetch("http://127.0.0.1:5000/staff/login", {
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
            // console.log(newdata)
            if (newdata.result === false)
                alert(newdata.error)
            if (newdata.result === true) {
                sessionStorage.setItem('IdStaff', newdata.id)
                sessionStorage.setItem('NameStaff', newdata.name)
                sessionStorage.setItem('Role', newdata.role)
                sessionStorage.setItem('UserStaff',user)
            }
            // console.log(sessionStorage.getItem('Role').toLocaleLowerCase)
            if (sessionStorage.getItem('Role').toLocaleLowerCase() === 'quản lý') {
                window.location.href = 'turnover.html'
            }
            if (sessionStorage.getItem('Role').toLocaleLowerCase() === 'nhân viên giao hàng') {
                window.location.href = 'shipper.html'
            }
            if (sessionStorage.getItem('Role').toLocaleLowerCase() === 'thu ngân') {
                window.location.href = 'saler.html'
            }
        })
}






