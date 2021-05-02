fetch(`http://127.0.0.1:5000/staff/${sessionStorage.getItem('IdStaff')}`)
    .then(res => res.json())
    .then(infoStaff => {
        var gioitinh1 = ''
        var gioitinh2 = ''
        var obj = document.getElementById('CusInfo')
        if (infoStaff.gender.toLowerCase() == 'nữ') {
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
                <label">Mã nhân viên</label>
                    <input type="text" disabled value="${infoStaff.id}" id="idStaff" style="margin-left: 30px;">
                    <br>
                    <br>
                        <label">Họ và tên</label>
                            <input type="text" value="${infoStaff.name}" id="name" style="margin-left: 57px;">
                            <br>
                            <br>
                            <label">Vai trò</label>
                                <input type="text" value="${infoStaff.role_name}" id="role" style="margin-left: 80px;" disabled>
                                <br>
                                <br>
                                <label">Địa chỉ</label>
                                    <input type="text" value="${infoStaff.address}" id="address" style="margin-left: 77px;">
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
                                            <input type="date" value="${infoStaff.day_of_birth}" style="margin-left: 55px;" id='birthday'>
                                         <br>
                                            <br>
                                            <label">CMND</label>
                                                <input type="text" disabled value="${infoStaff.identity_card}" style="margin-left: 75px;" id="CMND">
                                                <br>
                                                <br>
                                                <label>SĐT</label>
                                                <input type="text" value="${infoStaff.phone_num}" style = "margin-left: 90px" id='SDT' >
                                                <br>
                                                <br>
                                                <label>Lương</label>
                                                <input disabled type="text" value="${infoStaff.salary}" style = "margin-left: 75px" id='salary' >
    `
        obj.innerHTML = output
    })

const changeInfoStaff = function () {
    var id = document.getElementById('idStaff')
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