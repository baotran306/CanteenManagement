const checkPass = (myPass) => {
    var pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}$/
    if (!myPass.match(pass) || myPass.indexOf(' ') >= 0) {
        alert("Mật khẩu phải nhập từ 8-16 ký tự có ít nhất 1 chữ viết hoa và không sử dụng ký tự đặc biệt")
        return false
    }
    return true
}
var listAmount = []
var listId = []
var listName = []
var listPrice = []
var activeForm = (element) => {
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
    check = checkPass(newpass.value)
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
    check = checkPass(newpass.value)
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

let setDataCustomer = function () {
    var IdCustomer = document.getElementById('IdCustomer')
    var vip = document.getElementById('Vip')
    var data = {
        customer_id: IdCustomer.value,
        customer_type: vip.options[vip.selectedIndex].value
    }
    fetch('http://127.0.0.1:5000/admin/manage/update/customer/vip', {
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

let openEditCustomer = (element) => {
    let c = document.getElementById("modal");
    c.style.display = "flex";
    var idCustomer = document.getElementById('IdCustomer')
    var vip = document.getElementById('Vip')
    var listInfo = document.getElementsByClassName(element.id)
    idCustomer.value = element.id
}

var datHangOnline = function () {
    var address = document.getElementById("address")
    var idCustomer = document.getElementById("IdCustomer")
    var data = {
        address: address.value,
        customer_id: idCustomer.value,
        food_id: listId,
        num_food: listAmount,
        cur_price: listPrice,
    }
    console.log(data)

    fetch('http://127.0.0.1:5000/customer/order', {
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
                document.getElementById("modal").style.display = 'none'
            }
            if (newData.result == false) {
                alert(newData.error)
            }
        })

}

let openBillCustomer = function () {
    let c = document.getElementById("modal");
    c.style.display = "flex";
    var idCustomer = document.getElementById("IdCustomer")
    var address = document.getElementById("address")
    var billInfo = document.getElementById('billinfo')
    var total = document.getElementById('total')
    var table = ''
    listAmount = []
    listId = []
    listName = []
    listPrice = []
    idCustomer.value = sessionStorage.getItem('IdCustomer')
    fetch(`http://127.0.0.1:5000/customer/${sessionStorage.getItem('IdCustomer')}`)
        .then(res => res.json())
        .then(newData => {
            address.value = newData.address
        })
    var objListAmount = document.getElementsByClassName('valueAmount')
    var objListName = document.getElementsByClassName('nameProduct')
    var objListPrice = document.getElementsByClassName('priceProduct')


    for (let i = 0; i < objListAmount.length; i++) {
        if (Number.parseInt(objListAmount[i].value) > 0) {
            listAmount.push(Number.parseInt(objListAmount[i].value))
            listId.push(objListAmount[i].id)
            listName.push(objListName[i].innerHTML)
            listPrice.push(Number.parseInt(objListPrice[i].innerHTML))
        }
    }
    if (listId.length == 0) {
        alert("Đơn hàng đang trống")
        document.getElementById("modal").style.display = 'none'
        return
    }
    for (let k = 0; k < listId.length; k++) {
        table += `
            <tr>
            <th>${listId[k]}</th>
            <th>${listName[k]}</th>
            <th>${listPrice[k]}</th>
            <th>${listAmount[k]}</th>
            </tr> 
            `
    }
    var totalTemp = 0
    billInfo.innerHTML = table
    for (let j = 0; j < listPrice.length; j++) {
        totalTemp += listPrice[j] * listAmount[j]
    }
    if (sessionStorage.getItem("Vip").toLocaleLowerCase() == 'yes') {
        total.value = totalTemp * 95 / 100
    }
    else {
        total.value = totalTemp
    }
}

let datHangOffline = function () {
    var idStaff = document.getElementById("IdStaff")
    var data = {
        staff_id: idStaff.value,
        food_id: listId,
        num_food: listAmount,
        cur_price: listPrice,
    }

    fetch('http://127.0.0.1:5000/staff/order', {
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
                document.getElementById("modal").style.display = 'none'
            }

            if (newData.result == false) {
                alert(newData.error)
            }
        })

}

let openBillSaler = function () {
    let c = document.getElementById("modal");
    c.style.display = "flex";
    var idStaff = document.getElementById("IdStaff")
    var billInfo = document.getElementById('billinfo')
    var total = document.getElementById('total')
    var table = ''
    listAmount = []
    listId = []
    listName = []
    listPrice = []
    console.log(listAmount, listId, listName, listPrice)
    var objListAmount = document.getElementsByClassName('valueAmount')
    var objListName = document.getElementsByClassName('nameProduct')
    var objListPrice = document.getElementsByClassName('priceProduct')
    idStaff.value = sessionStorage.getItem('IdStaff')
    for (let i = 0; i < objListAmount.length; i++) {
        if (Number.parseInt(objListAmount[i].value) > 0) {
            listAmount.push(Number.parseInt(objListAmount[i].value))
            listId.push(objListAmount[i].id)
            listName.push(objListName[i].innerHTML)
            listPrice.push(Number.parseInt(objListPrice[i].innerHTML))
        }
    }
    for (let k = 0; k < listId.length; k++) {
        table += `
            <tr>
            <th>${listId[k]}</th>
            <th>${listName[k]}</th>
            <th>${listPrice[k]}</th>
            <th>${listAmount[k]}</th>
            </tr> 
            `
    }
    var totalTemp = 0
    billInfo.innerHTML = table
    for (let j = 0; j < listPrice.length; j++) {
        totalTemp += listPrice[j] * listAmount[j]
    }
    total.value = totalTemp

}