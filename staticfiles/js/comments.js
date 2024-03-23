// const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
// const deleteButtons = document.getElementsByClassName("btn-delete");
// const deleteConfirm = document.getElementById("deleteConfirm");


// for (let button of deleteButtons) {
//   button.addEventListener("click", (e) => {
//     let commentId = e.target.getAttribute("data-comment_id");
//     deleteConfirm.href = `delete_comment/${commentId}`;
//     deleteModal.show();
//   });
// }

document.addEventListener("DOMContentLoaded", function() {
  const printButton = document.getElementById("printButton");

  printButton.addEventListener("click", function() {
    printForm();
  });

  function printForm() {
    window.print();
  }
});