var startRenderHoaDon = function() {
    getData()
}



var getData = function() {
    fetch("http://127.0.0.1:3000/staff")
    .then(res => res.json())
    .then(data => renderHoaDon(data))
}

var renderHoaDon = function (listHoaDon) {
    var list = document.querySelector("#listbill")
    var htmls = listHoaDon.map(function(hoadon){
        return `
        <tr>
        <th>${hoadon.order_id}</th>
        <th>${hoadon.customer_id}</th>
        <th>${hoadon.staff_id}</th>
        <th>${hoadon.total}</th>
        <th>${hoadon.order_time}</th>
        <th>${hoadon.status_now}</th>
    </tr>
        `
    })
    list.innerHTML = htmls.join('')
}

