
fetch("http://127.0.0.1:5000/customer")
.then(res => res.json())
.then(listCustomer => {
    var list = document.querySelector("#listcustomer")
    var htmls = listCustomer.map(function (customer) {
        return `
            <tr class="${customer.id}">
            <th>${customer.id}</th>
            <th>${customer.name}</th>
            <th>${customer.identity_card}</th>
            <th>${customer.gender}</th>
            <th>${customer.address}</th>
            <th>${customer.day_of_birth}</th>
            <th>${customer.phone_num}</th>
            <th class="${customer.id}">${customer.vip}</th>
            <th>
                <button class="btn-primary btn-Edit" onmousedown="openEditCustomer(this)" id="${customer.id}">Chỉnh sửa</button>
            </th>
            </tr>
            `
    })
    list.innerHTML = htmls.join('')
})

setTimeout(function () {
$('#dataTable').DataTable({
    dom: 'Bfrtip',
    buttons: [
        'excel', 'pdf', 'print'
    ]
});
}, 1000);