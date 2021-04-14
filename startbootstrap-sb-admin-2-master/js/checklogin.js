const checklogin = function(notPermissRoles){
    var positionUser = sessionStorage.getItem("role")
    var nameUser = sessionStorage.getItem("name")
    var navItemList = document.getElementsByClassName("header__nav-item")
    var isPermiss = true
    if (nameUser != null)
    alert(`Chào ${nameUser}`)
    if (positionUser == null)
        {
            window.location.href='loginUser.html'
        }    
    for (let i=0;i<notPermissRoles.length;i++)
        {
            if (positionUser === notPermissRoles[i])
                isPermiss = false
        }   
    if (!isPermiss)    
        {
            if (positionUser=== "Shipper")
            window.location.href = 'listhoadon.html'
            else
            window.location.href = 'trangchu.html'
            
            alert (`Bạn không có quyền truy cập`)
        }
    if (positionUser !== "QuanLy")
        {
            for (let i=1;i<navItemList.length;i++)
                {
                    navItemList[i].classList.add("hidden")
                }
        }    
}