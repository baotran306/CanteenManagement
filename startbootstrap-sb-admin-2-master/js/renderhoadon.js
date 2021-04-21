// var startRenderHoaDon = async function () {
//     getData()
// }



// var getData = function () {
//     fetch("http://127.0.0.1:5000//admin/stats/order")
//         .then(res => res.json())
//         .then(data => renderHoaDon(data))
// }

// var renderHoaDon = function (listHoaDon) {
// var list = document.querySelector("#listbill")
// var htmls = listHoaDon.map(function (hoadon) {
//     return `
//     <tr>
//         <th>${hoadon.order_id}</th>
//         <th>${hoadon.customer_id}</th>
//         <th>${hoadon.staff_id}</th>
//         <th>${hoadon.total}</th>
//         <th>${hoadon.order_time}</th>
//         <th>${hoadon.status_now}</th>
//     </tr>
//     `
// })
// list.innerHTML = htmls.join('')
// }


fetch("http://127.0.0.1:5000//admin/stats/order")
    .then(res => res.json())
    .then(listHoaDon => {
        console.log(listHoaDon)
        var output = '';
        for (let i in listHoaDon) {
            output += `
        <tr>
            <th>${listHoaDon[i].order_id}</th>
            <th>${listHoaDon[i].customer_id}</th>
            <th>${listHoaDon[i].staff_id}</th>
            <th>${listHoaDon[i].total}</th>
            <th>${listHoaDon[i].order_time}</th>
            <th>${listHoaDon[i].status_now}</th>
        </tr>
        `
        }
        var list = document.querySelector("#listbill")

        list.innerHTML = output
    })
    .catch(error => console.log(error))

// $(document).ready(function () {
    setTimeout(function () {
        $('#dataTable').DataTable();
    },100)
// });
