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

const changeStatus = function (id, e) {
    if (e.target.innerHTML === "Chưa giao") {
        e.target.innerHTML = "Đã giao"
    }
    fetch(urlChangeStatus, {
        method: 'POST',
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
        })
}

const CancelBill = function (id) {
    fetch(urlCancelBill, {
        method: 'POST',
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

const renderHoaDonCustomer = function (IdCustomer) {
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
                output += billCode + `<th>` + listfood + `</th> <th>` + listamount + `</th> <th>` + listprice + `</th>` + all
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
                <th>${listHoaDon[i].status}</th>
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