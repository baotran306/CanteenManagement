fetch("http://127.0.0.1:5000/admin/all_food")
    .then(res => res.json())
    .then(listFood => {
        var list = document.querySelector("#listfood")
        var htmls = listFood.map(function (food) {
            return `
                <tr class="${food.id_food}">
                    <th>
                        <img src="img/Image_Food/${food.image} alt="Ảnh bị lỗi" width="150px">
                    </th>
                    <th>${food.id_food}</th>
                    <th>${food.food_name}</th>
                    <th>${food.price}</th>
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
            alert(data)
            var objCancel = document.querySelector("." + id)
            objCancel.remove()
        })
}