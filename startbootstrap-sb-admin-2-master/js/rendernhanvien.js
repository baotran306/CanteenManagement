var startRenderNhanVien = function() {
    getData()
}



var getData = function() {
    fetch("http://127.0.0.1:3000/staff")
    .then(res => res.json())
    .then(data => renderNhanVien(data))
}

var renderNhanVien = function (listNhanVien) {
    var list = document.querySelector("#listnhanvien")
    var htmls = listNhanVien.map(function(nhanvien){
        return `
        <tr>
            <td class="column1">${nhanvien.name}</td>
            <td class="column2">${nhanvien.id}</td>
            <td class="column3">${nhanvien.address}</td>
            <td class="column4">${nhanvien.phone}</td>
            <td class="column5">${nhanvien.role}</td>
            <td class="column6">
                <button class="btn-functional btn-delete">X</button>
                <button class="btn-functional btn-edit">Edit</button>
            </td>
        </tr>
        `
    })
    list.innerHTML = htmls.join('')
}

