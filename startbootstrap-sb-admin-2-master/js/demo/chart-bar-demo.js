// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// function number_format(number, decimals, dec_point, thousands_sep) {
//   // *     example: number_format(1234.56, 2, ',', ' ');
//   // *     return: '1 234,56'
//   number = (number + '').replace(',', '').replace(' ', '');
//   var n = !isFinite(+number) ? 0 : +number,
//     prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
//     sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
//     dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
//     s = '',
//     toFixedFix = function (n, prec) {
//       var k = Math.pow(10, prec);
//       return '' + Math.round(n * k) / k;
//     };
//   // Fix for IE parseFloat(0.55).toFixed(0) = 0;
//   s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
//   if (s[0].length > 3) {
//     s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
//   }
//   if ((s[1] || '').length < prec) {
//     s[1] = s[1] || '';
//     s[1] += new Array(prec - s[1].length + 1).join('0');
//   }
//   return s.join(dec);
// }
var mydata = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myBarChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6", "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "Tháng 11", "Tháng 12"],
    datasets: [{
      label: "Doanh thu",
      backgroundColor: "#4e73df",
      hoverBackgroundColor: "#2e59d9",
      borderColor: "#4e73df",
      data: mydata
      // data: [10, 20, 30, 40, 50, 60, 70, 80, 50, 60, 20, 10]
    }],
  },
  options: {
    maintainAspectRatio: false,
    layout: {
      padding: {
        left: 10,
        right: 25,
        top: 25,
        bottom: 0
      }
    },
    scales: {
      xAxes: [{
        time: {
          unit: 'Tháng'
        },
        gridLines: {
          display: false,
          drawBorder: false
        },
        ticks: {
          maxTicksLimit: 6
        },
        maxBarThickness: 25,
      }],
      yAxes: [{
        ticks: {
          min: 0,
          max: 60,
          maxTicksLimit: 5,
          padding: 10,
          // Include a dollar sign in the ticks
          callback: function (value, index, values) {
            return value + ` Triệu`;
          }
        },
        gridLines: {
          color: "rgb(234, 236, 244)",
          zeroLineColor: "rgb(234, 236, 244)",
          drawBorder: false,
          borderDash: [2],
          zeroLineBorderDash: [2]
        }
      }],
    },
    legend: {
      display: false
    },
    tooltips: {
      titleMarginBottom: 10,
      titleFontColor: '#6e707e',
      titleFontSize: 14,
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      callbacks: {
        label: function (tooltipItem, chart) {
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
          return datasetLabel + ' ' +tooltipItem.yLabel + ' Triệu';
        }
      }
    },
  }
});
setTimeout(function () {
  fetch(`http://127.0.0.1:5000/admin/stats/month/${Number.parseInt(document.getElementById('chosen-year').value)}`)
    .then(res => res.json())
    .then(newData => {
      if (newData != null) {
        for (let i = 0; i < newData.length; i++) {
          mydata[Number.parseInt(newData[i].month - 1)] = Number.parseFloat(newData[i].revenue / 1000000)
          console.log(mydata[Number.parseInt(newData[i].month) - 1])

        }
        myBarChart.update()
        document.getElementById('titleChart').innerHTML = `&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;DOANHTHU CỦA CĂN TIN PTIT NĂM ${document.getElementById('chosen-year').value}&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;`
      }
    })
}, 1000)
// console.log(mydata)


const tableYear = function () {
  var chosenYear = document.getElementById('chosen-year')
  var date = new Date()
  if (chosenYear.value - Number.parseInt(chosenYear.value) > 0)
    chosenYear.value = Number.parseInt(date.getFullYear())
  if (chosenYear.value < 0)
    chosenYear.value = Number.parseInt(date.getFullYear())
  if (chosenYear.value > 2100)
    chosenYear.value = Number.parseInt(date.getFullYear())
  if (chosenYear.value < 2000)
    chosenYear.value = Number.parseInt(date.getFullYear())
  fetch(`http://127.0.0.1:5000/admin/stats/month/${chosenYear.value}`)
    .then(res => res.json())
    .then(newData => {
      if (newData != null) {
        var mydata2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for (let i = 0; i < newData.length; i++) {
          mydata2[Number.parseInt(newData[i].month) - 1] = Number.parseFloat(newData[i].revenue / 1000000)
          console.log(mydata2[Number.parseInt(newData[i].month) - 1])
        }
        myBarChart.data.datasets[0].data = mydata2
        myBarChart.update()
        document.getElementById('titleChart').innerHTML = `&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;DOANHTHU CỦA CĂN TIN PTIT NĂM ${document.getElementById('chosen-year').value}&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;&star;`
      }
    })
}