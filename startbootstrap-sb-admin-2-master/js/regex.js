
const checkRegex = (mySDT, myCMND) => {
    var sdt = /^[0-9]{10,11}$/
    var cmnd = /^[0-9]{9,10}$/

    if (!mySDT.match(sdt)) {
        alert("Số điện thoại phải có 10 chữ số")
        return
    }
    if (!myCMND.match(cmnd)) {
        alert("CMND phải có 9-10 chữ số")
        return
    }
}
const checkBirthday = (date) => {
    if (date == '') {
        alert('Bạn chưa chọn ngày sinh')
        return
    }
    var newDate = new Date(date)
    var dateNow = new Date()
    if (newDate.getFullYear() + 17 < dateNow.getFullYear() + 1) {
        alert("Bạn cần đủ 16 tuổi để đăng ký")
        return
    }
}

const checkPass = (myPass) => {
    var pass = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,16}$/
    if (!myPass.match(pass) || myPass.indexOf(' ') >= 0) {
        alert("Mật khẩu phải nhập từ 8-16 ký tự có ít nhất 1 chữ viết hoa và không sử dụng ký tự đặc biệt")
        return
    }
}

const checkUser = (myUser) => {
    1
    var user = /^[a-zA-Z0-9]+$/
    if (!myUser.match(user)) {
        alert("Tên đăng nhập phải không dùng khoảng trắng và ký tự đặc biệt")
        return
    }
}

