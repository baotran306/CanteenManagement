// var today = new Date();
// var dd = String(today.getDate()).padStart(2, '0');
// var mm = String(today.getMonth() + 1).padStart(2, '0');
// var yyyy = today.getFullYear();
// today = yyyy + '-' + mm + '-' + dd;
var today = '2021-04-12'
var data1 = {
    day: today,
    session: 'Sáng'
}
var data2 = {
    day: today,
    session: 'Trưa',
}
var data3 = {
    day: today,
    session: "Chiều"
}
// Danh sách món ăn buổi sáng
fetch('http://127.0.0.1:5000/admin/menu/breakfast', {
    method: 'POST',
    mode: 'cors',
    cache: 'no-cache',
    credentials: 'same-origin',
    headers: {
        'Content-Type': 'application/json'
    },
    redirect: 'follow',
    referrerPolicy: 'no-referrer',
    body: JSON.stringify(data1)
})
    .then(res => res.json())
    .then(listmenu => {
        console.log(listmenu)
        if (listmenu.result == false)
        {
            return
        }
        var morning = document.getElementById('morning')
        var outputSang = ''
        for (let i =0;i<listmenu.id.length;i++)
        {

            outputSang += `
            
                <div class="container__products-item">
                    <img src="img/Image_Food/${listmenu.picture[i]}" alt="" class="img-product" title="${listmenu.description[i]}">
                    <br>
                    <div class="nameProduct">${listmenu.food_name[i]}</div>
                    <br>
                    <div class="priceProduct">${listmenu.food_price[i]} đồng</div>
                    <br>
                    <div class="wrap-amount hidden">
                    Số lượng đặt:
                    <input class="valueAmount" type="number" value='0' min="0" max="99" onchange="minMaxNum(event)">
                    </div>
                </div>
            
            `
        }
        morning.innerHTML = outputSang
    })
// Danh sách món ăn buổi trưa
setTimeout(() => {

    fetch('http://127.0.0.1:5000/admin/menu/lunch', {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(data2)
    })
        .then(res => res.json())
        .then(listmenu => {
            console.log(listmenu)
            if (listmenu.result == false)
            {
                return
            }

            var lunch = document.getElementById('lunch')
            var outputTrua = ''
            for (let i =0;i<listmenu.id.length;i++)
            {

                outputTrua += `
                
                    <div class="container__products-item">
                        <img src="img/Image_Food/${listmenu.picture[i]}" alt="" class="img-product" title="${listmenu.description[i]}">
                        <br>
                        <div class="nameProduct">${listmenu.food_name[i]}</div>
                        <br>
                        <div class="priceProduct">${listmenu.food_price[i]} đồng</div>
                        <br>
                        <div class="wrap-amount hidden">
                        Số lượng đặt:
                        <input class="valueAmount" type="number" value='0' min="0" max="99" onchange="minMaxNum(event)">
                        </div>
                    </div>
                
                `
            }

            lunch.innerHTML = outputTrua
        })
}, 500);
// Danh sách món ăn buổi chiều
setTimeout(() => {

    fetch('http://127.0.0.1:5000/admin/menu/dinner', {
        method: 'POST',
        mode: 'cors',
        cache: 'no-cache',
        credentials: 'same-origin',
        headers: {
            'Content-Type': 'application/json'
        },
        redirect: 'follow',
        referrerPolicy: 'no-referrer',
        body: JSON.stringify(data3)
    })
        .then(res => res.json())
        .then(listmenu => {
            console.log(listmenu)
            if (listmenu.result == false)
            {
                return
            }

            var afternoon = document.getElementById('afternoon')
            var outputChieu = ''
            for (let i=0;i<listmenu.id.length;i++)
            {

                outputChieu += `
                
                    <div class="container__products-item">
                        <img src="img/Image_Food/${listmenu.picture[i]}" alt="" class="img-product" title="${listmenu.description[i]}">
                        <br>
                        <div class="nameProduct">${listmenu.food_name[i]}</div>
                        <br>
                        <div class="priceProduct">${listmenu.food_price[i]} đồng</div>
                        <br>
                        <div class="wrap-amount hidden">
                        Số lượng đặt:
                        <input class="valueAmount" type="number" value='0' min="0" max="99" onchange="minMaxNum(event)">
                        </div>
                    </div>
                
                `
            }

            afternoon.innerHTML = outputChieu
        })
}, 1000)