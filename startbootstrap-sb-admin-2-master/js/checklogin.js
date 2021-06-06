const checkloginAdmin = function () {
    var role = sessionStorage.getItem("Role")
    var nameStaff = sessionStorage.getItem("NameStaff")
    var name = document.getElementById("UserName")

    if (name != null) {

        name.innerHTML = nameStaff
    }
    if (role == null) {
        window.location.href = 'loginStaff.html'
    }
    if (role.toLocaleLowerCase() === 'nhân viên giao hàng') {
        alert('Bạn không có quyền truy cập')
        window.location.href = 'shipper.html'
    }
    if (role.toLocaleLowerCase() === 'thu ngân') {
        alert('Bạn không có quyền truy cập')
        window.location.href = 'saler.html'
    }
}

const checkloginShipper = function () {
    var role = sessionStorage.getItem("Role")
    if (role == null) {
        window.location.href = 'loginStaff.html'
    }
    if (role.toLocaleLowerCase() === 'quản lý') {
        alert('Bạn là quản lý hãy xem thông tin hóa đơn ở mục danh sách hóa đơn nhé')
        window.location.href = 'listbill.html'
    }
    if (role.toLocaleLowerCase() === 'thu ngân') {
        alert('Bạn là nhân viên bán hàng hãy tập trung vào bán hàng nhé')
        window.location.href = 'saler.html'
    }
}

const checkloginSaler = function () {
    var role = sessionStorage.getItem("Role")
    if (role == null) {
        window.location.href = 'loginStaff.html'
    }
    if (role.toLocaleLowerCase() === 'quản lý') {
        alert('Bạn là quản lý hãy xem thông tin hóa đơn ở mục danh sách hóa đơn nhé')
        window.location.href = 'listbill.html'
    }
    if (role.toLocaleLowerCase() === 'nhân viên giao hàng') {
        alert('Bạn là nhân viên giao hàng hãy tập trung vào giao hàng nhé')
        window.location.href = 'shipper.html'
    }
}

const checkloginCustomer = function () {
    if (sessionStorage.getItem('IdCustomer') != null) {
        document.getElementById('DangNhap').classList.add('hidden')
        document.getElementById('DangXuat').classList.remove('hidden')
        document.getElementById('HoaDon').classList.remove('hidden')
        document.getElementById('Info').classList.remove('hidden')
    }
}