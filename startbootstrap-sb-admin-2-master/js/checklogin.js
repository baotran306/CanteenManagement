const checkloginAdmin = function(){
    var role = sessionStorage.getItem("Role")
    var nameStaff = sessionStorage.getItem("NameStaff")
    var name = document.getElementById("UserName")
    name.innerHTML = nameStaff
    if (role.toLocaleLowerCase() === 'nhân viên giao hàng')
    {
        alert('Bạn không có quyền truy cập')
        window.location.href = 'shipper.html' 
    }
    if (role.toLocaleLowerCase() === 'thu ngân')
    {
        alert('Bạn không có quyền truy cập')
        window.location.href = 'homepage.html'
    }
    if (role === null)
    {
        window.location.href = 'loginStaff.html'
    }
}