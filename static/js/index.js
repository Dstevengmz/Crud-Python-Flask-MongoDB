function confirmarGuardar() {
  Swal.fire({
    title: "¿Estás seguro?",
    text: "Esta seguro de guardar el producto",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sí,",
    cancelButtonText: "No,",
  }).then((result) => {
    if (result.isConfirmed) {
      document.querySelector("form").submit();
    }
  });
}

function confirmarEliminar(codigo) {
  event.preventDefault();
  Swal.fire({
    title: "¿Estás seguro?",
    text: "Esta seguro de eliminar el producto",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "No, cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/eliminar/" + codigo;
    }
  });
}

function confirmarEditar(codigo) {
  Swal.fire({
    title: "¿Estás seguro?",
    text: "Se modificara el producto",
    icon: "warning",
    showCancelButton: true,
    confirmButtonText: "Sí,",
    cancelButtonText: "No,",
  }).then((result) => {
    if (result.isConfirmed) {
      document.querySelector(`#form-editar-${codigo}`).submit();
    }
  });
}
