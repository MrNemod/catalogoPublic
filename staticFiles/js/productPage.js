const messageBtn = document.getElementById("messageButton")
const mianImage = document.getElementById('mainImage')

// Funcion para enviar mensaje con el link del producto
const sendMessage = (productName) => {
    const currentUrl = window.location.href;
    const encodeMessage = encodeURIComponent(`Me interesa el producto *${productName}* que vi en la pagina: ${currentUrl}`);
    const whatsappLink = `https://wa.me/3338310980?text=${encodeMessage}`;
    window.location = whatsappLink;
}

const changeImage = (src) => {
    mianImage.src = src
}