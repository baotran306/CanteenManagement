
let activeForm = (element) => {
    let c = document.getElementById("modal");
    c.style.display = "flex";
    var foodId = document.getElementById('food_id')
    var foodName = document.getElementById('food_name')
    var foodPrice = document.getElementById('food_price')
    var foodDescription = document.getElementById('food_description')
    var foodImg = document.getElementById('myImgLoad')
    console.log(element.id)
    var listInfo = document.getElementsByClassName(element.id)
    console.log(listInfo)
    console.log(listInfo[1].src)
    foodImg.src = listInfo[1].src
    foodId.value = listInfo[2].innerHTML
    foodName.value = listInfo[3].innerHTML
    foodPrice.value = listInfo[4].innerHTML
    foodDescription.value = listInfo[5].innerHTML

}

let closeForm = () => {

    let c = document.getElementById("modal");
    c.style.display = "none";

}

let editMenu = () => {
    var foodId = document.getElementById('food_id')
    var foodName = document.getElementById('food_name')
    var foodPrice = document.getElementById('food_price')
    var foodDescription = document.getElementById('food_description')
    var foodImg = document.getElementById('myInputImg')
    var nameIMG = ''
    try {
        nameIMG = foodImg.files[0].name
    } catch (error) {
        nameIMG = ''
    }
    var data = {
        foodId: foodId.value,
        foodName: foodName.value,
        foodPrice: foodPrice.value,
        foodDescription: foodDescription.value,
        foodImg: nameIMG
    }
    fetch("http://127.0.0.1:5000/admin/manage/food/update", {
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
        .then(res=>res.json())
        .then(newData => {
            if (newData.result== true)
            {
                alert(newData.error)
                window.location.reload()
            }
            if (newData.result== false)
            {
                alert(newData.error)
            }
        })
}
