
    var today = new Date();
    var dd = String(today.getDate()).padStart(2, '0');
    var mm = String(today.getMonth() + 1).padStart(2, '0');
    var yyyy = today.getFullYear();
    today = yyyy + '-' + mm + '-' + dd;
    document.getElementById('date-chosen').value = today;
    var turnoverDate = document.getElementById('turnoverDate')
    var amountBill = document.getElementById('amountBill')
    var finishPercent = document.getElementById('finishPercent')
    var percent = document.getElementById('percent')
    var data = {
        day : today
    }
    fetch("http://127.0.0.1:5000/admin/stats/day",{
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
    .then(newData=> {
        // console.log(newData)
        // console.log(turnoverDate)
        turnoverDate.innerHTML = newData.revenue
        amountBill.innerHTML = newData.num_success
        // percent.style.width = newData.percent_success
    })

const updateTurnOverDate = function () {
    var data2 = {
        day: document.getElementById('date-chosen').value
    }
    fetch("http://127.0.0.1:5000/admin/stats/day",{
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
    .then(res=>res.json())
    .then(newData=> {
        // console.log(newData)
        // console.log(turnoverDate)
        turnoverDate.innerHTML = newData.revenue
        amountBill.innerHTML = newData.num_success
        // percent.style.width = newData.percent_success
    })
}
