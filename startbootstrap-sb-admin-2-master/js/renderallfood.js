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
                </tr>
                `
        })
        list.innerHTML = htmls.join('')
    })

setTimeout(function () {
    $('#dataTable').DataTable();
}, 100);

