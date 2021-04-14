
var barsreach = document.querySelector('.sreach')
var buttonByID = document.querySelector('.byIdUser');
var buttonByName = document.querySelector('.byName')
function byName() {
    barsreach.placeholder = 'Nhập tên nhân viên'
    buttonByName.classList.remove('hidden')
    buttonByID.classList.add('hidden')

}
function byId() {
    barsreach.placeholder = 'Nhập id cần tìm'
    buttonByID.classList.remove('hidden')
    buttonByName.classList.add('hidden')
}