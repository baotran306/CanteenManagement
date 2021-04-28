const renderListFood = function () {
    fetch("http://127.0.0.1:5000/admin/all_food")
        .then(res => res.json())
        .then(listFood => {
            var list = document.querySelector("#listfood")
            var htmls = listFood.map(function (food) {
                return `
                <tr class="${food.id_food}">
                    <th>
                        <img src="img/Image_Food/${food.image}" alt="Ảnh bị lỗi" width="150px">
                    </th>
                    <th>${food.id_food}</th>
                    <th>${food.food_name}</th>
                    <th>${food.cur_price}</th>
                    <th>${food.describe}</th>
                    <th>
                        <button class="btn-primary btn-Edit" onclick="activeForm()">Chỉnh sửa</button>
                        <button class="btn-secondary" onclick="DeleteFood(${food.id_food})" style="margin-top:20px">Xóa</button>
                    </th>
                </tr>
                `
            })
            list.innerHTML = htmls.join('')
        })

    setTimeout(function () {
        $('#dataTable').DataTable();
    }, 100);
}
const DeleteFood = function (id) {
    fetch(urlDeleteFood, {
        method: 'DELETE',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
    })
        .then(res => res.json())
        .then(data => {
            if (data.result === true) {
                var objCancel = document.querySelector("." + id)
                objCancel.remove()
                alert("Xóa thành công")
            }
            if (data.result === false) {
                alert(data.error)
            }
        })
}

const renderListFoodAdd = function () {
    fetch("http://127.0.0.1:5000/admin/all_food")
        .then(res => res.json())
        .then(listFood => {
            var list = document.querySelector("#listfood")
            var htmls = listFood.map(function (food) {
                return `
                <tr class="${food.id_food}">
                    <th>
                        <img src="img/Image_Food/${food.image}" alt="Ảnh bị lỗi" width="150px">
                    </th>
                    <th>${food.id_food}</th>
                    <th>${food.food_name}</th>
                    <th>${food.cur_price}</th>
                    <th>${food.describe}</th>
                    <th>
                        <input type="checkbox" id="${food.id_food}" class="mycheckbox">
                    </th>
                </tr>
                `
            })
            list.innerHTML = htmls.join('')
        })

    setTimeout(function () {
        $('#dataTable').DataTable();
    }, 100);
}

const checkRenderListFoodAdd = function () {
    var chosenDate = document.getElementById('date-chosen')
    var chosenBuoi = document.getElementById('Buoi')
    var datenow = new Date()
    var datechosen = new Date(chosenDate.value)
    if (datenow > datechosen) {
        alert('Thời gian bạn chọn đã qua rồi bạn không thể tạo mới')
        window.location.reload()
    }

    var data = {
        Date: chosenDate.value,
        Buoi: chosenBuoi.value
    }
    fetch(url, {
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
        .then(resData => {
            var allCheckBox = document.getElementsByClassName('mycheckbox')
            for (let i = 0; i < allCheckBox.length; i++) {
                allCheckBox[i].checked = false
            }
            if (resData.listfood !== null) {
                for (let j = 0; j < resData.listfood.length; i++) {
                    document.getElementById(resData.listfood[i]).checked = true
                }
            }
        })
}