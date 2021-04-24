
fetch("http://127.0.0.1:5000//admin/stats/order")
    .then(res => res.json())
    .then(listHoaDon => {
        var output = '';
        for (let i in listHoaDon) {
            if (listHoaDon[i].status_now === "Hủy") {
                output += `
                <tr class="${listHoaDon[i].order_id}">
                    <th>${listHoaDon[i].order_id}</th>
                    <th>${listHoaDon[i].staff_id}</th>
                    <th>${listHoaDon[i].customer_id}</th>
                    <th>${listHoaDon[i].address}</th>
                    <th>${listHoaDon[i].total}</th>
                    <th>${listHoaDon[i].order_time}</th>
                    <th>
                        <button class="btn-primary" onclick="changeStatus(${listHoaDon[i].order_id})"> 
                            ${listHoaDon[i].status_now}
                        </button>
                    </th>
        
                </tr>
                `
            }
            else {
                output += `
        <tr class="${listHoaDon[i].order_id}">
            <th>${listHoaDon[i].order_id}</th>
            <th>${listHoaDon[i].staff_id}</th>
            <th>${listHoaDon[i].customer_id}</th>
            <th>${listHoaDon[i].address}</th>
            <th>${listHoaDon[i].total}</th>
            <th>${listHoaDon[i].order_time}</th>
            <th>
                <button class="btn-primary" onclick="changeStatus(${listHoaDon[i].order_id})"> 
                    ${listHoaDon[i].status_now}
                </button>
                <button class="btn-secondary" onclick="CancelBill(${listHoaDon[i].order_id})"> 
                    Hủy
                </button>
            </th>

        </tr>
        `
            }
        }
        var list = document.querySelector("#listbill")

        list.innerHTML = output
    })
    .catch(error => console.log(error))
setTimeout(function () {
    $('#dataTable').DataTable();
}, 100)

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
