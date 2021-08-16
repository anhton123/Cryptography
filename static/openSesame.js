function openSesame(n) {
    const arr = [1, 2, 3, 4, 5, 6, 7, 8]
    // Shows relevant form
    document.getElementById(n).style.display = 'block'

    // Clears out old forms to prevent stacking
    arr.splice(n-1, 1)
    for (var i = 0; i < arr.length; i++) {
        document.getElementById(arr[i]).style.display = "none"
    }
}