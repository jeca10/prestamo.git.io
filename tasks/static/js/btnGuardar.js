document.addEventListener('DOMContentLoaded', function() {
    const btnGuardar = document.querySelectorAll('.btnGuardar');


    
    
    btnGuardar.forEach(btn => {
        btn.addEventListener('click', function (e) {
                e.preventDefault();
                Swal.fire({
                    title: '¿Estas seguro?',
                    text: "No podras revertir esta accion!",
                    icon: 'success',
                    showCancelButton: true,
                    confirmButtonColor: '#00b91f',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, Guardar!',
                    backdrop: true,
                    showLoaderOnConfirm: true,
                    preConfirm: () => { 
                        location.href = e.target.href;
                    },
                    allowOutsideClick: () => false,
                    allowEscapekey: () => false

                })
            })
        });
});