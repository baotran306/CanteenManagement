const renderListFood = function () {
    fetch("http://127.0.0.1:5000/admin/all_food")
        .then(res => res.json())
        .then(listFood => {
            var list = document.querySelector("#listfood")
            var htmls = listFood.map(function (food) {
                return `
                <tr class="${food.id_food}">
                    <th>
                        <img src="img/Image_Food/${food.image}" alt="Ảnh bị lỗi" width="150px" class='${food.id_food}'>
                    </th>
                    <th class="${food.id_food}">${food.id_food}</th>
                    <th class="${food.id_food}">${food.food_name}</th>
                    <th class="${food.id_food}">${food.cur_price}</th>
                    <th class="${food.id_food}">${food.describe}</th>
                    <th>
                        <button class="btn-primary btn-Edit" onclick="activeForm(this)" id="${food.id_food}">Chỉnh sửa</button>
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
    fetch(`http://127.0.0.1:5000/admin/manage/food/${id}`, {
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
                // var objCancel = document.getElementsByClassName(id)
                // objCancel[0].remove()
                alert("Xóa thành công")
                window.location.reload()
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
                        <img src="img/Image_Food/${food.image}" alt="Ảnh bị lỗi" style="width:150px">
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
        $('#dataTable').DataTable(
            {
                "scrollY": "400px",
                "scrollX": false,
                "paging": false
            }
        );
    }, 100)

}

const checkRenderListFoodAdd = function () {
    var chosenDate = document.getElementById('date-chosen')
    var chosenBuoi = document.getElementById('Buoi')
    var datenow = new Date()
    var datechosen = new Date(chosenDate.value)
    // if (datenow > datechosen) {
    //     alert('Thời gian bạn chọn đã qua rồi bạn không thể tạo mới')
    //     window.location.reload()
    // }

    var data = {
        day: chosenDate.value,
        session: chosenBuoi.options[chosenBuoi.selectedIndex].value
    }
    fetch("http://127.0.0.1:5000/admin/menu/detail", {
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
            var mytable = document.getElementById('dataTable')
            for (let i = 0; i < allCheckBox.length; i++) {
                allCheckBox[i].checked = false
            }
            if (resData.id_food != undefined) {
                for (let j = 0; j < resData.id_food.length; j++) {
                    for (let k = 0; k < allCheckBox.length; k++) {
                        if (allCheckBox[k].id == resData.id_food[j]) {
                            allCheckBox[k].checked = true
                        }
                    }
                }
            }
        })
}

const makeNewMenu = function () {
    var chosenDate = document.getElementById('date-chosen')
    var chosenBuoi = document.getElementById('Buoi')
    var allCheckBox = document.getElementsByClassName('mycheckbox')
    var datenow = new Date()
    var datechosen = new Date(chosenDate.value)
    if (datenow > datechosen) {
        alert('Thời gian bạn chọn đã qua rồi bạn không thể tạo mới')
        window.location.reload()
        return
    }

    var listFood = []
    if (chosenDate.value == null) {
        alert("Hãy chọn ngày")
        return
    }
    for (let i = 0; i < allCheckBox.length; i++) {
        if (allCheckBox[i].checked == true) {
            listFood.push(allCheckBox[i].id)
        }
    }
    var data = {
        day: chosenDate.value,
        session: chosenBuoi.options[chosenBuoi.selectedIndex].value,
        list_food: listFood
    }
    fetch('http://127.0.0.1:5000/admin/update/menu/detail', {
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