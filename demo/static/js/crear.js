
document.addEventListener('DOMContentLoaded', () => {
    sessionStorage.clear();
    // Display "Create" page
    document.querySelector('#createShop').style.display = 'block';
    document.querySelector('#openShop').style.display = 'none';
    document.getElementById("deptID").value = 'Gerencia';
})
