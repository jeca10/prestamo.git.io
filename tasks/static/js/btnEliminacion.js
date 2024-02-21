document.addEventListener('DOMContentLoaded', function() {
    const btnEliminacion = document.querySelectorAll('.btnEliminacion');


    
    /* btnEliminacion.forEach(btn => {
        btn.addEventListener('click', function (e) {
            let confirmacion = confirm("¿Confirma la eliminacion del computador?");
            if(!confirmacion) {
                e.preventDefault();
            }
        })
    }); */
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', function (e) {
                e.preventDefault();
                Swal.fire({
                    title: '¿Estas seguro?',
                    text: "No podras revertir esta accion!",
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonColor: '#3085d6',
                    cancelButtonColor: '#d33',
                    confirmButtonText: 'Si, eliminar!',
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