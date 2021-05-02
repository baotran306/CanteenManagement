
let activeForm = (element) => {
    let c = document.getElementById("modal");
    c.style.display = "flex";
    var foodId = document.getElementById('food_id')
    var foodName = document.getElementById('food_name')
    var foodPrice = document.getElementById('food_price')
    var foodDescription = document.getElementById('food_description')
    var foodImg = document.getElementById('myImgLoad')
    console.log(element.id)
    var listInfo = document.getElementsByClassName(element.id)
    console.log(listInfo)
    console.log(listInfo[1].src)
    foodImg.src = listInfo[1].src
    foodId.value = listInfo[2].innerHTML
    foodName.value = listInfo[3].innerHTML
    foodPrice.value = listInfo[4].innerHTML
    foodDescription.value = listInfo[5].innerHTML

}

let closeForm = () => {

    let c = document.getElementById("modal");
    c.style.display = "none";

}

let editMenu = () => {
    var foodId = document.getElementById('food_id')
    var foodName = document.getElementById('food_name')
    var foodPrice = document.getElementById('food_price')
    var foodDescription = document.getElementById('food_description')
    var foodImg = document.getElementById('myInputImg')
    var nameIMG = ''
    try {
        nameIMG = foodImg.files[0].name
    } catch (error) {
        nameIMG = ''
    }
    var data = {
        foodId: foodId.value,
        foodName: foodName.value,
        foodPrice: foodPrice.value,
        foodDescription: foodDescription.value,
        foodImg: nameIMG
    }
    fetch("http://127.0.0.1:5000//admin/manage/update/food/update", {
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
        .then(newData => {
            if (newData.result == true) {
                alert(newData.error)
                window.location.reload()
            }
            if (newData.result == false) {
                alert(newData.error)
            }
        })
}
let openModal = function () {
    let c = document.getElementById("modal");
    c.style.display = "flex";
}


let changepass = function () {

    var oldpass = document.getElementById('oldpass')
    var newpass = document.getElementById('newpass')
    var repeatpass = document.getElementById('repeatpass')
    var check = true
    if (oldpass.value == '') {
        oldpass.focus()
        oldpass.placeholder = 'Bạn chưa nhập mật khẩu cũ'
        check = false
    }
    if (newpass.value == '') {
        newpass.focus()
        newpass.placeholder = 'Bạn chưa nhập mật khẩu mới'
        check = false
    }
    if (repeatpass.value == '') {
        repeatpass.focus()
        repeatpass.placeholder = 'Bạn chưa nhập lại mật khẩu mới'
        check = false
    }
    if (repeatpass.value != newpass.value) {
        alert('Mật khẩu nhập lại không trùng khớp')
        repeatpass.focus()
        check = false
    }
    if (check) {
        var data = {
            user: sessionStorage.getItem('UserCustomer'),
            old_pass: oldpass.value,
            new_pass: newpass.value
        }
        fetch(`http://127.0.0.1:5000/customer/change_password`, {
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
            .then(newData => {
                if (newData.result == true) {
                    alert(newData.error)
                    window.location.reload()
                }
                if (newData.result == false) {
                    alert(newData.error)
                }
            })
    }
}

let changepassStaff = function () {

    var oldpass = document.getElementById('oldpass')
    var newpass = document.getElementById('newpass')
    var repeatpass = document.getElementById('repeatpass')
    var check = true
    if (oldpass.value == '') {
        oldpass.focus()
        oldpass.placeholder = 'Bạn chưa nhập mật khẩu cũ'
        check = false
    }
    if (newpass.value == '') {
        newpass.focus()
        newpass.placeholder = 'Bạn chưa nhập mật khẩu mới'
        check = false
    }
    if (repeatpass.value == '') {
        repeatpass.focus()
        repeatpass.placeholder = 'Bạn chưa nhập lại mật khẩu mới'
        check = false
    }
    if (repeatpass.value != newpass.value) {
        alert('Mật khẩu nhập lại không trùng khớp')
        repeatpass.focus()
        check = false
    }
    if (check) {
        var data = {
            user: sessionStorage.getItem('UserStaff'),
            old_pass: oldpass.value,
            new_pass: newpass.value
        }
        fetch(`http://127.0.0.1:5000/staff/change_password`, {
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
            .then(newData => {
                if (newData.result == true) {
                    alert(newData.error)
                    window.location.reload()
                }
                if (newData.result == false) {
                    alert(newData.error)
                }
            })
    }
}


let openEditStaff = (element) => {
    let c = document.getElementById("modal");
    c.style.display = "flex";
    var idStaff = document.getElementById('IdStaff')
    var salary = document.getElementById('salary')
    var role = document.getElementById('Role')
    var listInfo = document.getElementsByClassName(element.id)
    console.log(listInfo[1])
    salary.value = Number.parseInt(listInfo[2].innerHTML)
    idStaff.value = element.id
}

let setDataStaff = function () {
    var idStaff = document.getElementById('IdStaff')
    var salary = document.getElementById('salary')
    var role = document.getElementById('Role')
    var data = {
        staff_id: idStaff.value,
        staff_salary: salary.value,
        role_name: role.options[role.selectedIndex].value
    }
    fetch('http://127.0.0.1:5000/admin/manage/update/staff', {
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
        .then(newData => {
            if (newData.result == true) {
                alert(newData.error)
                window.location.reload()
            }
            if (newData.result == false) {
                alert(newData.error)
            }
        })
}