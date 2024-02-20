document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM cargado');
    
    const table = document.getElementById('table');
    const modal = document.getElementById('modal-container');
    const inputs = document.querySelectorAll('input');

    console.log('table:', table); // Verifica si el elemento con ID 'table' se encuentra
    console.log('modal:', modal); // Verifica si el elemento con ID 'modal-container' se encuentra

    table.addEventListener('click', (e) => {
        console.log('Tabla clicada');
        e.stopPropagation();
        let data = e.target.parentElement.parentElement.children;
        fillData(data);
    });

    const fillData = (data) => {
        for (let compu_detail of inputs) {
            console.log(compu_detail);
            // Puedes realizar otras acciones con compu_detail aquí
        }
    };
});