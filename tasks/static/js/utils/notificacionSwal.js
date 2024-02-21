const notificacionSwal=(titleText,text,icon,confirButtonText)=>{
    Swal.fire({
        title: titleText,
        text: text,
        icon: icon,  //warning, error, success, info
        confirmButtonText: confirButtonText
    })
}