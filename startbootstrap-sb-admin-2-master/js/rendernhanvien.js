// var startRenderNhanVien = function () {
//     getData()
// }



fetch("http://127.0.0.1:5000/staff")
    .then(res => res.json())
    .then(listNhanVien => {
        var list = document.querySelector("#liststaff")
        var htmls = listNhanVien.map(function (nhanvien) {
            return `
                <tr class="${nhanvien.id}">
                <th>${nhanvien.id}</th>
                <th>${nhanvien.name}</th>
                <th>${nhanvien.identity_card}</th>
                <th>${nhanvien.gender}</th>
                <th>${nhanvien.address}</th>
                <th>${nhanvien.day_of_birth}</th>
                <th class="${nhanvien.id}">${nhanvien.role_name}</th>
                <th class="${nhanvien.id}">${nhanvien.salary}</th>
                <th>${nhanvien.phone_num}</th>
                <th>
                    <button class="btn-primary btn-Edit" onmousedown="openEditStaff(this)" id="${nhanvien.id}">Sửa</button>
                    <button class="btn-secondary" onclick="DeleStaff('${nhanvien.id}')" style="margin-top:20px">Xóa</button>
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

var DeleStaff = function (id) {
    console.log(id)
    fetch(`http://127.0.0.1:5000/admin/manage/staff/${id}`, {
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
            if (data.result == true) {

                alert(data.error)
                // var objCancel = document.querySelector("." + id)
                // objCancel.remove()
                window.location.reload()
            }
            if (data.result == false)
            {
                alert(data.error)
            }
        })
}