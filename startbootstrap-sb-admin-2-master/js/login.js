

function login() {
    document.getElementById("form-1").onsubmit = (e) => {
        e.preventDefault();
        // var idInput = document.getElementById("ID")
        // var passInput = document.getElementById("password")
        // data = [
        //     {
        //         idInput: idInput,
        //         passInput: passInput,
        //     }
        // ]
        fetch("http://127.0.0.1:3000/staff")
            .then(res=> res.json())
            // fetch(url checklogin, {
            // method: 'POST', 
            // mode: 'cors', 
            // cache: 'no-cache', 
            // credentials: 'same-origin', 
            // headers: {
            // 'Content-Type': 'application/json'
            // },
            // redirect: 'follow', 
            // referrerPolicy: 'no-referrer', 
            // body: JSON.stringify(data)
            // })
            .then(data =>
            {
                var isTrueAccount = false;
                for (let i=0;i<data.length;i++)
                {
                    if (document.getElementById("ID").value === data[i].id  && document.getElementById("password").value === data[i].password)
                    {
                        sessionStorage.setItem("name",data[i].name);
                        sessionStorage.setItem("role",data[i].role);
                        var x = sessionStorage.getItem("role")
                        isTrueAccount= true;
                    }
                }
                if (!isTrueAccount)
                {
                    alert("Tài khoản hoặc mật khẩu k đúng")
                }
                else 
                {
                    if (x==="NhanVien" || x=== "QuanLy" )
                    window.location.href = "trangchu.html"
                    if (x === "Shipper")
                    window.location.href = "listbill.html"
                }
                
            })
    }
}

