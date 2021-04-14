var startRenderNhanVien = function() {
    getData()
}



var getData = function() {
    fetch("http://127.0.0.1:3000/staff")
    .then(res => res.json())
    .then(data => renderNhanVien(data))
}

var renderNhanVien = function (listNhanVien) {
    var list = document.querySelector("#liststaff")
    var htmls = listNhanVien.map(function(nhanvien){
        return `
        <tr>
        <th>${nhanvien.id}</th>
        <th>${nhanvien.name}</th>
        <th>${nhanvien.identity_card}</th>
        <th>${nhanvien.gender}</th>
        <th>${nhanvien.address}</th>
        <th>${nhanvien.day_of_birth}</th>
        <th>${nhanvien.role_name}</th>
        <th>${nhanvien.salary}</th</th>>
        <th>${nhanvien.phone_num}</th>
        <th>
            <button class="btn-secondary">Delete</button>
            <button class="btn-primary">Edit</button>
        </th>
    </tr>
        `
    })
    list.innerHTML = htmls.join('')
}

