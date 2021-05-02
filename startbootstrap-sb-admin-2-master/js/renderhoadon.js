const renderHoaDonAdmin = function () {

    fetch("http://127.0.0.1:5000//admin/stats/order")
        .then(res => res.json())
        .then(listHoaDon => {
            var output = '';
            for (let i in listHoaDon) {
                output += `
            <tr class="${listHoaDon[i].order_id}">
                <th>${listHoaDon[i].order_id}</th>
                <th>${listHoaDon[i].staff_id}</th>
                <th>${listHoaDon[i].customer_id}</th>
                <th>${listHoaDon[i].address}</th>
                <th>${listHoaDon[i].total}</th>
                <th>${listHoaDon[i].order_time}</th>
                <th> ${listHoaDon[i].status_now}</th>
            </tr>
            `
            }
            var list = document.querySelector("#listbill")

            list.innerHTML = output
        })
        .catch(error => console.log(error))
    setTimeout(function () {
        $('#dataTable').DataTable();
    }, 100)
}

const changeStatus = function (element) {
    var data = {
        status: element.innerHTML,
        id_order: element.id,
        id_shipper: sessionStorage.getItem("IdStaff")
    }
    if (element.innerHTML == "Đang giao") {
        element.innerHTML = "Đã giao"
    }
    if (element.innerHTML == "Chưa giao") {
        element.innerHTML = "Đang giao"
    }
    console.log(data)
    fetch("http://127.0.0.1:5000/shipper/manage/order", {
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

const CancelBill = function (element) {
    var id_order = element.id
    fetch(`http://127.0.0.1:5000/customer/manage/order/${id_order}`)
        .then(res => res.json())
        .then(data => {
            alert(data.error)
            window.location.reload()
        })
}

const renderHoaDonCustomer = function () {
    var IdCustomer = sessionStorage.getItem('IdCustomer')
    fetch(`http://127.0.0.1:5000/customer/order/${IdCustomer}`)
        // fetch('http://127.0.0.1:5000/admin/stats/all_order')
        .then(res => res.json())
        .then(listHoaDon => {
            var output = ''
            for (let i in listHoaDon) {
                var billCode = ''
                billCode += `
            <tr class = "${listHoaDon[i].id_order}">
            <th>${listHoaDon[i].id_order}</th>
        `
                var listfood = ''
                for (let j = 0; j < listHoaDon[i].food.length; j++)
                    listfood += `
                ${listHoaDon[i].food[j]}
                <br>                
            `
                var listamount = ''
                for (let k = 0; k < listHoaDon[i].num_of_food.length; k++)
                    listamount += `
                ${listHoaDon[i].num_of_food[k]}
                <br>                
            `
                var listprice = ''
                for (let m = 0; m < listHoaDon[i].price.length; m++)
                    listprice += `
                ${listHoaDon[i].price[m]}
                <br>                
            `
                var all = ''
                all += `
                <th>${listHoaDon[i].total}</th>
                <th>${listHoaDon[i].address}</th>
                <th>${listHoaDon[i].order_time}</th>
                <th>${listHoaDon[i].status}</th>
                `
                var buttonCancel = '<th></th>'
                if (listHoaDon[i].status == "Chưa giao")
                {
                    buttonCancel = `
                    <th>
                        <button class ="btn-primary" id="${listHoaDon[i].id_order}" onclick = "CancelBill(this)">Hủy</button>
                    </th>
                    `
                }
                output += billCode + `<th>` + listfood + `</th> <th>` + listamount + `</th> <th>` + listprice + `</th>` + all + buttonCancel
            }
            var list = document.querySelector("#listbill")

            list.innerHTML = output
        })
    setTimeout(function () {
        $('#dataTable').DataTable();
    }, 100)
}

const renderHoaDonShipper = function () {
    // fetch(`http://127.0.0.1:5000/customer/order/${IdCustomer}`)
    fetch('http://127.0.0.1:5000/admin/stats/all_order')
        .then(res => res.json())
        .then(listHoaDon => {
            var output = ''
            for (let i in listHoaDon) {
                var billCode = ''
                billCode += `
            <tr class = "${listHoaDon[i].id_order}">
            <th>${listHoaDon[i].id_order}</th>
            <th>${listHoaDon[i].name_customer}
        `
                var listfood = ''
                for (let j = 0; j < listHoaDon[i].food.length; j++)
                    listfood += `
                ${listHoaDon[i].food[j]}
                <br>                
            `
                var listamount = ''
                for (let k = 0; k < listHoaDon[i].num_of_food.length; k++)
                    listamount += `
                ${listHoaDon[i].num_of_food[k]}
                <br>                
            `
                var listprice = ''
                for (let m = 0; m < listHoaDon[i].price.length; m++)
                    listprice += `
                ${listHoaDon[i].price[m]}
                <br>                
            `
                var all = ''
                all += `
                <th>${listHoaDon[i].total}</th>
                <th>${listHoaDon[i].address}</th>
                <th>${listHoaDon[i].order_time}</th>
                <th>
                <button class="btn-primary" id="${listHoaDon[i].id_order}" onclick="changeStatus(this)">${listHoaDon[i].status}</button>
                </th>
                `
                output += billCode + `<th>` + listfood + `</th> <th>` + listamount + `</th> <th>` + listprice + `</th>` + all
            }
            var list = document.querySelector("#listbill")

            list.innerHTML = output
        })
    setTimeout(function () {
        $('#dataTable').DataTable();
    }, 100)
}