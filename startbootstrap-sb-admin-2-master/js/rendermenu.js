// Danh sách món ăn buổi sáng
fetch(urlSang)
    .then(res => res.json())
    .then(listmenu => {
        var morning = document.getElementById('morning')
        var outputSang = ''
        for (let i in listmenu) {
            outputSang += `
        <div class="container__products-item">
            <img src="./img/mon_an/${listmenu[i].picture}" alt="" class="img-product" title="${listmenu[i].description}">
            <br>
            <div class="nameProduct">${listmenu[i].food_name}</div>
            <br>
            div class="priceProduct">${listmenu[i].food_price}</div>
            <br>
            <div>
            Số lượng đặt:
            <input class="valueAmount" type="number" value='0' min="0" max="99" onchange="minMaxNum(event)">
            </div>
        </div>
        `
        }
        morning.innerHTML = outputSang
    })
// Danh sách món ăn buổi trưa
    fetch(urlTrua)
    .then(res => res.json())
    .then(listmenu => {
        var lunch = document.getElementById('lunch')
        var outputTrua = ''
        for (let i in listmenu) {
            outputTrua += `
        <div class="container__products-item">
            <img src="./img/mon_an/${listmenu[i].picture}" alt="" class="img-product" title="${listmenu[i].description}">
            <br>
            <div class="nameProduct">${listmenu[i].food_name}</div>
            <br>
            div class="priceProduct">${listmenu[i].food_price}</div>
            <br>
            <div>
            Số lượng đặt:
            <input class="valueAmount" type="number" value='0' min="0" max="99" onchange="minMaxNum(event)">
            </div>
        </div>
        `
        }
        lunch.innerHTML = outputTrua
    })
// Danh sách món ăn buổi chiều
    fetch(urlChieu)
    .then(res => res.json())
    .then(listmenu => {
        var afternoon = document.getElementById('afternoon')
        var outputChieu = ''
        for (let i in listmenu) {
            outputChieu += `
        <div class="container__products-item">
            <img src="./img/mon_an/${listmenu[i].picture}" alt="" class="img-product" title="${listmenu[i].description}">
            <br>
            <div class="nameProduct">${listmenu[i].food_name}</div>
            <br>
            div class="priceProduct">${listmenu[i].food_price}</div>
            <br>
            <div>
            Số lượng đặt:
            <input class="valueAmount" type="number" value='0' min="0" max="99" onchange="minMaxNum(event)">
            </div>
        </div>
        `
        }
        afternoon.innerHTML = outputChieu
    })