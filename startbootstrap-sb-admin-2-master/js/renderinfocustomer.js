fetch(`http://127.0.0.1:5000/customer/info/${sessionStorage.getItem('IdCustomer')}`, {
    method: 'POST',
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
    .then(infoCustomer => {
        var gioitinh1 = ''
        var gioitinh2 = ''
        var obj = document.getElementById('CusInfo')
        if (infoCustomer.gender.toLowerCase()='nữ')
        {
            gioitinh1 = 'nữ'
            gioitinh2 = 'nam'
        }
        else
        {
            gioitinh1 = 'nam'
            gioitinh2 = 'nữ'
        }
        var output = ''
        output += `
    <h2 style="padding-bottom: 20px; padding-left: 350px;">THÔNG TIN TÀI KHOẢN CỦA BẠN</h2>
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
                                    <input type="text" value="${infoCustomer.address}" id="addresses" style="margin-left: 77px;">
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
                                            <input type="date" value="${infoCustomer.day_of_birth}" style="margin-left: 55px;">
                                         <br>
                                            <br>
                                            <label">CMND</label>
                                                <input type="text" disabled value="${infoCustomer.identity_card}" style="margin-left: 75px;">
    `
    })