var startRenderHoaDon = function() {
    getData()
}



var getData = function() {
    fetch("http://127.0.0.1:3000/staff")
    .then(res => res.json())
    .then(data => renderHoaDon(data))
}

var renderNhanVien = function (listHoaDon) {
    var list = document.querySelector("#listhoadon")
    var htmls = listHoaDon.map(function(hoadon){
        return `
        <tr>
            <td class="column1">${hoadon.name}</td>
            <td class="column2">${hoadon.id}</td>
            <td class="column3">${hoadon.address}</td>
            <td class="column4">${hoadon.phone}</td>
            <td class="column5">${hoadon.role}</td>
        </tr>
        `
    })
    list.innerHTML = htmls.join('')
}

