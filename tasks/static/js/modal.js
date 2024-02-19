const table = document.getElementById('table')
const modal = document.getElementById('modal')
const inputs = document.querySelectorAll('input')
console.log(inputs)

table.addEventListener('click', (e)=>{
    e.stopPropagation();
    let data = e.target.parentElement.parentElement.children;
    fillData(data)
})

const fillData = (data)=>{
    console.log(data)
}