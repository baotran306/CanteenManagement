
fetch(`http://127.0.0.1:5000/customer/${sessionStorage.getItem('IdCustomer')}`)
    .then(res => res.json())
    .then(infoCustomer => {
        var gioitinh1 = ''
        var gioitinh2 = ''
        var obj = document.getElementById('CusInfo')
        if (infoCustomer.gender.toLowerCase() == 'nữ') {
            gioitinh1 = 'nữ'
            gioitinh2 = 'nam'
        }
        else {
            gioitinh1 = 'nam'
            gioitinh2 = 'nữ'
        }
        var output = ''
        output += `
    <h2 style="padding-bottom: 20px; padding-left: 250px;">THÔNG TIN TÀI KHOẢN CỦA BẠN</h2>
                <label">Mã khách hàng</label>
                    <input type="text" disabled value="${infoCustomer.id}" id="idCustomer" style="margin-left: 15px;">
                    <br>
                    <br>
                        <label">Họ và tên</label>
                            <input type="text" value="${infoCustomer.name}" id="name" style="margin-left: 57px;">
                            <br>
                            <br>
                            <label">VIP</label>
                                <input type="text" value="${infoCustomer.vip.toLowerCase()}" id="vip" style="margin-left: 100px; width: 30px;" disabled>
                                <br>
                                <br>
                                <label">Địa chỉ</label>
                                    <input type="text" value="${infoCustomer.address}" id="address" style="margin-left: 77px;">
                                    <br>
                                    <br>
                                    <label">Giới tính</label>
                                        <select id="gender" style="margin-left: 65px;">
                                            <option value="${gioitinh1}">${gioitinh1}</option>
                                            <option value="${gioitinh2}">${gioitinh2}</option>
                                        </select>
                                        <br>
                                        <br>
                                        <label">Ngày sinh</label>
                                            <input type="date" value="${infoCustomer.day_of_birth}" style="margin-left: 55px;" id='birthday'>
                                         <br>
                                            <br>
                                            <label">CMND</label>
                                                <input type="text" disabled value="${infoCustomer.identity_card}" style="margin-left: 75px;" id="CMND">
                                                <br>
                                                <br>
                                                <label>SĐT</label>
                                                <input type="text" value="${infoCustomer.phone_num}" style = "margin-left: 90px" id='SDT' >
    `
        obj.innerHTML = output
    })

    const checkRegex = (mySDT, myCMND) => {
        var sdt = /^[0-9]{10,11}$/
        var cmnd = /^[0-9]{9,10}$/
    
        if (!mySDT.match(sdt)) {
            alert("Số điện thoại phải có 10 chữ số")
            return false
        }
        if (!myCMND.match(cmnd)) {
            alert("CMND phải có 9-10 chữ số")
            return false
        }
        return true
    }
    const checkBirthday = (date) => {
        if (date== '')
        {
            alert('Bạn chưa chọn ngày sinh')
            return false
        }
        var newDate = new Date(date)
        var dateNow = new Date()
        if (!(newDate.getFullYear() + 16 < dateNow.getFullYear())) {
            alert("Bạn cần đủ 16 tuổi để đăng ký")
            return false
        }
        return true
    }
    

 
    
    
const changeInfoCustomer = function () {
    var id = document.getElementById('idCustomer')
    var Name = document.getElementById('name')
    var gender = document.getElementById('gender')
    var id_card = document.getElementById('CMND')
    var dob = document.getElementById('birthday')
    var phone = document.getElementById('SDT')
    var address = document.getElementById('address')
    var check = true
    if (Name.value == '' || id_card.value == '' || dob.value == '' || phone == '' || address == '') {
        alert("Bạn không được phép để trống thông tin")
        check = false
    }
    check = checkRegex(phone.value,id_card.value)&&checkBirthday(dob.value)
    if (check) {
        var data = {
            id: id.value,
            name: Name.value,
            gender: gender.options[gender.selectedIndex].value,
            id_card: id_card.value,
            dob: dob.value,
            address: address.value,
            phone : phone.value
        }
        fetch('http://127.0.0.1:5000/person/update/info', {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'same-origin',
            headers: {
                'Content-Type': 'application/json'
            },
            redirect: 'follow',
            referrerPolicy: 'no-referrer',
            body: JSON.stringify(data)
        })
            .then(res => res.json())
            .then(newData => {
                if (newData.result == true)
                {
                    alert(newData.error)
                    window.location.reload()
                }
                if (newData.result == false)
                {
                    alert(newData.error)
                }
            })
    }
}